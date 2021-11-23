from flask import render_template

from app import app

@app.errorhandler(404)
def error_name(error):
    return render_template('error.html', error=error), 404
