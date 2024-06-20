import functools
import warnings
from app.lib import globals


def deprecated(reason):
    """
    This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used.
    """

    def decorator(func):
        @functools.wraps(func)
        def new_func(*args, **kwargs):
            warnings.simplefilter('always', DeprecationWarning)
            warnings.warn(f"Call to deprecated function {func.__name__}. {reason}",
                          category=DeprecationWarning,
                          stacklevel=2)
            warnings.simplefilter('default', DeprecationWarning)
            return func(*args, **kwargs)

        return new_func

    return decorator


def connect_callbacks(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        self = args[0]
        success_callback = kwargs.pop('success_callback', None)
        failure_callback = kwargs.pop('failure_callback', None)
        finish_callback = kwargs.pop('finish_callback', None)

        if success_callback:
            self.request_thread.success.connect(success_callback)
        if failure_callback:
            self.request_thread.failure.connect(failure_callback)
        if finish_callback:
            self.request_thread.finish.connect(finish_callback)

        func(*args, **kwargs)
        self.request_thread.start()
        globals.threads.append(self.request_thread)

    return wrapper
