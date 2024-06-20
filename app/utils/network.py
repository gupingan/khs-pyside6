"""
该模块提供了一个用于管理和执行后台网络任务的线程池。

用例：
    pool = NetworkPool()
    pool.set_max_thread(4)  # 设置最大线程数为4

    # 启动一个任务
    signals = pool.start_task(your_function, arg1, arg2, timeout=5, max_retries=5)
    signals.success.connect(lambda response: print(f'Task succeeded: {response}'))
    signals.failure.connect(lambda error: print(f'Task failed: {error}'))

    # 连接 allTasksDone 信号
    pool.allTasksDone.connect(lambda: print('All tasks done!'))
"""
import time
from requests import exceptions
from PySide6 import QtCore
from app.utils.logger import logger

exceptions = exceptions


class WorkerSignals(QtCore.QObject):
    success = QtCore.Signal(dict)
    failure = QtCore.Signal(Exception)
    finished = QtCore.Signal()


class Worker(QtCore.QRunnable):
    def __init__(self, function, *args, timeout=10, max_retries=3, retry_interval=1, **kwargs):
        super().__init__()
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        self.timeout = timeout
        self.max_retries = max_retries
        self.retry_interval = retry_interval
        self.retries = 0

    @QtCore.Slot()
    def run(self):
        try:
            while self.retries < self.max_retries:
                try:
                    response = self.function(*self.args, **self.kwargs)
                    logger.debug(f'线程池请求：{self.function.__name__} - {response}')
                    self.signals.success.emit(response)
                    break
                except ConnectionError:
                    self.retries += 1
                    time.sleep(self.retry_interval)
            else:
                raise ConnectionError('Maximum retry attempts reached')
        except Exception as e:
            logger.exception(e)
            self.signals.failure.emit(e)
        finally:
            self.signals.finished.emit()


class NetworkPool(QtCore.QObject):
    allTasksDone = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.threadPool = QtCore.QThreadPool()
        self.activeTasks = 0
        self.mutex = QtCore.QMutex()

    def set_max_thread(self, count: int = 4):
        self.threadPool.setMaxThreadCount(count)

    def start_task(self, function, *args, **kwargs):
        worker = Worker(function, *args, **kwargs)
        worker.signals.finished.connect(self.on_task_finished)
        self.mutex.lock()
        self.activeTasks += 1
        self.mutex.unlock()
        self.threadPool.start(worker)
        return worker.signals

    def on_task_finished(self):
        self.mutex.lock()
        self.activeTasks -= 1
        if self.activeTasks == 0:
            self.allTasksDone.emit()
        self.mutex.unlock()
