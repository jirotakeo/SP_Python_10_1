# from datetime import datetime
from typing import Any, Callable

from mypy_extensions import KwArg, VarArg


def log(filename=""):
    """Logging decorator"""

    def my_decorator(func: Callable) -> Callable[[tuple[Any, ...], dict[str, Callable[[Any, Any], str]]], str]:
        def wrapper(*args, **kwargs: Callable[[VarArg(Any), KwArg(Any)], str]) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "w") as file:
                        # file.write(f"Start: {datetime.now()}\n")
                        file.write(f"Function: {func.__name__} -> ok")
                        # file.write(f"Finish: {datetime.now()}\n")
                else:
                    # print(f"Start: {datetime.now()}\n")
                    print(f"Function: {func.__name__} ok")
                    # print(f"Finish: {datetime.now()}\n")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "w") as file:
                        # file.write(f"Start: {datetime.now()}\n")
                        file.write(
                            f"Function: {func.__name__} -> error: {e.__class__.__name__} -> inputs: {args, kwargs}"
                        )
                        # file.write(f"Finish: {datetime.now()}\n")
                else:
                    # print(f"Start: {datetime.now()}\n")
                    print(f"Function: {func.__name__} -> error: {e.__class__.__name__} -> inputs: {args, kwargs}")
                    # print(f"Finish: {datetime.now()}\n")

        return wrapper

    return my_decorator
