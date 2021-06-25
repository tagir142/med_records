from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
import datetime
from flask_login import UserMixin
# Подключение объекта для управления БД
from labapp import db

#таблица с пользователяеми


# Таблица с информацией об работниках больницы
class Specialists(UserMixin, db.Model):
    __tablename__ = 'specialists'
    # Основной ключ
    id = Column(Integer, primary_key=True)
    # ФИО специалиста
    fullname = Column(String(50))
    # Должность специалиста
    position = Column(String(50))
    # Взаимосвязь с таблицей history
    history = relationship('History', backref='specialists', cascade="delete")
    # Взаимосвязь с таблицей appointments
    appointments = relationship('Appointments', backref='specialists', cascade="delete")
    # Взаимосвязь с таблицей schedule
    schedule = relationship('Schedule', backref='schedule', cascade="delete")

# Картотека (все пациенты) 
class Patients(UserMixin, db.Model):
    __tablename__ = 'patients'
    # Основной ключ
    id = Column(Integer, primary_key=True)
    # Мед.полис
    medicalpolicy = Column(String(16))
    # ФИО пациента
    fullname = Column(String(50))
    # Дата рождения
    date = Column(DateTime, default=datetime.datetime.utcnow)
    # логин
    login = Column(String(11))
    # Пароль
    password = Column(String(101))
    # Эл.почта пациента
    email = Column(String(30))
    # Взаимосвязь с таблицей history
    history = relationship('History', backref='patients', cascade="delete")
    # Взаимосвязь с таблицей appointments
    appointments = relationship('Appointments', backref='patients', cascade="delete")


# Операции
#class Operations(db.Model):
#    __tablename__ = 'operations'
#    # Основной ключ
#    id = Column(Integer, primary_key=True)
#    # Мед.полис
#    typeofoperation = Column(String(30))
#    # Взаимосвязь с таблицей history
#    #history = relationship('History', backref='operations', cascade="delete")

# График работы
class Schedule(UserMixin, db.Model):
    __tablename__ = 'schedule'
    # Основной ключ
    num = Column(Integer, primary_key=True)
    # Внешние ключи (id врача)
    ids = Column(Integer, ForeignKey('specialists.id'), nullable=False)
    # График работы (2/2, 5/2)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    # Начало рабочего дня
    datestart = Column(DateTime, default=datetime.datetime.utcnow)
    # Конец рабочего дня
    datefinish = Column(DateTime, default=datetime.datetime.utcnow)


# Записи к врачу
class Appointments(UserMixin, db.Model):
    __tablename__ = 'appointments'
    # Основной ключ
    num = Column(Integer, primary_key=True)
    # Внешние ключи (id пациента, id врача)
    idp = Column(Integer, ForeignKey('patients.id'), nullable=False)
    ids = Column(Integer, ForeignKey('specialists.id'), nullable=False)
    # Дата приема
    date = Column(String, default=datetime.datetime.utcnow)

# История приемов пациентов у врачей
class History(UserMixin, db.Model):
    __tablename__ = 'history'
    # Основной ключ
    num = Column(Integer, primary_key=True)
    # Внешние ключи (id пациента, id врача, id операции)
    idp = Column(Integer, ForeignKey('patients.id'), nullable=False)
    #idop = Column(Integer, ForeignKey('operations.id'))
    ids = Column(Integer, ForeignKey('specialists.id'), nullable=False)
    
    # Дата приема
    date = Column(DateTime, default=datetime.datetime.utcnow)
    # Симптомы
    symptoms = Column(String(100))
    # Диагноз
    diagnosis = Column(String(30))
    # Назначения врача
    medications = Column(String(50))

    
# Удаление ВСЕХ таблиц в БД и создание чистых таблиц по заданным моделям
def reset_database():
    db.delete_all()
    db.create_all()
