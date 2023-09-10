import pymysql
import json
import sqlite3

def db_connect():
    # <editor-fold desc="Пробую читать первую строку в базе database из таблицы date_users">
    '''если что есть, то заполняю таблицу в интерфейсе'''
    connect_sqlite3 = sqlite3.connect('database.db')
    cursor_sqlite3 = connect_sqlite3.cursor()
    cursor_sqlite3.execute("SELECT * FROM date_users WHERE id = 1")
    rows = cursor_sqlite3.fetchall()
    if len(rows) > 0:
        host = rows[0][1]
        port = rows[0][2]
        user = rows[0][3]
        db_password = rows[0][4]
        db_name = rows[0][5]
        cursor_sqlite3.close()
        connect_sqlite3.close()
        connect = True
    else:
        '''Если ничего нет, это данные по умолчанию'''
        connect = False
        connection = "Нет данных для авторизации в базе"
        # </editor-fold>
    if connect == True:
        try:
            connection = pymysql.connect(
                host=host,
                port=int(port),
                user=user,
                password=db_password,
                database=db_name
                # cursorclass=pymysql.cursors.DictCursor
            )
            connect = True

        except Exception as ex:
            connection = ex
            connect = False

        result = {
            "connection": connection,
            "connect": connect
        }
    return result

if __name__ == '__main__':
    connect = db_connect()
    if connect['connect'] == True:
        print(connect)
        connect["connection"].close()
    else:
        print(connect)