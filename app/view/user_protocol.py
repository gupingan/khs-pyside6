from app.lib import QtCore, QtWidgets
from app.lib.globals import app_name, settings, Path
from app.utils.string import validate_chinese_name
from app.utils.time import get_current_date
from app.ui import user_protocol_ui


class UserProtocol(QtWidgets.QDialog):
    exit = QtCore.Signal(bool)

    def __init__(self, is_load: bool, parent=None):
        super().__init__(parent=parent)
        self.setWindowFlag(QtCore.Qt.WindowType.WindowCloseButtonHint)
        self.ui = user_protocol_ui.Ui_UserProtocol()
        self.ui.setupUi(self)
        self.is_load = is_load  # 区分是进入程序时(True) / 已经进入程序中(False)
        self.build_interface()
        self.connect_ui_events()

    def build_interface(self):
        name = settings.value('accept-name', '')
        date = settings.value('accept-date')
        if not date:  # fixed: 修复某些情况下签署日期不显示的问题
            settings.setValue('accept-date', get_current_date().strftime('%Y-%m-%d'))
            date = settings.value('accept-date')
        self.ui.name_edit.setText(name)
        self.ui.name_edit.setEnabled(self.is_load)
        self.ui.label_date.setText(date)
        self.ui.label_date.setEnabled(self.is_load)
        protocol_content = self.ui.label.text()
        self.ui.label.setText(protocol_content.format(appName=app_name))

    def connect_ui_events(self):
        self.ui.confirm_btn.clicked.connect(self.accept_protocol)
        self.ui.cancel_btn.clicked.connect(self.reject_protocol)
        self.ui.download_btn.clicked.connect(self.handle_download_btn_click)

    def handle_download_btn_click(self):
        desktop_dir = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.StandardLocation.DesktopLocation)
        real_file, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, '保存用户协议',
            str(Path(desktop_dir) / f'{app_name}-用户协议v1-{get_current_date().strftime("%Y%m%d")}'),
            'Markdown (*.md)'
        )
        if real_file:
            with open(real_file, 'w', encoding='utf-8') as fr:
                fr.write(str(self.ui.label.text()))

    def accept_protocol(self):
        name = self.ui.name_edit.text()
        if name:
            if validate_chinese_name(name):
                settings.setValue('accept-protocol', 1)
                settings.setValue('accept-name', name)
                settings.setValue('accept-date', self.ui.label_date.text())
                self.close()
            else:
                QtWidgets.QMessageBox.critical(self, '失败', '签署的名字不合法，请重新签署')
                self.ui.name_edit.clear()
        else:
            QtWidgets.QMessageBox.critical(self, '失败', '同意协议时，需要您签署您的名字')

    def reject_protocol(self):
        settings.setValue('accept-protocol', 0)
        settings.setValue('accept-name', '')
        settings.setValue('accept-date', '')
        self.close()

    def closeEvent(self, event):
        if settings.value('accept-protocol', 0) == 0:
            self.exit.emit(self.is_load)
        else:
            event.accept()
