import traceback
import platform
import os
import ctypes
import subprocess
import sys
from loguru import logger
from app.lib.globals import settings
from app.utils.decorators import deprecated


def _setup_console_for_windows():
    """
    Setup console for Windows platform.
    """
    if "PYCHARM_HOSTED" in os.environ:
        # fixed: 修复 PyCharm 终端无法接收 logger 日志的情况
        return None

    attached = ctypes.windll.kernel32.AttachConsole(-1)
    if attached == 0:
        ctypes.windll.kernel32.AllocConsole()
    try:
        subprocess.run('cmd.exe /c chcp 65001', shell=True)
        sys.stdout = open('CONOUT$', 'wt')
        sys.stderr = open('CONOUT$', 'wt')
    except Exception as e:
        logger.error(f"Failed to setup console for Windows: {e}")


@deprecated("This function is deprecated and will be removed in a future version.")
def _setup_console_for_linux():
    """
    Setup console for Linux platform.
    """
    master, slave = os.openpty()
    try:
        sys.stdout = os.fdopen(slave, 'w')
        sys.stderr = os.fdopen(slave, 'w')
    except Exception as e:
        logger.error(f"Failed to setup console for Linux: {e}")
    finally:
        if master is not None:
            os.close(master)


def setup_console_based_on_system():
    """
    Setup console based on the current operating system.
    """
    system = platform.system()
    if system == 'Windows':
        _setup_console_for_windows()
    else:
        logger.warning(f"Unsupported system for console setup: {system}")


def shorten_message(record):
    max_length = 1000
    message = record["message"]
    if len(message) > max_length:
        record["message"] = message[:max_length] + "..."
    return True


def register_logger(logs_folder):
    logger.remove()

    logger.add(
        f"{str(logs_folder)}/khs-pyqt.log",
        rotation="1 days",
        retention='2 weeks',
        level="INFO",
        compression='zip',
        encoding='utf-8'
    )
    if settings.value('debug') is None:
        settings.setValue('debug', 0)

    if settings.value('debug'):
        setup_console_based_on_system()
        if sys.stdout and sys.stderr:
            logger.add(sys.stdout, level='DEBUG', filter=lambda record: shorten_message(record))

    def handle_exception(exc_type, exc_value, exc_traceback):
        formatted_exception = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
        logger.error(f'Uncaught exception:\n{formatted_exception}')

    sys.excepthook = handle_exception
