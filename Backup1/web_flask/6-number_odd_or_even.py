#!/usr/bin/python3
"""
Starts a Flask web application.
"""

from flask import Flask, render_template
from urllib.parse import unquote

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Displays 'C ' followed by the value of the text variable"""
    return 'C {}'.format(unquote(text).replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """Displays 'Python ' followed by the value of the text variable"""
    return 'Python {}'.format(unquote(text).replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Displays 'n is a number' only if n is an integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Displays an HTML page only if n is an integer"""
    return render_template('6-number_template.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Displays an HTML page only if n is an integer"""
    odd_or_even = 'odd' if n % 2 != 0 else 'even'
    return render_template(
        '6-number_odd_or_even.html',
        number=n,
        odd_even=odd_or_even
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
