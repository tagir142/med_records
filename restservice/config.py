import os

from sqlalchemy.sql.elements import False_

"""
Модуль с описанием конфигурации для REST-сервера Flask
"""

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://user:qwerty@192.168.56.101/aisbase?charset=utf8"
    SECRET_KEY = 'secret-key-goes-here'