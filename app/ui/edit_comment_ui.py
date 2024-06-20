# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_comment_ui.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QDialog,
    QDialogButtonBox, QHBoxLayout, QLabel, QLineEdit,
    QListView, QPlainTextEdit, QSizePolicy, QToolButton,
    QVBoxLayout, QWidget)

class Ui_editCommentDialog(object):
    def setupUi(self, editCommentDialog):
        if not editCommentDialog.objectName():
            editCommentDialog.setObjectName(u"editCommentDialog")
        editCommentDialog.resize(466, 323)
        self.verticalLayout = QVBoxLayout(editCommentDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(editCommentDialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.split_char_edit = QLineEdit(editCommentDialog)
        self.split_char_edit.setObjectName(u"split_char_edit")

        self.horizontalLayout.addWidget(self.split_char_edit)

        self.select_common_char_btn = QToolButton(editCommentDialog)
        self.select_common_char_btn.setObjectName(u"select_common_char_btn")

        self.horizontalLayout.addWidget(self.select_common_char_btn)

        self.import_file_btn = QToolButton(editCommentDialog)
        self.import_file_btn.setObjectName(u"import_file_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.import_file_btn.sizePolicy().hasHeightForWidth())
        self.import_file_btn.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.import_file_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(editCommentDialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.comment_edit = QPlainTextEdit(editCommentDialog)
        self.comment_edit.setObjectName(u"comment_edit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comment_edit.sizePolicy().hasHeightForWidth())
        self.comment_edit.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.comment_edit)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(editCommentDialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.create_at_user_btn = QToolButton(editCommentDialog)
        self.create_at_user_btn.setObjectName(u"create_at_user_btn")

        self.horizontalLayout_3.addWidget(self.create_at_user_btn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.at_users_list = QListView(editCommentDialog)
        self.at_users_list.setObjectName(u"at_users_list")
        sizePolicy1.setHeightForWidth(self.at_users_list.sizePolicy().hasHeightForWidth())
        self.at_users_list.setSizePolicy(sizePolicy1)
        self.at_users_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.at_users_list.setItemAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.at_users_list)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label = QLabel(editCommentDialog)
        self.label.setObjectName(u"label")
        self.label.setScaledContents(False)
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.buttonBox = QDialogButtonBox(editCommentDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(editCommentDialog)
        self.buttonBox.accepted.connect(editCommentDialog.accept)
        self.buttonBox.rejected.connect(editCommentDialog.reject)

        QMetaObject.connectSlotsByName(editCommentDialog)
    # setupUi

    def retranslateUi(self, editCommentDialog):
        editCommentDialog.setWindowTitle(QCoreApplication.translate("editCommentDialog", u"\u914d\u7f6e - \u7f16\u8f91\u8bc4\u8bba", None))
        self.label_4.setText(QCoreApplication.translate("editCommentDialog", u"\u591a\u6761\u8bc4\u8bba\u6309\u4ec0\u4e48\u5b57\u7b26\u5206\u5272", None))
        self.select_common_char_btn.setText(QCoreApplication.translate("editCommentDialog", u"\u9009\u62e9\u5e38\u89c1\u5b57\u7b26", None))
        self.import_file_btn.setText(QCoreApplication.translate("editCommentDialog", u"\u5bfc\u5165\u8bc4\u8bba", None))
        self.label_2.setText(QCoreApplication.translate("editCommentDialog", u"\u8bc4\u8bba\u6846", None))
        self.label_3.setText(QCoreApplication.translate("editCommentDialog", u"@\u7528\u6237", None))
        self.create_at_user_btn.setText(QCoreApplication.translate("editCommentDialog", u"\u6dfb\u52a0", None))
        self.label.setText(QCoreApplication.translate("editCommentDialog", u"<html><head/><body><p><span style=\" color:#0055ff;\">\u4e00\u822c\u591a\u884c\u8bc4\u8bba\u4ee5\u9ed8\u8ba4\u7684</span><span style=\" font-weight:600; color:#0055ff;\"> \\n </span><span style=\" color:#0055ff;\">\u5373\u53ef\u3002@\u7528\u6237\u6309\u4f4f </span><span style=\" font-weight:700; color:#0055ff;\">ctrl</span><span style=\" color:#0055ff;\"> \u952e\u548c\u9f20\u6807</span><span style=\" font-weight:700; color:#0055ff;\">\u5de6\u952e</span><span style=\" color:#0055ff;\">\u70b9\u51fb\u591a\u9009</span></p></body></html>", None))
    # retranslateUi

