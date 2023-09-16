from PySide6.QtWidgets import QDialog, QFileDialog
from PySide6.QtCore import Qt, Signal, QObject
import json

import sqlite3
import logging
# TODO: сделать общее открытие и закрытие базы
logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
        # datefmt="%Y-%m-%d %H:%M:%S",
        filename="basic.log",
        filemode="w", # чистит файл при каждом запуске
        encoding="utf-8"  # чтоб по русски писало
    )
# logging.info(f"progress_bar удалён {name}")  Это вставить в нужное место

from ui.base_ui.ui_window_dialog_setting import Ui_WindowDialogSetting
from connect_db import db_connect

class Signals(QObject):
    signal_emit_count_thred = Signal(int)

class WindowDialogSetting(QDialog):
    def __init__(self):
        super(WindowDialogSetting, self).__init__()
        self.ui = Ui_WindowDialogSetting()
        self.ui.setupUi(self)
        self.signals = Signals()

        # <editor-fold desc="Пробую читать первую строку в базе database из таблицы date_users">
        '''если что есть, то заполняю таблицу в интерфейсе'''
        self.connect_sqlite3 = sqlite3.connect('database.db')
        self.cursor_sqlite3 = self.connect_sqlite3.cursor()
        logging.info(f"База есть")

        self.cursor_sqlite3.execute('''CREATE TABLE IF NOT EXISTS date_users 
                            (
                                id INTEGER PRIMARY KEY, 
                                host VARCHAR, 
                                port INTEGER, 
                                user TEXT, 
                                db_password TEXT, 
                                db_name TEXT,
                                count_threds INTEGER,
                                path_to_file_links TEXT
                            )'''
                                    )
        query = "UPDATE date_users SET host = ? WHERE id = ?"
        values = ("localhost", 1)
        self.cursor_sqlite3.execute(query, values)
        self.connect_sqlite3.commit()

        self.cursor_sqlite3.execute("SELECT * FROM date_users WHERE id = 1")
        logging.info(f"Таблицы нет")

        self.rows = self.cursor_sqlite3.fetchall()
        if len(self.rows) > 0:
            self.host = self.rows[0][1]
            self.port = self.rows[0][2]
            self.user = self.rows[0][3]
            self.db_password = self.rows[0][4]
            self.db_name = self.rows[0][5]
            self.count_threds = self.rows[0][6]
            self.path_to_file_links = self.rows[0][7]
            self.cursor_sqlite3.close()
            self.connect_sqlite3.close()
            # print(self.rows)
        else:
            '''Если ничего нет, это данные по умолчанию'''
            self.host = "localhost или ip"
            self.port = "3306"
            self.user = "имя пользователя"
            self.db_password = "пароль"
            self.db_name = "имя базы"
            self.count_threds = "30"
            self.path_to_file_links = "путь к файлу с сылками"
        # </editor-fold>

        self.ui.lineEdit_db_host.setText(self.host)
        self.ui.lineEdit_db_port.setText(str(self.port))
        self.ui.lineEdit_db_user.setText(self.user)
        self.ui.lineEdit_db_password.setText(self.db_password)
        self.ui.lineEdit_db_name.setText(self.db_name)
        self.ui.tredsSpinBox.setValue(int(self.count_threds))
        self.ui.lineEdit_find_file.setText(self.path_to_file_links)

        self.chek_connect_db()
        self.ui.btn_test_db.clicked.connect(self.chek_connect_db)
        self.ui.btn_find_file.clicked.connect(self.path_to_file)
        self.ui.btn_save_total_threds.clicked.connect(self.save_total_threds)


    def save_total_threds(self):
        self.connect_sqlite3 = sqlite3.connect('database.db')
        self.cursor_sqlite3 = self.connect_sqlite3.cursor()

        self.cursor_sqlite3.execute("SELECT EXISTS(SELECT 1 FROM date_users WHERE id = 1)")
        result = self.cursor_sqlite3.fetchone()[0]
        # print(result)
        if result == 1:
            query = "UPDATE date_users SET count_threds = ? WHERE id = ?"
            values = (int(self.ui.tredsSpinBox.text()), 1)
            # print(type(int(self.ui.tredsSpinBox.text())))
        elif result == 0:
            query = "INSERT INTO date_users (count_threds) VALUES (?)"
            values = (int(self.ui.tredsSpinBox.text()))
        self.cursor_sqlite3.execute(query, values)
        self.connect_sqlite3.commit()
        self.cursor_sqlite3.close()
        self.connect_sqlite3.close()
        self.signals.signal_emit_count_thred.emit(int(self.ui.tredsSpinBox.text()))


    def chek_connect_db(self):
        db_connect_data = {
            "host": self.ui.lineEdit_db_host.text(),
            "port": self.ui.lineEdit_db_port.text(),
            "user": self.ui.lineEdit_db_user.text(),
            "db_password": self.ui.lineEdit_db_password.text(),
            "db_name": self.ui.lineEdit_db_name.text(),
            "count_threds": self.ui.tredsSpinBox.text()
        }
        self.connect_sqlite3 = sqlite3.connect('database.db')
        self.cursor_sqlite3 = self.connect_sqlite3.cursor()
        self.cursor_sqlite3.execute('''CREATE TABLE IF NOT EXISTS date_users 
        (
            id INTEGER PRIMARY KEY, 
            host VARCHAR, 
            port INTEGER, 
            user TEXT, 
            db_password TEXT, 
            db_name TEXT,
            count_threds INTEGER,
            path_to_file_links TEXT
        )'''
                            )
        self.cursor_sqlite3.execute("SELECT EXISTS(SELECT 1 FROM date_users WHERE id = 1)")
        result = self.cursor_sqlite3.fetchone()[0]
        # print(result)
        if result == 1:
            query = "UPDATE date_users SET " \
                    "host = ?," \
                    "port = ?," \
                    "user = ?," \
                    "db_password = ?," \
                    "db_name = ?" \
                    "WHERE id = ?"

            values = (
                f'{self.ui.lineEdit_db_host.text()}',
                f'{self.ui.lineEdit_db_port.text()}',
                f'{self.ui.lineEdit_db_user.text()}',
                f'{self.ui.lineEdit_db_password.text()}',
                f'{self.ui.lineEdit_db_name.text()}',
                1
            )
            # print("UPDATE date_users SET")
        elif result == 0:
            query = "INSERT INTO date_users " \
                    "(host, port, user, db_password, db_name) " \
                    "VALUES (?, ?, ?, ?, ?)"
            values = (
                f'{self.ui.lineEdit_db_host.text()}',
                f'{self.ui.lineEdit_db_port.text()}',
                f'{self.ui.lineEdit_db_user.text()}',
                f'{self.ui.lineEdit_db_password.text()}',
                f'{self.ui.lineEdit_db_name.text()}'
            )
        self.cursor_sqlite3.execute(query, values)
        self.connect_sqlite3.commit()
        self.cursor_sqlite3.close()
        self.connect_sqlite3.close()

        self.ui.btn_test_db.setEnabled(False)
        self.ui.btn_test_db.setText("Тестирую")
        self.ui.btn_test_db.repaint()  # перерисовывает кнопку
        # self.ui.btn_test_db.setCursor(Qt.WaitCursor)

        self.chek_connect = db_connect()
        if self.chek_connect['connect'] == True:
            self.ui.label_test_db.setText("Есть контакт")
            self.ui.label_test_db.setStyleSheet("color: rgb(0, 170, 127);")
        else:
            self.ui.label_test_db.setText("Нет соеденения")
            self.ui.label_test_db.setStyleSheet("color: rgb(255, 0, 0);")

        self.ui.btn_test_db.setEnabled(True)
        self.ui.btn_test_db.setText("Тест соеденения")
        # self.ui.btn_test_db.setCursor(Qt.PointingHandCursor)

        # with open('data/db_connect_data.json', 'w', encoding="utf-8") as f:
        #     json.dump(db_connect_data, f)

    def path_to_file(self):  # Открыть окно выбора файла
        self.fname = QFileDialog.getOpenFileName(
            self,
            "Открыть файл",
            "",
            "*.txt"
        )
        if self.fname:
            self.ui.lineEdit_find_file.setText(self.fname[0])

            self.connect_sqlite3 = sqlite3.connect('database.db')
            self.cursor_sqlite3 = self.connect_sqlite3.cursor()
            self.cursor_sqlite3.execute('''CREATE TABLE IF NOT EXISTS date_users 
                    (
                        id INTEGER PRIMARY KEY, 
                        host VARCHAR, 
                        port INTEGER, 
                        user TEXT, 
                        db_password TEXT, 
                        db_name TEXT,
                        count_threds INTEGER,
                        path_to_file_links TEXT
                    )'''
                                        )
            query = "UPDATE date_users SET path_to_file_links = ? WHERE id = ?"
            values = (self.fname[0], 1)
            self.cursor_sqlite3.execute(query, values)
            self.connect_sqlite3.commit()
            self.cursor_sqlite3.close()
            self.connect_sqlite3.close()


