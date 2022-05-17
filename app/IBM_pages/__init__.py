from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

from app import IBM_pages

simple_pages = Blueprint('IBM_pages', __name__,
                        template_folder='templates')


@IBM_pages.route('/')
def index():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)

@IBM_pages.route('/form')
def about():
    try:
        return render_template('form.html')
    except TemplateNotFound:
        abort(404)

@IBM_pages.route('/interestRate')
def welcome():
    try:
        return render_template('interestRate.html')
    except TemplateNotFound:
        abort(404)
