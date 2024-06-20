from app.lib import QtCore, QtWidgets, QtGui
from app.lib.core import Config, PrivateUser, List, ConfigCenter, PrivateUserCenter
from app.lib.globals import COLLECT_TYPES, CellStates
from app.ui import create_unit_ui
from app.view import create_user, edit_user, edit_config


class ConfigProxy:
    def __init__(self, config):
        self.config: Config = config
        self.is_checked: bool = False

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.config == other.config
        return False


class ConfigTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data: List[Config]):
        super().__init__()
        self.proxy = [ConfigProxy(c) for c in data]
        self.select_config: Config = None
        self.header = ['配置名称', '采集方式']

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
            config_proxy = self.proxy[row]
            config = config_proxy.config
            if config:
                if col == 0:
                    return config.name
                elif col == 1:
                    return COLLECT_TYPES.get(config.collect_type, '未知')
            return None

        if role == QtCore.Qt.ItemDataRole.TextAlignmentRole:
            return QtCore.Qt.AlignmentFlag.AlignCenter

        if role == QtCore.Qt.ItemDataRole.CheckStateRole and col == 0:
            config_proxy = self.proxy[row]
            return QtCore.Qt.CheckState.Checked if config_proxy.is_checked else QtCore.Qt.CheckState.Unchecked

        return None

    def setData(self, index, value, role=QtCore.Qt.ItemDataRole.EditRole):
        if not index.isValid():
            return False

        row = index.row()
        col = index.column()

        config_proxy = self.proxy[row]

        if role == QtCore.Qt.ItemDataRole.CheckStateRole and col == 0:
            # 如果要设置为选中状态
            if value == QtCore.Qt.CheckState.Checked:
                # 先将所有行设置为未选中状态
                for proxy in self.proxy:
                    proxy.is_checked = False

                # 再将当前行设置为选中状态
                config_proxy.is_checked = True
                self.select_config = config_proxy.config
            # 如果要设置为未选中状态,直接设置为未选中
            else:
                config_proxy.is_checked = False
                self.select_config = None

            self.dataChanged.emit(self.index(0, 0), self.index(self.rowCount() - 1, self.columnCount() - 1))
            return True

        return False

    def flags(self, index):
        if not index.isValid():
            return QtCore.Qt.ItemFlag.NoItemFlags

        flags = QtCore.Qt.ItemFlag.ItemIsEnabled

        return flags

    def headerData(self, section, orientation, role=QtCore.Qt.ItemDataRole.DisplayRole):
        if role == QtCore.Qt.ItemDataRole.TextAlignmentRole and orientation == QtCore.Qt.Orientation.Horizontal:
            return QtCore.Qt.AlignmentFlag.AlignCenter

        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if orientation == QtCore.Qt.Orientation.Horizontal:
                if 0 <= section < len(self.header):
                    return self.header[section]
            elif orientation == QtCore.Qt.Orientation.Vertical:
                return str(section + 1)

        return None

    def insertRow(self, row, parent=QtCore.QModelIndex(), config: Config = None):
        self.beginInsertRows(parent, row, row)
        self.proxy.append(ConfigProxy(config))
        self.endInsertRows()
        return True


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
        self.header = ['昵称', '工作状态', '备注']

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
                    return CellStates.get(CellStates.WORK_STATES, private_user.working).display_name
                elif col == 2:
                    return private_user.remark
            return None

        if role == QtCore.Qt.ItemDataRole.ForegroundRole:
            private_user_proxy = self.proxy[row]
            private_user = private_user_proxy.private_user
            if private_user:
                if col == 1:
                    color_str = CellStates.get(CellStates.WORK_STATES, private_user.working).foreground_color
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


