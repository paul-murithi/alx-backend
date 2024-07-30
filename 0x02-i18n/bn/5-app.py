#!/usr/bin/env python3
""" Task 0 Basic Flask app """


from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ Congiguration variable"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map_strict_slashes = False

babel = Babel(app)

@app.route('/')
def index() -> str:
    """Index route"""

    return render_template("3-index.html")

@babel.localeselector
def get_locale() -> str:
    """ Determines best match of supported languages"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

if __name__ == "__main__":
    app.run(debug=True)
