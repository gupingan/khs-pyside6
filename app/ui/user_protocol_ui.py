# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_protocol_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_UserProtocol(object):
    def setupUi(self, UserProtocol):
        if not UserProtocol.objectName():
            UserProtocol.setObjectName(u"UserProtocol")
        UserProtocol.resize(513, 480)
        self.verticalLayout = QVBoxLayout(UserProtocol)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(UserProtocol)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 476, 938))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size: 11pt;")
        self.label.setTextFormat(Qt.MarkdownText)
        self.label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_2 = QLabel(UserProtocol)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-size: 10pt;")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_date = QLabel(UserProtocol)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setStyleSheet(u"font: 11pt \"\u534e\u6587\u884c\u6977\";")

        self.horizontalLayout_2.addWidget(self.label_date)

        self.widget = QWidget(UserProtocol)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(30, 0))

        self.horizontalLayout_2.addWidget(self.widget)

        self.label_3 = QLabel(UserProtocol)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font-size: 10pt;")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.name_edit = QLineEdit(UserProtocol)
        self.name_edit.setObjectName(u"name_edit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_edit.sizePolicy().hasHeightForWidth())
        self.name_edit.setSizePolicy(sizePolicy)
        self.name_edit.setMinimumSize(QSize(99, 0))
        self.name_edit.setStyleSheet(u"QLineEdit {\n"
"	font: 11pt \"\u534e\u6587\u884c\u6977\";\n"
"	border: none;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-bottom: 1px solid black; \n"
"}\n"
"QLineEdit:focus {\n"
"	border-bottom: 1px solid blue;  \n"
"}")
        self.name_edit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.name_edit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.download_btn = QPushButton(UserProtocol)
        self.download_btn.setObjectName(u"download_btn")
        self.download_btn.setStyleSheet(u"font-size: 11pt;")

        self.horizontalLayout.addWidget(self.download_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancel_btn = QPushButton(UserProtocol)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setStyleSheet(u"color: rgb(0, 170, 0);\n"
"font-size: 11pt;")

        self.horizontalLayout.addWidget(self.cancel_btn)

        self.confirm_btn = QPushButton(UserProtocol)
        self.confirm_btn.setObjectName(u"confirm_btn")
        self.confirm_btn.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font-size: 11pt;")

        self.horizontalLayout.addWidget(self.confirm_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(UserProtocol)

        QMetaObject.connectSlotsByName(UserProtocol)
    # setupUi

    def retranslateUi(self, UserProtocol):
        UserProtocol.setWindowTitle(QCoreApplication.translate("UserProtocol", u"\u7528\u6237\u534f\u8bae", None))
        self.label.setText(QCoreApplication.translate("UserProtocol", u"# **{appName}\u7528\u6237\u534f\u8bae**\n"
"\n"
"## **1. \u534f\u8bae\u63a5\u53d7**\n"
"\n"
"\u6b22\u8fce\u60a8\u4f7f\u7528\u201c{appName}\u201d\u8f6f\u4ef6\uff08\u4ee5\u4e0b\u7b80\u79f0\u201c\u672c\u8f6f\u4ef6\u201d\uff09\u3002\u672c\u8f6f\u4ef6\u662f\u4e00\u4e2a\u5f00\u6e90\u7684\u81ea\u52a8\u5316\u5de5\u5177\uff0c\u65e8\u5728\u901a\u8fc7\u4f7f\u7528\u5c0f\u7ea2\u4e66\u5b98\u65b9API\u63a5\u53e3\u6765\u5e2e\u52a9\u7528\u6237\u81ea\u52a8\u5316\u64cd\u4f5c\uff0c\u5982\u70b9\u8d5e\u7b14\u8bb0\u4f5c\u54c1\u7b49\u884c\u4e3a\u3002\n"
"\n"
"\u5728\u60a8\u4e0b\u8f7d\u3001\u5b89\u88c5\u6216\u4f7f\u7528\u672c\u8f6f\u4ef6\u4e4b\u524d\uff0c\u8bf7\u4ed4\u7ec6\u9605\u8bfb\u672c\u534f\u8bae\u7684\u5168\u90e8\u6761\u6b3e\u3002\u901a\u8fc7\u4e0b\u8f7d\u3001\u5b89\u88c5\u3001\u590d\u5236\u6216\u4ee5\u5176\u4ed6\u65b9\u5f0f\u4f7f\u7528\u672c\u8f6f\u4ef6\uff0c\u60a8\u8868\u660e\u60a8\u540c\u610f\u63a5\u53d7\u672c\u534f\u8bae\u7684\u6761\u6b3e\u3002\u5982\u679c\u60a8\u4e0d\u540c\u610f\u672c\u534f\u8bae\u7684\u6761\u6b3e\uff0c\u8bf7"
                        "\u4e0d\u8981\u4e0b\u8f7d\u3001\u5b89\u88c5\u6216\u4f7f\u7528\u672c\u8f6f\u4ef6\u3002\n"
"\n"
"## **2. \u8bb8\u53ef\u8303\u56f4**\n"
"\n"
"\u672c\u8f6f\u4ef6\u7684\u57fa\u7840\u8f6f\u4ef6\u4e3a\u5f00\u6e90\u8f6f\u4ef6\uff0c\u57fa\u7840\u8f6f\u4ef6\u9075\u5faa MIT \u7684\u6761\u6b3e\uff0c\u672c\u8f6f\u4ef6\u57fa\u4e8e\u8be5\u8f6f\u4ef6\u4e4b\u4e0a\u4fee\u6539\u52a0\u5f3a\u3002\n"
"\n"
"## **3. \u7528\u6237\u8d23\u4efb**\n"
"\n"
"- \u60a8\u627f\u8ba4\u4f7f\u7528\u672c\u8f6f\u4ef6\u7684\u6240\u6709\u98ce\u9669\u7531\u60a8\u4e2a\u4eba\u627f\u62c5\u3002\n"
"- \u60a8\u540c\u610f\u4e0d\u5c06\u672c\u8f6f\u4ef6\u7528\u4e8e\u4efb\u4f55\u975e\u6cd5\u76ee\u7684\u6216\u4ee5\u4efb\u4f55\u975e\u6cd5\u65b9\u5f0f\u4f7f\u7528\u672c\u8f6f\u4ef6\u3002\n"
"- \u60a8\u9700\u8d1f\u8d23\u9075\u5b88\u6240\u6709\u9002\u7528\u7684\u5f53\u5730\u3001\u56fd\u5bb6\u548c\u56fd\u9645\u6cd5\u5f8b\u548c\u89c4\u5b9a\u3002\n"
"\n"
"## **4. \u514d\u8d23\u58f0\u660e**\n"
"\n"
"- \u672c\u8f6f\u4ef6\u4ee5\u201c\u73b0\u72b6\u201d\u548c\u201c\u53ef\u7528"
                        "\u201d\u57fa\u7840\u63d0\u4f9b\uff0c\u6ca1\u6709\u4efb\u4f55\u5f62\u5f0f\u7684\u660e\u793a\u6216\u6697\u793a\u7684\u4fdd\u8bc1\u3002\n"
"- \u5f00\u53d1\u8005\u4e0d\u5bf9\u56e0\u4f7f\u7528\u6216\u65e0\u6cd5\u4f7f\u7528\u672c\u8f6f\u4ef6\uff08\u5305\u62ec\u4f46\u4e0d\u9650\u4e8e\u6570\u636e\u4e22\u5931\u6216\u8f6f\u4ef6\u8fd0\u884c\u4e0d\u7a33\u5b9a\uff09\u6240\u9020\u6210\u7684\u4efb\u4f55\u76f4\u63a5\u3001\u95f4\u63a5\u3001\u5076\u7136\u3001\u7279\u6b8a\u3001\u8fde\u5e26\u6216\u60e9\u7f5a\u6027\u7684\u635f\u5bb3\u8d1f\u8d23\u3002\n"
"- \u5f00\u53d1\u8005\u4e0d\u4fdd\u8bc1\u672c\u8f6f\u4ef6\u7684\u8fde\u7eed\u6027\u548c\u5b89\u5168\u6027\uff0c\u4f7f\u7528\u8005\u5e94\u81ea\u884c\u627f\u62c5\u4f7f\u7528\u672c\u8f6f\u4ef6\u7684\u98ce\u9669\u3002\n"
"\n"
"## **5. \u77e5\u8bc6\u4ea7\u6743**\n"
"\n"
"\u672c\u8f6f\u4ef6\u7684\u7248\u6743\u53ca\u5176\u6240\u6709\u6743\u5229\u3001\u5229\u76ca\u548c\u6210\u679c\u5f52\u539f\u4f5c\u8005\u6240\u6709\u3002\u672c\u8f6f\u4ef6\u7684\u4f7f\u7528\u4e0d\u89c6\u4e3a\u8f6c\u8ba9\u4efb"
                        "\u4f55\u77e5\u8bc6\u4ea7\u6743\u3002\n"
"\n"
"## **6. \u534f\u8bae\u53d8\u66f4\u548c\u7ec8\u6b62**\n"
"\n"
"\u5f00\u53d1\u8005\u6709\u6743\u5728\u5fc5\u8981\u65f6\u4fee\u6539\u534f\u8bae\u6761\u6b3e\u3002\u4fee\u6539\u540e\u7684\u534f\u8bae\u4e00\u65e6\u5728\u672c\u8f6f\u4ef6\u7684\u76f8\u5173\u9875\u9762\u516c\u5e03\u5373\u6709\u6548\u4ee3\u66ff\u539f\u6765\u7684\u534f\u8bae\u3002\u60a8\u53ef\u968f\u65f6\u5220\u9664\u672c\u8f6f\u4ef6\u4ee5\u7ec8\u6b62\u672c\u534f\u8bae\u3002\n"
"\n"
"## **7. \u5176\u4ed6**\n"
"\n"
"\u672c\u534f\u8bae\u7684\u89e3\u91ca\u3001\u9002\u7528\u53ca\u4e89\u8bae\u7684\u89e3\u51b3\uff0c\u9002\u7528\u4e8e\u4e2d\u56fd\u5927\u9646\u5730\u533a\u7684\u6cd5\u5f8b\u3002\u82e5\u60a8\u548c\u5f00\u53d1\u8005\u6216\u8005\u6240\u6709\u8005\u4e4b\u95f4\u53d1\u751f\u4efb\u4f55\u4e89\u8bae\u6216\u7ea0\u7eb7\uff0c\u9996\u5148\u5e94\u53cb\u597d\u534f\u5546\u89e3\u51b3\uff0c\u534f\u5546\u4e0d\u6210\u7684\uff0c\u4efb\u4e00\u65b9\u53ef\u63d0\u4ea4\u5f00\u53d1\u8005\u6216\u6240\u6709\u8005\u6240\u5728\u5730"
                        "\u7684\u6cd5\u9662\u8bc9\u8bbc\u89e3\u51b3\u3002\n"
"\n"
"---\n"
"\n"
"**\u8bf7\u5728\u4e0b\u8f7d\u6216\u4f7f\u7528\u672c\u8f6f\u4ef6\u524d\u4ed4\u7ec6\u9605\u8bfb\u5e76\u540c\u610f\u4ee5\u4e0a\u6761\u6b3e\u3002**\n"
"", None))
        self.label_2.setText(QCoreApplication.translate("UserProtocol", u"\u7b7e\u7f72\u65e5\u671f\uff1a", None))
        self.label_date.setText(QCoreApplication.translate("UserProtocol", u"---", None))
        self.label_3.setText(QCoreApplication.translate("UserProtocol", u"\u7b7e\u7f72\u4eba\uff1a", None))
        self.download_btn.setText(QCoreApplication.translate("UserProtocol", u"\u4e0b\u8f7d", None))
        self.cancel_btn.setText(QCoreApplication.translate("UserProtocol", u"\u62d2\u7edd\u5e76\u9000\u51fa", None))
        self.confirm_btn.setText(QCoreApplication.translate("UserProtocol", u"\u540c\u610f\u5e76\u4f7f\u7528", None))
    # retranslateUi

