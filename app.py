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
app = Flask(__name__)

# Simple initial working page
@app.route("/")
def hello_world():
    print(__name__)
    return render_template(
		"login.html"
		)



#================TEMPORARY====================================
# For visualizing Frontend development using blocks
@app.route("/test")
def test():
    return render_template("base.html")
#=============================================================

if __name__ == "__main__":
    app.debug = True
    app.run()
