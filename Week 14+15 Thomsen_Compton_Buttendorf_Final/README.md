# Final Project for CSI-260
This repository contains the code for the final project for CSI-260, created by [Matt Compton](https://github.com/SomethingGeneric), [Abijah Buttendorf](https://github.com/T20A026), and [David Thomsen](https://github.com/dthomsen116). The project involves developing a facial recognition module/webapp in Python.

# Setup
* `pip install -r requirements.txt`

# Usage
`python app.py`

________________________________________________________________________________________

# Write Up - David, Matt, Abijah

## 1. What we chose to do:
We chose to make a facial recognition module that takes frames of the users face and proceeds to analyze it and pull what the AI thinks is the dominant emotion, race, and gender. We had originally had a few different plans all regarding to working with the Facial recognition module Deepface.

## 2. Why did we choose to do it?
Abijah and David are in Dr. Banfill's Surveillence Capitalism class and thought this would be an interesting project for that class. Then, we had also been assigned this final and had wanted to make both work for both finals. So we had enlisted the help of Matt and he had wanted to work with us for this final (and kindly benefit Abijah and Dave in the process).

## 3. Requirements
- Class or Static Methods - **User and Userdatabase Classes in user.py**

- Properties - **User's Name/Pass/History**
    
- Variable argument lists or key word argument lists - **Flask Routing Logic, UserDatabase methods**
    
- List/Dictionary comprehensions - **Page generation for analysis output**
   
- Significant use of a python package - **Flask, DeepFace, bcrypt, toml**
    
- File I/O that is not pickle - **toml**

## 4. Things we learnt(+ve and -ve)

### Positive:

- Built on prior knowledge of flask

- Taking Live camera feed and cutting it into frames to be scanned

- Worked to make sure other users could not access pictures taken from other sessions

### Negative:

- We ran into issues gathering the images from deepface

- We also ran into issues while trying to get the camera working properly. 

- Issues using the class requirements to store information about each user. 

- Bounding boxes on the detected face took a while to work.