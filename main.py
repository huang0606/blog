import os
from flask import Flask, request, render_template
from models import Tag, Post, Category, app, db


os.environ.setdefault('FLASK_ENV', 'development')


@app.route('/', methods=['GET'])
@app.route('/index.html', methods=['GET'])
def index():
    context = dict()
    return render_template(
        'index.html',
        **context
    )


@app.route('/categories/', methods=['GET'])
def categories():
    context = dict()
    return render_template(
        'categories.html',
        **context
    )


@app.route('/tags/', methods=['GET'])
def tags():
    context = dict()
    return render_template(
        'tags.html',
        **context
    )


@app.route('/archives/', methods=['GET'])
def archives():
    context = dict()
    return render_template(
        'archives.html',
        **context
    )


@app.route('/<year>/<month>/<post_name>.html', methods=['GET'])
def post(year, month, post_name):
    context = dict()
    return render_template(
        'post.html',
        **context
    )


if __name__ == '__main__':
    app.run()
