import asyncio
import data.variables
import sqlite3

import ui.progress_bar
from PySide6.QtWidgets import QMainWindow, QDialog, QProgressBar, QToolTip, QWidget, QApplication
from PySide6.QtCore import Slot, Signal, QObject, QThread, QRunnable, QThreadPool, QTime
import time
import sys
import random
import logging

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


from ui.base_ui.ui_main_window import Ui_MainWindow
from ui.base_ui.ui_help_window import Ui_HelpWindow
from ui.window_dialog_setting import WindowDialogSetting
from ui.progress_bar import ProgressBar
from parser import *
# from data.variables import *


with open('data/trustpilot.txt', 'r', encoding='utf-8') as f_read:
    url_list = f_read.read().split('\n')
if len(url_list) > 0:
    pass
else:
    print("ссылки закончились")

class Signals(QObject):
    signal_started = Signal(int)
    signal_stop = Signal(str)
    create_progress_bar = Signal(object)
    # signal_progress_update = Signal(int)
    signal_progress_update = Signal(list)


class WorkerThread(QRunnable):
    def __init__(self, index_thred):
        super().__init__()
        self.index_thred = index_thred
        self.signals = Signals()

    def run(self):
        for url in url_list:
            url_list.remove(url)
            data_work = [self.index_thred, url, 0, "этап"]
            for i in range(100):
                if i == 100:
                    break
                else:
                    for stage in range(1, 4):
                        data_work[2] = i
                        data_work[3] = f"этап {stage}"
                        self.signals.signal_progress_update.emit(data_work)
                        delay = QTime(0, 0).msecsTo(QTime.currentTime())
                        delay = abs(delay) % 10  # Ограничиваем задержку до 10 миллисекунд
                        time.sleep(delay / 1000)  # Преобразуем задержку в секунды

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        try:
            self.connect_sqlite3 = sqlite3.connect('database.db')
            self.cursor_sqlite3 = self.connect_sqlite3.cursor()
            self.cursor_sqlite3.execute("SELECT count_threds FROM date_users WHERE id = 1")
            self.quantity_ProgressBar = self.cursor_sqlite3.fetchone()[0]
            self.cursor_sqlite3.close()
            self.connect_sqlite3.close()
            self.ui.total_streams.setText(str(self.quantity_ProgressBar))
        except:
            pass

        # привязать к кнопкам слоты
        self.ui.btn_start.clicked.connect(self.start_jobs)
        self.ui.action_help.triggered.connect(self.show_help_window)
        self.ui.action_setting.triggered.connect(self.show_window_dialog_setting)



    def start_jobs(self):
        self.ui.btn_start.setEnabled(False)
        self.ui.btn_start.setToolTip("Нехуй сюда тыкать по 100 раз.\n Не видишь работаю")

        self.threadpool = QThreadPool.globalInstance()
        self.Max_Thread_Count = 3
        self.threadpool.setMaxThreadCount(self.Max_Thread_Count)
        self.progress_bars = []
        self.threads = []
        i = 0
        while i < 3:
            i+=1
            self.progress_bar = ProgressBar()
            self.ui.verticalLayout_scroll_area.addWidget(self.progress_bar)
            self.progress_bars.append(self.progress_bar)
            self.index_thred = len(self.progress_bars)
            self.thread_parser = WorkerThread(self.index_thred - 1)
            self.threadpool.start(self.thread_parser)
            self.threads.append(self.thread_parser)
            logging.info(f"запущен поток {self.index_thred}")
            self.thread_parser.signals.signal_progress_update.connect(self.update_progress)
        self.ui.btn_start.setEnabled(True)

    @Slot()
    def update_progress(self, update):  # data_work = [self.index_thred, url, 0, "этап"]
        self.index_thred = update[0]
        # logging.info(f"получил обновление для {self.name}")
        self.widget_progress_bar = self.progress_bars[self.index_thred]
        if self.widget_progress_bar != None:
            self.widget_progress_bar.ui.groupBox.setTitle(update[1])
            self.widget_progress_bar.ui.progressBar.setValue(update[2])
            self.widget_progress_bar.ui.label_action.setText(update[3])  # Что делаем
        else:
            pass

    # @Slot()
    # def Create_Progress_Bar(self, progress_bar_object):
    #     self.p_r = progress_bar_object
    #     print(f"что получил {self.p_r}")
    #     self.ui.verticalLayout_scroll_area.addWidget(self.p_r)


    @Slot()
    def show_help_window(self):
        self.help_win = QDialog()
        self.help_window = Ui_HelpWindow()
        self.help_window.setupUi(self.help_win)
        self.help_win.show()

    @Slot()
    def show_window_dialog_setting(self):
        # self.win_dialog_setting = QDialog()
        self.window_dialog_setting = WindowDialogSetting()
        self.window_dialog_setting.show()