class CreateUnit(QtWidgets.QDialog):
    confirm = QtCore.Signal(Config, list)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowFlag(QtCore.Qt.WindowType.WindowCloseButtonHint)
        self.ui = create_unit_ui.Ui_CreateUnit()
        self.ui.setupUi(self)
        self.build_interface()
        self.connect_ui_events()

    def build_interface(self):
        self.ui.cancel_button.setFocus()

        self.config_table_model = ConfigTableModel(ConfigCenter.data)
        self.ui.config_table.setModel(self.config_table_model)
        self.ui.config_table.setMouseTracking(True)
        self.ui.config_table.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ui.config_table.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.ui.config_table.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ui.config_table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.ui.config_table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)

        self.private_user_table_model = UserTableModel(PrivateUserCenter.data)
        self.ui.user_table.setModel(self.private_user_table_model)
        self.ui.user_table.setMouseTracking(True)
        self.ui.user_table.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ui.user_table.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.ui.user_table.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ui.user_table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.ui.user_table.horizontalHeader().setStretchLastSection(True)

        self.ui.config_number.setText(f'{self.config_table_model.rowCount()} 条')
        self.ui.user_number.setText(f'{self.private_user_table_model.rowCount()} 个')

    def connect_ui_events(self):
        """
        连接 UI 事件
        :return:
        """
        self.ui.cancel_button.clicked.connect(self.close)
        self.ui.confirm_button.clicked.connect(self.handle_confirm_btn_click)
        self.ui.create_config_btn.clicked.connect(self.display_create_config_dialog)
        self.ui.create_user_btn.clicked.connect(self.display_create_user_dialog)
        self.ui.config_table.clicked.connect(self.handle_config_table_item_click)
        self.ui.config_table.doubleClicked.connect(self.handle_config_table_item_dbclick)
        self.ui.user_table.clicked.connect(self.handle_user_table_item_click)
        self.ui.user_table.doubleClicked.connect(self.handle_user_table_item_dbclick)
        self.ui.config_table.entered.connect(self.on_config_table_entered)
        self.ui.user_table.entered.connect(self.on_user_table_entered)
        self.ui.config_table.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.config_table.customContextMenuRequested.connect(self.show_config_context_menu)
        self.ui.user_table.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.user_table.customContextMenuRequested.connect(self.show_user_context_menu)

    def get_selected_config(self):
        """
        获取用户选中的配置
        :return: 未选中调用时返回 None，否则返回正常数据
        """
        return self.config_table_model.select_config

    def get_selected_user_rows(self):
        """
        获取选中用户的行号列表
        :return:
        """
        return self.private_user_table_model.checked_rows

    def handle_confirm_btn_click(self):
        """
        处理确认按钮的点击事件
        :return:
        """
        select_config = self.get_selected_config()
        select_rows = self.get_selected_user_rows()
        if select_config and select_rows:
            if select_config.collect_type in (1, 2) and select_config.is_similarity_filter:
                if not select_config.similarity_keywords:
                    QtWidgets.QMessageBox.critical(
                        self, '操作失败', '选中的配置为在线搜索或者推荐页采集时，相似度过筛必须填写关键词')
                    return None

            select_users = []
            for row in select_rows:
                user = PrivateUserCenter.find(row)
                if user:
                    select_users.append(user)
            self.close()
            self.confirm.emit(select_config, select_users)
        else:
            if not select_rows:
                QtWidgets.QMessageBox.critical(self, '操作失败', '请从右边列表选择至少一个未使用的账号')
            elif not select_config:
                QtWidgets.QMessageBox.critical(self, '操作失败', '请从左边列表选择一个配置')

    def display_create_config_dialog(self):
        """
        显示添加配置表格对话框
        :return:
        """
        create_config_dialog = edit_config.EditConfig(parent=self)
        create_config_dialog.saved.connect(self.create_config_after_update_table)
        create_config_dialog.exec()

    def create_config_after_update_table(self, config: Config):
        """
        添加 Config实例 后调用，主要是更新 config 表格
        :param config: 已添加的 Config 实例
        :return:
        """
        if isinstance(config, Config):
            self.config_table_model.insertRow(self.config_table_model.rowCount(), config=config)
            self.ui.config_number.setText(f'{self.config_table_model.rowCount()} 条')

    def display_create_user_dialog(self):
        """
        显示添加用户对话框
        :return:
        """
        add_user_dialog = create_user.CreateUser(parent=self)
        add_user_dialog.created.connect(self.create_user_after_update_table)
        add_user_dialog.exec()

    def create_user_after_update_table(self, user: PrivateUser, is_new: bool):
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

        self.ui.user_number.setText(f'{self.private_user_table_model.rowCount()} 个')

    def handle_config_table_item_click(self, index: QtCore.QModelIndex):
        """
        处理配置管理表的单击事件
        :param index:
        :return:
        """
        if index.column() == 0:
            check_state = self.config_table_model.data(index, QtCore.Qt.ItemDataRole.CheckStateRole)
            if isinstance(check_state, QtCore.Qt.CheckState):
                self.config_table_model.setData(index, QtCore.Qt.CheckState.Checked,
                                                QtCore.Qt.ItemDataRole.CheckStateRole)

    def handle_config_table_item_dbclick(self, index: QtCore.QModelIndex):
        """
        处理配置管理表的双击事件
        :param index:
        :return:
        """
        if index.column() != 0:
            config = ConfigCenter.find(index.row())
            if isinstance(config, Config):
                edit_config_dialog = edit_config.EditConfig(self, config=config, edit_type='exist')
                edit_config_dialog.saved.connect(self.edit_config_after_update_table(index))
                edit_config_dialog.exec()

    def edit_config_after_update_table(self, index: QtCore.QModelIndex):
        def wrapper(edited_config: Config):
            if edited_config:
                self.config_table_model.dataChanged.emit(index, index)

        return wrapper

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
                edit_user_dialog.saved.connect(self.edit_user_after_update_table(index))
                edit_user_dialog.exec()

    def edit_user_after_update_table(self, index: QtCore.QModelIndex):
        def wrapper(edited_user: PrivateUser):
            if edited_user:
                if edited_user.working:
                    row = index.row()
                    self.private_user_table_model.proxy[index.row()].is_checked = False
                    if row in self.private_user_table_model.checked_rows:
                        self.private_user_table_model.checked_rows.remove(index.row())
                self.private_user_table_model.dataChanged.emit(index, index)

        return wrapper

    def on_config_table_entered(self, index):
        if index.isValid() and index.column() == 0:
            data = index.data(QtCore.Qt.ItemDataRole.DisplayRole)
            QtWidgets.QToolTip.showText(
                self.ui.config_table.mapToGlobal(self.ui.config_table.visualRect(index).bottomRight()),
                str(data))

    def on_user_table_entered(self, index):
        if index.isValid() and index.column() == 0:
            data = index.data(QtCore.Qt.ItemDataRole.DisplayRole)
            QtWidgets.QToolTip.showText(
                self.ui.user_table.mapToGlobal(self.ui.user_table.visualRect(index).bottomRight()),
                str(data))

    def show_config_context_menu(self, pos):
        menu = QtWidgets.QMenu(self)
        copy_action = menu.addAction("复制")
        copy_action.triggered.connect(self.copy_selected_cell(self.ui.config_table))
        menu.exec_(self.ui.config_table.mapToGlobal(pos))

    def show_user_context_menu(self, pos):
        menu = QtWidgets.QMenu(self)
        copy_action = menu.addAction("复制")
        copy_action.triggered.connect(self.copy_selected_cell(self.ui.user_table))
        menu.exec_(self.ui.user_table.mapToGlobal(pos))

    @staticmethod
    def copy_selected_cell(table: QtWidgets.QTableView):
        def wrapper():
            index = table.currentIndex()
            if index.isValid():
                data = index.data(QtCore.Qt.ItemDataRole.DisplayRole)
                clipboard = QtGui.QGuiApplication.clipboard()
                clipboard.setText(str(data))

        return wrapper
