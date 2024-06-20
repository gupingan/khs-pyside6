# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'set_cookies_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_SetCookies(object):
    def setupUi(self, SetCookies):
        if not SetCookies.objectName():
            SetCookies.setObjectName(u"SetCookies")
        SetCookies.resize(363, 191)
        self.verticalLayout = QVBoxLayout(SetCookies)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(SetCookies)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.open_url_btn = QPushButton(SetCookies)
        self.open_url_btn.setObjectName(u"open_url_btn")

        self.horizontalLayout.addWidget(self.open_url_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.cookies_edit = QPlainTextEdit(SetCookies)
        self.cookies_edit.setObjectName(u"cookies_edit")

        self.verticalLayout.addWidget(self.cookies_edit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.cancel_btn = QPushButton(SetCookies)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.horizontalLayout_2.addWidget(self.cancel_btn)

        self.save_btn = QPushButton(SetCookies)
        self.save_btn.setObjectName(u"save_btn")

        self.horizontalLayout_2.addWidget(self.save_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(SetCookies)

        QMetaObject.connectSlotsByName(SetCookies)
    # setupUi

    def retranslateUi(self, SetCookies):
        SetCookies.setWindowTitle(QCoreApplication.translate("SetCookies", u"\u8bbe\u7f6e\u73af\u5883CK", None))
        self.label.setText(QCoreApplication.translate("SetCookies", u"\u8bf7\u586b\u5199\u672c\u5730\u7ea2\u4e66\u7684 Cookies", None))
        self.open_url_btn.setText(QCoreApplication.translate("SetCookies", u"\u70b9\u51fb\u6253\u5f00\u6d4f\u89c8\u5668", None))
        self.cancel_btn.setText(QCoreApplication.translate("SetCookies", u"\u9000\u51fa", None))
        self.save_btn.setText(QCoreApplication.translate("SetCookies", u"\u4fdd\u5b58CK", None))
    # retranslateUi

