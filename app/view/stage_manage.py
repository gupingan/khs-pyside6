from app.lib import QtCore, QtWidgets
from app.lib.core import Unit, Tasker
from app.ui import stage_manage_ui, tasker_item_ui
from app.view import edit_config, note_manage


class TaskerListItem(QtWidgets.QWidget):
    def __init__(self, tasker: Tasker, unit: Unit, parent=None):
        super().__init__(parent)
        self.ui = tasker_item_ui.Ui_TaskerItem()
        self.ui.setupUi(self)
        self.tasker = tasker
        self.unit = unit
        self.build_interface()
        self.connect_ui_events()

    def parent(self) -> QtWidgets.QListWidget:
        return super().parent()

    def build_interface(self):
        self.ui.username.setText(self.tasker.user.name)
        self.ui.spinBox.setValue(self.tasker.task_count)
        self.ui.spinBox.setStyleSheet("QSpinBox::hover { }")
        self.ui.slider.setValue(self.tasker.task_count)
        self.ui.show_note_btn.setVisible(True)
        self.ui.allow_btn.setEnabled(self.tasker.is_allow)
        self.ui.spinBox.setEnabled(self.tasker.is_allow)
        self.ui.slider.setEnabled(self.tasker.is_allow)
        self.ui.allow_btn.setText('不执行' if self.tasker.allow_running else '允许执行')
        self.setContentsMargins(4, 4, 4, 4)

    def connect_ui_events(self):
        self.ui.show_note_btn.clicked.connect(self.handle_show_note_click)
        self.ui.allow_btn.clicked.connect(self.handle_allow_btn_click)
        self.ui.edit_config.clicked.connect(self.handle_edit_config_click)
        self.ui.spinBox.valueChanged.connect(self.ui.slider.setValue)
        self.ui.slider.valueChanged.connect(self.ui.spinBox.setValue)
        self.ui.slider.valueChanged.connect(self.tasker.set_task_count)

    def handle_show_note_click(self):
        note_manage_dialog = note_manage.NoteManage(unit=self.unit, tasker=self.tasker, show_type='tasker')
        note_manage_dialog.exec()

    def handle_allow_btn_click(self):
        self.tasker.allow_running = bool(not self.tasker.allow_running)
        self.ui.allow_btn.setText('不执行' if self.tasker.allow_running else '允许执行')

    def handle_edit_config_click(self):
        edit_config_dialog = edit_config.EditConfig(parent=self, config=self.tasker.config, edit_type='copy')
        edit_config_dialog.exec()


class StageManage(QtWidgets.QDialog):
    def __init__(self, unit: Unit, parent=None):
        super().__init__(parent=parent)
        self.ui = stage_manage_ui.Ui_StageManage()
        self.ui.setupUi(self)
        self.unit = unit
        self.build_interface()
        self.connect_ui_events()

    def build_interface(self):
        self.from_unit_paint_view(self.unit.current_stage)

    def connect_ui_events(self):
        self.unit.currentChanged.connect(self.from_unit_paint_view)

    def from_unit_paint_view(self, current_stage: int):
        self.ui.current_stage.setText(f'{current_stage}')
        self.ui.listWidget.clear()

        row = 0
        for tasker in self.unit.tasks:
            row += 1
            item = QtWidgets.QListWidgetItem()
            tasker_widget = TaskerListItem(tasker, self.unit)
            if current_stage == row:
                tasker_widget.ui.stage_label.setText(f'**[正在运行]第{row}阶段**')
            else:
                tasker_widget.ui.stage_label.setText(f'**第{row}阶段**')
            item.setSizeHint(tasker_widget.sizeHint())
            self.ui.listWidget.addItem(item)
            self.ui.listWidget.setItemWidget(item, tasker_widget)

        self.ui.tasker_count.setText(f'{self.ui.listWidget.count()}')
