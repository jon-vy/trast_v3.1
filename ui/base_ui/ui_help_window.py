# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_help_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QSizePolicy, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_HelpWindow(object):
    def setupUi(self, HelpWindow):
        if not HelpWindow.objectName():
            HelpWindow.setObjectName(u"HelpWindow")
        HelpWindow.setWindowModality(Qt.ApplicationModal)
        HelpWindow.resize(460, 290)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(HelpWindow.sizePolicy().hasHeightForWidth())
        HelpWindow.setSizePolicy(sizePolicy)
        HelpWindow.setMinimumSize(QSize(460, 290))
        HelpWindow.setMaximumSize(QSize(460, 290))
        HelpWindow.setModal(True)
        self.verticalLayout = QVBoxLayout(HelpWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser = QTextBrowser(HelpWindow)
        self.textBrowser.setObjectName(u"textBrowser")
        font = QFont()
        font.setPointSize(14)
        self.textBrowser.setFont(font)

        self.verticalLayout.addWidget(self.textBrowser)


        self.retranslateUi(HelpWindow)

        QMetaObject.connectSlotsByName(HelpWindow)
    # setupUi

    def retranslateUi(self, HelpWindow):
        HelpWindow.setWindowTitle(QCoreApplication.translate("HelpWindow", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
        self.textBrowser.setHtml(QCoreApplication.translate("HelpWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041e\u0442\u0447\u0435 \u043d\u0430\u0448 \u0441\u0443\u0449\u0438\u0439 \u043d\u0430 \u043d\u0435\u0431\u0435\u0441\u0430\u0445! </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0414\u0430 \u0441\u0432\u044f\u0442\u0438\u0442\u0441\u044f \u0438\u043c\u044f \u0422\u0432\u043e\u0451, </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0434\u0430 \u043f\u0440\u0438\u0438\u0434\u0435\u0442 \u0426\u0430"
                        "\u0440\u0441\u0442\u0432\u0438\u0435 \u0422\u0432\u043e\u0451,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0434\u0430 \u0431\u0443\u0434\u0435\u0442 \u0432\u043e\u043b\u044f \u0422\u0432\u043e\u044f \u0438 \u043d\u0430 \u0437\u0435\u043c\u043b\u0435 \u043a\u0430\u043a \u043d\u0430 \u043d\u0435\u0431\u0435,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0445\u043b\u0435\u0431 \u043d\u0430\u0448 \u043d\u0430\u0441\u0443\u0449\u043d\u044b\u0439 \u0434\u0430\u0439 \u043d\u0430\u043c \u043d\u0430 \u0441\u0435\u0439 \u0434\u0435\u043d\u044c,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0438 \u043f\u0440\u043e\u0441\u0442\u0438 \u043d\u0430\u043c \u0434\u043e\u043b\u0433\u0438 \u043d\u0430\u0448\u0438 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-l"
                        "eft:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u043a\u0430\u043a \u0438 \u043c\u044b \u043f\u0440\u043e\u0449\u0430\u0435\u043c \u0434\u043e\u043b\u0436\u043d\u0438\u043a\u0430\u043c \u043d\u0430\u0448\u0438\u043c,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0438 \u043d\u0435 \u0432\u0432\u0435\u0434\u0438 \u043d\u0430\u0441 \u0432 \u0438\u0441\u043a\u0443\u0448\u0435\u043d\u0438\u0435,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u043d\u043e \u0438\u0437\u0431\u0430\u0432\u044c \u043d\u0430\u0441 \u043e\u0442 \u043b\u0443\u043a\u0430\u0432\u043e\u0433\u043e.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0418\u0431\u043e \u0422\u0432\u043e\u0451 \u0435\u0441\u0442\u044c \u0426\u0430\u0440\u0441\u0442\u0432\u043e \u0438 \u0441\u0438\u043b\u0430"
                        " \u0438 \u0441\u043b\u0430\u0432\u0430 \u0432\u043e \u0432\u0435\u043a\u0438. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0410\u043c\u0438\u043d\u044c.</p></body></html>", None))
    # retranslateUi

