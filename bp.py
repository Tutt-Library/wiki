"""Module extends app for use as a Blueprint in other projects."""
__author__ = "Jeremy Nelson"

from app import wiki 
from flask import Blueprint

wiki_blueprint = Blueprint(
    'wiki_blueprint', 
    __name__,
    template_folder='templates')


