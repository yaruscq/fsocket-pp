import os
from flask import Blueprint, render_template



main = Blueprint("main", __name__)

var_val = os.getenv('var_val')
name1 = os.getenv('name1')
name2 = os.getenv('name2')

@main.route("/")
def index():
    return render_template("index.html", var_val=var_val, name1=name1, name2=name2)