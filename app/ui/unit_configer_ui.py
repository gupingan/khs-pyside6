# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'unit_configer_ui.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QToolButton, QVBoxLayout, QWidget)

class Ui_UnitConfiger(object):
    def setupUi(self, UnitConfiger):
        if not UnitConfiger.objectName():
            UnitConfiger.setObjectName(u"UnitConfiger")
        UnitConfiger.resize(468, 507)
        self.verticalLayout_2 = QVBoxLayout(UnitConfiger)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(UnitConfiger)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.tasker_count = QLabel(UnitConfiger)
        self.tasker_count.setObjectName(u"tasker_count")

        self.horizontalLayout.addWidget(self.tasker_count)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.distribute_count_sb = QSpinBox(UnitConfiger)
        self.distribute_count_sb.setObjectName(u"distribute_count_sb")
        self.distribute_count_sb.setMaximum(1000)

        self.horizontalLayout.addWidget(self.distribute_count_sb)

        self.distribute_toolbtn = QToolButton(UnitConfiger)
        self.distribute_toolbtn.setObjectName(u"distribute_toolbtn")

        self.horizontalLayout.addWidget(self.distribute_toolbtn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listWidget = QListWidget(UnitConfiger)
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

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.cancel_btn = QPushButton(UnitConfiger)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.horizontalLayout_2.addWidget(self.cancel_btn)

        self.create_btn = QPushButton(UnitConfiger)
        self.create_btn.setObjectName(u"create_btn")

        self.horizontalLayout_2.addWidget(self.create_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.retranslateUi(UnitConfiger)

        QMetaObject.connectSlotsByName(UnitConfiger)
    # setupUi

    def retranslateUi(self, UnitConfiger):
        UnitConfiger.setWindowTitle(QCoreApplication.translate("UnitConfiger", u"\u5355\u5143\u5fae\u914d\u7f6e", None))
        self.label.setText(QCoreApplication.translate("UnitConfiger", u"<html><head/><body><p><span style=\" font-weight:700;\">\u5f53\u524d\u7528\u6237\u6570\u91cf</span></p></body></html>", None))
        self.tasker_count.setText(QCoreApplication.translate("UnitConfiger", u"0", None))
        self.distribute_toolbtn.setText(QCoreApplication.translate("UnitConfiger", u"\u7edf\u4e00\u5206\u914d", None))
        self.cancel_btn.setText(QCoreApplication.translate("UnitConfiger", u"\u53d6\u6d88", None))
        self.create_btn.setText(QCoreApplication.translate("UnitConfiger", u"\u521b\u5efa\u5355\u5143", None))
    # retranslateUi

