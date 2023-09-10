from PySide6.QtWidgets import QMainWindow, QDialog, QProgressBar
from PySide6.QtCore import Slot, Signal, QObject, QThread, QRunnable, QThreadPool
import time
import sys
import random

from ui.base_ui.ui_main_window import Ui_MainWindow
from ui.base_ui.ui_help_window import Ui_HelpWindow
from ui.window_dialog_setting import WindowDialogSetting
from ui.progress_bar import ProgressBar
# from parser import parser_url

class Signals(QObject):
    signal_started = Signal(int)
    signal_completed = Signal(int)
    signal_progress_update = Signal(list)

class WorkerThread(QRunnable):
    def __init__(self, id):
        super().__init__()
        self.id = id
        self.signals = Signals()

    def run(self):
        # self.signals.signal_started.emit(self.id)
        for i in range(101):
            data = [self.id, i]
            self.signals.signal_progress_update.emit(data)
            # print(self.id, i)
            # self.msleep(random.uniform(0, .01))
            # time.sleep(.01)
            time.sleep(random.uniform(0, .01))
        self.signals.signal_completed.emit(self.id)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # привязать к кнопкам слоты
        self.ui.btn_start.clicked.connect(self.start_jobs)
        self.ui.action_help.triggered.connect(self.show_help_window)
        self.ui.action_setting.triggered.connect(self.show_window_dialog_setting)



    def start_jobs(self):

        pool = QThreadPool.globalInstance()
        # progress_bar = QProgressBar(self)
        # progress_bar.delete.connect(self.delete_progress_bar_widget)
        for id in range(0, 6):
            print(f"создание прогресс бара {id}")
            progress_bar = ProgressBar()
            self.ui.verticalLayout_scroll_area.addWidget(progress_bar)
            worker = WorkerThread(id)
            worker.signals.signal_progress_update.connect(self.update_progress)
            # worker.signals.signal_completed.connect(self.complete)
            # worker.signals.completed.connect(self.complete)
            # worker.signals.started.connect(self.start)
            pool.start(worker)

    @Slot()
    def update_progress(self, data):
        id, value = data[0], data[1]
        # print(f"{data} ")
        widget_progress_bar = self.ui.verticalLayout_scroll_area.itemAt(id).widget()
        widget_progress_bar.ui.progressBar.setValue(value)




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

