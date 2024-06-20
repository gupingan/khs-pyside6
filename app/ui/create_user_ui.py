# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_user_ui.ui'
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
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_CreateUser(object):
    def setupUi(self, CreateUser):
        if not CreateUser.objectName():
            CreateUser.setObjectName(u"CreateUser")
        CreateUser.resize(424, 198)
        self.horizontalLayout = QHBoxLayout(CreateUser)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_qrcode = QLabel(CreateUser)
        self.label_qrcode.setObjectName(u"label_qrcode")
        self.label_qrcode.setMinimumSize(QSize(128, 128))
        self.label_qrcode.setMaximumSize(QSize(128, 128))
        self.label_qrcode.setScaledContents(True)
        self.label_qrcode.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_qrcode, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.refresh_qrcode_btn = QPushButton(CreateUser)
        self.refresh_qrcode_btn.setObjectName(u"refresh_qrcode_btn")

        self.horizontalLayout_2.addWidget(self.refresh_qrcode_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(CreateUser)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setTextFormat(Qt.MarkdownText)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_nickname = QLabel(CreateUser)
        self.label_nickname.setObjectName(u"label_nickname")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_nickname.sizePolicy().hasHeightForWidth())
        self.label_nickname.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label_nickname)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(CreateUser)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setTextFormat(Qt.MarkdownText)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.label_user_id = QLabel(CreateUser)
        self.label_user_id.setObjectName(u"label_user_id")
        sizePolicy.setHeightForWidth(self.label_user_id.sizePolicy().hasHeightForWidth())
        self.label_user_id.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.label_user_id)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_6 = QLabel(CreateUser)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setTextFormat(Qt.MarkdownText)

        self.verticalLayout_4.addWidget(self.label_6)

        self.edit_remark = QTextEdit(CreateUser)
        self.edit_remark.setObjectName(u"edit_remark")

        self.verticalLayout_4.addWidget(self.edit_remark)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.check_button = QPushButton(CreateUser)
        self.check_button.setObjectName(u"check_button")

        self.horizontalLayout_5.addWidget(self.check_button)

        self.confirm_button = QPushButton(CreateUser)
        self.confirm_button.setObjectName(u"confirm_button")

        self.horizontalLayout_5.addWidget(self.confirm_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(CreateUser)

        QMetaObject.connectSlotsByName(CreateUser)
    # setupUi

    def retranslateUi(self, CreateUser):
        CreateUser.setWindowTitle(QCoreApplication.translate("CreateUser", u"\u6dfb\u52a0\u7528\u6237", None))
        self.label_qrcode.setText(QCoreApplication.translate("CreateUser", u"Loading ...", None))
        self.refresh_qrcode_btn.setText(QCoreApplication.translate("CreateUser", u"\u5237\u65b0\u4e8c\u7ef4\u7801", None))
        self.label_2.setText(QCoreApplication.translate("CreateUser", u"**\u6635 \u79f0**", None))
        self.label_nickname.setText(QCoreApplication.translate("CreateUser", u"\u5c1a\u672a\u767b\u5f55\u2026\u2026", None))
        self.label_4.setText(QCoreApplication.translate("CreateUser", u"**\u7528\u6237ID**", None))
        self.label_user_id.setText(QCoreApplication.translate("CreateUser", u"\u5c1a\u672a\u767b\u5f55\u2026\u2026", None))
        self.label_6.setText(QCoreApplication.translate("CreateUser", u"**\u529f\u80fd\u5907\u6ce8**", None))
        self.check_button.setText(QCoreApplication.translate("CreateUser", u"\u5148\u68c0\u6d4b", None))
        self.confirm_button.setText(QCoreApplication.translate("CreateUser", u"\u540e\u6dfb\u52a0", None))
    # retranslateUi

