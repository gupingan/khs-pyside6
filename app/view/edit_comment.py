from pathlib import Path
from app.lib import QtCore, QtWidgets
from app.lib.core import Comment, AtUser, AtUserCenter, List
from app.utils.string import restore_str
from app.ui import edit_comment_ui
from app.view import char_picker, edit_at_user


class UserListModel(QtCore.QAbstractListModel):
    def __init__(self):
        super().__init__()

    def data(self, index: QtCore.QModelIndex, role: int = QtCore.Qt.ItemDataRole.DisplayRole):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            user = AtUserCenter.data[index.row()]  # type: AtUser
            return f'{user.name} | {user.id}'
        return None

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(AtUserCenter.data)

    def insertRow(self, row, parent=QtCore.QModelIndex(), at_user: AtUser = None):
        self.beginInsertRows(parent, row, row)
        AtUserCenter.append(at_user)
        self.endInsertRows()
        return True

    def removeRow(self, row, parent=QtCore.QModelIndex()):
        self.beginRemoveRows(parent, row, row)
        AtUserCenter.pop(row)
        self.endRemoveRows()
        return True


class EditComment(QtWidgets.QDialog):
    editedSignal = QtCore.Signal(list)

    def __init__(self, comments: List[Comment], parent=None):
        super().__init__(parent=parent)
        self.ui = edit_comment_ui.Ui_editCommentDialog()
        self.ui.setupUi(self)
        self.comments = comments
        self.build_interface()
        self.connect_ui_events()

    def build_interface(self):
        # 字符选择弹窗
        self.char_picker_dialog = char_picker.CharPicker(parent=self)
        # 评论内容编辑框
        comments = '\n'.join([comment_obj.content for comment_obj in self.comments])
        self.ui.comment_edit.setPlainText(comments)
        self.ui.split_char_edit.setText('\\n')
        # 右侧@用户列表
        self.at_users_model = UserListModel()
        self.ui.at_users_list.setModel(self.at_users_model)

        # 设置初始选中的 at_users
        at_users = []
        if self.comments:
            at_users = self.comments[0].at_users
        for row in range(self.at_users_model.rowCount()):
            index = self.at_users_model.index(row, 0)
            at_user = AtUserCenter.find(row)
            if at_user in at_users:
                self.ui.at_users_list.selectionModel().select(index, QtCore.QItemSelectionModel.SelectionFlag.Select)
            else:
                self.ui.at_users_list.selectionModel().select(index, QtCore.QItemSelectionModel.SelectionFlag.Deselect)

    def connect_ui_events(self):
        self.char_picker_dialog.selectedSignal.connect(self.ui.split_char_edit.setText)
        self.ui.import_file_btn.clicked.connect(self.handle_import_file_btn_click)
        self.ui.select_common_char_btn.clicked.connect(self.char_picker_dialog.exec)
        self.ui.create_at_user_btn.clicked.connect(self.handle_create_at_user_click)

    def handle_import_file_btn_click(self):
        """
        处理导入评论按钮的点击事件
        功能：从外部导入 .txt 文件内容
        :return:
        """
        route_folder = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.StandardLocation.DesktopLocation)
        file_dialog = QtWidgets.QFileDialog()
        file_info = file_dialog.getOpenFileName(
            self, '请选择评论素材', route_folder, '评论素材(*.txt)'
        )
        if not file_info[0]:
            return None
        comment_path = Path(file_info[0])
        with comment_path.open('r', encoding='utf8') as fr:
            self.ui.comment_edit.setPlainText(fr.read())

    def accept(self):
        raw_content = self.ui.comment_edit.toPlainText()
        contents = raw_content.split(restore_str(self.ui.split_char_edit.text()))
        at_users = [AtUserCenter.find(index.row()) for index in self.ui.at_users_list.selectedIndexes()]

        comments = []
        for content in contents:
            comment_obj = Comment(content, at_users)
            if comment_obj:
                comments.append(comment_obj)

        self.editedSignal.emit(comments)
        super().accept()

    def handle_create_at_user_click(self):
        """
        处理创建艾特用户按钮的单击事件
        :return:
        """
        edit_at_user_dialog = edit_at_user.EditAtUser(parent=self)
        edit_at_user_dialog.saved.connect(self.saved_after_create_at_user)
        edit_at_user_dialog.exec()

    def saved_after_create_at_user(self, at_user: AtUser):
        """
        保存后添加艾特用户
        :param at_user: AtUser 实例
        :return:
        """
        if isinstance(at_user, AtUser):
            self.at_users_model.insertRow(self.at_users_model.rowCount(), at_user=at_user)
            AtUserCenter.save()
