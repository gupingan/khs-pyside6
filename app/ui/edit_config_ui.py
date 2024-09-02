# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_config_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QToolButton, QVBoxLayout, QWidget)

class Ui_EditConfig(object):
    def setupUi(self, EditConfig):
        if not EditConfig.objectName():
            EditConfig.setObjectName(u"EditConfig")
        EditConfig.resize(460, 567)
        self.verticalLayout_3 = QVBoxLayout(EditConfig)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_1 = QGroupBox(EditConfig)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_1)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_16 = QLabel(self.groupBox_1)
        self.label_16.setObjectName(u"label_16")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_16)

        self.config_name_edit = QLineEdit(self.groupBox_1)
        self.config_name_edit.setObjectName(u"config_name_edit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.config_name_edit.sizePolicy().hasHeightForWidth())
        self.config_name_edit.setSizePolicy(sizePolicy1)
        self.config_name_edit.setClearButtonEnabled(True)

        self.horizontalLayout_11.addWidget(self.config_name_edit)


        self.verticalLayout_16.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_23 = QLabel(self.groupBox_1)
        self.label_23.setObjectName(u"label_23")
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_21.addWidget(self.label_23)

        self.config_id_label = QLabel(self.groupBox_1)
        self.config_id_label.setObjectName(u"config_id_label")

        self.horizontalLayout_21.addWidget(self.config_id_label)

        self.smart_title_btn = QPushButton(self.groupBox_1)
        self.smart_title_btn.setObjectName(u"smart_title_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.smart_title_btn.sizePolicy().hasHeightForWidth())
        self.smart_title_btn.setSizePolicy(sizePolicy2)

        self.horizontalLayout_21.addWidget(self.smart_title_btn)


        self.verticalLayout_16.addLayout(self.horizontalLayout_21)


        self.verticalLayout_3.addWidget(self.groupBox_1)

        self.groupBox_2 = QGroupBox(EditConfig)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_22 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.radioButton_1 = QRadioButton(self.groupBox_2)
        self.radioButton_1.setObjectName(u"radioButton_1")

        self.horizontalLayout_22.addWidget(self.radioButton_1)

        self.radioButton_2 = QRadioButton(self.groupBox_2)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_22.addWidget(self.radioButton_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(EditConfig)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_17)

        self.search_edit = QLineEdit(self.groupBox_3)
        self.search_edit.setObjectName(u"search_edit")
        sizePolicy1.setHeightForWidth(self.search_edit.sizePolicy().hasHeightForWidth())
        self.search_edit.setSizePolicy(sizePolicy1)

        self.horizontalLayout_12.addWidget(self.search_edit)


        self.verticalLayout_7.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_19 = QLabel(self.groupBox_3)
        self.label_19.setObjectName(u"label_19")
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)

        self.horizontalLayout_14.addWidget(self.label_19)

        self.note_type_cb = QComboBox(self.groupBox_3)
        self.note_type_cb.addItem("")
        self.note_type_cb.addItem("")
        self.note_type_cb.addItem("")
        self.note_type_cb.addItem("")
        self.note_type_cb.addItem("")
        self.note_type_cb.setObjectName(u"note_type_cb")

        self.horizontalLayout_14.addWidget(self.note_type_cb)

        self.label_20 = QLabel(self.groupBox_3)
        self.label_20.setObjectName(u"label_20")
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)

        self.horizontalLayout_14.addWidget(self.label_20)

        self.sort_method_cb = QComboBox(self.groupBox_3)
        self.sort_method_cb.addItem("")
        self.sort_method_cb.addItem("")
        self.sort_method_cb.addItem("")
        self.sort_method_cb.setObjectName(u"sort_method_cb")

        self.horizontalLayout_14.addWidget(self.sort_method_cb)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_5)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)


        self.verticalLayout_3.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(EditConfig)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.similarity_filter_chk = QCheckBox(self.groupBox_4)
        self.similarity_filter_chk.setObjectName(u"similarity_filter_chk")

        self.horizontalLayout_4.addWidget(self.similarity_filter_chk)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.similarity_lower_limit_dsb = QDoubleSpinBox(self.groupBox_4)
        self.similarity_lower_limit_dsb.setObjectName(u"similarity_lower_limit_dsb")
        self.similarity_lower_limit_dsb.setDecimals(2)
        self.similarity_lower_limit_dsb.setMaximum(1.000000000000000)
        self.similarity_lower_limit_dsb.setSingleStep(0.010000000000000)

        self.horizontalLayout_4.addWidget(self.similarity_lower_limit_dsb)

        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.similarity_keyword_le = QLineEdit(self.groupBox_4)
        self.similarity_keyword_le.setObjectName(u"similarity_keyword_le")

        self.horizontalLayout_4.addWidget(self.similarity_keyword_le)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout_3.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(EditConfig)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setFlat(False)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.comment_chk = QCheckBox(self.groupBox_5)
        self.comment_chk.setObjectName(u"comment_chk")

        self.horizontalLayout_15.addWidget(self.comment_chk)

        self.fav_no_comment_chk = QCheckBox(self.groupBox_5)
        self.fav_no_comment_chk.setObjectName(u"fav_no_comment_chk")
        self.fav_no_comment_chk.setTristate(False)

        self.horizontalLayout_15.addWidget(self.fav_no_comment_chk)

        self.comment_fav_chk = QCheckBox(self.groupBox_5)
        self.comment_fav_chk.setObjectName(u"comment_fav_chk")
        self.comment_fav_chk.setTristate(False)

        self.horizontalLayout_15.addWidget(self.comment_fav_chk)

        self.check_block_chk = QCheckBox(self.groupBox_5)
        self.check_block_chk.setObjectName(u"check_block_chk")

        self.horizontalLayout_15.addWidget(self.check_block_chk)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.edit_comment_btn = QToolButton(self.groupBox_5)
        self.edit_comment_btn.setObjectName(u"edit_comment_btn")
        sizePolicy1.setHeightForWidth(self.edit_comment_btn.sizePolicy().hasHeightForWidth())
        self.edit_comment_btn.setSizePolicy(sizePolicy1)
        self.edit_comment_btn.setPopupMode(QToolButton.DelayedPopup)
        self.edit_comment_btn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_17.addWidget(self.edit_comment_btn)


        self.verticalLayout_6.addLayout(self.horizontalLayout_17)


        self.verticalLayout_3.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(EditConfig)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout = QVBoxLayout(self.groupBox_6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.linked_check_chk = QCheckBox(self.groupBox_6)
        self.linked_check_chk.setObjectName(u"linked_check_chk")

        self.horizontalLayout_3.addWidget(self.linked_check_chk)

        self.skip_over_comment_chk = QCheckBox(self.groupBox_6)
        self.skip_over_comment_chk.setObjectName(u"skip_over_comment_chk")

        self.horizontalLayout_3.addWidget(self.skip_over_comment_chk)

        self.label_22 = QLabel(self.groupBox_6)
        self.label_22.setObjectName(u"label_22")
        sizePolicy2.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy2)
        self.label_22.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_22)

        self.comment_threshold_sb = QSpinBox(self.groupBox_6)
        self.comment_threshold_sb.setObjectName(u"comment_threshold_sb")
        self.comment_threshold_sb.setMaximum(9999)

        self.horizontalLayout_3.addWidget(self.comment_threshold_sb)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.consecutive_block_stop_chk = QCheckBox(self.groupBox_6)
        self.consecutive_block_stop_chk.setObjectName(u"consecutive_block_stop_chk")

        self.horizontalLayout_2.addWidget(self.consecutive_block_stop_chk)

        self.label_18 = QLabel(self.groupBox_6)
        self.label_18.setObjectName(u"label_18")
        sizePolicy2.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy2)
        self.label_18.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_18)

        self.consecutive_block_threshold_sb = QSpinBox(self.groupBox_6)
        self.consecutive_block_threshold_sb.setObjectName(u"consecutive_block_threshold_sb")
        self.consecutive_block_threshold_sb.setMaximum(999)

        self.horizontalLayout_2.addWidget(self.consecutive_block_threshold_sb)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.overall_block_stop_chk = QCheckBox(self.groupBox_6)
        self.overall_block_stop_chk.setObjectName(u"overall_block_stop_chk")

        self.horizontalLayout_2.addWidget(self.overall_block_stop_chk)

        self.label_21 = QLabel(self.groupBox_6)
        self.label_21.setObjectName(u"label_21")
        sizePolicy2.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy2)
        self.label_21.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_21)

        self.overall_block_threshold_sb = QSpinBox(self.groupBox_6)
        self.overall_block_threshold_sb.setObjectName(u"overall_block_threshold_sb")
        self.overall_block_threshold_sb.setMaximum(999)

        self.horizontalLayout_2.addWidget(self.overall_block_threshold_sb)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.retry_after_block_chk = QCheckBox(self.groupBox_6)
        self.retry_after_block_chk.setObjectName(u"retry_after_block_chk")
        self.retry_after_block_chk.setTristate(False)

        self.horizontalLayout.addWidget(self.retry_after_block_chk)

        self.random_comment_chk = QCheckBox(self.groupBox_6)
        self.random_comment_chk.setObjectName(u"random_comment_chk")

        self.horizontalLayout.addWidget(self.random_comment_chk)

        self.label_14 = QLabel(self.groupBox_6)
        self.label_14.setObjectName(u"label_14")
        sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy2)
        self.label_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_14)

        self.retry_count_sb = QSpinBox(self.groupBox_6)
        self.retry_count_sb.setObjectName(u"retry_count_sb")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.retry_count_sb.sizePolicy().hasHeightForWidth())
        self.retry_count_sb.setSizePolicy(sizePolicy3)
        self.retry_count_sb.setMaximum(9)

        self.horizontalLayout.addWidget(self.retry_count_sb)

        self.label_15 = QLabel(self.groupBox_6)
        self.label_15.setObjectName(u"label_15")
        sizePolicy2.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy2)
        self.label_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_15)

        self.retry_interval_ds = QDoubleSpinBox(self.groupBox_6)
        self.retry_interval_ds.setObjectName(u"retry_interval_ds")
        sizePolicy3.setHeightForWidth(self.retry_interval_ds.sizePolicy().hasHeightForWidth())
        self.retry_interval_ds.setSizePolicy(sizePolicy3)
        self.retry_interval_ds.setDecimals(1)
        self.retry_interval_ds.setMinimum(1.000000000000000)
        self.retry_interval_ds.setMaximum(100.000000000000000)
        self.retry_interval_ds.setSingleStep(1.000000000000000)

        self.horizontalLayout.addWidget(self.retry_interval_ds)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.groupBox_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.cancel_btn = QPushButton(EditConfig)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.horizontalLayout_7.addWidget(self.cancel_btn)

        self.save_btn = QPushButton(EditConfig)
        self.save_btn.setObjectName(u"save_btn")

        self.horizontalLayout_7.addWidget(self.save_btn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)


        self.retranslateUi(EditConfig)

        QMetaObject.connectSlotsByName(EditConfig)
    # setupUi

    def retranslateUi(self, EditConfig):
        EditConfig.setWindowTitle(QCoreApplication.translate("EditConfig", u"\u7f16\u8f91\u914d\u7f6e", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("EditConfig", u"\u914d\u7f6e\u4fe1\u606f", None))
        self.label_16.setText(QCoreApplication.translate("EditConfig", u"\u540d\u79f0", None))
        self.config_name_edit.setPlaceholderText(QCoreApplication.translate("EditConfig", u"\u8bf7\u8bbe\u5b9a\u542b\u4e49\u6e05\u6670\u660e\u4e86\u7684\u540d\u79f0\uff0c\u65b9\u4fbf\u540e\u7eed\u4f7f\u7528", None))
        self.label_23.setText(QCoreApplication.translate("EditConfig", u"\u7f16\u53f7", None))
        self.config_id_label.setText(QCoreApplication.translate("EditConfig", u"\u6682\u672a\u83b7\u53d6\u5230\u914d\u7f6eID", None))
        self.smart_title_btn.setText(QCoreApplication.translate("EditConfig", u"\u667a\u80fd\u6807\u9898", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("EditConfig", u"\u91c7\u96c6\u65b9\u5f0f", None))
        self.radioButton_1.setText(QCoreApplication.translate("EditConfig", u"\u5728\u7ebf\u641c\u7d22", None))
        self.radioButton_2.setText(QCoreApplication.translate("EditConfig", u"\u63a8\u8350\u9875\u91c7\u96c6", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("EditConfig", u"\u5728\u7ebf\u641c\u7d22", None))
        self.label_17.setText(QCoreApplication.translate("EditConfig", u"\u641c\u7d22\u8bcd", None))
        self.search_edit.setPlaceholderText(QCoreApplication.translate("EditConfig", u"\u591a\u641c\u7d22\u8bcd\u4ee5 | \u5206\u9694", None))
        self.label_19.setText(QCoreApplication.translate("EditConfig", u"\u7b14\u8bb0\u7c7b\u578b", None))
        self.note_type_cb.setItemText(0, QCoreApplication.translate("EditConfig", u"\u91c7\u96c6\u5168\u90e8", None))
        self.note_type_cb.setItemText(1, QCoreApplication.translate("EditConfig", u"\u4ec5\u91c7\u96c6\u56fe\u6587", None))
        self.note_type_cb.setItemText(2, QCoreApplication.translate("EditConfig", u"\u4ec5\u91c7\u96c6\u89c6\u9891", None))
        self.note_type_cb.setItemText(3, QCoreApplication.translate("EditConfig", u"\u5148\u56fe\u6587\u540e\u89c6\u9891", None))
        self.note_type_cb.setItemText(4, QCoreApplication.translate("EditConfig", u"\u5148\u89c6\u9891\u540e\u56fe\u6587", None))

        self.label_20.setText(QCoreApplication.translate("EditConfig", u"\u6392\u5e8f\u65b9\u5f0f", None))
        self.sort_method_cb.setItemText(0, QCoreApplication.translate("EditConfig", u"\u7efc\u5408", None))
        self.sort_method_cb.setItemText(1, QCoreApplication.translate("EditConfig", u"\u6700\u65b0", None))
        self.sort_method_cb.setItemText(2, QCoreApplication.translate("EditConfig", u"\u6700\u70ed", None))

        self.groupBox_4.setTitle(QCoreApplication.translate("EditConfig", u"\u76f8\u4f3c\u5ea6\u8fc7\u7b5b", None))
        self.similarity_filter_chk.setText(QCoreApplication.translate("EditConfig", u"\u542f\u7528", None))
        self.label_2.setText(QCoreApplication.translate("EditConfig", u"\u76f8\u4f3c\u5ea6\u5e95\u9650", None))
        self.label.setText(QCoreApplication.translate("EditConfig", u"\u5173\u952e\u8bcd", None))
        self.similarity_keyword_le.setPlaceholderText(QCoreApplication.translate("EditConfig", u"\u591a\u5173\u952e\u8bcd\u4ee5 | \u5206\u9694", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("EditConfig", u"\u8bc4\u8bba\u8bbe\u7f6e", None))
        self.comment_chk.setText(QCoreApplication.translate("EditConfig", u"\u662f\u5426\u8bc4\u8bba", None))
        self.fav_no_comment_chk.setText(QCoreApplication.translate("EditConfig", u"\u5df2\u6536\u85cf\u4e0d\u8bc4\u8bba", None))
        self.comment_fav_chk.setText(QCoreApplication.translate("EditConfig", u"\u8bc4\u8bba\u540e\u6536\u85cf", None))
        self.check_block_chk.setText(QCoreApplication.translate("EditConfig", u"\u662f\u5426\u68c0\u67e5\u5c4f\u853d", None))
        self.edit_comment_btn.setText(QCoreApplication.translate("EditConfig", u"\u7f16\u8f91\u8bc4\u8bba", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("EditConfig", u"\u5c4f\u853d\u53c2\u6570", None))
        self.linked_check_chk.setText(QCoreApplication.translate("EditConfig", u"\u8054\u52a8\u68c0\u67e5[\u52a0\u901f]", None))
        self.skip_over_comment_chk.setText(QCoreApplication.translate("EditConfig", u"\u8fc7\u591a\u8bc4\u8bba\u4e0d\u68c0\u67e5\u5c4f\u853d", None))
        self.label_22.setText(QCoreApplication.translate("EditConfig", u"\u9608\u503c", None))
        self.consecutive_block_stop_chk.setText(QCoreApplication.translate("EditConfig", u"\u8fde\u7eed\u5c4f\u853d\u505c\u6b62", None))
        self.label_18.setText(QCoreApplication.translate("EditConfig", u"\u9608\u503c", None))
        self.overall_block_stop_chk.setText(QCoreApplication.translate("EditConfig", u"\u603b\u4f53\u5c4f\u853d\u505c\u6b62", None))
        self.label_21.setText(QCoreApplication.translate("EditConfig", u"\u9608\u503c", None))
        self.retry_after_block_chk.setText(QCoreApplication.translate("EditConfig", u"\u5c4f\u853d\u540e\u91cd\u8bd5", None))
        self.random_comment_chk.setText(QCoreApplication.translate("EditConfig", u"\u8bc4\u8bba\u968f\u673a", None))
        self.label_14.setText(QCoreApplication.translate("EditConfig", u"\u91cd\u8bd5", None))
        self.retry_count_sb.setSuffix(QCoreApplication.translate("EditConfig", u" \u6b21", None))
        self.label_15.setText(QCoreApplication.translate("EditConfig", u"\u91cd\u8bd5\u95f4\u9694", None))
        self.retry_interval_ds.setPrefix("")
        self.retry_interval_ds.setSuffix(QCoreApplication.translate("EditConfig", u" \u79d2", None))
        self.cancel_btn.setText(QCoreApplication.translate("EditConfig", u"\u53d6\u6d88", None))
        self.save_btn.setText(QCoreApplication.translate("EditConfig", u"\u4fdd\u5b58", None))
    # retranslateUi

