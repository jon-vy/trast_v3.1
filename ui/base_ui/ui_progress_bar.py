# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_progress_bar.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QProgressBar, QSizePolicy, QVBoxLayout, QWidget)

class Ui_WidgetProgresBar(object):
    def setupUi(self, WidgetProgresBar):
        if not WidgetProgresBar.objectName():
            WidgetProgresBar.setObjectName(u"WidgetProgresBar")
        WidgetProgresBar.resize(500, 70)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WidgetProgresBar.sizePolicy().hasHeightForWidth())
        WidgetProgresBar.setSizePolicy(sizePolicy)
        WidgetProgresBar.setMinimumSize(QSize(500, 70))
        WidgetProgresBar.setMaximumSize(QSize(16777213, 70))
        self.horizontalLayout = QHBoxLayout(WidgetProgresBar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.groupBox = QGroupBox(WidgetProgresBar)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 4)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.progressBar = QProgressBar(self.groupBox)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setInvertedAppearance(False)

        self.verticalLayout.addWidget(self.progressBar)

        self.label_action = QLabel(self.groupBox)
        self.label_action.setObjectName(u"label_action")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_action.sizePolicy().hasHeightForWidth())
        self.label_action.setSizePolicy(sizePolicy1)
        self.label_action.setFont(font)

        self.verticalLayout.addWidget(self.label_action)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout.addWidget(self.groupBox)


        self.retranslateUi(WidgetProgresBar)

        QMetaObject.connectSlotsByName(WidgetProgresBar)
    # setupUi

    def retranslateUi(self, WidgetProgresBar):
        WidgetProgresBar.setWindowTitle(QCoreApplication.translate("WidgetProgresBar", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("WidgetProgresBar", u"Link", None))
        self.label_action.setText(QCoreApplication.translate("WidgetProgresBar", u"\u0427\u0442\u043e \u0434\u0435\u043b\u0430\u0435\u0442\u0441\u044f", None))
    # retranslateUi

