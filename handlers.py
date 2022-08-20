from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def not_found(error):
    return render_template('errors/404.html')


@errors.app_errorhandler(500)
def not_found(error):
    return render_template('errors/500.html')