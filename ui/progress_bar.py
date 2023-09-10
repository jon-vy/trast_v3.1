from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot, Signal
import time

from ui.base_ui.ui_progress_bar import Ui_WidgetProgresBar

class ProgressBar(QWidget):
    delete = Signal(int)

    def __init__(self):
    # def __init__(self, id_widget:int, parent=None):
    #     super(ProgressBar, self).__init__(parent)
        super().__init__()
        self.ui = Ui_WidgetProgresBar()
        self.ui.setupUi(self)
        # self.id_widget = id_widget
        # self.ui.groupBox.setTitle(str(id_widget))
        # self.ui.label_link.setText(str(self.id_widget))


