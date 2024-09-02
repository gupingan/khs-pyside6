import xhs
from loguru import logger
from app.lib import QtCore, QtWidgets, QtGui
from app.lib.factory import PrivateUser, LoginQrCode, PrivateUserCenter, PrivateUserFactory
from app.ui import create_user_ui
from app.utils.network import NetworkPool


class CreateUser(QtWidgets.QDialog):
    created = QtCore.Signal(PrivateUser, bool)  # 用户、是否为新用户

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowFlag(QtCore.Qt.WindowType.WindowCloseButtonHint)
        self.ui = create_user_ui.Ui_CreateUser()
        self.ui.setupUi(self)
        self.build_init_datas()
        self.connect_ui_events()
        self.service_deployment()

    def build_init_datas(self):
        """
        构建初始的数据 控件参数
        :return:
        """
        self.factory = PrivateUserFactory()
        self.ui.edit_remark.setFocus()
        self.reset_relative_parameters()

    def connect_ui_events(self):
        """
        连接各个控件的槽函数与信号
        :return:
        """
        self.ui.refresh_qrcode_btn.clicked.connect(self.handle_refresh_qrcode_click)
        self.ui.confirm_button.clicked.connect(self.handle_confirm_btn_click)
        self.ui.check_button.clicked.connect(self.handle_check_btn_click)

    def service_deployment(self):
        self.network_pool = NetworkPool(parent=self)

    def reset_relative_parameters(self):
        self.factory.retrieve_qrcode_params()
        self.login_qrcode: LoginQrCode = None
        self.login_user: PrivateUser = None
        self.ui.check_button.setEnabled(True)
        self.ui.label_nickname.setText('')
        self.ui.label_user_id.setText('')
        self.ui.edit_remark.setText('')

    def handle_refresh_qrcode_click(self):
        self.reset_relative_parameters()
        self.ui.refresh_qrcode_btn.setEnabled(False)
        create_qrcode_signals = self.network_pool.start_task(xhs.API().set_cookies(self.factory.make_cookies()).create_qrcode)
        create_qrcode_signals.success.connect(self.on_create_qrcode_success)
        create_qrcode_signals.finished.connect(lambda: self.ui.refresh_qrcode_btn.setEnabled(True))

    def on_create_qrcode_success(self, response: dict):
        try:
            url = response['data'].get('url') if response.get('data') else ''
            qr_id = response['data'].get('qr_id') if response.get('data') else ''
            code = response['data'].get('code') if response.get('data') else ''
            self.factory.import_qrcode_params(url, qr_id, code)
            self.login_qrcode = self.factory.make_qrcode()
            qr_img = QtGui.QImage()
            qr_img.loadFromData(self.login_qrcode.bytes, 'PNG')
            self.ui.label_qrcode.setPixmap(QtGui.QPixmap.fromImage(qr_img))
        except Exception as e:
            logger.error(f'Create qrcode: {response}')
            logger.exception(e)
            QtWidgets.QMessageBox.critical(self, '刷新失败', '获取二维码失败，请查看日志')

    def handle_check_btn_click(self):
        """
        处理`先检测`按钮的单击事件
        功能：根据 qr_id 与 code 去实现
        :return:
        """
        if self.login_qrcode:
            self.ui.check_button.setEnabled(False)
            check_qrcode_signals = self.network_pool.start_task(
                xhs.API().set_cookies(self.factory.make_cookies()).qrcode_status,
                self.login_qrcode.qr_id, self.login_qrcode.code
            )
            check_qrcode_signals.success.connect(self.on_check_qrcode_success)
            check_qrcode_signals.finished.connect(lambda: self.ui.check_button.setEnabled(True))
        else:
            QtWidgets.QMessageBox.critical(self, '检测失败', '当前二维码的相关数据未获取到，请稍后重试')

    def on_check_qrcode_success(self, response: dict):
        try:
            code_status = response['data'].get('code_status', -1) if response['data'] else -1
            if code_status == -1:
                QtWidgets.QMessageBox.critical(self, '登录失败', '当前二维码的登录状态暂未获取到')
            elif code_status == 0:
                QtWidgets.QMessageBox.warning(self, '登录失败', '请使用小红书或者微信扫码')
            elif code_status == 1:
                QtWidgets.QMessageBox.warning(self, '登录失败', '请务必在手机上确认登录')
            elif code_status == 2:
                session = response['data']['login_info']['session']
                cookies = self.factory.make_cookies(session)
                user_id = response['data']['login_info']['user_id']
                self.ui.label_user_id.setText(user_id)
                get_user_info = xhs.API().set_cookies(cookies).user_me()
                logger.debug(f'获取账号个人信息：{get_user_info}')
                if get_user_info.get('data'):
                    nickname = get_user_info['data'].get('nickname', '获取昵称失败')
                else:
                    nickname = '获取昵称失败'
                self.ui.label_nickname.setText(nickname)
                self.login_user = self.factory.make_user(user_id, nickname, session, '')
            elif code_status == 3:
                QtWidgets.QMessageBox.critical(self, '登录失败', '当前二维码已过期，请刷新二维码')
        except Exception as e:
            logger.exception(e)
            QtWidgets.QMessageBox.critical(self, '检测失败', '未知原因导致检测失败，请查看日志')

    def handle_confirm_btn_click(self):
        """
        处理`后添加`按钮的单击事件
        功能：添加用户到列表中
        :return:
        """
        if self.login_user and self.login_user.session:
            # fixed: 修复创建账号时备注无法得到正确修改的问题
            self.login_user.remark = self.ui.edit_remark.toPlainText()

            if self.login_user in PrivateUserCenter.data:
                self.created.emit(self.login_user, False)
            else:
                self.created.emit(self.login_user, True)
                PrivateUserCenter.append(self.login_user)

            PrivateUserCenter.save()

            result = QtWidgets.QMessageBox.critical(
                self, '添加成功', f'红薯账号{self.login_user.name}已添加。\n继续添加还是退出？',
                QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.Cancel
            )
            if result == QtWidgets.QMessageBox.StandardButton.Yes:
                self.handle_refresh_qrcode_click()
            else:
                self.close()
        else:
            QtWidgets.QMessageBox.critical(self, '添加失败', '暂未检测到用户已登录')

    def closeEvent(self, event):
        if hasattr(self, 'check_qrcode_timer') and isinstance(self.check_qrcode_timer, QtCore.QTimer):
            self.check_qrcode_timer.stop()
        if hasattr(self, 'get_info_timer') and isinstance(self.get_info_timer, QtCore.QTimer):
            self.get_info_timer.stop()
        if hasattr(self, 'check_qrcode_timer') and isinstance(self.check_qrcode_timer, QtCore.QTimer):
            self.check_qrcode_timer.stop()
