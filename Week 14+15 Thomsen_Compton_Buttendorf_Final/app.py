"""Flask server code for the web interface"""

# Stdlib
import os
import io
import random
import string
import base64

# Pip Packages
from PIL import Image, ImageDraw
from deepface import DeepFace
from flask import Flask, render_template, request, make_response, redirect

# Custom
from user import UsersDatabase

app = Flask(__name__)
db = UsersDatabase()

if not os.path.exists(f"static{os.sep}frames"):
    os.makedirs(f"static{os.sep}frames", exist_ok=True)


def rndstr():
    """Generate a random 10 character string from ascii letters"""
    letters = string.ascii_letters
    return "".join(random.choice(letters) for i in range(100))


def handle_cookies(trequest):
    """Seperates out any cookies used to pass end-user messages from the input request object"""
    stuff = [
        trequest.cookies.get("FAILMSG"),
        trequest.cookies.get("WARNMSG"),
        trequest.cookies.get("SUCCESSMSG"),
    ]
    return stuff


@app.route("/stream/<id>", methods=["POST"])
def lecamera(uid):
    """This endpoint is called by the camera page, and turns an input frame into data."""
    session = request.cookies.get("goomba")
    if db.check_cookie(session):
        try:
            # Get the frame from the request
            frame = request.json["frame"].replace("data:image/jpeg;base64,", "")
            # Save the frame to disk or process it as needed
            img = Image.open(io.BytesIO(base64.decodebytes(bytes(frame, "utf-8"))))

            data_path = f"static{os.sep}frames{os.sep}{uid}"

            if not os.path.exists(data_path):
                os.makedirs(data_path, exist_ok=True)

            filename = f"static{os.sep}frames{os.sep}{uid}{os.sep}frame-{rndstr()}.jpg"

            img.save(filename)
            # print(f"Saved to {filename}")

            person = DeepFace.analyze(img_path=filename)[0]

            # print(person)
            # 'region': {'x': 313, 'y': 220, 'w': 140, 'h': 140}

            region_x = person["region"]["x"]
            region_y = person["region"]["y"]
            region_w = person["region"]["w"]
            region_h = person["region"]["h"]

            print(f"From DeepFace: {region_x}, {region_y} & {region_w}, {region_h}")

            box_x1 = region_x
            box_y1 = region_y

            box_x2 = region_x + region_w
            box_y2 = region_y + region_h

            print(f"Bounding box: ({box_x1},{box_y1}) & ({box_x2},{box_y2})")

            image_obj = Image.open(filename)
            draw = ImageDraw.Draw(image_obj)

            draw.rectangle((box_x1, box_y1, box_x2, box_y2), fill=None, outline=(255, 0, 0))

            image_obj.save(filename)

            age = person["age"]  # normal
            main_emotion = person["dominant_emotion"]  # normal
            main_gender = person["dominant_gender"]  # normal
            main_race = person["dominant_race"]  # normal

            emotions = person["emotion"]  # dict
            sorted_emotions = {
                k: v
                for k, v in sorted(
                    emotions.items(), key=lambda item: item[1], reverse=True
                )
            }
            clean_emotions = {}
            for k, val in sorted_emotions.items():
                if "e-" not in str(val):
                    clean_emotions[k] = f"{val:.2f}"

            genders = person["gender"]  # dict
            sorted_genders = {
                k: v
                for k, v in sorted(
                    genders.items(), key=lambda item: item[1], reverse=True
                )
            }
            likely_genders = {}
            for k, val in sorted_genders.items():
                likely_genders[k] = f"{val:.2f}"

            races = person["race"]  # dict
            sorted_races = {
                k: v
                for k, v in sorted(
                    races.items(), key=lambda item: item[1], reverse=True
                )
            }
            likely_races = {}
            for k, val in sorted_races.items():
                if float(str(val).replace("%", "")) > 1.0:
                    likely_races[k] = f"{float(str(val).replace('%','')):.2f}"

            all_the_things = {
                "age": age,
                "main_emotion": main_emotion,
                "main_gender": main_gender,
                "main_race": main_race,
                "cleaned_emotions": clean_emotions,  # dict
                "likely_genders": likely_genders,  # dict
                "likely_races": likely_races,  # dict,
                "filename": filename,
            }

            db.add_history_to(session, all_the_things)

            return render_template(
                "result.html",
                filename=filename,
                age=age,
                main_em=main_emotion,
                main_gender=main_gender,
                main_race=main_race,
                s_em=clean_emotions,
                s_gender=likely_genders,
                s_races=likely_races,
            )
        except Exception as excep:
            print("Error: " + str(excep))
            return f"FAIL: {str(excep)}"
    else:
        return render_template(
            "fail.html", fail="<p>Please sign in first. <a href='/'>Go back.</a></p>"
        )


@app.route("/webcam")
def webcamera():
    """Returns the portal page that accesses the browser's camera"""
    session = request.cookies.get("goomba")
    if db.check_cookie(session):
        return render_template(
            "camera.html",
            SESSION=db.get_id_for_session(session),
            username=db.get_user_for_session(session),
        )
    else:
        return render_template(
            "fail.html", fail="<p>Please sign in first. <a href='/'>Go back.</a></p>"
        )


@app.route("/trends")
def trendspage():
    """Create a page with the history of analysis of the user"""
    session = request.cookies.get("goomba")
    if db.check_cookie(session):
        return db.do_trends_for(db.get_user_for_session(session))
    else:
        return render_template(
            "fail.html", fail="<p>Please sign in first. <a href='/'>Go back.</a></p>"
        )


@app.route("/", methods=["GET", "POST"])
def indexr():
    """Return the main page, or process a sign in event"""
    if request.method == "GET":
        cookies = handle_cookies(request)
        res = make_response(
            render_template(
                "index.html", fail=cookies[0], warning=cookies[1], success=cookies[2]
            )
        )
        for key in ["FAILMSG", "WARNMSG", "SUCCESSMSG"]:
            res.delete_cookie(key)
        return res
    else:
        usern = request.form["usern"]
        passw = request.form["passw"]

        if db.auth_by_user(usern, passw):
            # woo yea
            resp = make_response(redirect("/webcam"))
            token = rndstr()
            resp.set_cookie("goomba", token)
            db.set_cookie(usern, token)
            return resp
        else:
            return render_template(
                "fail.html",
                fail=f"<p>Failed to auth for {usern}. <a href='/'>Go back.</a></p>",
            )


@app.route("/register", methods=["GET", "POST"])
def doreg():
    """Return the registration form, or process a new account"""
    if request.method == "GET":
        return render_template("register.html")
    else:
        usern = request.form["usern"]
        passw = request.form["passw"]

        db.register_user(rndstr(), usern, passw)

        res = make_response(redirect("/"))
        res.set_cookie("SUCCESSMSG", "Registed a new user: " + usern)
        return res


if __name__ == "__main__":
    try:
        import webbrowser
        webbrowser.open("http://127.0.0.1:5000")
        app.run(host="0.0.0.0", debug=True)
    except Exception as e:
        print(str(e))
