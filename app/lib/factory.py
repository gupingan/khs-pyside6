import typing as t
from queue import Queue
from app.lib.core import PrivateUser, PrivateUserCenter, LoginQrCode,TomlBase, Unit, Tasker, Config


class PrivateUserFactory:
    def __init__(self):
        self._url = None
        self._qr_id = None
        self._code = None
        self._cookies = TomlBase.cookies

    @staticmethod
    def _find_user(user_id: str) -> PrivateUser:
        return PrivateUserCenter.find(user_id)

    def make_cookies(self, web_session: str = None):
        cookies = self._cookies.copy()
        if isinstance(web_session, str):
            cookies['web_session'] = web_session
        return cookies

    def import_qrcode_params(self, url=None, qr_id=None, code=None):
        self._url = url
        self._qr_id = qr_id
        self._code = code

    def retrieve_qrcode_params(self):
        self._url = None
        self._qr_id = None
        self._code = None

    def make_qrcode(self):
        if self._url and self._qr_id and self._code:
            return LoginQrCode(self._url, self._qr_id, self._code)
        return None

    def make_user(self, user_id, nickname, session, remark):
        find_user = self._find_user(user_id)
        if find_user is None:
            find_user = PrivateUser(user_id, nickname, session, remark)
            find_user.init_time()
        else:
            find_user.name = nickname
            find_user.session = session
            find_user.update_time()

        find_user.available = 1

        return find_user


class UnitWarehouse:
    units: t.Dict[str, Unit] = dict()

    @classmethod
    def add(cls, unit: Unit):
        cls.units[unit.id] = unit

    @classmethod
    def pop(cls, unit: t.Union[Unit, str], default=None):
        if isinstance(unit, Unit):
            return cls.units.pop(unit.id, default)
        if isinstance(unit, str):
            return cls.units.pop(unit, default)

    @classmethod
    def get(cls, unit_id: t.Union[str]):
        return cls.units.get(unit_id, None)


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class UnitFactory(metaclass=Singleton):
    queue = Queue(65535)

    def __init__(self):
        self.tasks: t.List[Tasker] = []
        self.unit: t.Union[Unit] = None

    def restore_factory(self):
        self.unit = None
        self.tasks.clear()

    def make_tasker(
            self,
            user: t.Union[PrivateUser] = None,
            config: t.Union[Config] = None,
            task_count: t.Union[int] = 0,
            parent=None):
        tasker = Tasker(user, config, task_count, parent)
        self.tasks.append(tasker)
        return tasker

    def make_unit(self, root_config, log_view):
        for task in self.tasks:
            task.setParent(self.unit)

        self.unit.root_config = root_config
        self.unit.tasks.extend(self.tasks)
        self.unit.setParent(log_view)

        UnitWarehouse.add(self.unit)

        return self.unit

    def make_logger(self, log_view_class):
        self.unit = Unit()
        log_view = log_view_class(self.unit)
        return log_view
