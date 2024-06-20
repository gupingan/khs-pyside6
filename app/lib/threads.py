import zipfile
from pathlib import Path
from loguru import logger
from app.lib import QtCore
from app.lib.core import Unit
from app.lib.core import AtUserCenter, PrivateUserCenter, ConfigCenter, BaseCenter, TomlBase


class PreloadThread(QtCore.QThread):
    sendMessage = QtCore.Signal(str)
    sendProgress = QtCore.Signal(int)
    close = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.running = False
        self.works = {
            BaseCenter.check_valid: (0.2, '校验配置中'),
            TomlBase.load: (0.2, '读取基本配置'),
            AtUserCenter.load: (0.2, '读取艾特用户列表'),
            PrivateUserCenter.load: (0.2, '读取用户列表'),
            ConfigCenter.load: (0.2, '读取配置列表'),
        }
        self.total_score = 0

    def run(self):
        try:
            for callback, info in self.works.items():
                score = info[0]
                msg = info[1]
                if self.total_score >= 100:
                    break
                self.sendMessage.emit(f"{msg}...")
                callback()
                self.total_score += int(100 * score)
                self.sendProgress.emit(self.total_score)
                self.msleep(100)
                logger.debug(f'预加载：{msg} (完成{self.total_score}%)')
            self.finished.emit()
        except Exception as e:
            logger.exception(e)
            self.close.emit()

    def stop(self):
        self.running = False
        self.wait()


class UpdateInfoThread(QtCore.QThread):
    send = QtCore.Signal(Unit)

    def __init__(self, unit: Unit = None, parent=None):
        super().__init__(parent=parent)
        self.running = False
        self.unit = unit

    def set_unit(self, unit: Unit):
        self.unit = unit

    def run(self):
        self.running = True
        while True:
            if self.unit:
                self.send.emit(self.unit)

            if not self.running:
                break

            self.sleep(1)

    def stop(self):
        self.running = False
        self.wait()


class SaveAllLogsThread(QtCore.QThread):
    success = QtCore.Signal()
    finish = QtCore.Signal()
    error = QtCore.Signal(str)

    def __init__(self, tab_browser, parent=None):
        super().__init__(parent)
        self.tab_browser = tab_browser

    def run(self):
        tab_browser = self.tab_browser
        desktop_path = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.StandardLocation.DesktopLocation)
        zip_path = Path(desktop_path) / 'all_unit_logs.zip'

        try:
            with zipfile.ZipFile(zip_path, 'w') as zip_file:
                for i in range(tab_browser.count()):
                    widget = tab_browser.widget(i)
                    unit = widget.unit
                    if isinstance(unit, Unit):
                        logs = widget.pain_logs
                        log_file_path = f'{unit.id}.log'
                        zip_file.writestr(log_file_path, '\n'.join(logs))
            self.success.emit()
        except Exception as e:
            self.error.emit(str(e))

        self.finish.emit()

    def stop(self):
        self.quit()
        self.wait()
