from labapp import db
from .models import *

"""
В данном модуле реализуются CRUD-методы для работы с БД
"""

# Метод для преобразования объекта строки БД в стандартный тип данных Python
# (в объект dict), который хранит пары { 'ключ': значение }
def row_to_dict(row):
    # Если полученная строка из БД является объектом типа tuple
    # (неизменяемая коллекция, может быть получена, если в запросе указываются конкретные колонки для выбора)
    if isinstance(row, tuple):
        # возвращаем dict с помощью маппинга значений tuple и соответствующих названиям колонок ключей
        return dict(zip(row.keys(), row))
    # Если строка не "пустая", т.е. запрос к БД был успешен
    if row != None:
        # преобразуем row-объект в dict
        result = dict(row.__dict__)
        # удаляем поле с лишней служебной информацией
        result.pop('_sa_instance_state', None)
        return result
    else:
        return None

# получаем информацию о всех группах
#def get_groups():
    # объявляем пустой список
#    result = []
    # получаем итерируемый объект, где содержатся все строки с информацией об агентах с сортировкой по id
#    rows = db.session.query(Group).order_by(Group.id)
    # конвертируем каждую строку в dict и добавляем в список result
#    for row in rows:
#        result.append(row_to_dict(row))
    # возвращаем dict формата { 'groups': result }, где result - это список, содержащий в строках информацию по каждому агенту
#    return { 'groups': result }


# получаем информацию о всех специалистах
def get_specialists():
    # объявляем пустой список
    result = []
    # получаем итерируемый объект, где содержатся все строки с информацией об агентах с сортировкой по id
    rows = db.session.query(Specialists).order_by(Specialists.id)
    # конвертируем каждую строку в dict и добавляем в список result
    for row in rows:
        result.append(row_to_dict(row))
    # возвращаем dict формата { 'groups': result }, где result - это список, содержащий в строках информацию по каждому агенту
    return { 'specialists': result }


# получаем информацию о всех пациентах
def get_patients():
    # объявляем пустой список
    result = []
    # получаем итерируемый объект, где содержатся все строки с информацией об агентах с сортировкой по id
    rows = db.session.query(Patients).order_by(Patients.id)
    # конвертируем каждую строку в dict и добавляем в список result
    for row in rows:
        result.append(row_to_dict(row))
    # возвращаем dict формата { 'groups': result }, где result - это список, содержащий в строках информацию по каждому агенту
    return { 'patients': result }

# Получаем информацию об агенте по id
#def get_agent_by_id(id):
#    result = db.session.query(Agent).filter(Agent.id == int(id)).first()
#    return row_to_dict(result)


# Получаем информацию о графике работы по id
def get_schedule_by_id(num):
    result = db.session.query(Schedule).filter(Schedule.num == int(num)).first()
    return row_to_dict(result)


# получаем информацию о всех агентах в группе
#def get_agents():
    # объявляем пустой список
#    result = []
    # получаем итерируемый объект, где содержатся все строки с информацией об агентах с сортировкой по id
#    rows = db.session.query(Agent).order_by(Agent.id)
    # конвертируем каждую строку в dict и добавляем в список result
#    for row in rows:
#        result.append(row_to_dict(row))
    # возвращаем dict формата { 'agents': result }, где result - это список, содержащий в строках информацию по каждому агенту
#    return { 'agents': result }


# получаем информацию о всем графике работы специалиста
def get_schedule():
    # объявляем пустой список
    result = []
    # получаем итерируемый объект, где содержатся все строки с информацией об агентах с сортировкой по id
    rows = db.session.query(Schedule).order_by(Schedule.num)
    # конвертируем каждую строку в dict и добавляем в список result
    for row in rows:
        result.append(row_to_dict(row))
    # возвращаем dict формата { 'agents': result }, где result - это список, содержащий в строках информацию по каждому агенту
    return { 'Schedule': result }

def get_appointments():
    # объявляем пустой список
    result = []
    # получаем итерируемый объект, где содержатся все строки с информацией об агентах с сортировкой по id
    rows = db.session.query(Appointments).order_by(Appointments.num)
    # конвертируем каждую строку в dict и добавляем в список result
    for row in rows:
        result.append(row_to_dict(row))
    # возвращаем dict формата { 'agents': result }, где result - это список, содержащий в строках информацию по каждому агенту
    return { 'Appointments': result }

def get_namespecialistsbyid(id):
    # объявляем пустой список
    result = []
    # получаем итерируемый объект, где содержатся все строки с информацией об агентах с сортировкой по id
    rows = db.session.query(Specialists).filter(Specialists.id==id)
    # конвертируем каждую строку в dict и добавляем в список result
    for row in rows:
        result.append(row_to_dict(row))
    # возвращаем dict формата { 'agents': result }, где result - это список, содержащий в строках информацию по каждому агенту
    return { 'Specialists': result }

def get_appointmentsbyIDP(idp):
    # объявляем пустой список
    result = []
    # получаем итерируемый объект, где содержатся все строки с информацией об агентах с сортировкой по id
    rows = db.session.query(Appointments).filter(Appointments.idp==idp)
    # конвертируем каждую строку в dict и добавляем в список result
    for row in rows:
        result.append(row_to_dict(row))
    # возвращаем dict формата { 'agents': result }, где result - это список, содержащий в строках информацию по каждому агенту
    return { 'Appointments': result }
# Получение данных из двух связанных таблиц (join Group и Agent) по идентификатору группы
#def get_agents_by_groupId(groupId):
    # объявляем пустой список
