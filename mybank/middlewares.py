from typing import Callable

from mybank.logger import myprint


def log_action(func: Callable):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        myprint(f"User {func.__name__} funksiyasini ishlatdi.", "DEBUG")

    return wrapper