from flask import render_template


def not_found(code):
    return render_template("404.html"), 404
