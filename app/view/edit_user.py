from app.lib import QtCore, QtWidgets
from app.lib.core import PrivateUser, PrivateUserCenter
from app.ui import edit_user_ui


class EditUser(QtWidgets.QDialog):
    saved = QtCore.Signal(PrivateUser)

    def __init__(self, parent=None, user: PrivateUser = None):
        super().__init__(parent=parent)
        self.ui = edit_user_ui.Ui_EditUser()
        self.ui.setupUi(self)
        self.user = user
        self.build_interface()
        self.connect_ui_events()

    def build_interface(self):
        self.work_group = QtWidgets.QButtonGroup()
        self.work_group.addButton(self.ui.radioButton_4, 0)
        self.work_group.addButton(self.ui.radioButton_5, 1)
        self.work_group.setExclusive(True)
        if isinstance(self.user.working, bool):
            self.work_group.button(int(self.user.working)).setChecked(True)
        else:
            self.work_group.button(0).setChecked(True)

        self.available_group = QtWidgets.QButtonGroup()
        self.available_group.addButton(self.ui.radioButton_1, 0)
        self.available_group.addButton(self.ui.radioButton_2, 1)
        self.available_group.addButton(self.ui.radioButton_3, 2)
        self.available_group.setExclusive(True)
        if -1 <= self.user.available <= 1:
            self.available_group.button(self.user.available + 1).setChecked(True)
        else:
            self.available_group.button(1).setChecked(True)

        self.comment_group = QtWidgets.QButtonGroup()
        self.comment_group.addButton(self.ui.radioButton_6, 0)
        self.comment_group.addButton(self.ui.radioButton_7, 1)
        self.comment_group.addButton(self.ui.radioButton_8, 2)
        self.comment_group.addButton(self.ui.radioButton_9, 3)
        if -2 <= self.user.comment_state <= 1:
            self.comment_group.button(self.user.comment_state + 2).setChecked(True)
        else:
            self.comment_group.button(1).setChecked(True)

        self.ui.label_user_id.setText(self.user.id)
        self.ui.edit_nickname.setText(self.user.name)
        self.ui.edit_session.setText(self.user.session)
        self.ui.edit_remark.setText(self.user.remark)
        self.ui.cancel_button.setFocus()

    def connect_ui_events(self):
        self.ui.cancel_button.clicked.connect(self.close)
        self.ui.save_button.clicked.connect(self.handle_save_btn_click)

    def handle_save_btn_click(self):
        """
        处理保存按钮点击事件
        :return:
        """
        self.user.name = self.ui.edit_nickname.text()
        self.user.session = self.ui.edit_session.text()
        self.user.remark = self.ui.edit_remark.toPlainText()
        self.user.available = self.get_selected_available_state()
        self.user.working = self.get_selected_work_state()
        self.user.comment_state = self.get_selected_comment_state()
        self.user.update_time()
        PrivateUserCenter.save()
        self.saved.emit(self.user)
        self.close()

    def get_selected_work_state(self):
        """
        获取用户选中的工作状态
        :return: 未选中时返回 False，否则返回正常选中 False True
        """
        checked_id = self.work_group.checkedId()
        if 0 <= checked_id <= 1:
            return bool(checked_id)
        else:
            return False

    def get_selected_available_state(self):
        """
        获取用户选中的登录状态
        :return: 未选中时返回 -1，否则返回正常选中 -1 0 1
        """
        checked_id = self.available_group.checkedId()
        if 0 <= checked_id <= 2:
            return checked_id - 1
        else:
            return -1

    def get_selected_comment_state(self):
        """
        获取用户选中的评论状态
        :return: 未选中时返回 -1，否则返回正常选中 -2 -1 0 1
        """
        checked_id = self.comment_group.checkedId()
        if 0 <= checked_id <= 3:
            return checked_id - 2
        else:
            return -1

