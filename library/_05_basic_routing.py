"""Flask routing.

Specifying routes for our Flask app is simple. We do it just by providing
the desired route in the `@app.route()` decorator. Sometimes our routes have
dynamic parameters. For example:
* `/posts/23` -> The number 23 (post id) is dynamic
* `/repo/flask-introduction/stars` -> The name of the repo (flask-introduction)
                                      is dynamic

Supporting dynamic routing parameters is really simple. We just need to
specify the desired dynamic portion by giving it a name and surrounding
it between `<>`.
"""
import json
from flask import Flask, render_template
with open("member.json") as f:
  info = json.load(f)
  
app = Flask(__name__)




@app.route('/')
def authors():
    return render_template('authors.html')


@app.route('/author/<authors_last_name>')
def author(authors_last_name):
    return render_template('author.html',
                           author=info[authors_last_name])
