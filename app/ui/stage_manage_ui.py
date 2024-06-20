# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stage_manage_ui.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QLabel, QListView, QListWidget, QListWidgetItem,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_StageManage(object):
    def setupUi(self, StageManage):
        if not StageManage.objectName():
            StageManage.setObjectName(u"StageManage")
        StageManage.resize(462, 486)
        self.verticalLayout_2 = QVBoxLayout(StageManage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(StageManage)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.tasker_count = QLabel(StageManage)
        self.tasker_count.setObjectName(u"tasker_count")

        self.horizontalLayout.addWidget(self.tasker_count)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(StageManage)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.current_stage = QLabel(StageManage)
        self.current_stage.setObjectName(u"current_stage")

        self.horizontalLayout.addWidget(self.current_stage)

        self.label_3 = QLabel(StageManage)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listWidget = QListWidget(StageManage)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setFocusPolicy(Qt.NoFocus)
        self.listWidget.setFrameShape(QFrame.NoFrame)
        self.listWidget.setFrameShadow(QFrame.Sunken)
        self.listWidget.setLineWidth(0)
        self.listWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.listWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listWidget.setResizeMode(QListView.Adjust)
        self.listWidget.setLayoutMode(QListView.SinglePass)
        self.listWidget.setSpacing(5)

        self.verticalLayout.addWidget(self.listWidget)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(StageManage)

        QMetaObject.connectSlotsByName(StageManage)
    # setupUi

    def retranslateUi(self, StageManage):
        StageManage.setWindowTitle(QCoreApplication.translate("StageManage", u"\u9636\u6bb5\u7ba1\u7406", None))
        self.label.setText(QCoreApplication.translate("StageManage", u"<html><head/><body><p><span style=\" font-weight:700;\">\u5f53\u524d\u7528\u6237\u6570\u91cf</span></p></body></html>", None))
        self.tasker_count.setText(QCoreApplication.translate("StageManage", u"0", None))
        self.label_2.setText(QCoreApplication.translate("StageManage", u"<html><head/><body><p><span style=\" font-weight:700;\">\u5f53\u524d\u8fd0\u884c\u9636\u6bb5</span></p></body></html>", None))
        self.current_stage.setText(QCoreApplication.translate("StageManage", u"0", None))
        self.label_3.setText(QCoreApplication.translate("StageManage", u"\u9636\u6bb5", None))
    # retranslateUi

