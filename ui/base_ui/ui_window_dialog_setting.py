# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_window_dialog_setting.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_WindowDialogSetting(object):
    def setupUi(self, WindowDialogSetting):
        if not WindowDialogSetting.objectName():
            WindowDialogSetting.setObjectName(u"WindowDialogSetting")
        WindowDialogSetting.setWindowModality(Qt.ApplicationModal)
        WindowDialogSetting.resize(390, 430)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WindowDialogSetting.sizePolicy().hasHeightForWidth())
        WindowDialogSetting.setSizePolicy(sizePolicy)
        WindowDialogSetting.setMinimumSize(QSize(390, 430))
        WindowDialogSetting.setMaximumSize(QSize(390, 430))
        WindowDialogSetting.setModal(True)
        self.horizontalLayout_9 = QHBoxLayout(WindowDialogSetting)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(3, 3, 3, 3)
        self.groupBox = QGroupBox(WindowDialogSetting)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 1, 381, 421))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, -1, 5, -1)
        self.groupBox_2 = QGroupBox(self.layoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 9)
        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 0, 0, 0)
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_db_host = QLineEdit(self.groupBox_3)
        self.lineEdit_db_host.setObjectName(u"lineEdit_db_host")
        sizePolicy.setHeightForWidth(self.lineEdit_db_host.sizePolicy().hasHeightForWidth())
        self.lineEdit_db_host.setSizePolicy(sizePolicy)
        self.lineEdit_db_host.setMinimumSize(QSize(264, 0))

        self.horizontalLayout.addWidget(self.lineEdit_db_host)


        self.verticalLayout_3.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_db_port = QLineEdit(self.groupBox_4)
        self.lineEdit_db_port.setObjectName(u"lineEdit_db_port")
        sizePolicy.setHeightForWidth(self.lineEdit_db_port.sizePolicy().hasHeightForWidth())
        self.lineEdit_db_port.setSizePolicy(sizePolicy)
        self.lineEdit_db_port.setMinimumSize(QSize(264, 0))

        self.horizontalLayout_2.addWidget(self.lineEdit_db_port)


        self.verticalLayout_3.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 0, 0, 0)
        self.label_3 = QLabel(self.groupBox_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setLineWidth(1)
        self.label_3.setMidLineWidth(0)
        self.label_3.setWordWrap(False)
        self.label_3.setMargin(0)
        self.label_3.setOpenExternalLinks(False)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_db_user = QLineEdit(self.groupBox_5)
        self.lineEdit_db_user.setObjectName(u"lineEdit_db_user")
        sizePolicy.setHeightForWidth(self.lineEdit_db_user.sizePolicy().hasHeightForWidth())
        self.lineEdit_db_user.setSizePolicy(sizePolicy)
        self.lineEdit_db_user.setMinimumSize(QSize(264, 0))

        self.horizontalLayout_3.addWidget(self.lineEdit_db_user)


        self.verticalLayout_3.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.groupBox_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 0, 0, 0)
        self.label_4 = QLabel(self.groupBox_6)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit_db_password = QLineEdit(self.groupBox_6)
        self.lineEdit_db_password.setObjectName(u"lineEdit_db_password")
        sizePolicy.setHeightForWidth(self.lineEdit_db_password.sizePolicy().hasHeightForWidth())
        self.lineEdit_db_password.setSizePolicy(sizePolicy)
        self.lineEdit_db_password.setMinimumSize(QSize(264, 0))

        self.horizontalLayout_4.addWidget(self.lineEdit_db_password)


        self.verticalLayout_3.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.groupBox_2)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 0, 0, 0)
        self.label_5 = QLabel(self.groupBox_7)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.lineEdit_db_name = QLineEdit(self.groupBox_7)
        self.lineEdit_db_name.setObjectName(u"lineEdit_db_name")
        sizePolicy.setHeightForWidth(self.lineEdit_db_name.sizePolicy().hasHeightForWidth())
        self.lineEdit_db_name.setSizePolicy(sizePolicy)
        self.lineEdit_db_name.setMinimumSize(QSize(264, 0))

        self.horizontalLayout_5.addWidget(self.lineEdit_db_name)


        self.verticalLayout_3.addWidget(self.groupBox_7)

        self.groupBox_8 = QGroupBox(self.groupBox_2)
        self.groupBox_8.setObjectName(u"groupBox_8")
        sizePolicy1.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy1)
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_6.setSpacing(80)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_test_db = QPushButton(self.groupBox_8)
        self.btn_test_db.setObjectName(u"btn_test_db")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_test_db.sizePolicy().hasHeightForWidth())
        self.btn_test_db.setSizePolicy(sizePolicy2)
        self.btn_test_db.setMinimumSize(QSize(0, 30))
        self.btn_test_db.setBaseSize(QSize(0, 30))
        self.btn_test_db.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.btn_test_db)

        self.label_test_db = QLabel(self.groupBox_8)
        self.label_test_db.setObjectName(u"label_test_db")

        self.horizontalLayout_6.addWidget(self.label_test_db)


        self.verticalLayout_3.addWidget(self.groupBox_8)


        self.verticalLayout.addWidget(self.groupBox_2)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.groupBox_12 = QGroupBox(self.layoutWidget)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.btn_save_total_threds = QPushButton(self.groupBox_12)
        self.btn_save_total_threds.setObjectName(u"btn_save_total_threds")
        self.btn_save_total_threds.setGeometry(QRect(290, 3, 75, 23))
        self.tredsSpinBox = QSpinBox(self.groupBox_12)
        self.tredsSpinBox.setObjectName(u"tredsSpinBox")
        self.tredsSpinBox.setGeometry(QRect(200, 3, 71, 21))
        self.label_6 = QLabel(self.groupBox_12)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(7, 3, 159, 23))
        self.label_6.setMargin(2)
        self.label_6.setIndent(1)

        self.verticalLayout_5.addWidget(self.groupBox_12)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, -1, 5, -1)
        self.groupBox_9 = QGroupBox(self.layoutWidget)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 9)
        self.btn_find_file = QPushButton(self.groupBox_9)
        self.btn_find_file.setObjectName(u"btn_find_file")
        self.btn_find_file.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_7.addWidget(self.btn_find_file)

        self.lineEdit_find_file = QLineEdit(self.groupBox_9)
        self.lineEdit_find_file.setObjectName(u"lineEdit_find_file")

        self.horizontalLayout_7.addWidget(self.lineEdit_find_file)


        self.verticalLayout_4.addWidget(self.groupBox_9)

        self.groupBox_10 = QGroupBox(self.layoutWidget)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox_11 = QGroupBox(self.groupBox_10)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_parser_password = QPushButton(self.groupBox_11)
        self.pushButton_parser_password.setObjectName(u"pushButton_parser_password")
        self.pushButton_parser_password.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_8.addWidget(self.pushButton_parser_password)

        self.lineEdit_parser_password = QLineEdit(self.groupBox_11)
        self.lineEdit_parser_password.setObjectName(u"lineEdit_parser_password")

        self.horizontalLayout_8.addWidget(self.lineEdit_parser_password)


        self.verticalLayout_2.addWidget(self.groupBox_11)

        self.label_7 = QLabel(self.groupBox_10)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMargin(3)

        self.verticalLayout_2.addWidget(self.label_7)

        self.label_8 = QLabel(self.groupBox_10)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setMargin(3)

        self.verticalLayout_2.addWidget(self.label_8)


        self.verticalLayout_4.addWidget(self.groupBox_10)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.horizontalLayout_9.addWidget(self.groupBox)


        self.retranslateUi(WindowDialogSetting)

        QMetaObject.connectSlotsByName(WindowDialogSetting)
    # setupUi

    def retranslateUi(self, WindowDialogSetting):
        WindowDialogSetting.setWindowTitle(QCoreApplication.translate("WindowDialogSetting", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.groupBox.setTitle("")
        self.groupBox_2.setTitle(QCoreApplication.translate("WindowDialogSetting", u"\u0414\u043e\u0441\u0442\u0443\u043f \u043a \u0431\u0430\u0437\u0435", None))
        self.groupBox_3.setTitle("")
        self.label.setText(QCoreApplication.translate("WindowDialogSetting", u"   DB_HOST", None))
        self.groupBox_4.setTitle("")
        self.label_2.setText(QCoreApplication.translate("WindowDialogSetting", u"      port", None))
        self.groupBox_5.setTitle("")
        self.label_3.setText(QCoreApplication.translate("WindowDialogSetting", u"      user", None))
        self.groupBox_6.setTitle("")
        self.label_4.setText(QCoreApplication.translate("WindowDialogSetting", u"DB_PASSWORD", None))
        self.groupBox_7.setTitle("")
        self.label_5.setText(QCoreApplication.translate("WindowDialogSetting", u"    DB_NAME", None))
        self.groupBox_8.setTitle("")
        self.btn_test_db.setText(QCoreApplication.translate("WindowDialogSetting", u"\u0422\u0435\u0441\u0442 \u0441\u043e\u0435\u0434\u0435\u043d\u0435\u043d\u0438\u044f", None))
        self.label_test_db.setText(QCoreApplication.translate("WindowDialogSetting", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u0442\u0435\u0441\u0442\u0430", None))
        self.groupBox_12.setTitle("")
        self.btn_save_total_threds.setText(QCoreApplication.translate("WindowDialogSetting", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label_6.setText(QCoreApplication.translate("WindowDialogSetting", u"\u0421\u043a\u043e\u043b\u044c\u043a\u043e \u043f\u043e\u0442\u043e\u043a\u043e\u0432 \u0437\u0430\u043f\u0443\u0441\u043a\u0430\u0442\u044c?", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("WindowDialogSetting", u"\u0424\u0430\u0439\u043b \u0441 \u0441\u0441\u044b\u043b\u043a\u0430\u043c\u0438", None))
        self.btn_find_file.setText(QCoreApplication.translate("WindowDialogSetting", u"\u041e\u0431\u0437\u043e\u0440", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("WindowDialogSetting", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.groupBox_11.setTitle("")
        self.pushButton_parser_password.setText(QCoreApplication.translate("WindowDialogSetting", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.label_7.setText(QCoreApplication.translate("WindowDialogSetting", u"\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u043d\u0430\u044f \u0432\u0435\u0440\u0441\u0438\u044f. \u041f\u043e\u0441\u043b\u0435 \u043d\u0430\u0436\u0430\u0442\u0438\u044f \u043d\u0430 \u0441\u0442\u0430\u0440\u0442 \u0434\u0435\u043b\u0430\u0435\u0442 \u043e\u0434\u043d\u0443 \u0441\u0441\u044b\u043b\u043a\u0443.", None))
        self.label_8.setText(QCoreApplication.translate("WindowDialogSetting", u"\u0414\u043b\u044f \u0441\u043d\u044f\u0442\u0438\u044f \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0439 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c.", None))
    # retranslateUi

