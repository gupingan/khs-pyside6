# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'disclaim_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_DisclaimView(object):
    def setupUi(self, DisclaimView):
        if not DisclaimView.objectName():
            DisclaimView.setObjectName(u"DisclaimView")
        DisclaimView.resize(777, 438)
        self.horizontalLayout = QHBoxLayout(DisclaimView)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.scrollArea = QScrollArea(DisclaimView)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 740, 548))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setTextFormat(Qt.MarkdownText)
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)


        self.retranslateUi(DisclaimView)

        QMetaObject.connectSlotsByName(DisclaimView)
    # setupUi

    def retranslateUi(self, DisclaimView):
        DisclaimView.setWindowTitle(QCoreApplication.translate("DisclaimView", u"\u5173\u4e8e\u8f6f\u4ef6-\u514d\u8d23\u58f0\u660e", None))
        self.label.setText(QCoreApplication.translate("DisclaimView", u"<html><head><title>\u70e4\u7ea2\u85af App \u514d\u8d23\u58f0\u660e</title></head><body><h1 style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700;\">\u514d\u8d23\u58f0\u660e</span></h1><p><span style=\" font-size:11pt;\">\u611f\u8c22\u60a8\u9009\u62e9\u201c{appName}\u201d\u5e94\u7528\uff08\u4ee5\u4e0b\u7b80\u79f0\u201c\u672c\u5e94\u7528\u201d\uff09\u3002\u5728\u4f7f\u7528\u672c\u5e94\u7528\u4e4b\u524d\uff0c\u8bf7\u4ed4\u7ec6\u9605\u8bfb\u4ee5\u4e0b\u514d\u8d23\u58f0\u660e\uff1a </span></p><h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700;\">1. \u4f7f\u7528\u6761\u6b3e</span></h2><p><span style=\" font-size:11pt;\">\u672c\u5e94\u7528\u4ec5\u4f9b\u4ed8\u8d39\u7528\u6237\u4f7f\u7528\uff0c\u4e25\u7981\u7528\u4e8e\u4efb\u4f55\u4e0d\u826f\u7528\u9014\u3002\u4e00\u7ecf\u53d1\u73b0\u6b64\u7c7b"
                        "\u884c\u4e3a\uff0c\u6211\u4eec\u4fdd\u7559\u64a4\u9500\u4f7f\u7528\u6743\u7684\u6743\u5229\u3002 </span></p><h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700;\">2. \u98ce\u9669\u627f\u62c5</span></h2><p><span style=\" font-size:11pt;\">\u7528\u6237\u5e94\u7406\u89e3\u4f7f\u7528\u672c\u5e94\u7528\u5b58\u5728\u7684\u98ce\u9669\uff0c\u5e76\u5c06\u5168\u9762\u627f\u62c5\u4f7f\u7528\u672c\u5e94\u7528\u53ef\u80fd\u5bfc\u81f4\u7684\u4e00\u5207\u540e\u679c\u3002\u672c\u5e94\u7528\u7684\u4f5c\u8005\u6216\u56e2\u961f\u4e0d\u627f\u62c5\u56e0\u4f7f\u7528\u672c\u5e94\u7528\u800c\u4ea7\u751f\u7684\u4efb\u4f55\u8d23\u4efb\u3002 </span></p><h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700;\">3. \u514d\u8d23\u8303\u56f4</span></h2><p><span style=\" font-size:11pt;\">\u5bf9\u4e8e\u56e0\u4f7f"
                        "\u7528\u672c\u5e94\u7528\u800c\u5bfc\u81f4\u7684\u4efb\u4f55\u610f\u5916\u3001\u758f\u5ffd\u3001\u5408\u540c\u7834\u574f\u3001\u8bfd\u8c24\u3001\u7248\u6743\u6216\u5176\u4ed6\u77e5\u8bc6\u4ea7\u6743\u4fb5\u72af\u53ca\u5176\u9020\u6210\u7684\u4efb\u4f55\u5f62\u5f0f\u7684\u635f\u5931\uff0c\u672c\u5e94\u7528\u4f5c\u8005\u53ca\u5176\u56e2\u961f\u6982\u4e0d\u8d1f\u8d23\uff0c\u4ea6\u4e0d\u627f\u62c5\u4efb\u4f55\u6cd5\u5f8b\u8d23\u4efb\u3002 </span></p><h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700;\">4. \u4e0d\u53ef\u6297\u529b</span></h2><p><span style=\" font-size:11pt;\">\u5bf9\u4e8e\u56e0\u4e0d\u53ef\u6297\u529b\u6216\u4e0d\u53ef\u9884\u89c1\u7684\u4e8b\u4ef6\uff08\u5305\u62ec\u4f46\u4e0d\u9650\u4e8e\u9ed1\u5ba2\u653b\u51fb\u3001\u7b2c\u4e09\u65b9\u670d\u52a1\u6545\u969c\u3001\u653f\u5e9c\u884c\u4e3a\u6216\u81ea\u7136\u707e\u5bb3\u7b49\uff09\u5bfc\u81f4\u7684\u670d\u52a1\u4e2d\u65ad\u6216\u4f7f"
                        "\u7528\u969c\u788d\uff0c\u672c\u5e94\u7528\u4e0d\u627f\u62c5\u8d23\u4efb\uff0c\u4f46\u6211\u4eec\u5c06\u5c3d\u53ef\u80fd\u5730\u51cf\u5c11\u7528\u6237\u7531\u6b64\u906d\u53d7\u7684\u635f\u5931\u548c\u4e0d\u4fbf\u3002 </span></p><h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700;\">5. \u6cd5\u5f8b\u9002\u7528\u4e0e\u89e3\u91ca</span></h2><p><span style=\" font-size:11pt;\">\u672c\u58f0\u660e\u53ca\u672c\u5e94\u7528\u7684\u4f7f\u7528\u53d7\u4e2d\u534e\u4eba\u6c11\u5171\u548c\u56fd\u6cd5\u5f8b\u7ba1\u8f96\u3002\u672a\u5728\u672c\u58f0\u660e\u4e2d\u660e\u786e\u63d0\u53ca\u7684\u95ee\u9898\uff0c\u5c06\u4f9d\u7167\u56fd\u5bb6\u76f8\u5173\u6cd5\u5f8b\u6cd5\u89c4\u5904\u7406\u3002\u82e5\u672c\u58f0\u660e\u4e0e\u56fd\u5bb6\u6cd5\u5f8b\u6709\u51b2\u7a81\uff0c\u4ee5\u56fd\u5bb6\u6cd5\u5f8b\u4e3a\u51c6\u3002</span></p><p><span style=\" font-size:11pt;\">\u672c\u58f0\u660e\u7684\u4fee\u6539\u6743\u3001\u66f4"
                        "\u65b0\u6743\u548c\u6700\u7ec8\u89e3\u91ca\u6743\u5f52\u201c{appName}\u201d\u5e94\u7528\u7684\u4f5c\u8005\u6216\u56e2\u961f\u6240\u6709\u3002 </span></p></body></html>", None))
    # retranslateUi

