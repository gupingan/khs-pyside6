from app.lib import QtCore, QtWidgets
from app.lib.core import Unit, Config, List, PrivateUser, Tasker
from app.lib.factory import UnitFactory
from app.ui import unit_configer_ui, tasker_item_ui
from app.view import edit_config, log_view


class TaskerListItem(QtWidgets.QWidget):
    def __init__(self, tasker: Tasker, parent=None):
        super().__init__(parent)
        self.tasker = tasker
        self.ui = tasker_item_ui.Ui_TaskerItem()
        self.ui.setupUi(self)
        self.build_interface()
        self.connect_ui_events()

    def parent(self) -> QtWidgets.QListWidget:
        return super().parent()

    def build_interface(self):
        self.ui.username.setText(self.tasker.user.name)
        self.ui.spinBox.setValue(self.tasker.task_count)
        self.ui.spinBox.setStyleSheet("QSpinBox::hover { }")
        self.ui.slider.setValue(self.tasker.task_count)
        self.setContentsMargins(4, 4, 4, 4)
        self.ui.show_note_btn.setVisible(False)
        self.ui.allow_btn.setVisible(False)
        self.ui.allow_btn.setEnabled(self.tasker.is_allow)

    def connect_ui_events(self):
        self.ui.edit_config.clicked.connect(self.handle_edit_config_click)
        self.ui.spinBox.valueChanged.connect(self.ui.slider.setValue)
        self.ui.slider.valueChanged.connect(self.ui.spinBox.setValue)
        self.ui.slider.valueChanged.connect(self.tasker.set_task_count)

    def handle_edit_config_click(self):
        edit_config_dialog = edit_config.EditConfig(parent=self, config=self.tasker.config, edit_type='copy')
        edit_config_dialog.exec()

    def update_ui_elements(self, value: int):
        self.ui.spinBox.setValue(value)
        self.ui.slider.setValue(value)
        self.tasker.set_task_count(value)


class UnitConfiger(QtWidgets.QDialog):
    created = QtCore.Signal(Unit)
    sentValue = QtCore.Signal(int)

    def __init__(self, parent=None, root_config: Config = None, select_users: List[PrivateUser] = None):
        super().__init__(parent=parent)
        self.ui = unit_configer_ui.Ui_UnitConfiger()
        self.ui.setupUi(self)
        self.root_config = root_config
        self.select_users = select_users
        self.factory = UnitFactory()
        self.build_taskers()
        self.build_interface()
        self.connect_ui_events()

    def build_taskers(self):
        if not (self.root_config and self.select_users):
            return None

        for user in self.select_users:
            self.factory.make_tasker(user, self.root_config, 0)

    def build_interface(self):
        row = 0
        for tasker in self.factory.tasks:
            row += 1
            item = QtWidgets.QListWidgetItem()
            tasker_widget = TaskerListItem(tasker)
            tasker_widget.ui.stage_label.setText(f'**第{row}阶段**')
            self.sentValue.connect(tasker_widget.update_ui_elements)
            item.setSizeHint(tasker_widget.sizeHint())
            self.ui.listWidget.addItem(item)
            self.ui.listWidget.setItemWidget(item, tasker_widget)

        self.ui.tasker_count.setText(f'{self.ui.listWidget.count()}')

    def connect_ui_events(self):
        self.ui.distribute_toolbtn.clicked.connect(self.handle_distribute_btn_click)
        self.ui.create_btn.clicked.connect(self.handle_create_btn_click)
        self.ui.cancel_btn.clicked.connect(self.handle_cancel_btn_click)

    def handle_distribute_btn_click(self):
        value = self.ui.distribute_count_sb.value()
        self.sentValue.emit(value)

    def handle_create_btn_click(self):
        log_view_widget = self.factory.make_logger(log_view.LogView)
        unit = self.factory.make_unit(self.root_config, log_view_widget)
        self.created.emit(unit)
        self.close()

    def handle_cancel_btn_click(self):
        self.close()

    def closeEvent(self, event):
        self.factory.restore_factory()
