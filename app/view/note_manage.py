from app.lib import QtCore, QtWidgets, QtGui
from app.lib.core import NormalNote, Unit, Tasker, List
from app.ui import note_manage_ui


class NoteProxy:
    def __init__(self, note):
        self.note: NormalNote = note
        self.is_checked: bool = False

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.note == other.note
        return False


class NoteModel(QtCore.QAbstractTableModel):
    NoteDataRole = QtCore.Qt.ItemDataRole.UserRole + 1

    def __init__(self, data: List[NormalNote], unit: Unit):
        super().__init__()
        self.proxy = [NoteProxy(n) for n in data]
        self.unit = unit
        self.checked_rows = []
        self.header = ["标题", "类型", "笔记ID", "创作者", "创作者ID", "状态"]

    def rowCount(self, parent=None):
        return len(self.proxy)

    def columnCount(self, parent=None):
        return len(self.header)

    def data(self, index, role=QtCore.Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None

        row = index.row()
        col = index.column()

        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            note_proxy = self.proxy[row]
            note = note_proxy.note
            if note:
                if col == 0:
                    return note.note_title
                elif col == 1:
                    return note.note_type
                elif col == 2:
                    return note.id
                elif col == 3:
                    return note.author.name
                elif col == 4:
                    return note.author.id
                elif col == 5:
                    if note in self.unit.hash_success_notes:
                        return '已评论'
                    if note in self.unit.hash_failure_notes:
                        return '评论失败'
                    if note in self.unit.hash_uncomment_notes:
                        return '不评论'
                    return '未处理'
            return None

        if role == QtCore.Qt.ItemDataRole.ForegroundRole:
            note = self.proxy[row].note
            if note and col == len(self.header) - 1:
                if note in self.unit.hash_success_notes:
                    color_str = 'green'
                elif note in self.unit.hash_failure_notes:
                    color_str = 'red'
                elif note in self.unit.hash_uncomment_notes:
                    color_str = 'blue'
                else:
                    color_str = 'black'
                return QtGui.QBrush(QtGui.QColor(color_str))

            return None

        if role == QtCore.Qt.ItemDataRole.TextAlignmentRole:
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

        note_proxy = self.proxy[row]

        if role == QtCore.Qt.ItemDataRole.CheckStateRole and col == 0:
            if value == QtCore.Qt.CheckState.Checked:
                if row not in self.checked_rows:
                    self.checked_rows.append(row)
            else:
                if row in self.checked_rows:
                    self.checked_rows.remove(row)
            note_proxy.is_checked = (value == QtCore.Qt.CheckState.Checked)
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


class NoteManage(QtWidgets.QDialog):
    def __init__(self, parent=None, unit: Unit = None, tasker: Tasker = None, show_type: str = 'unit'):
        super().__init__(parent=parent)
        self.setWindowFlag(QtCore.Qt.WindowType.WindowCloseButtonHint)
        self.ui = note_manage_ui.Ui_NoteManage()
        self.ui.setupUi(self)
        self.unit = unit
        self.tasker = tasker
        self.show_type = show_type
        self.build_interface()
        self.connect_ui_events()

    def build_interface(self):
        if self.show_type == 'tasker':
            self.note_model = NoteModel(self.tasker.work_notes, self.unit)
        else:
            self.note_model = NoteModel(self.unit.notes, self.unit)

        self.ui.table_notes.setModel(self.note_model)
        self.ui.table_notes.setMouseTracking(True)
        self.ui.table_notes.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)

        self.ui.table_notes.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.ui.table_notes.horizontalHeader().setSectionResizeMode(1,
                                                                    QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.ui.table_notes.horizontalHeader().setSectionResizeMode(2,
                                                                    QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.ui.table_notes.horizontalHeader().setSectionResizeMode(4,
                                                                    QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.ui.table_notes.horizontalHeader().setSectionResizeMode(5,
                                                                    QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

        self.ui.table_notes.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.NoSelection)
        self.ui.table_notes.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)

        self.ui.note_number.setText(f'{self.note_model.rowCount()} 条')
        self.ui.refresh_btn.setFocus()

    def connect_ui_events(self):
        """
        连接各个UI控件的信号与槽函数
        :return:
        """
        self.ui.refresh_btn.clicked.connect(self.handle_refresh_btn_click)
        self.ui.table_notes.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.table_notes.customContextMenuRequested.connect(self.show_context_menu)
        self.ui.table_notes.clicked.connect(self.handle_note_table_click)
        self.ui.table_notes.entered.connect(self.on_note_table_entered)

    def handle_refresh_btn_click(self):
        """
        处理用户点击刷新按钮的事件
        :return:
        """
        self.note_model.beginResetModel()
        self.note_model.endResetModel()

    def show_context_menu(self, pos):
        menu = QtWidgets.QMenu(self)
        copy_action = menu.addAction("复制")
        copy_action.triggered.connect(self.copy_selected_cell)
        menu.exec_(self.ui.table_notes.mapToGlobal(pos))

    def copy_selected_cell(self):
        index = self.ui.table_notes.currentIndex()
        if index.isValid():
            data = index.data(QtCore.Qt.ItemDataRole.DisplayRole)
            clipboard = QtGui.QGuiApplication.clipboard()
            clipboard.setText(str(data))


    def handle_note_table_click(self, index: QtCore.QModelIndex):
        """
        处理 Note Table Cell 的单击事件
        功能：笔记选择 - 勾选框的点击
        :param index: 被点击项的模型索引
        :return:
        """
        if index.column() != 0:
            index = self.note_model.index(index.row(), 0)
        check_state = self.note_model.data(index, QtCore.Qt.ItemDataRole.CheckStateRole)
        if isinstance(check_state, QtCore.Qt.CheckState):
            new_check_state = (
                QtCore.Qt.CheckState.Unchecked
                if check_state == QtCore.Qt.CheckState.Checked
                else QtCore.Qt.CheckState.Checked
            )
            self.note_model.setData(index, new_check_state, QtCore.Qt.ItemDataRole.CheckStateRole)

    def on_note_table_entered(self, index):
        if index.isValid() and index.column() == 0:
            data = index.data(QtCore.Qt.ItemDataRole.DisplayRole)
            QtWidgets.QToolTip.showText(self.ui.table_notes.mapToGlobal(self.ui.table_notes.visualRect(index).bottomRight()),
                                        str(data))
