from app.lib import QtCore, QtWidgets, QtGui
from app.lib.core import Config, ConfigCenter, List
from app.lib.globals import COLLECT_TYPES
from app.ui import config_manage_ui
from app.view import edit_config


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
        self.checked_rows = []
        self.header = ['配置名称', '采集方式', '是否评论']

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
                elif col == 2:
                    return '是' if config.is_comment else '否'
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

    def removeRow(self, row, parent=QtCore.QModelIndex()):
        self.beginRemoveRows(parent, row, row)
        ConfigCenter.pop(row)
        self.proxy.pop(row)
        self.checked_rows.clear()
        self.endRemoveRows()
        return True


class ConfigManage(QtWidgets.QDialog):
    select_all = False

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowFlag(QtCore.Qt.WindowType.WindowCloseButtonHint)
        self.ui = config_manage_ui.Ui_ConfigManage()
        self.ui.setupUi(self)
        self.build_interface()
        self.connect_ui_events()

    def build_interface(self):
        self.config_table_model = ConfigTableModel(ConfigCenter.data)
        self.ui.tableView.setModel(self.config_table_model)
        self.ui.tableView.setMouseTracking(True)
        self.ui.tableView.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ui.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.ui.tableView.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ui.tableView.horizontalHeader().setStretchLastSection(True)
        header = self.ui.tableView.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.ui.toggle_select_btn.setText('取消全选' if self.select_all else '全选')
        self.ui.config_number.setText(f'{self.config_table_model.rowCount()}个')

    def connect_ui_events(self):
        self.ui.toggle_select_btn.clicked.connect(self.handle_toggle_select_click)
        self.ui.add_config_btn.clicked.connect(self.handle_create_config_click)
        self.ui.del_config_btn.clicked.connect(self.handle_delete_config_click)
        self.ui.tableView.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.tableView.customContextMenuRequested.connect(self.show_context_menu)
        self.ui.tableView.clicked.connect(self.handle_config_table_item_click)
        self.ui.tableView.doubleClicked.connect(self.handle_config_table_item_dbclick)
        self.ui.tableView.entered.connect(self.on_config_table_entered)

    def get_selected_rows(self):
        """
        获取选中项目的行号
        :return:
        """
        return self.config_table_model.checked_rows

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
        count = self.config_table_model.rowCount()
        display_select_count = count if self.select_all else 0
        for row in range(count):
            index = self.config_table_model.index(row, 0)
            self.config_table_model.setData(index, check_state, QtCore.Qt.ItemDataRole.CheckStateRole)
            self.ui.select_config_number.setText(f'{display_select_count}个')

    def handle_create_config_click(self):
        """
        处理创建配置按钮的点击事件
        :return:
        """
        edit_config_dialog = edit_config.EditConfig(self)
        edit_config_dialog.saved.connect(self.create_after_update_table)
        edit_config_dialog.exec()

    def create_after_update_table(self, config):
        """
        创建配置后更新表格
        :param config:
        :return:
        """
        if isinstance(config, Config):
            self.config_table_model.insertRow(self.config_table_model.rowCount(), config=config)
            self.ui.config_number.setText(f'{self.config_table_model.rowCount()}个')

    def handle_delete_config_click(self):
        """
        处理删除配置按钮的点击事件
        :return:
        """
        selected_rows = self.get_selected_rows()
        if selected_rows:
            result = QtWidgets.QMessageBox.question(
                self, '提示', '您确定要删除选中的配置吗?',
                QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
            )
            if result == QtWidgets.QMessageBox.StandardButton.Yes:
                for row in sorted(selected_rows, reverse=True):
                    self.config_table_model.removeRow(row)

                self.ui.config_number.setText(f'{self.config_table_model.rowCount()}个')
                self.ui.select_config_number.setText(f'{len(self.get_selected_rows())}个')
                ConfigCenter.save()
        else:
            QtWidgets.QMessageBox.warning(
                self, '操作失败', '你需要选择至少1个配置才能进行删除',
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

    def handle_config_table_item_click(self, index: QtCore.QModelIndex):
        """
        处理配置管理表的单击事件
        :param index:
        :return:
        """
        if index.column() == 0:
            check_state = self.config_table_model.data(index, QtCore.Qt.ItemDataRole.CheckStateRole)
            if isinstance(check_state, QtCore.Qt.CheckState):
                new_check_state = (
                    QtCore.Qt.CheckState.Unchecked
                    if check_state == QtCore.Qt.CheckState.Checked
                    else QtCore.Qt.CheckState.Checked
                )
                self.config_table_model.setData(index, new_check_state, QtCore.Qt.ItemDataRole.CheckStateRole)

                select_number = len(self.get_selected_rows())
                self.ui.select_config_number.setText(f'{select_number}个')

                if select_number == self.config_table_model.rowCount():
                    self.ui.toggle_select_btn.setText('取消全选')
                    self.select_all = True
                else:
                    self.ui.toggle_select_btn.setText('全选')
                    self.select_all = False

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
                edit_config_dialog.saved.connect(self.edit_after_update_table(index))
                edit_config_dialog.exec()

    def edit_after_update_table(self, index: QtCore.QModelIndex):
        def wrapper(edited_config: Config):
            if edited_config:
                self.config_table_model.dataChanged.emit(index, index)

        return wrapper

    def on_config_table_entered(self, index):
        if index.isValid() and index.column() == 0:
            data = index.data(QtCore.Qt.ItemDataRole.DisplayRole)
            QtWidgets.QToolTip.showText(
                self.ui.tableView.mapToGlobal(self.ui.tableView.visualRect(index).bottomRight()),
                str(data))
