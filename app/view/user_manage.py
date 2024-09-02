import threading
import random
import re
import time
import pathlib
import xhs
from loguru import logger
from app.lib import QtCore, QtWidgets, QtGui
from app.lib.browser import startup_browser
from app.lib.core import PrivateUser, PrivateUserCenter, List, TomlBase
from app.lib.globals import CellStates
from app.ui import user_manage_ui
from app.utils.network import NetworkPool
from app.view import create_user, edit_user


class PrivateUserProxy:
    def __init__(self, private_user):
        self.private_user: PrivateUser = private_user
        self.is_checked: bool = False

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.private_user == other.private_user
        return False


class UserTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data: List[PrivateUser]):
        super().__init__()
        self.proxy = [PrivateUserProxy(p_u) for p_u in data]
        self.checked_rows = []
        self.header = ['昵称', '用户ID', '工作状态', '登录状态', '评论状态', '修改时间', '创建时间', '备注']

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
            private_user_proxy = self.proxy[row]
            private_user = private_user_proxy.private_user
            if private_user:
                if col == 0:
                    return private_user.name
                elif col == 1:
                    return private_user.id
                elif col == 2:
                    return CellStates.get(CellStates.WORK_STATES, private_user.working).display_name
                elif col == 3:
                    return CellStates.get(CellStates.LOGIN_STATES, private_user.available).display_name
                elif col == 4:
                    return CellStates.get(CellStates.COMMENT_STATES, private_user.comment_state).display_name
                elif col == 5:
                    return private_user.modify_time
                elif col == 6:
                    return private_user.create_time
                elif col == 7:
                    return private_user.remark
            return None

        if role == QtCore.Qt.ItemDataRole.ForegroundRole:
            private_user_proxy = self.proxy[row]
            private_user = private_user_proxy.private_user
            if private_user:
                if col == 2:
                    color_str = CellStates.get(CellStates.WORK_STATES, private_user.working).foreground_color
                    return QtGui.QBrush(QtGui.QColor(color_str))
                elif col == 3:
                    color_str = CellStates.get(CellStates.LOGIN_STATES, private_user.available).foreground_color
                    return QtGui.QBrush(QtGui.QColor(color_str))
                elif col == 4:
                    color_str = CellStates.get(CellStates.COMMENT_STATES, private_user.comment_state).foreground_color
                    return QtGui.QBrush(QtGui.QColor(color_str))
            return None

        if role == QtCore.Qt.ItemDataRole.TextAlignmentRole:
            if col != len(self.header) - 1:
                return QtCore.Qt.AlignmentFlag.AlignCenter

        if role == QtCore.Qt.ItemDataRole.CheckStateRole and col == 0:
            private_user_proxy = self.proxy[row]
            private_user = private_user_proxy.private_user
            if private_user.working:
                return QtCore.Qt.CheckState.Unchecked
            return QtCore.Qt.CheckState.Checked if private_user_proxy.is_checked else QtCore.Qt.CheckState.Unchecked

        return None

    def setData(self, index, value, role=QtCore.Qt.ItemDataRole.EditRole):
        if not index.isValid():
            return False

        row = index.row()
        col = index.column()

        private_user_proxy = self.proxy[row]

        if role == QtCore.Qt.ItemDataRole.CheckStateRole and col == 0:
            if value == QtCore.Qt.CheckState.Checked:
                if row not in self.checked_rows:
                    self.checked_rows.append(row)
            else:
                if row in self.checked_rows:
                    self.checked_rows.remove(row)
            private_user_proxy.is_checked = (value == QtCore.Qt.CheckState.Checked)
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

    def insertRow(self, row, parent=QtCore.QModelIndex(), private_user: PrivateUser = None):
        self.beginInsertRows(parent, row, row)
        self.proxy.append(PrivateUserProxy(private_user))
        self.endInsertRows()
        return True

    def removeRow(self, row, parent=QtCore.QModelIndex()):
        self.beginRemoveRows(parent, row, row)
        PrivateUserCenter.pop(row)
        self.proxy.pop(row)
        self.checked_rows.clear()
        self.endRemoveRows()
        return True


class CommentProxy:
    def __init__(self, user: PrivateUser, index: QtCore.QModelIndex, note_id: str):
        self.user = user
        self.index = index
        self.note_id = note_id
        self.comment_id = None


