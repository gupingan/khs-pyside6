# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_at_user_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_EditAtUser(object):
    def setupUi(self, EditAtUser):
        if not EditAtUser.objectName():
            EditAtUser.setObjectName(u"EditAtUser")
        EditAtUser.resize(343, 205)
        self.verticalLayout = QVBoxLayout(EditAtUser)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(4)
        self.edit_user_id = QLineEdit(EditAtUser)
        self.edit_user_id.setObjectName(u"edit_user_id")
        self.edit_user_id.setMaxLength(40)
        self.edit_user_id.setFrame(True)
        self.edit_user_id.setEchoMode(QLineEdit.Normal)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.edit_user_id)

        self.label_6 = QLabel(EditAtUser)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setTextFormat(Qt.MarkdownText)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.edit_remark = QTextEdit(EditAtUser)
        self.edit_remark.setObjectName(u"edit_remark")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.edit_remark)

        self.edit_nickname = QLineEdit(EditAtUser)
        self.edit_nickname.setObjectName(u"edit_nickname")
        self.edit_nickname.setMaxLength(40)
        self.edit_nickname.setFrame(True)
        self.edit_nickname.setEchoMode(QLineEdit.Normal)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.edit_nickname)

        self.label_2 = QLabel(EditAtUser)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setTextFormat(Qt.MarkdownText)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(EditAtUser)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setTextFormat(Qt.MarkdownText)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.cancel_button = QPushButton(EditAtUser)
        self.cancel_button.setObjectName(u"cancel_button")

        self.horizontalLayout_5.addWidget(self.cancel_button)

        self.save_button = QPushButton(EditAtUser)
        self.save_button.setObjectName(u"save_button")

        self.horizontalLayout_5.addWidget(self.save_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.verticalLayout.addLayout(self.verticalLayout_4)


        self.retranslateUi(EditAtUser)

        QMetaObject.connectSlotsByName(EditAtUser)
    # setupUi

    def retranslateUi(self, EditAtUser):
        EditAtUser.setWindowTitle(QCoreApplication.translate("EditAtUser", u"\u7f16\u8f91\u827e\u7279\u7528\u6237", None))
        self.label_6.setText(QCoreApplication.translate("EditAtUser", u"**\u5907\u6ce8**", None))
        self.label_2.setText(QCoreApplication.translate("EditAtUser", u"**\u6635\u79f0**", None))
        self.label_3.setText(QCoreApplication.translate("EditAtUser", u"**\u7528\u6237ID**", None))
        self.cancel_button.setText(QCoreApplication.translate("EditAtUser", u"\u53d6\u6d88", None))
        self.save_button.setText(QCoreApplication.translate("EditAtUser", u"\u4fdd\u5b58", None))
    # retranslateUi

