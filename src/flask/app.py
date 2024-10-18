from flask import Flask, render_template, request

app = Flask(__name__)

from main import get_recipes


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/food_list")
def food_list():
    return render_template("food_list.html", food_list=[])


@app.route("/suggested_recipes")
def recipes():
    return render_template("suggested_recipes.html", recipes_list=get_recipes())


app.run(host="0.0.0.0")
