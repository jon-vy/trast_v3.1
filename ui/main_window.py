import asyncio
import sqlite3

import ui.progress_bar
from PySide6.QtWidgets import QMainWindow, QDialog, QProgressBar, QToolTip, QWidget, QApplication
from PySide6.QtCore import Slot, Signal, QObject, QThread, QRunnable, QThreadPool
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
        filemode="w",  # чистит файл при каждом запуске
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
    signal_finish = Signal(list)
    create_progress_bar = Signal(object)
    # signal_progress_update = Signal(int)
    signal_progress_update = Signal(list)


class WorkerThread(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = Signals()
        # self.url = self.get_url()


    def setParams(self, url, index):
        self.url = url
        self.index = index
        # self.progress_bar = progress_bar

    def run(self):
        # self.progress_bar = ProgressBar()
        # self.progress_bar.setObjectName(self.progress_bar_name)
        # print(f"что отправил {self.progress_bar}")
        # MainWindow.window(self).ui.verticalLayout_scroll_area.addWidget(self.progress_bar)
        # self.ui_obj.verticalLayout_scroll_area.addWidget(self.progress_bar)
        # self.signals.create_progress_bar.emit(self.progress_bar)
        logging.info(f"принял url в run {self.thread} {self.url}")
        self.name = self.url.split('/')[-1].replace('.', '_')
        data_work = [self.progress_bar, self.url, 0, "этап"]
        i = 0
        while True:
            i+=1
            if i == 100:
                i = 0
                # break
                # Дать сигнал об окончании работы потока
                self.data_finish = [self.progress_bar, self.thread]
                self.signals.signal_finish.emit(self.data_finish)
                # QThreadPool.globalInstance().releaseThread()
            time.sleep(random.uniform(0, 0.01))
            data_work[2] = i
            data_work[3] = "этап 1"
            self.signals.signal_progress_update.emit(data_work)
            # time.sleep(random.uniform(0, 0.01))
            # data_work[3] = "этап 2"
            # self.signals.signal_progress_update.emit(data_work)
            # time.sleep(random.uniform(0, 0.01))
            # data_work[3] = "этап 3"
            # self.signals.signal_progress_update.emit(data_work)
            logging.info(f"отправил обновление {data_work}")

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

        self.connect_sqlite3 = sqlite3.connect('database.db')
        self.cursor_sqlite3 = self.connect_sqlite3.cursor()
        self.cursor_sqlite3.execute("SELECT count_threds FROM date_users WHERE id = 1")
        self.quantity_ProgressBar = self.cursor_sqlite3.fetchone()[0]
        self.cursor_sqlite3.close()
        self.connect_sqlite3.close()
        self.ui.total_streams.setText(str(self.quantity_ProgressBar))

        # привязать к кнопкам слоты
        self.ui.btn_start.clicked.connect(self.start_jobs)
        self.ui.action_help.triggered.connect(self.show_help_window)
        self.ui.action_setting.triggered.connect(self.show_window_dialog_setting)



    def start_jobs(self):
        self.ui.btn_start.setEnabled(False)
        self.ui.btn_start.setToolTip("Нехуй сюда тыкать по 100 раз.\n Не видишь работаю")

        self.threadpool = QThreadPool.globalInstance()
        # self.threadpool.setMaxThreadCount(3)
        # self.running_threads = self.threadpool.activeThreadCount()
        self.threads = []
        self.progress_bars = []
        for i in range(3):
        # for i in range(self.threadpool.maxThreadCount()):
            self.progress_bar = ProgressBar()
            self.ui.verticalLayout_scroll_area.addWidget(self.progress_bar)
            self.progress_bars.append(self.progress_bar)

            self.thread_parser = WorkerThread()
            self.threads.append(self.thread_parser)
            # self.thread_parser.setParams("Ждём ссылку", len(self.threads))
            self.threadpool.start(self.thread_parser)

            logging.info(f"создан progress_bar + поток {self.index}")

        self.index = 0
        for url in self.url_list: # [0:3]
            if self.index != len(self.threads):
                self.threads[self.index].setParams(url, self.index)
                self.index += 1
            else:
                while True:
                    for thread in self.threads:
                        self.thread.signals.signal_progress_update.connect(self.update_progress)
                        self.thread.signals.signal_finish.connect(self.get_finish_thread)
        #     logging.info(f"Отправил url {self.index} {url} ")
        #     if self.index == len(self.threads):
        #         while True:
        #             time.sleep(random.random(0.03))
        #             for i, self.thread in enumerate(self.threads):
        #                 logging.info(f"Проверяю обновление для потока № {i}")
        #                 self.thread.signals.signal_progress_update.connect(self.update_progress)
        #                 # self.thread.signals.signal_finish.connect(self.get_finish_thread)
        #     else:
                # Добавил в поток параметры
                # self.threads[self.tndex].setParams(url, self.index, self.progress_bars[self.index])
                # self.threadpool.start(self.threads[self.index])
                # self.index += 1


            # self.thread = 0
            # self.thread = 0
            # self.name = url.split('/')[-1].replace('.', '_')

        #     self.progress_bar.setObjectName(self.name)
        #     # logging.info(f"запущен поток {self.name}")
        #     # print("Количество работающих потоков в for:", self.running_threads)
        #
        #     # self.thread_parser.signals.signal_stop.connect(self.stop_thred)
        #     # self.running_threads = self.threadpool.activeThreadCount()
        #     # logging.info(f"количество потоков в for {self.running_threads}")
        #     self.url_list.remove(url)
        self.ui.btn_start.setEnabled(True)
    def get_finish_thread(self, finish_thread):
        self.finish_thread = finish_thread
    @Slot()
    def stop_thred(self, name):
        self.progress_bar = self.findChild(QWidget, name)
        self.progress_bar.deleteLater()
        self.thread_parser.stop()
        # print(f"поток остановлен {name}")
        logging.info(f"поток остановлен {name}")
        # self.thread_parser.quit()


    @Slot()
    #data_work = [self.progress_bar, self.url, 0, "этап"]
    def update_progress(self, update):
        logging.info(f"получил обновление для {update}")
        self.widget_progress_bar = update[0]
        self.widget_progress_bar.ui.progressBar.setValue(update[2])
        self.widget_progress_bar.ui.groupBox.setTitle(update[1])
        self.widget_progress_bar.ui.label_action.setText(update[3])  # Что делаем

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

