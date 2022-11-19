from . import main
from flask import render_template, flash


@main.route("/", methods=['GET', 'POST'])
def books_storage():
    return render_template("index.html")
