# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tasker_item_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QToolButton, QVBoxLayout, QWidget)

class Ui_TaskerItem(object):
    def setupUi(self, TaskerItem):
        if not TaskerItem.objectName():
            TaskerItem.setObjectName(u"TaskerItem")
        TaskerItem.resize(436, 114)
        self.verticalLayout = QVBoxLayout(TaskerItem)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stage_label = QLabel(TaskerItem)
        self.stage_label.setObjectName(u"stage_label")
        self.stage_label.setStyleSheet(u"")
        self.stage_label.setTextFormat(Qt.MarkdownText)
        self.stage_label.setMargin(10)

        self.horizontalLayout.addWidget(self.stage_label)

        self.username = QLabel(TaskerItem)
        self.username.setObjectName(u"username")

        self.horizontalLayout.addWidget(self.username)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.edit_config = QPushButton(TaskerItem)
        self.edit_config.setObjectName(u"edit_config")

        self.horizontalLayout.addWidget(self.edit_config)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slider = QSlider(TaskerItem)
        self.slider.setObjectName(u"slider")
        self.slider.setMaximum(1000)
        self.slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.slider)

        self.spinBox = QSpinBox(TaskerItem)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(1000)

        self.horizontalLayout_2.addWidget(self.spinBox)

        self.show_note_btn = QToolButton(TaskerItem)
        self.show_note_btn.setObjectName(u"show_note_btn")

        self.horizontalLayout_2.addWidget(self.show_note_btn)

        self.allow_btn = QToolButton(TaskerItem)
        self.allow_btn.setObjectName(u"allow_btn")

        self.horizontalLayout_2.addWidget(self.allow_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(TaskerItem)

        QMetaObject.connectSlotsByName(TaskerItem)
    # setupUi

    def retranslateUi(self, TaskerItem):
        TaskerItem.setWindowTitle(QCoreApplication.translate("TaskerItem", u"TaskerItem", None))
        self.stage_label.setText(QCoreApplication.translate("TaskerItem", u"**\u7b2c0\u9636\u6bb5**", None))
        self.username.setText(QCoreApplication.translate("TaskerItem", u"\u6635\u79f0", None))
        self.edit_config.setText(QCoreApplication.translate("TaskerItem", u"\u7f16\u8f91\u914d\u7f6e", None))
        self.show_note_btn.setText(QCoreApplication.translate("TaskerItem", u"\u67e5\u770b\u7b14\u8bb0", None))
        self.allow_btn.setText(QCoreApplication.translate("TaskerItem", u"\u4e0d\u6267\u884c", None))
    # retranslateUi

