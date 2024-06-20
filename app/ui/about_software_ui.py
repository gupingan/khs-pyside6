# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about_software_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_AboutSoftware(object):
    def setupUi(self, AboutSoftware):
        if not AboutSoftware.objectName():
            AboutSoftware.setObjectName(u"AboutSoftware")
        AboutSoftware.resize(213, 240)
        self.verticalLayout_2 = QVBoxLayout(AboutSoftware)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.appIcon = QLabel(AboutSoftware)
        self.appIcon.setObjectName(u"appIcon")
        self.appIcon.setMinimumSize(QSize(88, 88))
        self.appIcon.setMaximumSize(QSize(88, 88))
        self.appIcon.setPixmap(QPixmap(u"../src/images/icon-round.png"))
        self.appIcon.setScaledContents(True)
        self.appIcon.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.appIcon, 0, Qt.AlignHCenter)

        self.appName = QLabel(AboutSoftware)
        self.appName.setObjectName(u"appName")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei"])
        font.setPointSize(12)
        font.setBold(True)
        font.setKerning(True)
        self.appName.setFont(font)
        self.appName.setFrameShape(QFrame.NoFrame)
        self.appName.setLineWidth(0)
        self.appName.setMidLineWidth(0)
        self.appName.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.appName)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label_3 = QLabel(AboutSoftware)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(63, 63, 63);")

        self.horizontalLayout.addWidget(self.label_3)

        self.appVersionName = QLabel(AboutSoftware)
        self.appVersionName.setObjectName(u"appVersionName")
        self.appVersionName.setStyleSheet(u"color: rgb(63, 63, 63);")

        self.horizontalLayout.addWidget(self.appVersionName)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.label_4 = QLabel(AboutSoftware)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.disclaim = QLabel(AboutSoftware)
        self.disclaim.setObjectName(u"disclaim")
        self.disclaim.setCursor(QCursor(Qt.PointingHandCursor))
        self.disclaim.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.disclaim)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.retranslateUi(AboutSoftware)

        QMetaObject.connectSlotsByName(AboutSoftware)
    # setupUi

    def retranslateUi(self, AboutSoftware):
        AboutSoftware.setWindowTitle(QCoreApplication.translate("AboutSoftware", u"\u5173\u4e8e\u8f6f\u4ef6", None))
        self.appIcon.setText("")
        self.appName.setText(QCoreApplication.translate("AboutSoftware", u"\u8bb8\u66f0\u70e4\u7ea2\u85af", None))
        self.label_3.setText(QCoreApplication.translate("AboutSoftware", u"\u7248\u672c:", None))
        self.appVersionName.setText(QCoreApplication.translate("AboutSoftware", u"\u65e0\u6cd5\u83b7\u53d6\u7248\u672c", None))
        self.label_4.setText(QCoreApplication.translate("AboutSoftware", u"Xu Yue\u00a92024-2025", None))
        self.disclaim.setText(QCoreApplication.translate("AboutSoftware", u"<html><head/><body><p><span style=\" text-decoration: underline;\">\u514d\u8d23\u58f0\u660e</span></p></body></html>", None))
    # retranslateUi

