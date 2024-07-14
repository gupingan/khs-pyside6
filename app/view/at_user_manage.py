import xhsAPI
from loguru import logger
from app.lib import QtCore, QtWidgets, QtGui
from app.lib.core import AtUser, AtUserCenter, List, LinkedUser
from app.utils.network import NetworkPool
from app.ui import at_user_manage_ui
from app.view import edit_at_user


class AtUserProxy:
    def __init__(self, at_user):
        self.at_user: AtUser = at_user
        self.is_checked: bool = False

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.at_user == other.at_user
        return False


class AtUserTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data: List[AtUser]):
        super().__init__()
        self.proxy = [AtUserProxy(a) for a in data]
        self.checked_rows = []
        self.header = ['昵称', '用户ID', '签名', '备注']

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.proxy)

    def columnCount(self, parent=QtCore.QModelIndex()):
        return len(self.header)

    def data(self, index, role=QtCore.Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None

        row = index.row()
        col = index.column()

        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            at_user_proxy = self.proxy[row]
            at_user = at_user_proxy.at_user
            if at_user:
                if col == 0:
                    return at_user.name
                elif col == 1:
                    return at_user.id
                elif col == 2:
                    return at_user.sign
                elif col == 3:
                    return at_user.remark
            return None

        if role == QtCore.Qt.ItemDataRole.TextAlignmentRole:
            if col != len(self.header) - 1:
                return QtCore.Qt.AlignmentFlag.AlignCenter

        if role == QtCore.Qt.ItemDataRole.CheckStateRole and col == 0:
            at_user_proxy = self.proxy[row]
            return QtCore.Qt.CheckState.Checked if at_user_proxy.is_checked else QtCore.Qt.CheckState.Unchecked

        return None

    def setData(self, index, value, role=QtCore.Qt.ItemDataRole.EditRole):
        if not index.isValid():
            return False

        row = index.row()
        col = index.column()

        config_proxy = self.proxy[row]

        if role == QtCore.Qt.ItemDataRole.CheckStateRole and col == 0:
            if value == QtCore.Qt.CheckState.Checked:
                if row not in self.checked_rows:
                    self.checked_rows.append(row)
            else:
                if row in self.checked_rows:
                    self.checked_rows.remove(row)
            config_proxy.is_checked = (value == QtCore.Qt.CheckState.Checked)
            self.dataChanged.emit(index, index)
            return True

        return False

    def flags(self, index):
        if not index.isValid():
            return QtCore.Qt.ItemFlag.NoItemFlags

        flags = QtCore.Qt.ItemFlag.ItemIsEnabled

        return flags

    def headerData(self, section, orientation, role=QtCore.Qt.ItemDataRole.DisplayRole):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if orientation == QtCore.Qt.Orientation.Horizontal:
                if 0 <= section < len(self.header):
                    return self.header[section]
            elif orientation == QtCore.Qt.Orientation.Vertical:
                return str(section + 1)

        return None

    def insertRow(self, row, parent=QtCore.QModelIndex(), at_user: AtUser = None):
        self.beginInsertRows(parent, row, row)
        AtUserCenter.append(at_user)
        self.proxy.append(AtUserProxy(at_user))
        self.endInsertRows()
        return True

    def removeRow(self, row, parent=QtCore.QModelIndex()):
        self.beginRemoveRows(parent, row, row)
        AtUserCenter.pop(row)
        self.proxy.pop(row)
        self.checked_rows.clear()
        self.endRemoveRows()
        return True


class AtUserManage(QtWidgets.QDialog):
    select_all = False
    exist_sign_error = False

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowFlag(QtCore.Qt.WindowType.WindowCloseButtonHint)
        self.ui = at_user_manage_ui.Ui_AtUserManage()
        self.ui.setupUi(self)
        self.build_interface()
        self.connect_ui_events()
        self.service_deployment()

    def build_interface(self):
        self.at_user_table_model = AtUserTableModel(AtUserCenter.data)
        self.ui.tableView.setModel(self.at_user_table_model)
        self.ui.tableView.setMouseTracking(True)
        self.ui.tableView.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ui.tableView.horizontalHeader().setStretchLastSection(True)
        self.ui.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.ui.tableView.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.ui.tableView.horizontalHeader().setStretchLastSection(True)
        self.ui.toggle_select_btn.setText('取消全选' if self.select_all else '全选')

    def connect_ui_events(self):
        """
        连接各个UI控件的信号与槽函数
        :return:
        """
        self.ui.toggle_select_btn.clicked.connect(self.handle_toggle_select_click)
        self.ui.create_at_user_btn.clicked.connect(self.handle_create_at_user_click)
        self.ui.delete_at_user_btn.clicked.connect(self.handle_delete_at_user_click)
        self.ui.tableView.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.tableView.customContextMenuRequested.connect(self.show_context_menu)
        self.ui.tableView.clicked.connect(self.handle_at_user_table_item_click)
        self.ui.tableView.doubleClicked.connect(self.handle_at_user_table_item_dbclick)
        self.ui.tableView.entered.connect(self.on_at_user_table_entered)
        self.ui.get_info_btn.clicked.connect(self.on_get_info_click)

    def service_deployment(self):
        self.get_info_thread = NetworkPool()
        self.get_info_thread.set_max_thread(8)
        self.get_info_thread.allTasksDone.connect(self.on_get_info_all_finished)

    def get_selected_rows(self):
        """
        获取选中项目的行号
        :return:
        """
        return self.at_user_table_model.checked_rows

    def handle_toggle_select_click(self):
        """
        处理 全选/取消全选 切换按钮的单击事件
        :return:
        """
        if not self.select_all:
            self.ui.toggle_select_btn.setText('取消全选')
            self.select_all = True
        else:
            self.ui.toggle_select_btn.setText('全选')
            self.select_all = False

        check_state = QtCore.Qt.CheckState.Checked if self.select_all else QtCore.Qt.CheckState.Unchecked
        count = self.at_user_table_model.rowCount()
        for row in range(count):
            index = self.at_user_table_model.index(row, 0)
            self.at_user_table_model.setData(index, check_state, QtCore.Qt.ItemDataRole.CheckStateRole)

    def handle_create_at_user_click(self):
        """
        处理艾特用户添加按钮的单击事件
        :return:
        """
        edit_at_user_dialog = edit_at_user.EditAtUser(parent=self)
        edit_at_user_dialog.saved.connect(self.saved_after_create_at_user)
        edit_at_user_dialog.exec()

    def saved_after_create_at_user(self, user: AtUser):
        """
        保存后添加艾特用户
        :param user: AtUser 实例
        :return:
        """
        if isinstance(user, AtUser):
            self.at_user_table_model.insertRow(self.at_user_table_model.rowCount(), at_user=user)
            AtUserCenter.save()

    def handle_delete_at_user_click(self):
        """
        处理删除用户按钮的单击事件
        :return:
        """
        selected_rows = self.get_selected_rows()
        if selected_rows:
            result = QtWidgets.QMessageBox.question(
                self, '提示', '您确定要删除选中的艾特用户吗？',
                QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
            )
            if result == QtWidgets.QMessageBox.StandardButton.Yes:
                for row in sorted(selected_rows, reverse=True):
                    self.at_user_table_model.removeRow(row)

                AtUserCenter.save()
        else:
            QtWidgets.QMessageBox.warning(
                self, '操作失败', '你需要选择至少 1 名艾特用户才能进行删除',
            )

    def show_context_menu(self, pos):
        menu = QtWidgets.QMenu(self)
        copy_action = menu.addAction("复制")
        copy_action.triggered.connect(self.copy_selected_cell)
        menu.exec_(self.ui.tableView.mapToGlobal(pos))

    def copy_selected_cell(self):
        index = self.ui.tableView.currentIndex()
        if index.isValid():
            data = index.data(QtCore.Qt.ItemDataRole.DisplayRole)
            clipboard = QtGui.QGuiApplication.clipboard()
            clipboard.setText(str(data))

    def handle_at_user_table_item_click(self, index: QtCore.QModelIndex):
        """
        处理表格的单击事件
        :param index:
        :return:
        """
        if index.column() == 0:
            check_state = self.at_user_table_model.data(index, QtCore.Qt.ItemDataRole.CheckStateRole)
            if isinstance(check_state, QtCore.Qt.CheckState):
                new_check_state = (
                    QtCore.Qt.CheckState.Unchecked
                    if check_state == QtCore.Qt.CheckState.Checked
                    else QtCore.Qt.CheckState.Checked
                )
                self.at_user_table_model.setData(index, new_check_state, QtCore.Qt.ItemDataRole.CheckStateRole)
                select_number = len(self.get_selected_rows())

                if select_number == self.at_user_table_model.rowCount():
                    self.ui.toggle_select_btn.setText('取消全选')
                    self.select_all = True
                else:
                    self.ui.toggle_select_btn.setText('全选')
                    self.select_all = False

    def handle_at_user_table_item_dbclick(self, index: QtCore.QModelIndex):
        """
        处理艾特用户表格的双击事件
        :param index:
        :return:
        """
        if index.column() != 0:
            at_user = AtUserCenter.find(index.row())
            if isinstance(at_user, AtUser):
                edit_at_user_dialog = edit_at_user.EditAtUser(self, at_user)
                edit_at_user_dialog.saved.connect(self.saved_after_edit_at_user(index))
                edit_at_user_dialog.exec()

    def saved_after_edit_at_user(self, index: QtCore.QModelIndex):
        def wrapper(saved_at_user: AtUser):
            if saved_at_user:
                self.at_user_table_model.dataChanged.emit(index, index)

        return wrapper

    def on_at_user_table_entered(self, index):
        if index.isValid() and index.column() in {0, 2, 3}:
            data = index.data(QtCore.Qt.ItemDataRole.DisplayRole)
            QtWidgets.QToolTip.showText(
                self.ui.tableView.mapToGlobal(self.ui.tableView.visualRect(index).bottomRight()),
                str(data))

    def on_get_info_click(self):
        selected_rows = self.get_selected_rows()
        if selected_rows:
            self.exist_sign_error = False
            self.ui.get_info_btn.setEnabled(False)
            for row in selected_rows:
                start = self.at_user_table_model.index(row, 0)
                end = self.at_user_table_model.index(row, 2)
                at_user = AtUserCenter.find(row)
                linked_user = LinkedUser.from_session()
                signals = self.get_info_thread.start_task(
                    xhsAPI.G(linked_user.string_cookies).search_at_users,
                    at_user.id, 1, 1
                )
                signals.success.connect(self.on_get_info_success(at_user, start, end))

        else:
            QtWidgets.QMessageBox.warning(self, '操作失败', '你需要选择至少 1 名艾特用户才能进行获取', )

    def on_get_info_success(self, at_user: AtUser, start: QtCore.QModelIndex, end: QtCore.QModelIndex):
        def wrapper(response: dict):
            try:
                if not self.exist_sign_error:
                    if response.get('success') and response['code'] == 0:
                        if response['data'] and response['data']['items']:
                            result = response['data']['items'][0]
                            userid = result['userid']
                            nickname = result['nickname']
                            at_user.name = nickname
                            userid_sign = userid.split('_', 1)
                            at_user.sign = userid_sign[-1] if len(userid_sign) == 2 else ''
                    elif response.get('code') == -100:
                        self.exist_sign_error = True
            except Exception as e:
                logger.error('获取艾特用户信息失败，原因如下：')
                logger.exception(e)
            finally:
                self.at_user_table_model.dataChanged.emit(start, end)

        return wrapper

    def on_get_info_all_finished(self):
        AtUserCenter.save()
        self.ui.get_info_btn.setEnabled(True)
        if self.exist_sign_error:
            QtWidgets.QMessageBox.critical(self, '获取艾特用户信息失败', '联动账号可能已经登录失效')
        self.exist_sign_error = False