class UserManage(QtWidgets.QDialog):
    select_all = False

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowFlag(QtCore.Qt.WindowType.WindowCloseButtonHint)
        self.ui = user_manage_ui.Ui_UserManage()
        self.ui.setupUi(self)
        self.build_interface()
        self.connect_ui_events()
        self.service_deployment()

    def build_interface(self):
        self.private_user_table_model = UserTableModel(PrivateUserCenter.data)
        self.ui.tableView.setModel(self.private_user_table_model)
        self.ui.tableView.setMouseTracking(True)
        self.ui.tableView.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ui.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.ui.tableView.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.ui.tableView.horizontalHeader().setStretchLastSection(True)
        self.ui.toggle_select_btn.setText('取消全选' if self.select_all else '全选')
        self.ui.user_number.setText(f'{self.private_user_table_model.rowCount()}个')

    def connect_ui_events(self):
        """
        连接各个UI控件的信号与槽函数
        :return:
        """
        self.ui.toggle_select_btn.clicked.connect(self.handle_toggle_select_click)
        self.ui.check_login_btn.clicked.connect(self.handle_check_login_btn_click)
        self.ui.check_comment_btn.clicked.connect(self.handle_check_shield_btn_click)
        self.ui.create_user_btn.clicked.connect(self.handle_create_user_click)
        self.ui.delete_user_btn.clicked.connect(self.handle_delete_user_click)
        self.ui.tableView.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.tableView.customContextMenuRequested.connect(self.show_context_menu)
        self.ui.tableView.clicked.connect(self.handle_user_table_item_click)
        self.ui.tableView.doubleClicked.connect(self.handle_user_table_item_dbclick)
        self.ui.tableView.entered.connect(self.on_user_table_entered)

    def get_selected_rows(self):
        """
        获取选中项目的行号
        :return:
        """
        return self.private_user_table_model.checked_rows

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
        count = self.private_user_table_model.rowCount()
        display_select_count = count if self.select_all else 0
        for row in range(count):
            user = PrivateUserCenter.find(row)
            if user and not user.working:
                index = self.private_user_table_model.index(row, 0)
                self.private_user_table_model.setData(index, check_state, QtCore.Qt.ItemDataRole.CheckStateRole)
                self.ui.select_user_number.setText(f'{display_select_count}个')

    def service_deployment(self):
        self.check_login_thread = NetworkPool()
        self.check_login_thread.set_max_thread(8)
        self.check_login_thread.allTasksDone.connect(self.on_all_check_finished)
        self.post_comment_thead = NetworkPool()
        self.post_comment_thead.set_max_thread(6)
        self.check_comment_thread = NetworkPool()
        self.check_comment_thread.set_max_thread(6)
        self.check_comment_thread.allTasksDone.connect(self.on_all_check_finished)

    def handle_check_login_btn_click(self):
        """
        处理检测用户登录状态按钮的单击事件
        :return:
        """
        select_rows = self.get_selected_rows()
        if select_rows:
            # fixed: 修复未选中任意用户时 检测用户登录按钮 持续无法点击的问题
            self.ui.check_comment_btn.setEnabled(False)
            self.ui.check_login_btn.setEnabled(False)

        for row in select_rows:
            user = PrivateUserCenter.find(row)
            index = self.private_user_table_model.index(row, 3)
            if user:
                signals = self.check_login_thread.start_task(xhs.API().set_cookies(user.string_cookies).user_me)
                signals.success.connect(self.on_check_login_success(user, index))

    def on_check_login_success(self, user: PrivateUser, index: QtCore.QModelIndex):

        def wrapper(response: dict):
            try:
                user.available = -1
                if response.get('success') and response['code'] == 0:
                    user.available = 1
                elif response['code'] == -100:
                    user.available = 0
            except Exception as e:
                logger.exception(e)
            finally:
                self.private_user_table_model.dataChanged.emit(index, index)
                self.ui.select_user_number.setText(f'{len(self.get_selected_rows())}个')

        return wrapper

    def handle_check_shield_btn_click(self):
        """
        处理检测评论按钮的单击事件
        :return:
        """
        check_note_id = TomlBase.target_note_id

        if not check_note_id:
            QtWidgets.QMessageBox.critical(
                self, '失败',
                '你必须设置一个检测笔记ID。\n点击 设置 > 检测笔记'
            )
            return None

        pattern = r'^[a-z0-9]{24}$'

        if not re.match(pattern, check_note_id):
            QtWidgets.QMessageBox.critical(
                self, '失败',
                f'笔记ID {check_note_id} 不合法，请重新设置。\n点击 设置 > 检测笔记'
            )
            return None

        select_rows = self.get_selected_rows()
        if select_rows:
            # fixed: 修复未选中任意用户时 检测评论限制按钮 持续无法点击的问题
            self.ui.check_comment_btn.setEnabled(False)
            self.ui.check_login_btn.setEnabled(False)

        for row in select_rows:
            user = PrivateUserCenter.find(row)
            index = self.private_user_table_model.index(row, 4)
            zodiac_signs = [
                "白羊座", "金牛座", "双子座", "巨蟹座",
                "狮子座", "处女座", "天秤座", "天蝎座",
                "射手座", "摩羯座", "水瓶座", "双鱼座"
            ]
            comment_text = f'{random.choice(zodiac_signs)}{random.choice(range(7, 24))}岁'
            signals = self.post_comment_thead.start_task(xhs.API().set_cookies(user.string_cookies).comment_post, check_note_id,
                                                         comment_text)
            comment_proxy = CommentProxy(user, index, check_note_id)
            signals.success.connect(self.on_post_comment_success(comment_proxy))

    def on_post_comment_success(self, comment_proxy):
        def wrapper(response: dict):
            self.check_comment_thread.start_task(self.on_check_comment_success, response, comment_proxy)

        return wrapper

    def on_check_comment_success(self, response: dict, comment_schema: CommentProxy):
        try:
            comment_schema.user.comment_state = -1
            if 'code' in response:
                if response['code'] == 0:
                    if response.get('data', {}) and 'comment' in response['data']:
                        comment_schema.comment_id = response['data']['comment']['id']
                    if comment_schema.comment_id:
                        time.sleep(5)
                        check_result = self.recur_check_comment_state(
                            comment_schema.user,
                            comment_schema.note_id,
                            comment_schema.comment_id
                        )

                        comment_schema.user.comment_state = check_result

                        xhs.API().set_cookies(comment_schema.user.string_cookies).comment_delete(
                            comment_schema.note_id,
                            comment_schema.comment_id
                        )
                else:
                    if response['code'] == 10001:
                        comment_schema.user.comment_state = -2
                    elif response['code'] == -10000:
                        comment_schema.user.comment_state = -2
                    elif response['code'] == -100:
                        comment_schema.user.available = 0
        except Exception as e:
            logger.exception(e)
        finally:
            self.private_user_table_model.dataChanged.emit(comment_schema.index, comment_schema.index)
            self.ui.select_user_number.setText(f'{len(self.get_selected_rows())}个')

    def on_all_check_finished(self):
        """
        所有检查均已结束后调用的事件
        :return:
        """
        PrivateUserCenter.save()
        self.ui.check_login_btn.setEnabled(True)
        self.ui.check_comment_btn.setEnabled(True)

    def recur_check_comment_state(self, user: PrivateUser, note_id: str, comment_id: str, cursor: str = ""):
        response = xhs.API().set_cookies(user.string_cookies).show_comments(note_id, cursor)
        if not response['success']:
            return -1

        if 'comments' in response['data']:
            for comment in response['data']['comments']:
                if comment is None:
                    continue
                if comment['id'] == comment_id:
                    if comment['status'] in {0, 2, 4}:
                        return 1
                    return 0
            if not response['data'].get('has_more', False):
                return 0
            cursor = response['data'].get('cursor', '')
            return self.recur_check_comment_state(user, note_id, comment_id, cursor)

    def handle_create_user_click(self):
        """
        显示添加用户的弹窗
        :return:
        """
        add_user_dialog = create_user.CreateUser(parent=self)
        add_user_dialog.created.connect(self.create_after_update_table)
        add_user_dialog.exec()

    def create_after_update_table(self, user: PrivateUser, is_new: bool):
        """
        用户添加后，同步更新表格
        :param user:  PrivateUser 实例
        :param is_new: 是否为新账号
        :return:
        """
        if not isinstance(user, PrivateUser):
            return None

        if is_new:
            self.private_user_table_model.insertRow(self.private_user_table_model.rowCount(), private_user=user)
        else:
            row = PrivateUserCenter.index(user)
            index = self.private_user_table_model.index(row, 0)
            self.private_user_table_model.dataChanged.emit(index, index)

        self.ui.user_number.setText(f'{self.private_user_table_model.rowCount()}个')

    def handle_delete_user_click(self):
        """
        处理删除用户按钮的点击事件
        :return:
        """
        select_rows = self.get_selected_rows()
        if select_rows:
            result = QtWidgets.QMessageBox.question(
                self, '提示', '您确定要删除选中的用户吗？',
                QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
            )
            if result == QtWidgets.QMessageBox.StandardButton.Yes:
                for row in sorted(select_rows, reverse=True):
                    user = PrivateUserCenter.find(row)
                    if not user.working:
                        self.private_user_table_model.removeRow(row)

                self.ui.user_number.setText(f'{self.private_user_table_model.rowCount()}个')
                self.ui.select_user_number.setText(f'{len(self.get_selected_rows())}个')
                PrivateUserCenter.save()
        else:
            QtWidgets.QMessageBox.warning(self, '操作失败', '你需要选择至少1名用户才能进行删除')

    def show_context_menu(self, pos):
        menu = QtWidgets.QMenu(self)
        copy_action = menu.addAction("复制")
        copy_action.triggered.connect(self.copy_selected_cell)
        open_url_action = menu.addAction("访问")
        open_url_action.triggered.connect(self.open_selected_user)
        menu.exec_(self.ui.tableView.mapToGlobal(pos))

    def copy_selected_cell(self):
        index = self.ui.tableView.currentIndex()
        if index.isValid():
            data = index.data(QtCore.Qt.ItemDataRole.DisplayRole)
            clipboard = QtGui.QGuiApplication.clipboard()
            clipboard.setText(str(data))

    def open_selected_user(self):
        if not TomlBase.browser_path:
            QtWidgets.QMessageBox.critical(
                self, '打开失败', '暂未设置浏览器程序的路径！\n点击: 设置 > 设置浏览器'
            )
            return None

        if not pathlib.Path(TomlBase.browser_path).exists():
            QtWidgets.QMessageBox.critical(self, '打开失败', '浏览器程序的路径不存在，请重新设置')
            return None

        if pathlib.Path(TomlBase.browser_path).suffix != '.exe':
            QtWidgets.QMessageBox.critical(self, '打开失败', '设置的路径指向了非可执行程序，请重新设置')
            return None

        index = self.ui.tableView.currentIndex()
        if index.isValid():
            user: PrivateUser = PrivateUserCenter.find(index.row())
            listener_thread = threading.Thread(target=startup_browser, args=(user.dict_cookies,), daemon=True)
            listener_thread.start()

    def handle_user_table_item_click(self, index: QtCore.QModelIndex):
        """
        处理用户管理表的单击事件
        :param index:
        :return:
        """
        if index.column() == 0:
            user = PrivateUserCenter.find(index.row())
            if user and not user.working:
                check_state = self.private_user_table_model.data(index, QtCore.Qt.ItemDataRole.CheckStateRole)
                if isinstance(check_state, QtCore.Qt.CheckState):
                    new_check_state = (
                        QtCore.Qt.CheckState.Unchecked
                        if check_state == QtCore.Qt.CheckState.Checked
                        else QtCore.Qt.CheckState.Checked
                    )
                    self.private_user_table_model.setData(index, new_check_state, QtCore.Qt.ItemDataRole.CheckStateRole)
                    select_number = len(self.get_selected_rows())
                    self.ui.select_user_number.setText(f'{select_number}个')

                    if select_number == self.private_user_table_model.rowCount():
                        self.ui.toggle_select_btn.setText('取消全选')
                        self.select_all = True
                    else:
                        self.ui.toggle_select_btn.setText('全选')
                        self.select_all = False

    def handle_user_table_item_dbclick(self, index: QtCore.QModelIndex):
        """
        处理用户管理表的双击事件
        :param index:
        :return:
        """
        if index.column() != 0:
            user = PrivateUserCenter.find(index.row())
            if isinstance(user, PrivateUser):
                edit_user_dialog = edit_user.EditUser(parent=self, user=user)
                edit_user_dialog.saved.connect(self.edit_after_update_table(index))
                edit_user_dialog.exec()

    def edit_after_update_table(self, index: QtCore.QModelIndex):
        def wrapper(edited_user: PrivateUser):
            if edited_user:
                if edited_user.working:
                    row = index.row()
                    self.private_user_table_model.proxy[index.row()].is_checked = False
                    if row in self.private_user_table_model.checked_rows:
                        self.private_user_table_model.checked_rows.remove(index.row())
                    self.ui.select_user_number.setText(f'{len(self.get_selected_rows())}个')
                self.private_user_table_model.dataChanged.emit(index, index)

        return wrapper

    def on_user_table_entered(self, index):
        if index.isValid() and index.column() == 0:
            data = index.data(QtCore.Qt.ItemDataRole.DisplayRole)
            QtWidgets.QToolTip.showText(
                self.ui.tableView.mapToGlobal(self.ui.tableView.visualRect(index).bottomRight()), str(data))
