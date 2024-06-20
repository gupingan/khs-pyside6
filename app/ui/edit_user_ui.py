# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_user_ui.ui'
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
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_EditUser(object):
    def setupUi(self, EditUser):
        if not EditUser.objectName():
            EditUser.setObjectName(u"EditUser")
        EditUser.resize(361, 287)
        self.verticalLayout = QVBoxLayout(EditUser)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(4)
        self.edit_session = QLineEdit(EditUser)
        self.edit_session.setObjectName(u"edit_session")
        self.edit_session.setMaxLength(1024)
        self.edit_session.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.edit_session)

        self.label_4 = QLabel(EditUser)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setTextFormat(Qt.MarkdownText)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.label_user_id = QLabel(EditUser)
        self.label_user_id.setObjectName(u"label_user_id")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_user_id)

        self.edit_nickname = QLineEdit(EditUser)
        self.edit_nickname.setObjectName(u"edit_nickname")
        self.edit_nickname.setMaxLength(40)
        self.edit_nickname.setFrame(True)
        self.edit_nickname.setEchoMode(QLineEdit.Normal)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.edit_nickname)

        self.label_2 = QLabel(EditUser)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setTextFormat(Qt.MarkdownText)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_2)

        self.label_5 = QLabel(EditUser)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setTextFormat(Qt.MarkdownText)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_5)

        self.edit_remark = QTextEdit(EditUser)
        self.edit_remark.setObjectName(u"edit_remark")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.edit_remark)

        self.label_6 = QLabel(EditUser)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setTextFormat(Qt.MarkdownText)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_6)

        self.label_3 = QLabel(EditUser)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setTextFormat(Qt.MarkdownText)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton_1 = QRadioButton(EditUser)
        self.radioButton_1.setObjectName(u"radioButton_1")

        self.horizontalLayout.addWidget(self.radioButton_1)

        self.radioButton_2 = QRadioButton(EditUser)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(EditUser)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout.addWidget(self.radioButton_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_7 = QLabel(EditUser)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setTextFormat(Qt.MarkdownText)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radioButton_4 = QRadioButton(EditUser)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.horizontalLayout_2.addWidget(self.radioButton_4)

        self.radioButton_5 = QRadioButton(EditUser)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.horizontalLayout_2.addWidget(self.radioButton_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.label_8 = QLabel(EditUser)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setTextFormat(Qt.MarkdownText)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_8)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.radioButton_6 = QRadioButton(EditUser)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.horizontalLayout_3.addWidget(self.radioButton_6)

        self.radioButton_7 = QRadioButton(EditUser)
        self.radioButton_7.setObjectName(u"radioButton_7")

        self.horizontalLayout_3.addWidget(self.radioButton_7)

        self.radioButton_8 = QRadioButton(EditUser)
        self.radioButton_8.setObjectName(u"radioButton_8")

        self.horizontalLayout_3.addWidget(self.radioButton_8)

        self.radioButton_9 = QRadioButton(EditUser)
        self.radioButton_9.setObjectName(u"radioButton_9")

        self.horizontalLayout_3.addWidget(self.radioButton_9)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.cancel_button = QPushButton(EditUser)
        self.cancel_button.setObjectName(u"cancel_button")

        self.horizontalLayout_5.addWidget(self.cancel_button)

        self.save_button = QPushButton(EditUser)
        self.save_button.setObjectName(u"save_button")

        self.horizontalLayout_5.addWidget(self.save_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.verticalLayout.addLayout(self.verticalLayout_4)


        self.retranslateUi(EditUser)

        QMetaObject.connectSlotsByName(EditUser)
    # setupUi

    def retranslateUi(self, EditUser):
        EditUser.setWindowTitle(QCoreApplication.translate("EditUser", u"\u7f16\u8f91\u7528\u6237", None))
        self.label_4.setText(QCoreApplication.translate("EditUser", u"**\u7528\u6237 ID**", None))
        self.label_user_id.setText(QCoreApplication.translate("EditUser", u"\u7528\u6237 ID \u4e0d\u53ef\u66f4\u6539", None))
        self.label_2.setText(QCoreApplication.translate("EditUser", u"**\u7528\u6237\u6635\u79f0**", None))
        self.label_5.setText(QCoreApplication.translate("EditUser", u"**session**", None))
        self.label_6.setText(QCoreApplication.translate("EditUser", u"**\u529f\u80fd\u5907\u6ce8**", None))
        self.label_3.setText(QCoreApplication.translate("EditUser", u"**\u767b\u5f55\u72b6\u6001**", None))
        self.radioButton_1.setText(QCoreApplication.translate("EditUser", u"\u672a\u77e5", None))
        self.radioButton_2.setText(QCoreApplication.translate("EditUser", u"\u5931\u6548", None))
        self.radioButton_3.setText(QCoreApplication.translate("EditUser", u"\u6709\u6548", None))
        self.label_7.setText(QCoreApplication.translate("EditUser", u"**\u5de5\u4f5c\u72b6\u6001**", None))
        self.radioButton_4.setText(QCoreApplication.translate("EditUser", u"\u672a\u5de5\u4f5c", None))
        self.radioButton_5.setText(QCoreApplication.translate("EditUser", u"\u5de5\u4f5c\u4e2d", None))
        self.label_8.setText(QCoreApplication.translate("EditUser", u"**\u8bc4\u8bba\u72b6\u6001**", None))
        self.radioButton_6.setText(QCoreApplication.translate("EditUser", u"\u7981\u8a00", None))
        self.radioButton_7.setText(QCoreApplication.translate("EditUser", u"\u672a\u77e5", None))
        self.radioButton_8.setText(QCoreApplication.translate("EditUser", u"\u5c4f\u853d", None))
        self.radioButton_9.setText(QCoreApplication.translate("EditUser", u"\u6b63\u5e38", None))
        self.cancel_button.setText(QCoreApplication.translate("EditUser", u"\u53d6\u6d88", None))
        self.save_button.setText(QCoreApplication.translate("EditUser", u"\u4fdd\u5b58", None))
    # retranslateUi

