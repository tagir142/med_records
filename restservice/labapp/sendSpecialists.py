from operator import concat
import re
from threading import Timer
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from .models import Patients, Appointments
from labapp import db

send= Blueprint('send', __name__)

@send.route('/send', methods=['POST'])
def send_post():
    idpatient = current_user.id
    idspecialist = int(request.form.get('spec'))+int(1)
    date = str(request.form.get('selectDate'))
    time = str(request.form.get('selectTime'))
    dateand=concat(date, ' ')
    datetime=concat(dateand,time)
    print(datetime, idpatient, idspecialist)
    
    appointment=Appointments.query.filter_by(date=datetime).first()
    
    if appointment:
        flash('Время занято. Пожалуйста выберите другое.')
        return redirect(url_for('zapis'))
    
    new_appointment = Appointments(idp=idpatient, ids=idspecialist, date=datetime)
    
    db.session.add(new_appointment)
    db.session.commit()
    
    return redirect(url_for('proofofappt'))


