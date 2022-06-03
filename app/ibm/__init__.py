from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound


ibm = Blueprint('ibm', __name__,
                        template_folder='templates')


@ibm.route('/')
def home():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)

@ibm.route('/form')
def form():
    try:
        return render_template('form.html')
    except TemplateNotFound:
        abort(404)

@ibm.route('/interestRate')
def interestRate():
    try:
        return render_template('interestRate.html')
    except TemplateNotFound:
        abort(404)

@ibm.route('/geolocation')
def geolocation():
    try:
        return render_template('geolocation.html')
    except TemplateNotFound:
        abort(404)

@ibm.route('/cities')
def cities():
    try:
        return render_template('cities.html')
    except TemplateNotFound:
        abort(404)