#    result = []
    # получаем итерируемый объект, где содержатся с троки с ифнормацией из 2-х таблиц:
    # Agent.id, Agent.location, Group.last_update, Group.status
    #rows = db.session.query(Agent).join(Group).filter(Group.id == int(groupId)).all()
#    rows = db.session.query(Agent.id, Agent.location, Group.last_update, Group.status).join(Group).filter(Group.id == int(groupId)).all()
    # конвертируем каждую строку в dict и добавляем в список result
#    for row in rows:
#        result.append(row_to_dict(row))
    # возвращаем dict формата { 'agents': result }, где result - это список, содержащий в строках информацию по каждому агенту
#    return { 'agents': result }


# Получение данных из двух связанных таблиц (join Patients и Specialists) по идентификатору пациента
def get_specialists_by_patientsId(idp):
    # объявляем пустой список
    result = []
    # получаем итерируемый объект, где содержатся с троки с ифнормацией из 2-х таблиц:
    # Agent.id, Agent.location, Group.last_update, Group.status
    #rows = db.session.query(Agent).join(Group).filter(Group.id == int(groupId)).all()
    rows = db.session.query(Patients.id, Patients.medicalpolicy, Patients.fullname, Patients.numberofpnone, Specialists.fullname, Specialists.position).join(Patients).filter(Patients.id == int(idp)).all()
    # конвертируем каждую строку в dict и добавляем в список result
    for row in rows:
        result.append(row_to_dict(row))
    # возвращаем dict формата { 'agents': result }, где result - это список, содержащий в строках информацию по каждому агенту
    return { 'specialists': result }

# Добавить нового пациента в таблицу Agent
#def add_agent(json_data):
#    try:
        # Формируем объект Agent по данным из json_data
#        agent = Agent(lidar=json_data['lidar'], location=json_data['location'])
        # INSERT запрос в БД
#        result = db.session.add(agent)
        # Подтверждение изменений в БД
#        db.session.commit()
#        return { 'result': result }
    # если возникла ошибка запроса в БД, возвращаем dict с ключом 'error' и тектом ошибки
#    except Exception as e:
#        return {'error': str(e) }


# Добавить нового пациента в таблицу Patients
def add_patient(json_data):
    try:
        # Формируем объект Patients по данным из json_data
        patient = Patients(medicalpolicy=json_data['medicalpolicy'], fullname=json_data['fullname'], date=json_data['date'], numberofpnone=json_data['numberofpnone'], email=json_data['email'])
        # INSERT запрос в БД
        result = db.session.add(patient)
        # Подтверждение изменений в БД
        db.session.commit()
        return { 'result': result }
    # если возникла ошибка запроса в БД, возвращаем dict с ключом 'error' и тектом ошибки
    except Exception as e:
        return {'error': str(e) }


# Добавить новую запись в таблицу Appointments
def add_appointments(json_data):
    try:
        # Формируем объект Appointments по данным из json_data
        appointment = Appointments(date=json_data['date'])
        # INSERT запрос в БД
        result = db.session.add(appointment)
        # Подтверждение изменений в БД
        db.session.commit()
        return { 'result': result }
    # если возникла ошибка запроса в БД, возвращаем dict с ключом 'error' и тектом ошибки
    except Exception as e:
        return {'error': str(e) }

# Обновить данные в таблице Agent по идентификатору
#def update_agent_by_id(id, json_data):
#    try:
        # UPDATE запрос в БД
#        result = db.session.query(Agent).filter(Agent.id == id).update(json_data)
#        db.session.commit()
#        return {'result': result}
#    except Exception as e:
#        return {'error': str(e)}
#    return 0


# Обновить данные в таблице Appointments по идентификатору
def update_appointment_by_id(num, json_data):
    try:
        # UPDATE запрос в БД
        result = db.session.query(Appointments).filter(Appointments.num == num).update(json_data)
        db.session.commit()
        return {'result': result}
    except Exception as e:
        return {'error': str(e)}
    return 0

# Обновить данные в таблице Patients по идентификатору
def update_patient_by_id(id, json_data):
    try:
        # UPDATE запрос в БД
        result = db.session.query(Patients).filter(Patients.id == id).update(json_data)
        db.session.commit()
        return {'result': result}
    except Exception as e:
        return {'error': str(e)}
    return 0


# Удаление данных из таблицы Agent по идентификатору
# Если необходимо очистить таблицу полностью используйте: db.session.query(Agent).delete()
#def delete_agent_by_id(id):
#    try:
#        # DELETE запрос в БД
#        result = db.session.query(Agent).filter(Agent.id == int(id)).delete()
#        db.session.commit()
#        return {'result': result}
#    except Exception as e:
#        return {'error': str(e)}



# Удаление данных из таблицы Appointments по идентификатору
# Если необходимо очистить таблицу полностью используйте: db.session.query(Appointments).delete()
def delete_appointment_by_id(num):
    try:
        # DELETE запрос в БД
        result = db.session.query(Appointments).filter(Appointments.num == int(num)).delete()
        db.session.commit()
        return {'result': result}
    except Exception as e:
        return {'error': str(e)}



# Удаление данных из таблицы Patients по идентификатору
# Если необходимо очистить таблицу полностью используйте: db.session.query(Patients).delete()
def delete_patient_by_id(num):
    try:
        # DELETE запрос в БД
        result = db.session.query(Patients).filter(Patients.id == int(id)).delete()
        db.session.commit()
        return {'result': result}
    except Exception as e:
        return {'error': str(e)}