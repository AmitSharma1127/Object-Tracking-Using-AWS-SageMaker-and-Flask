import os
import time
from flask import Flask, render_template, request, redirect, url_for, flash

# Configure app
app = Flask(__name__)
app.secret_key = '45b4f55592ebe3deba33b88d8ff660f9'

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres+psycopg2://postgres:root@localhost:5432/bhavahchat'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
@app.route("/index.html", methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404



if __name__ == "__main__":
    app.run(debug=True, port=5002)
