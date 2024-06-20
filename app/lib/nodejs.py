import os
import platform
import xhsAPI
from abc import ABC, abstractmethod
from pathlib import Path
from loguru import logger


class NodeJSStrategyABC(ABC):
    """设置 Node.js 环境变量的策略接口"""

    @abstractmethod
    def setup(self, folder: Path):
        """设置 Node.js 环境变量"""
        pass


class WindowsX64Strategy(NodeJSStrategyABC):
    """Windows 64位系统的策略"""

    def setup(self, folder: Path):
        node_folder = self._get_node_folder(folder)
        if node_folder is not None:
            abs_folder = node_folder.resolve()
            path_str = os.environ['Path'] + os.pathsep + str(abs_folder)
            existing_paths = os.environ['Path'].split(os.pathsep)
            if str(abs_folder) not in existing_paths:
                os.environ['Path'] = path_str
                if xhsAPI.unregister(xhsAPI.runtime_names.Node) and \
                        xhsAPI.unregister(xhsAPI.runtime_names.JScript):
                    xhsAPI.register(xhsAPI.runtime_names.Node, xhsAPI.external_runtime.node())

    @staticmethod
    def _get_node_folder(folder: Path):
        if not folder.exists() or not folder.is_dir():
            return None

        for node_folder in folder.iterdir():
            if node_folder.name.endswith('win-x64'):
                return node_folder
        return None


class NodeJS:
    def __init__(self):
        self.supports = {
            ('windows', '64bit'): WindowsX64Strategy()
        }
        self.architecture = self._get_architecture()

    @staticmethod
    def _get_architecture():
        system = platform.system().lower()
        bites = platform.architecture()[0].lower()
        return system, bites

    def setup(self, folder: Path):
        architecture = self.architecture
        if architecture in self.supports.keys():
            _strategy = self.supports[architecture]
            _strategy.setup(folder)
            logger.debug(f'环境 NodeJS 部署: {architecture} {xhsAPI.execjs.get()}')
        else:
            raise OSError('Unsupported platform or architecture')
