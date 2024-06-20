# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preload_view_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QProgressBar, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_PreloadView(object):
    def setupUi(self, PreloadView):
        if not PreloadView.objectName():
            PreloadView.setObjectName(u"PreloadView")
        PreloadView.resize(323, 78)
        self.verticalLayout = QVBoxLayout(PreloadView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(PreloadView)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.content_label = QLabel(self.widget)
        self.content_label.setObjectName(u"content_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.content_label.sizePolicy().hasHeightForWidth())
        self.content_label.setSizePolicy(sizePolicy)
        self.content_label.setStyleSheet(u"")
        self.content_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.content_label)

        self.progressBar = QProgressBar(self.widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximumSize(QSize(16777215, 2))
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.verticalLayout_2.addWidget(self.progressBar)

        self.hint_label = QLabel(self.widget)
        self.hint_label.setObjectName(u"hint_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.hint_label.sizePolicy().hasHeightForWidth())
        self.hint_label.setSizePolicy(sizePolicy1)
        self.hint_label.setStyleSheet(u"color:  rgb(108, 108, 108);\n"
"font-size: 10px")
        self.hint_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.hint_label)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(PreloadView)

        QMetaObject.connectSlotsByName(PreloadView)
    # setupUi

    def retranslateUi(self, PreloadView):
        PreloadView.setWindowTitle(QCoreApplication.translate("PreloadView", u"\u9884\u52a0\u8f7d\u9875\u9762", None))
        self.content_label.setText("")
        self.hint_label.setText("")
    # retranslateUi

