# Matthew Chan (PM), Hannah Fried, Coby Sontag, Jionghao Wu [Team SOS]
# SoftDev1 pd2
# P00 -- Da Art of Storytellin'
# 2019-10-28

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(32) # secret key set to randomly generated string

# Landing page to check if user is logged in
# Redirects to either /home or /login
@app.route("/")
def hello_world():
    print(__name__)
    if 'username' in session:
        return redirect("/home")
    else:
        return redirect("/login")

# Login page
@app.route("/login")
def login():
    return render_template("login.html")

# Authentication page for login
# Flashes appropriate error messages
@app.route("/login/authenticate")
def authenticateLogin():
    username = request.form("username")
    password = request.form("password")
    if authenticate(username, password):
        return redirect("/home")
    '''
    =====TEMPORARILY NOT FLASHING=====
    else if userExists?(username):
        flash("incorrect password")
        return redirect("/login")
    else:
        flash("username does not exist")
        return redirect("/login")
    '''
    flash("Error: something went wrong") # TEMP flash message placeholder
    return redirect("/login")



if __name__ == "__main__":
    app.debug = True
    app.run()
