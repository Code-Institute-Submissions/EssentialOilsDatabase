import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/get_essentialoils")
def get_essentialoils():
    essentialoils = list(mongo.db.essential_oils.find())
    return render_template(
        "essentialoils.html", essentialoils=essentialoils)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    essentialoils = list(mongo.db.essential_oils.find(
        {"$text": {"$search": query}}))
    return render_template(
        "essentialoils.html", essentialoils=essentialoils)


@app.route("/add_oil", methods=["GET", "POST"])
def add_oil():
    if request.method == "POST":
        source_inc = "on" if request.form.get("source_inc") else "off"
        oil = {
            "category_name": request.form.get("category_name"),
            "type": request.form.get("type"),
            "oil_name": request.form.get("oil_name"),
            "oil_description": request.form.get("oil_description"),
            "source_inc": source_inc,
        }
        mongo.db.essential_oils.insert_one(oil)
        flash("Oil Sucessfully Added")
        return redirect(url_for("get_essentialoils"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_oil.html", categories=categories)


@app.route("/edit_oil/<oil_id>", methods=["GET", "POST"])
def edit_oil(oil_id):
    if request.method == "POST":
        source_inc = "on" if request.form.get("source_inc") else "off"
        submit = {
            "category_name": request.form.get("category_name"),
            "type": request.form.get("type"),
            "oil_name": request.form.get("oil_name"),
            "oil_description": request.form.get("oil_description"),
            "source_inc": source_inc,
        }
        mongo.db.essential_oils.update({"_id": ObjectId(oil_id)}, submit)
        flash("Oil Sucessfully Updated")

    oil = mongo.db.essential_oils.find_one({"_id": ObjectId(oil_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    print(oil)
    return render_template("edit_oil.html", oil=oil, categories=categories)


@app.route("/delete_oil/<oil_id>")
def delete_oil(oil_id):
    mongo.db.essential_oils.remove({"_id": ObjectId(oil_id)})
    flash("Oil Successfully Deleted")
    return redirect(url_for("get_essentialoils"))


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_categories.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Sucessfully Deleted")
    return redirect(url_for("get_categories"))


# errorhandler 404 copied and 500 adapted from:
# https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
