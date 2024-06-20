# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_manage_ui.ui'
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

class Ui_UserManage(object):
    def setupUi(self, UserManage):
        if not UserManage.objectName():
            UserManage.setObjectName(u"UserManage")
        UserManage.resize(945, 523)
        self.verticalLayout = QVBoxLayout(UserManage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(UserManage)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setTextFormat(Qt.MarkdownText)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.user_number = QLabel(UserManage)
        self.user_number.setObjectName(u"user_number")
        sizePolicy.setHeightForWidth(self.user_number.sizePolicy().hasHeightForWidth())
        self.user_number.setSizePolicy(sizePolicy)
        self.user_number.setStyleSheet(u"")
        self.user_number.setTextFormat(Qt.AutoText)
        self.user_number.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.user_number.setWordWrap(True)

        self.horizontalLayout.addWidget(self.user_number)

        self.user_number_3 = QLabel(UserManage)
        self.user_number_3.setObjectName(u"user_number_3")
        sizePolicy.setHeightForWidth(self.user_number_3.sizePolicy().hasHeightForWidth())
        self.user_number_3.setSizePolicy(sizePolicy)
        self.user_number_3.setStyleSheet(u"")
        self.user_number_3.setTextFormat(Qt.AutoText)
        self.user_number_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.user_number_3.setWordWrap(True)

        self.horizontalLayout.addWidget(self.user_number_3)

        self.label_4 = QLabel(UserManage)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setTextFormat(Qt.MarkdownText)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_4)

        self.select_user_number = QLabel(UserManage)
        self.select_user_number.setObjectName(u"select_user_number")
        sizePolicy.setHeightForWidth(self.select_user_number.sizePolicy().hasHeightForWidth())
        self.select_user_number.setSizePolicy(sizePolicy)
        self.select_user_number.setStyleSheet(u"")
        self.select_user_number.setTextFormat(Qt.AutoText)
        self.select_user_number.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.select_user_number.setWordWrap(True)

        self.horizontalLayout.addWidget(self.select_user_number)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.toggle_select_btn = QPushButton(UserManage)
        self.toggle_select_btn.setObjectName(u"toggle_select_btn")
        sizePolicy.setHeightForWidth(self.toggle_select_btn.sizePolicy().hasHeightForWidth())
        self.toggle_select_btn.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.toggle_select_btn)

        self.check_login_btn = QPushButton(UserManage)
        self.check_login_btn.setObjectName(u"check_login_btn")
        sizePolicy.setHeightForWidth(self.check_login_btn.sizePolicy().hasHeightForWidth())
        self.check_login_btn.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.check_login_btn)

        self.check_comment_btn = QPushButton(UserManage)
        self.check_comment_btn.setObjectName(u"check_comment_btn")
        sizePolicy.setHeightForWidth(self.check_comment_btn.sizePolicy().hasHeightForWidth())
        self.check_comment_btn.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.check_comment_btn)

        self.create_user_btn = QPushButton(UserManage)
        self.create_user_btn.setObjectName(u"create_user_btn")

        self.horizontalLayout.addWidget(self.create_user_btn)

        self.delete_user_btn = QPushButton(UserManage)
        self.delete_user_btn.setObjectName(u"delete_user_btn")

        self.horizontalLayout.addWidget(self.delete_user_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableView = QTableView(UserManage)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)


        self.retranslateUi(UserManage)

        QMetaObject.connectSlotsByName(UserManage)
    # setupUi

    def retranslateUi(self, UserManage):
        UserManage.setWindowTitle(QCoreApplication.translate("UserManage", u"\u7ba1\u7406 - \u7528\u6237\u7ba1\u7406", None))
        self.label_3.setText(QCoreApplication.translate("UserManage", u"**\u7528\u6237\u6570\u91cf**", None))
        self.user_number.setText(QCoreApplication.translate("UserManage", u"0\u4e2a", None))
        self.user_number_3.setText("")
        self.label_4.setText(QCoreApplication.translate("UserManage", u"**\u5df2\u9009\u4e2d**", None))
        self.select_user_number.setText(QCoreApplication.translate("UserManage", u"0\u4e2a", None))
        self.toggle_select_btn.setText(QCoreApplication.translate("UserManage", u"\u5168\u9009", None))
        self.check_login_btn.setText(QCoreApplication.translate("UserManage", u"\u767b\u5f55\u68c0\u6d4b", None))
        self.check_comment_btn.setText(QCoreApplication.translate("UserManage", u"\u8bc4\u8bba\u68c0\u6d4b", None))
        self.create_user_btn.setText(QCoreApplication.translate("UserManage", u"\u6dfb\u52a0", None))
        self.delete_user_btn.setText(QCoreApplication.translate("UserManage", u"\u5220\u9664", None))
    # retranslateUi

