# -*- coding: utf-8 -*-
# Подключаем объект приложения Flask из __init__.py
from labapp import app, db
# Подключаем библиотеку для "рендеринга" html-шаблонов из папки templates
from flask import render_template, make_response, request, Response, jsonify, json, Blueprint
from . import dbapi
from .models import *
import urllib.parse
import requests
from flask_login import login_required, current_user
"""
Модуль регистрации маршрутов для запросов к серверу, т.е.
здесь реализуется REST API
"""
#blueprint

main = Blueprint('main', __name__)



@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.fullname, title='Профиль')



#парсинг страниц URL
@app.route('/persdannie')
def persdannie():
    # "рендеринг" (т.е. вставка динамически изменяемых данных) index.html и возвращение готовой страницы
    return render_template('persdannie.html', name=current_user.fullname, medicalpolicy=current_user.medicalpolicy, email=current_user.email, login=current_user.login, title='Персональные данные')
"""
@app.route('/medkarta')
def medkarta():
    # "рендеринг" (т.е. вставка динамически изменяемых данных) index.html и возвращение готовой страницы
    return render_template('medkarta.html', name=current_user.fullname, medicalpolicy=current_user.medicalpolicy, email=current_user.email, login=current_user.login, title='Медицинская карта')
"""
@app.route('/proofofappt')
def proofofappt():
    # "рендеринг" (т.е. вставка динамически изменяемых данных) index.html и возвращение готовой страницы
    return render_template('proofofappt.html', title='Запись к врачу')

@app.route('/zapis')
def zapis():
    # "рендеринг" (т.е. вставка динамически изменяемых данных) index.html и возвращение готовой страницы
    return render_template('zapis.html', title='Запись к врачу')

@app.route('/okompanii')
def okompanii():
    # "рендеринг" (т.е. вставка динамически изменяемых данных) index.html и возвращение готовой страницы
    return render_template('okompanii.html', title='О компании')

@app.route('/uslugi')
def uslugi():
    # "рендеринг" (т.е. вставка динамически изменяемых данных) index.html и возвращение готовой страницы
    return render_template('uslugi.html', title='Услуги')
"""
@app.route('/lk')
def lk():
    # "рендеринг" (т.е. вставка динамически изменяемых данных) index.html и возвращение готовой страницы
    return render_template('lk.html', title='Личный кабинет')
"""
# Обработка обращения к индексной странице, где представлено описание вашего REST API
@app.route('/')
@app.route('/index')
def index():
    """
    methods = [
        {
            'type': 'GET',
            'note': 'Получить какие-то данные',
            'addr': '/context'
        },
        {
            'type': 'GET',
            'note': 'Получить еще какие-то данные',
            'addr': '/context'
        },
        {
            'type': 'POST',
            'note': 'Отправить какие-то данные',
            'addr': '/context'
        },
        {
            'type': 'PUT',
            'note': 'Обновить какие-то данные',
            'addr': '/context'
        },
        {
            'type': 'DELETE',
            'note': 'Удалить какие-то данные',
            'addr': '/context'
        }
    ]
    """
    # "рендеринг" (т.е. вставка динамически изменяемых данных) index.html и возвращение готовой страницы
    return render_template('index.html', title='МИС Medicinae records')

"""
Реализация response-методов, возвращающих клиенту стандартные коды протокола HTTP
"""

# Возврат html-страницы с кодом 404 (Не найдено)
@app.route('/notfound')
def not_found_html():
    return render_template('404.html', title='404', err={ 'error': 'Not found', 'code': 404 })

# Формирование json-ответа. Если в метод передается только data (dict-объект), то по-умолчанию устанавливаем код возврата code = 200
# В Flask есть встроенный метод jsonify(dict), который также реализует данный метод (см. пример метода not_found())
def json_response(data, code=200):
    return Response(status=code, mimetype="application/json", response=json.dumps(data))

