from flask import Flask
# Подключение конфигурации приложения Flask из модуля config.py
from config import Config
# Подключение ORM
from flask_sqlalchemy import SQLAlchemy

# Регистрируем приложение Flask
app = Flask(__name__)
# Подключаем конфигурацию приложения
app.config.from_object(Config)
# Данный объект для работы с базой данных, интегрированный в Flask, берет на себя все функции по управлению сессиями
db = SQLAlchemy(app)

# Подключаем маршруты (адреса REST запросов)
from labapp import routes

   # blueprint for auth routes in our app
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)
 # blueprint for non-auth parts of app
from .routes import main as main_blueprint
app.register_blueprint(main_blueprint)

from .medkarta import medkarta as medkarta_blueprint
app.register_blueprint(medkarta_blueprint)

from .sendSpecialists import send as send_blueprint
app.register_blueprint(send_blueprint)


from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from .models import Patients

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return Patients.query.get(int(user_id))