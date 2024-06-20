import sys
from app.lib import QtWidgets, QtCore, QtGui
from app.lib.globals import LOCK_FILE, ICONS_DIR, LOGS_DIR, NODE_DIR, GlobalStyle, app_name_en
from app.lib.nodejs import NodeJS
from app.utils.logger import logger, register_logger
from app.view.main_window import MainWindow

QtCore.QCoreApplication.setAttribute(QtCore.Qt.ApplicationAttribute.AA_EnableHighDpiScaling)


class QSingleApplication(QtWidgets.QApplication):

    def __init__(self, app_name: str = 'my_app', app_icon=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app_name = app_name
        self.app_icon = app_icon
        if app_icon:
            self.setWindowIcon(QtGui.QPixmap(app_icon))

        self.shared_memory = QtCore.QSharedMemory(app_name)

    def __enter__(self):
        if not self.shared_memory.attach():
            self.shared_memory.create(1)
        else:
            QtWidgets.QMessageBox.information(None, '提示', '应用已在已运行')
            sys.exit(1)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def app_exit(app=None, errors=None, exit_code=0, clear_lock=True):
    """
    退出程序，确保资源得到释放，并提供错误信息。
    :param app: QApp 应用实例
    :param errors: 应用异常终止所接受的异常示例，提供给 logger记录
    :param exit_code: 退出代码，正常情况下为 0
    :param clear_lock: 是否要清除应用单例锁
    :return:
    """
    if errors:
        logger.exception(errors)
    if app:
        app.closeAllWindows()
    if app and clear_lock:
        app.close_lock()
    sys.exit(exit_code)


def show_message_box(title: str, text: str, icon=QtWidgets.QMessageBox.Icon.Warning):
    msg_box = QtWidgets.QMessageBox()
    msg_box.setIcon(icon)
    msg_box.setWindowTitle(title)
    msg_box.setText(text)
    msg_box.exec()


def run_app():
    try:
        register_logger(LOGS_DIR)
        NodeJS().setup(NODE_DIR)
    except PermissionError:
        show_message_box(
            '权限错误',
            "解决方式任选其一："
            "\n1.请以管理员身份运行程序；"
            "\n2.请将软件安装在有权限的目录。"
        )
        app_exit()
    except OSError:
        show_message_box(
            '不支持该系统',
            "非常抱歉，当前我们仅对 Windows 64 位系统进行支持\n"
            "您可以安装Virtual box 或者 VM 等虚拟软件后使用。"
        )
        app_exit()
    except Exception as e:
        app_exit(errors=e)

    with QSingleApplication(app_name_en, ICONS_DIR / 'app-x48.ico', sys.argv) as app:
        app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        main_window = MainWindow()
        main_window.show()
        sys.exit(app.exec())
