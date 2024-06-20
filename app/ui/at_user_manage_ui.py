# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'at_user_manage_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QPushButton,
    QSizePolicy, QSpacerItem, QTableView, QVBoxLayout,
    QWidget)

class Ui_AtUserManage(object):
    def setupUi(self, AtUserManage):
        if not AtUserManage.objectName():
            AtUserManage.setObjectName(u"AtUserManage")
        AtUserManage.resize(518, 338)
        self.verticalLayout = QVBoxLayout(AtUserManage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.toggle_select_btn = QPushButton(AtUserManage)
        self.toggle_select_btn.setObjectName(u"toggle_select_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggle_select_btn.sizePolicy().hasHeightForWidth())
        self.toggle_select_btn.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.toggle_select_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.create_at_user_btn = QPushButton(AtUserManage)
        self.create_at_user_btn.setObjectName(u"create_at_user_btn")

        self.horizontalLayout.addWidget(self.create_at_user_btn)

        self.delete_at_user_btn = QPushButton(AtUserManage)
        self.delete_at_user_btn.setObjectName(u"delete_at_user_btn")

        self.horizontalLayout.addWidget(self.delete_at_user_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableView = QTableView(AtUserManage)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)


        self.retranslateUi(AtUserManage)

        QMetaObject.connectSlotsByName(AtUserManage)
    # setupUi

    def retranslateUi(self, AtUserManage):
        AtUserManage.setWindowTitle(QCoreApplication.translate("AtUserManage", u"\u7ba1\u7406 - \u827e\u7279\u7528\u6237\u7ba1\u7406", None))
        self.toggle_select_btn.setText(QCoreApplication.translate("AtUserManage", u"\u5168\u9009", None))
        self.create_at_user_btn.setText(QCoreApplication.translate("AtUserManage", u"\u6dfb\u52a0", None))
        self.delete_at_user_btn.setText(QCoreApplication.translate("AtUserManage", u"\u5220\u9664", None))
    # retranslateUi

