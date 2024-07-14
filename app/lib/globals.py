import typing as t
import sys
from pathlib import Path
from tempfile import gettempdir
from PySide6 import QtCore

T = t.TypeVar('T')

threads: t.List[t.Union[QtCore.QThread]] = []

settings = QtCore.QSettings('gupingan', 'KHS-Open')

app_name = '烤红薯开源版'
app_name_en = 'KHS-Open'
version_number = 2
version_name = '1.1.0'

COMMON_CHARS = {
    '换行符': '\\n',
    '缩进': '\\t',
    '4个空格': ' ' * 4,
    '8个空格': ' ' * 8,
}

WORK_TYPES = {
    '采集全部': ['全部'],
    '仅采集图文': ['图文'],
    '仅采集视频': ['视频'],
    '先图文后视频': ['图文', '视频'],
    '先视频后图文': ['视频', '图文'],
}

NOTE_TYPES = {
    'normal': '图文',
    'video': '视频',
}

COLLECT_TYPES = {
    1: '在线搜索',
    2: '推荐页采集',
    3: '本地导入'
}

if getattr(sys, 'frozen', False):
    # 使用打包工具运行
    file = sys.executable
    APP_DIR = Path(sys._MEIPASS).resolve()
else:
    # 正常运行
    file = __file__
    APP_DIR = Path(file).resolve().parent.parent

HOME_DIR = Path.home()
ROOT_DIR = APP_DIR.parent
ASSETS_DIR = APP_DIR / 'assets'
IMAGES_DIR = ASSETS_DIR / 'images'
ICONS_DIR = ASSETS_DIR / 'icons'
NODE_DIR = ASSETS_DIR / 'node'
STYLES_DIR = ASSETS_DIR / 'styles'
UPDATES_DIR = ROOT_DIR / 'updates'
LOGS_DIR = ROOT_DIR / 'logs'
CONFIG_FILE = ROOT_DIR / 'config.toml'
JS_FILE = NODE_DIR / 'xhs-api.js'
LOCK_FILE = Path(gettempdir()) / 'khs-open-lockfile.lock'


class GlobalStyle:
    pass


toml_template = {
    'core': {
        'configs': [],
        'users': [],
        'at_users': []
    },
    'base': {
        'cookies': {},
        'template': {},
        'target_note_id': '',
        'linked_user_session': '',
        'startup_check_update': True,
        'auto_rename': True,
        'browser_path': ''
    }
}

base_cookies_keys = {
    'a1', 'acw_tc',
    'websectiga', 'webBuild',
    'sec_poison_id', 'web_session',
    'webId', 'abRequestId',
    'xsecappid', 'gid'
}


class CellState:
    def __init__(self, display_name: str, foreground_color: str):
        self.display_name = display_name
        self.foreground_color = foreground_color


class CellStates:
    DEFAULT = CellState('非预设状态', 'orange')

    WORK_STATES = {
        False: CellState('未使用', 'green'),
        True: CellState('使用中', 'orange')
    }

    LOGIN_STATES = {
        -1: CellState('未知', 'orange'),
        0: CellState('失效', 'red'),
        1: CellState('有效', '#008000')
    }
    COMMENT_STATES = {
        -2: CellState('禁言/封号', 'red'),
        -1: CellState('未知', '#FFA500'),
        0: CellState('屏蔽', '#800080'),
        1: CellState('正常', '#008000')
    }

    @classmethod
    def get(cls, states: t.Dict[T, CellState], key: t.Union[T], default: CellState = None):
        default = default or cls.DEFAULT
        return states.get(key, default)
