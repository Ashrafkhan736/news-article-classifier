from flask import Flask, render_template, request, redirect
from .utils import scrap_url
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os
from bson import ObjectId

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mongo = PyMongo(app)


@app.route("/", methods=["GET"])
def get_data():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def get_prediction():
    """
    Route for posting request for predicting the news category
    and also inserting that result into database

    expected json response : {'url':url_string}
    """

    url = request.form.get("url")
    try:
        result, content = scrap_url(url)
        data = mongo.db.result.insert_one(
            {"url": url, "result": result, "content": content}
        )
        return (
            render_template(
                "result.html",
                url=url,
                result=result,
                content=content,
                id=data.inserted_id,
            ),
            201,
        )

    except:
        return render_template("500.html"), 500


@app.route("/results")
def show_result():
    """
    Route for showing all the documents in the database
    """
    data = mongo.db.result.find()
    return render_template("all_result.html", data=data)


@app.route("/delete/<string:id>", methods=["GET"])
def delete_result(id: str):
    """
    Route for deleting a single documnet in database
    id : string representation of ObjectId
    """
    data = mongo.db.result.delete_one({"_id": ObjectId(id)})
    return redirect("/", code=302)


@app.errorhandler(500)
def internal_server_error(error):
    """
    Route for HTTP 500 - Internal Server Error
    """
    return render_template("500.html"), 500


@app.errorhandler(404)
def not_found_error(error):
    """
    Route for HTTP 404 - Not Found
    """
    return render_template("404.html"), 404
