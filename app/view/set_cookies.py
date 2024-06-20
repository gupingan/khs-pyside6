from loguru import logger
from app.lib import QtWidgets, QtCore, QtGui
from app.lib.core import TomlBase, Cookies
from app.lib.globals import base_cookies_keys
from app.ui import set_cookies_ui


class SetCookies(QtWidgets.QDialog):
    exit = QtCore.Signal(bool)

    def __init__(self, is_load: bool, parent=None):
        super().__init__(parent=parent)
        self.ui = set_cookies_ui.Ui_SetCookies()
        self.ui.setupUi(self)
        self.is_load = is_load  # 区分是进入程序时(True) / 已经进入程序中(False)
        self.build_interface()
        self.connect_ui_events()

    def build_interface(self):
        self.cookies = Cookies(TomlBase.cookies)
        self._valid = self.cookies.check_keys(base_cookies_keys)
        self.ui.cookies_edit.setPlainText(self.cookies.to_string())
        logger.debug(f'环境Cookie值：{self.cookies.to_string()}')

    def connect_ui_events(self):
        self.ui.cancel_btn.clicked.connect(self.close)
        self.ui.save_btn.clicked.connect(self.handle_confirm_btn_click)
        self.ui.open_url_btn.clicked.connect(self.handle_open_url_btn_click)

    def handle_confirm_btn_click(self):
        string_cookies = self.ui.cookies_edit.toPlainText()
        self.cookies.from_string(string_cookies)
        cookie_valid = self.cookies.check_keys(base_cookies_keys)

        if cookie_valid:
            logger.debug(f'保存Cookie值：{self.cookies.data}')
            TomlBase.cookies = self.cookies.data
            TomlBase.save()
            self._valid = True
            self.close()
        else:
            QtWidgets.QMessageBox.critical(self, 'Cookies 不合法', self.cookies.logs(str))

    @staticmethod
    def handle_open_url_btn_click():
        url = 'https://www.xiaohongshu.com/'
        q_url = QtCore.QUrl(url)
        QtGui.QDesktopServices.openUrl(q_url)

    def closeEvent(self, event):
        if not self._valid:
            self.exit.emit(self.is_load)