# Пример формирования json-ответа с использованием встроенного метода jsonify()
# Обработка ошибки 404 протокола HTTP (Данные/страница не найдены)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)

# Обработка ошибки 400 протокола HTTP (Неверный запрос)
def bad_request():
    return make_response(jsonify({'error': 'Bad request'}), 400)

"""
Реализация основных REST-методов
"""

"""
# Получение списка групп
@app.route('/mas/json/groups', methods=['GET'])
def get_groups():
    resp = dbapi.get_groups()
    return json_response(resp)
"""

# Получение списка специалистов
@app.route('/mas/json/specialists', methods=['GET'])
def get_specialists():
    resp = dbapi.get_specialists()
    return json_response(resp)

# Получение списка пациентов
@app.route('/mas/json/patients', methods=['GET'])
def get_patients():
    resp = dbapi.get_patients()
    return json_response(resp)


"""
# Получение списка агентов
@app.route('/mas/json/agents', methods=['GET'])
def get_agents():
    # Считываем дополнительный параметр groupId,
    # т.е. адрес запроса выглядит так: /mas/json/agents?groupId=<id>
    groupId = request.args.get('groupId')
    # Если параметр не установлен, выводим все строки таблицы
    if groupId == None:
        resp = dbapi.get_agents()
    # иначе делаем запрос по двум таблицам в соответствии с ForeignKey('group.id')
    else:
        resp = dbapi.get_agents_by_groupId(groupId)
    return json_response(resp)
"""

# Получение графика работы специалистов
@app.route('/mas/json/schedule', methods=['GET'])
def get_schedule():
    # Считываем дополнительный параметр ids,
    # т.е. адрес запроса выглядит так: /mas/json/schedule?ids=<id>
    ids = request.args.get('ids')
    # Если параметр не установлен, выводим все строки таблицы
    if ids == None:
        resp = dbapi.get_schedule()
        
    # иначе делаем запрос по двум таблицам в соответствии с ForeignKey('group.id')
    else:
        return not_found()     # !!!!ПОКА ОСТАВИМ ТАК, ПОТОМ ? !!!!иначе возвращаем код 500 и текст ошибки
    return json_response(resp)
    
@app.route('/mas/json/appointments', methods=['GET'])
def get_appointments(idp):
    idp = request.args.get('idp')
    if idp == None:
        resp = dbapi.get_appointments()
    else:
        resp=dbapi.get_appointmentsbyIDP(idp)
    return resp

@app.route('/mas/json/specialists', methods=['GET'])
def get_namespecialistsbyid(id):
    id = request.args.get('id')
          
    
    resp=dbapi.get_namespecialistsbyid(id)
    return resp
"""
@app.route('/mas/json/agents/<int:id>', methods=['GET'])
def get_agent_by_id(id):
    resp = dbapi.get_agent_by_id(id)
    # Если агент с заданным id найден
    if resp != None:
        # Возвращаем json с данными
        return json_response(resp)
    else:
        # иначе возвращаем json с ошибкой 'Not found'
        return not_found()
"""


@app.route('/mas/json/schedule/<int:num>', methods=['GET'])
def get_schedule_by_id(num):
    resp = dbapi.get_schedule_by_id(num)
    # Если агент с заданным id найден
    if resp != None:
        # Возвращаем json с данными
        return json_response(resp)
    else:
        # иначе возвращаем json с ошибкой 'Not found'
        return not_found()


"""
@app.route('/mas/json/agents', methods=['POST'])
def add_agent():
    # Если в запросе нет данных или неверный заголовок запроса (т.е. нет 'application/json'),
    # или в этом объекте нет, например, обязательного поля 'location'
    if not request.json or not 'location' in request.json:
        # возвращаем стандартный код 400 HTTP-протокола (неверный запрос)
        return bad_request()
    # Иначе добавляем данные в БД
    resp = dbapi.add_agent(request.json)
    # Проверяем, есть ли ошибка при выполнении запроса к БД
    if not 'error' in resp:
        return json_response({'result': 'Created'}, 201)    # в случае успеха возвращаем код 201
    else:
        return json_response(resp, 500)     # иначе возвращаем код 500 и текст ошибки
"""

