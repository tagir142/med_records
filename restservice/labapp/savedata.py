from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_manager
from .models import Patients
from labapp import db
from . import routes, dbapi

savedata= Blueprint('savedata', __name__)
"""
@savedata.route('/savedata', methods)
def get_id():
    id=Patients.query.get()
    return id

"""