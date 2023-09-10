import asyncio
import data.variables
import sqlite3

import ui.progress_bar
from PySide6.QtWidgets import QMainWindow, QDialog, QProgressBar, QToolTip, QWidget, QApplication
from PySide6.QtCore import Slot, Signal, QObject, QThread, QRunnable, QThreadPool, QTime, QElapsedTimer
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


class Signals(QObject):
    signal_started = Signal(int)
    signal_stop = Signal(str)
    create_progress_bar = Signal(object)
    # signal_progress_update = Signal(int)
    signal_progress_update = Signal(list)


class WorkerThread(QRunnable):
    def __init__(self, url, name):  #, ui_obj
        super().__init__()
        self.progress_bar_name = name
        self.thred_name = name
        self.signals = Signals()
        self.is_running = True

    def run(self):
        data_work = [self.progress_bar_name, 0, "w"]
        i = 0
        while True:
        # while self.is_running == True:
            i+=1
            if i == 100:
                # Дать сигнал на удаление self.progress_bar и остановку потока
                self.signals.signal_stop.emit(self.thred_name)
                # QThreadPool.globalInstance().releaseThread()
            try:
                for stage in range(1, 4):
                    data_work[1] = i
                    data_work[2] = f"этап {stage}"
                    self.signals.signal_progress_update.emit(data_work)
                    delay = QTime(0, 0).msecsTo(QTime.currentTime())
                    delay = abs(delay) % 10  # Ограничиваем задержку до 10 миллисекунд
                    time.sleep(delay / 1000)  # Преобразуем задержку в секунды
            except:
                pass
        # print(self.thred_name)

    def stop(self):
        # self.is_running = False
        QThreadPool.globalInstance().releaseThread()


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        with open('data/trustpilot.txt', 'r', encoding='utf-8') as f_read:
            self.url_list = f_read.read().split('\n')
        if len(self.url_list) > 0:
            pass
        else:
            print("ссылки закончились")

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
        self.threadpool.setMaxThreadCount(3)
        self.running_threads = self.threadpool.activeThreadCount()
        # while True:
        for url in self.url_list[0:3]:
            self.name = url.split('/')[-1].replace('.', '_')
            self.progress_bar = ProgressBar()
            self.progress_bar.setObjectName(self.name)
            self.ui.verticalLayout_scroll_area.addWidget(self.progress_bar)
            logging.info(f"создан progress_bar {self.name}")
            self.thread_parser = WorkerThread(url, self.name)  #, self.ui
            self.threadpool.start(self.thread_parser)
            # logging.info(f"запущен поток {self.name}")
            # print("Количество работающих потоков в for:", self.running_threads)
            self.thread_parser.signals.signal_progress_update.connect(self.update_progress)
            self.thread_parser.signals.signal_stop.connect(self.stop_thred)
            self.running_threads = self.threadpool.activeThreadCount()
            # logging.info(f"количество потоков в for {self.running_threads}")
            self.url_list.remove(url)
        self.ui.btn_start.setEnabled(True)

    @Slot()
    def stop_thred(self, name):
        self.progress_bar = self.findChild(QWidget, name)
        self.progress_bar.deleteLater()
        self.thread_parser.stop()
        # print(f"поток остановлен {name}")
        logging.info(f"поток остановлен {name}")
        # self.thread_parser.quit()


    @Slot()
    def update_progress(self, update):
        self.name = update[0]
        # logging.info(f"получил обновление для {self.name}")
        self.widget_progress_bar = self.findChild(QWidget, self.name)
        if self.widget_progress_bar != None:
            self.widget_progress_bar.ui.progressBar.setValue(update[1])
            self.widget_progress_bar.ui.groupBox.setTitle(update[0])
            self.widget_progress_bar.ui.label_action.setText(update[2])  # Что делаем
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