@app.route('/mas/json/appointments', methods=['POST'])
def add_appointment():
    # Если в запросе нет данных или неверный заголовок запроса (т.е. нет 'application/json'),
    # или в этом объекте нет, например, обязательного поля 'date'
    if not request.json or not 'date' in request.json:
        # возвращаем стандартный код 400 HTTP-протокола (неверный запрос)
        return bad_request()
    # Иначе добавляем данные в БД
    resp = dbapi.add_appointments(request.json)
    # Проверяем, есть ли ошибка при выполнении запроса к БД
    if not 'error' in resp:
        return json_response({'result': 'Created'}, 201)    # в случае успеха возвращаем код 201
    else:
        return json_response(resp, 500)     # иначе возвращаем код 500 и текст ошибки



@app.route('/mas/json/patients', methods=['POST'])
def add_patient():
    # Если в запросе нет данных или неверный заголовок запроса (т.е. нет 'application/json'),
    # или в этом объекте нет, например, обязательного поля 'medicalpolicy'
    if not request.json or not 'medicalpolicy' in request.json:
        # возвращаем стандартный код 400 HTTP-протокола (неверный запрос)
        return bad_request()
    # Иначе добавляем данные в БД
    resp = dbapi.add_patient(request.json)
    # Проверяем, есть ли ошибка при выполнении запроса к БД
    if not 'error' in resp:
        return json_response({'result': 'Created'}, 201)    # в случае успеха возвращаем код 201
    else:
        return json_response(resp, 500)     # иначе возвращаем код 500 и текст ошибки


"""
@app.route('/mas/json/agents/<int:id>', methods=['PUT'])
def update_agent_by_id(id):
    # Аналогично методу add_agent() проверяем преобразование json-данных
    if not request.json:
        return bad_request()
    resp = dbapi.update_agent_by_id(id, request.json)
    if not 'error' in resp:
        return json_response({'result': 'Accepted'}, 202)
    else:
        return json_response(resp, 500)
"""
@app.route('/mas/json/patients/<int:id>', methods=['PUT'])
def update_patient_by_id(id):
    # Аналогично методу add_patient() проверяем преобразование json-данных
    if not request.json:
        return bad_request()
    resp = dbapi.update_patient_by_id(id, request.json)
    if not 'error' in resp:
        return json_response({'result': 'Accepted'}, 202)
    else:
        return json_response(resp, 500)

@app.route('/mas/json/appointments/<int:id>', methods=['PUT'])
def update_appointment_by_id(id):
    # Аналогично методу add_appointment() проверяем преобразование json-данных
    if not request.json:
        return bad_request()
    resp = dbapi.update_appointment_by_id(id, request.json)
    if not 'error' in resp:
        return json_response({'result': 'Accepted'}, 202)
    else:
        return json_response(resp, 500)





"""
@app.route('/mas/json/agents/<int:id>', methods=['DELETE'])
def delete_agent_by_id(id):
    resp = dbapi.delete_agent_by_id(id)
    if not 'error' in resp:
        return json_response({'result': 'Deleted'}, 200)
    else:
        return json_response(resp, 500)

"""


@app.route('/mas/json/appointments/<int:id>', methods=['DELETE'])
def delete_appointment_by_id(id):
    resp = dbapi.delete_appointment_by_id(id)
    if not 'error' in resp:
        return json_response({'result': 'Deleted'}, 200)
    else:
        return json_response(resp, 500)


@app.route('/mas/json/patients/<int:id>', methods=['DELETE'])
def delete_patient_by_id(id):
    resp = dbapi.delete_patient_by_id(id)
    if not 'error' in resp:
        return json_response({'result': 'Deleted'}, 200)
    else:
        return json_response(resp, 500)