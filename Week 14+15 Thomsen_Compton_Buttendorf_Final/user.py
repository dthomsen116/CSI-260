# stdlib
import os

# pip packages
import toml
import bcrypt
from flask import render_template

class User:
    """Represents a user, with all of the attributes needed, and analysis history"""
    def __init__(self, id_str=None, usern=None, passw=None, ihistory=None):
        self.uid = id_str
        self.username = usern
        self.passw = passw
        self.history = ihistory if ihistory is not None else []

    def add_to_history(self, new_history):
        """Store a given history dict object for later tallying"""
        self.history.append(new_history)

    def __str__(self):
        all_my_stuff = {
            "id": self.uid,
            "username": self.username,
            "password": self.passw,
            "history": self.history,
        }
        return toml.dumps(all_my_stuff)


class UsersDatabase:
    """Various auxiliary functions for operating on users and creating pages"""
    def __init__(self):
        if not os.path.exists("db"):
            os.makedirs("db")
        self.cookies = []

    def expire_cookie(self, user):
        """Remove a given cookie for a user by name"""
        for data in self.cookies:
            if data["user"] == user:
                self.cookies.remove(data)
                return True
        return False

    def set_cookie(self, user, key):
        """Set an authentication cookie for a user by name"""
        self.expire_cookie(user)
        self.cookies.append({"user": user, "key": key})

    def check_cookie(self, untrusted):
        """Check if a string is a valid cookie"""
        for data in self.cookies:
            if data["key"] == untrusted:
                return True
        return False

    def get_cookie_thing(self, untrusted):
        """Return a cookie dict object by key string value"""
        for data in self.cookies:
            if data["key"] == untrusted:
                return data
        return None

    def get_id_for_session(self, untrusted):
        """Return a UID for a given session cookie, if there is one"""
        data = self.get_cookie_thing(untrusted)
        return self.find_id_by_username(data["user"])

    def get_user_for_session(self, untrusted):
        """Return the username of a given session cookie"""
        data = self.get_cookie_thing(untrusted)
        return data["user"]

    def commit_user(self, user):
        """Save a given user object to disk, using toml"""
        with open(f"db{os.sep}{user.uid}.toml", "w", encoding='utf-8') as f:
            f.write(str(user))

    def load_user(self, user_id):
        """Load a user object from disk by user id"""
        filename = f"db{os.sep}{user_id}.toml"
        if os.path.exists(filename):
            stuff = open(filename, encoding='utf-8').read()
            data = toml.loads(stuff)

            uid = None
            username = None
            password = None
            history = None

            if "id" in data.keys():
                uid = data["id"]

            if "username" in data.keys():
                username = data["username"]

            if "password" in data.keys():
                password = data["password"]

            if "history" in data.keys():
                history = data["history"]

            new = User(uid, username, password, history)
            return new
        return None

    def find_id_by_username(self, user):
        """Find the user id for a given username"""
        for filename in os.listdir("db"):
            if ".toml" in filename:
                stuff = open(f"db{os.sep}{filename}", encoding='utf-8').read()
                data = toml.loads(stuff)
                if data["username"] == user:
                    return data["id"]
        return None

    def add_history_to(self, session, new_history):
        """Add a history object to a user's history by session cookie"""
        obj = self.get_cookie_thing(session)
        username = obj["user"]
        user_id = self.find_id_by_username(username)
        user_object = self.load_user(user_id)
        user_object.add_to_history(new_history)
        self.commit_user(user_object)

    def register_user(self, uid, user, passw):
        """Register a new user account, with specified details"""
        ptpw = passw
        hashed_pw = bcrypt.hashpw(ptpw, bcrypt.gensalt())
        new = User(uid, user, hashed_pw)
        self.commit_user(new)

    def auth_user(self, uid, attempt):
        """Try to authenticate a user with given id by password"""
        user = self.load_user(uid)
        if user:
            return bcrypt.checkpw(attempt, user.passw)
        return False

    def auth_by_user(self, username, attempt):
        """Authenticate a user by username with password"""
        uid = self.find_id_by_username(username)
        if uid:
            return self.auth_user(uid, attempt)
        return False

    def do_trends_for(self, username):
        """Generate a trends page for the given username"""
        user_obj = self.load_user(self.find_id_by_username(username))

        ages_tally = {}
        all_ages = []  # special since average age is cool imo

        tally_emotions = {}

        tally_genders = {}

        tally_races = {}

        # here #

        all_cleaned_emotions = []

        all_likely_genders = []

        all_likely_races = []

        history_html = ""

        for history in user_obj.history:
            age = history["age"]
            if age in ages_tally.keys():
                ages_tally[age] += 1
            else:
                ages_tally[age] = 1
            all_ages.append(age)

            emotion = history["main_emotion"]
            if emotion in tally_emotions.keys():
                tally_emotions[emotion] += 1
            else:
                tally_emotions[emotion] = 1

            gender = history["main_gender"]
            if gender in tally_genders.keys():
                tally_genders[gender] += 1
            else:
                tally_genders[gender] = 1

            race = history["main_race"]
            if race in tally_races.keys():
                tally_races[race] += 1
            else:
                tally_races[race] = 1

            ##### not using the below for now ######
            all_cleaned_emotions.append(history["cleaned_emotions"])
            all_likely_genders.append(history["likely_genders"])
            all_likely_races.append(history["likely_races"])

            history_html += (
                render_template(
                    "result.html",
                    filename=history["filename"],
                    age=history["age"],
                    main_em=history["main_emotion"],
                    main_gender=history["main_gender"],
                    main_race=history["main_race"],
                    s_em=history["cleaned_emotions"],
                    s_gender=history["likely_genders"],
                    s_races=history["likely_races"],
                )
                + "<hr/>"
            )

        final_html = render_template(
            "trends.html",
            username=username,
            history=render_template(
                "trends_list.html",
                ages_tally=ages_tally,
                avg_age=sum(all_ages) / len(all_ages),
                tally_emotions=tally_emotions,
                tally_genders=tally_genders,
                tally_races=tally_races,
            )
            + "<hr/><h3>Previous frames</h3>"
            + history_html,
        )

        return final_html


if __name__ == "__main__":
    db = UsersDatabase()

    db.register_user("1", "matt", "TestPassword")

    if db.auth_by_user("matt", input("Password for matt: ")):
        print("Woo yea!")
    else:
        print("You failed to auth")
