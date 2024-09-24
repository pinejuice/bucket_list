import sys
sys.dont_write_bytecode = True

from flask import Blueprint, render_template, current_app

top = Blueprint("top", __name__, template_folder="templates")

@top.route("/top", methods=("GET", ))
def display_top():
    return render_template(
        "top.html"
    )
