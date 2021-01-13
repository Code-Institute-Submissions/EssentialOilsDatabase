import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config ["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config ["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/get_essentialoils")
def get_essentialoils():
    essentialoils = list(mongo.db.essential_oils.find())
    return render_template(
        "essentialoils.html", essentialoils = essentialoils)
#check to make sure variation between essential_oils database and other essentialoils without _ are ok

@app.route("/add_oils")
def add_oils():
        return render_template("add_oils.html")

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
