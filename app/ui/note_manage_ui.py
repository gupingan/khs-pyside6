# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'note_manage_ui.ui'
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

class Ui_NoteManage(object):
    def setupUi(self, NoteManage):
        if not NoteManage.objectName():
            NoteManage.setObjectName(u"NoteManage")
        NoteManage.resize(773, 456)
        self.verticalLayout = QVBoxLayout(NoteManage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(NoteManage)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setTextFormat(Qt.MarkdownText)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.note_number = QLabel(NoteManage)
        self.note_number.setObjectName(u"note_number")
        sizePolicy.setHeightForWidth(self.note_number.sizePolicy().hasHeightForWidth())
        self.note_number.setSizePolicy(sizePolicy)
        self.note_number.setStyleSheet(u"")
        self.note_number.setTextFormat(Qt.AutoText)
        self.note_number.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.note_number.setWordWrap(True)

        self.horizontalLayout.addWidget(self.note_number)

        self.user_number_3 = QLabel(NoteManage)
        self.user_number_3.setObjectName(u"user_number_3")
        sizePolicy.setHeightForWidth(self.user_number_3.sizePolicy().hasHeightForWidth())
        self.user_number_3.setSizePolicy(sizePolicy)
        self.user_number_3.setStyleSheet(u"")
        self.user_number_3.setTextFormat(Qt.AutoText)
        self.user_number_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.user_number_3.setWordWrap(True)

        self.horizontalLayout.addWidget(self.user_number_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.refresh_btn = QPushButton(NoteManage)
        self.refresh_btn.setObjectName(u"refresh_btn")

        self.horizontalLayout.addWidget(self.refresh_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.table_notes = QTableView(NoteManage)
        self.table_notes.setObjectName(u"table_notes")

        self.verticalLayout.addWidget(self.table_notes)


        self.retranslateUi(NoteManage)

        QMetaObject.connectSlotsByName(NoteManage)
    # setupUi

    def retranslateUi(self, NoteManage):
        NoteManage.setWindowTitle(QCoreApplication.translate("NoteManage", u"\u7b14\u8bb0\u5217\u8868", None))
        self.label_3.setText(QCoreApplication.translate("NoteManage", u"**\u7b14\u8bb0\u6570\u91cf**", None))
        self.note_number.setText(QCoreApplication.translate("NoteManage", u"0 \u6761", None))
        self.user_number_3.setText("")
        self.refresh_btn.setText(QCoreApplication.translate("NoteManage", u"\u5237\u65b0\u663e\u793a", None))
    # retranslateUi

