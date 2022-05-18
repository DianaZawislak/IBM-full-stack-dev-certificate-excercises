from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound


IBM_pages = Blueprint('ibm_pages', __name__,
                        template_folder='templates')


@IBM_pages.route('/')
def home():
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


