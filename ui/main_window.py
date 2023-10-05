import sqlite3
from PySide6.QtWidgets import QMainWindow, QDialog
from PySide6.QtCore import Slot, Signal, QObject, QRunnable, QThreadPool, QTime
import time
import logging
from ui.base_ui.ui_main_window import Ui_MainWindow
from ui.base_ui.ui_help_window import Ui_HelpWindow
from ui.window_dialog_setting import WindowDialogSetting
from ui.progress_bar import ProgressBar
# from parser import *
# from data.variables import *

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


with open('data/trustpilot.txt', 'r', encoding='utf-8') as f_read:
    url_list = f_read.read().split('\n')
if len(url_list) > 0:
    pass
else:
    print("ссылки закончились")


class Signals(QObject):
    signal_progress_update = Signal(list)


class WorkerThread(QRunnable):
    def __init__(self, index_thred):
        super().__init__()
        self.index_thred = index_thred
        self.signals = Signals()
        self.work_thread = True

    def run(self):
        # TODO: Прикрутить сюда парсер
        for url in url_list:
            url_list.remove(url)
            data_work = [self.index_thred, url, 0, "этап"]
            for i in range(100):
                if i == 100:
                    break
                else:
                    for stage in range(1, 4):
                        if self.work_thread == False:
                            return
                        else:
                            data_work[2] = i
                            data_work[3] = f"этап {stage}"
                            self.signals.signal_progress_update.emit(data_work)
                            delay = QTime(0, 0).msecsTo(QTime.currentTime())
                            delay = abs(delay) % 10  # Ограничиваем задержку до 10 миллисекунд
                            time.sleep(delay / 1000)  # Преобразуем задержку в секунды
                        if self.work_thread == False:
                            return

    def stop(self):
        self.work_thread = False


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.threadpool = QThreadPool.globalInstance()
        self.connect_sqlite3 = sqlite3.connect('database.db')
        self.cursor_sqlite3 = self.connect_sqlite3.cursor()
        self.cursor_sqlite3.execute("SELECT count_threds FROM date_users WHERE id = 1")
        self.quantity_thread = self.cursor_sqlite3.fetchone()[0]  # получил количество потоков из базы
        self.cursor_sqlite3.close()
        self.connect_sqlite3.close()

        self.ui.label_total_streams.setText(f"Всего потоков: {self.quantity_thread}")
        self.Max_Thread_Count = self.threadpool.maxThreadCount()  # Рекомендуемое количество потоков
        self.ui.label_recommended_streams.setText(f"Рекомендуемое число потоков: {self.Max_Thread_Count}")


        # привязать к кнопкам слоты
        self.ui.btn_start.clicked.connect(self.start_jobs)
        self.ui.btn_stop.clicked.connect(self.stop_jobs)
        self.ui.action_help.triggered.connect(self.show_help_window)
        self.ui.action_setting.triggered.connect(self.show_window_dialog_setting)

        self.threadpool.setMaxThreadCount(self.quantity_thread)  # во сколько потоков работать

        self.screen = self.screen()
        self.screen_height = self.screen.geometry().height()  # высота монитора
        self.size_height_window()

    def size_height_window(self):
        self.total_for_widgets = (self.quantity_thread * 70)+240  # окно под виджеты
        if self.screen_height - 100 < self.total_for_widgets:
            self.total_for_widgets = self.screen_height - 100
        self.resize(self.width(), self.total_for_widgets)

    @Slot()
    def start_jobs(self):
        self.ui.btn_start.setEnabled(False)
        self.ui.btn_start.setToolTip("Нехуй сюда тыкать по 100 раз.\n Не видишь работаю")
        self.progress_bars = []
        self.threads = []
        i = 0
        while i < self.quantity_thread:
            i += 1
            self.progress_bar = ProgressBar()
            self.ui.verticalLayout_scroll_area.addWidget(self.progress_bar)
            self.progress_bars.append(self.progress_bar)
            self.index_thred = len(self.progress_bars)
            self.thread_parser = WorkerThread(self.index_thred - 1)
            self.threadpool.start(self.thread_parser)
            self.threads.append(self.thread_parser)
            self.thread_parser.signals.signal_progress_update.connect(self.update_progress)
        self.ui.btn_start.setEnabled(True)

    @Slot()
    def stop_jobs(self):
        # logging.info(f"Нажата кнопка стоп")
        for thread in self.threads:
            thread.stop()
            # logging.info(f"удалил поток")

        for progress_bar in self.progress_bars:
            progress_bar.deleteLater()




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
        self.window_dialog_setting.signals.signal_emit_count_thred.connect(self.set_total_streams)

    @Slot()
    def set_total_streams(self, total_streams):
        self.total_streams = total_streams
        self.ui.label_total_streams.setText(f"Всего потоков: {self.total_streams}")
        self.quantity_thread = self.total_streams
        self.size_height_window()



    # TODO: сделать диалоговое окно которое будет отображать ошибки
    # TODO: без пароля при каждом нажатии на старт делает одну ссылку

