from re import A
from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
import json
from .models import Patients, Appointments, Specialists, Schedule
from labapp import db
from flask_login import current_user
from .routes import get_appointments, get_namespecialistsbyid

medkarta = Blueprint('medkarta', __name__)

@medkarta.route('/medkarta', methods=['GET'])
def show_med():
    spisok=[]
    tablica=get_appointments(current_user.id)
    for i in tablica['Appointments']:
        namespec=''
        a=(i['ids'])
        if a==1:
            namespec='Иванов Иван Иванович'
        elif a==2:
            namespec='Федоров Федор Федорович'
        elif a==3:
            namespec='Петров Петр Петрович'
        elif a==4:
            namespec='Павлов Павел Павлович'
        app=apps(str(i['date']), namespec)
        #app.date=str(i['date'])
        #app.idpat=str(i['idp'])
        #app.idspec=str(i['ids'])
        spisok.append(app)
       # print(tablica['Appointments'][i]['date'])
        
        #print(tablica['Appointments'][i]['idp'])
        #print(tablica['Appointments'][i]['ids'])
    ###print(spisok[0].date)
    # "рендеринг" (т.е. вставка динамически изменяемых данных) index.html и возвращение готовой страницы
    
    #namevrach = get_namespecialistsbyid(int(1))#meetlist[0].idspec
    #print(namevrach)
    return render_template('medkarta.html',  meetlist=spisok , name=current_user.fullname, medicalpolicy=current_user.medicalpolicy, email=current_user.email, login=current_user.login, title='Медицинская карта')

class apps:
    def __init__(self, date, namespec):
        self.date = date
        
        self.namespec = namespec
    
