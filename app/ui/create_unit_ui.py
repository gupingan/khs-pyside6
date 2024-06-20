# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_unit_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QVBoxLayout, QWidget)

class Ui_CreateUnit(object):
    def setupUi(self, CreateUnit):
        if not CreateUnit.objectName():
            CreateUnit.setObjectName(u"CreateUnit")
        CreateUnit.resize(700, 383)
        self.verticalLayout_3 = QVBoxLayout(CreateUnit)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(CreateUnit)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setTextFormat(Qt.MarkdownText)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.config_number = QLabel(CreateUnit)
        self.config_number.setObjectName(u"config_number")
        sizePolicy.setHeightForWidth(self.config_number.sizePolicy().hasHeightForWidth())
        self.config_number.setSizePolicy(sizePolicy)
        self.config_number.setStyleSheet(u"")
        self.config_number.setTextFormat(Qt.AutoText)
        self.config_number.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.config_number.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.config_number)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.create_config_btn = QPushButton(CreateUnit)
        self.create_config_btn.setObjectName(u"create_config_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.create_config_btn.sizePolicy().hasHeightForWidth())
        self.create_config_btn.setSizePolicy(sizePolicy1)
        self.create_config_btn.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.create_config_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.config_table = QTableView(CreateUnit)
        self.config_table.setObjectName(u"config_table")

        self.verticalLayout.addWidget(self.config_table)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(CreateUnit)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setTextFormat(Qt.MarkdownText)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.user_number = QLabel(CreateUnit)
        self.user_number.setObjectName(u"user_number")
        sizePolicy.setHeightForWidth(self.user_number.sizePolicy().hasHeightForWidth())
        self.user_number.setSizePolicy(sizePolicy)
        self.user_number.setStyleSheet(u"")
        self.user_number.setTextFormat(Qt.AutoText)
        self.user_number.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.user_number.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.user_number)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.create_user_btn = QPushButton(CreateUnit)
        self.create_user_btn.setObjectName(u"create_user_btn")
        sizePolicy1.setHeightForWidth(self.create_user_btn.sizePolicy().hasHeightForWidth())
        self.create_user_btn.setSizePolicy(sizePolicy1)
        self.create_user_btn.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.create_user_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.user_table = QTableView(CreateUnit)
        self.user_table.setObjectName(u"user_table")

        self.verticalLayout_2.addWidget(self.user_table)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.cancel_button = QPushButton(CreateUnit)
        self.cancel_button.setObjectName(u"cancel_button")

        self.horizontalLayout.addWidget(self.cancel_button)

        self.confirm_button = QPushButton(CreateUnit)
        self.confirm_button.setObjectName(u"confirm_button")

        self.horizontalLayout.addWidget(self.confirm_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        QWidget.setTabOrder(self.cancel_button, self.confirm_button)
        QWidget.setTabOrder(self.confirm_button, self.create_config_btn)
        QWidget.setTabOrder(self.create_config_btn, self.create_user_btn)

        self.retranslateUi(CreateUnit)

        QMetaObject.connectSlotsByName(CreateUnit)
    # setupUi

    def retranslateUi(self, CreateUnit):
        CreateUnit.setWindowTitle(QCoreApplication.translate("CreateUnit", u"\u7ba1\u7406 - \u521b\u5efa\u5355\u5143", None))
        self.label.setText(QCoreApplication.translate("CreateUnit", u"**\u914d\u7f6e\u6570\u91cf**", None))
        self.config_number.setText(QCoreApplication.translate("CreateUnit", u"0\u6761", None))
        self.create_config_btn.setText(QCoreApplication.translate("CreateUnit", u"\u65b0\u589e", None))
        self.label_3.setText(QCoreApplication.translate("CreateUnit", u"**\u7528\u6237\u6570\u91cf**", None))
        self.user_number.setText(QCoreApplication.translate("CreateUnit", u"0\u4e2a", None))
        self.create_user_btn.setText(QCoreApplication.translate("CreateUnit", u"\u6dfb\u52a0", None))
        self.cancel_button.setText(QCoreApplication.translate("CreateUnit", u"\u53d6\u6d88", None))
        self.confirm_button.setText(QCoreApplication.translate("CreateUnit", u"\u786e\u8ba4", None))
    # retranslateUi

