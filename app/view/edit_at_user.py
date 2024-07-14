from app.lib import QtCore, QtWidgets
from app.lib.core import AtUser
from app.ui import edit_at_user_ui
from app.utils.string import validate_user_id


class EditAtUser(QtWidgets.QDialog):
    saved = QtCore.Signal(AtUser)

    def __init__(self, parent=None, user: AtUser = None):
        super().__init__(parent=parent)
        self.ui = edit_at_user_ui.Ui_EditAtUser()
        self.ui.setupUi(self)
        self.is_create = not bool(user)
        self.user = user or AtUser('', '')
        self.build_interface()
        self.connect_ui_events()

    def build_interface(self):
        self.ui.edit_nickname.setEnabled(not self.is_create)
        if self.is_create:
            self.ui.edit_nickname.setText('创建艾特用户时无需填写昵称')
        else:
            self.ui.edit_nickname.setText(self.user.name)
        self.ui.edit_user_id.setText(self.user.id)
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
        user_id = self.ui.edit_user_id.text().strip()
        if not validate_user_id(user_id):
            QtWidgets.QMessageBox.critical(
                self, '保存失败',
                f'当前用户ID {user_id} 不合法，请重新输入'
            )
            return None

        if not self.is_create:
            self.user.name = self.ui.edit_nickname.text()
        self.user.id = user_id
        self.user.remark = self.ui.edit_remark.toPlainText()
        self.saved.emit(self.user)
        self.close()
