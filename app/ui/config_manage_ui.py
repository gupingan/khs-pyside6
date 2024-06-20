# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config_manage_ui.ui'
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

class Ui_ConfigManage(object):
    def setupUi(self, ConfigManage):
        if not ConfigManage.objectName():
            ConfigManage.setObjectName(u"ConfigManage")
        ConfigManage.resize(603, 419)
        self.verticalLayout = QVBoxLayout(ConfigManage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(ConfigManage)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setTextFormat(Qt.MarkdownText)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.config_number = QLabel(ConfigManage)
        self.config_number.setObjectName(u"config_number")
        sizePolicy.setHeightForWidth(self.config_number.sizePolicy().hasHeightForWidth())
        self.config_number.setSizePolicy(sizePolicy)
        self.config_number.setStyleSheet(u"")
        self.config_number.setTextFormat(Qt.AutoText)
        self.config_number.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.config_number.setWordWrap(True)

        self.horizontalLayout.addWidget(self.config_number)

        self.user_number_3 = QLabel(ConfigManage)
        self.user_number_3.setObjectName(u"user_number_3")
        sizePolicy.setHeightForWidth(self.user_number_3.sizePolicy().hasHeightForWidth())
        self.user_number_3.setSizePolicy(sizePolicy)
        self.user_number_3.setStyleSheet(u"")
        self.user_number_3.setTextFormat(Qt.AutoText)
        self.user_number_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.user_number_3.setWordWrap(True)

        self.horizontalLayout.addWidget(self.user_number_3)

        self.label_4 = QLabel(ConfigManage)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setTextFormat(Qt.MarkdownText)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_4)

        self.select_config_number = QLabel(ConfigManage)
        self.select_config_number.setObjectName(u"select_config_number")
        sizePolicy.setHeightForWidth(self.select_config_number.sizePolicy().hasHeightForWidth())
        self.select_config_number.setSizePolicy(sizePolicy)
        self.select_config_number.setStyleSheet(u"")
        self.select_config_number.setTextFormat(Qt.AutoText)
        self.select_config_number.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.select_config_number.setWordWrap(True)

        self.horizontalLayout.addWidget(self.select_config_number)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.toggle_select_btn = QPushButton(ConfigManage)
        self.toggle_select_btn.setObjectName(u"toggle_select_btn")

        self.horizontalLayout.addWidget(self.toggle_select_btn)

        self.add_config_btn = QPushButton(ConfigManage)
        self.add_config_btn.setObjectName(u"add_config_btn")

        self.horizontalLayout.addWidget(self.add_config_btn)

        self.del_config_btn = QPushButton(ConfigManage)
        self.del_config_btn.setObjectName(u"del_config_btn")

        self.horizontalLayout.addWidget(self.del_config_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableView = QTableView(ConfigManage)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)


        self.retranslateUi(ConfigManage)

        QMetaObject.connectSlotsByName(ConfigManage)
    # setupUi

    def retranslateUi(self, ConfigManage):
        ConfigManage.setWindowTitle(QCoreApplication.translate("ConfigManage", u"\u7ba1\u7406 - \u914d\u7f6e\u7ba1\u7406", None))
        self.label_3.setText(QCoreApplication.translate("ConfigManage", u"**\u914d\u7f6e\u6570\u91cf**", None))
        self.config_number.setText(QCoreApplication.translate("ConfigManage", u"0\u4e2a", None))
        self.user_number_3.setText("")
        self.label_4.setText(QCoreApplication.translate("ConfigManage", u"**\u5df2\u9009\u4e2d**", None))
        self.select_config_number.setText(QCoreApplication.translate("ConfigManage", u"0\u4e2a", None))
        self.toggle_select_btn.setText(QCoreApplication.translate("ConfigManage", u"\u5168\u9009", None))
        self.add_config_btn.setText(QCoreApplication.translate("ConfigManage", u"\u6dfb\u52a0", None))
        self.del_config_btn.setText(QCoreApplication.translate("ConfigManage", u"\u5220\u9664", None))
    # retranslateUi

