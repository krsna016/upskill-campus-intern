# main/Main.py
import os
import random
import string
from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField
import json

templates_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
json_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'json', 'urls.json'))


app = Flask(__name__, template_folder=templates_folder)
app.config['SECRET_KEY'] = os.urandom(24)  # Generate a random secret key
bootstrap = Bootstrap(app)

# Initialize shortened_urls as an empty dictionary
shortened_urls = {}


class ShortenURLForm(FlaskForm):
    long_urls = StringField('Long URL')


def generate_short_url(length=6):
    chars = string.ascii_letters + string.digits
    short_url = "".join(random.choice(chars) for _ in range(length))
    return short_url


def load_shortened_urls():
    try:
        with open(json_file_path, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}


@app.route("/", methods=["GET", "POST"])
def index():
    form = ShortenURLForm()

    if form.validate_on_submit():
        long_url = form.long_urls.data
        short_url = generate_short_url()

        while short_url in shortened_urls:
            short_url = generate_short_url()

        shortened_urls[short_url] = long_url
        with open(json_file_path, "w") as f:
            json.dump(shortened_urls, f)

        # Use 'index.html' directly as Flask knows to look in the 'templates' folder
        return render_template('index.html', form=form, short_url=f"{request.url_root}{short_url}")

    return render_template('index.html', form=form)


@app.route("/<short_url>")
def redirect_urls(short_url):
    long_url = shortened_urls.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return "URL not found", 404


if __name__ == "__main__":
    shortened_urls = load_shortened_urls()
    app.run(debug=True)
