import logging
import sys
from typing import Any, Callable

formatter = logging.Formatter("%(asctime)s %(levelname)s\t%(message)s")
logging.basicConfig(handlers=[logging.NullHandler()], force=True, encoding="utf-8", level=logging.DEBUG)
logger = logging.getLogger(__name__)


def log(filename: str = "") -> Callable[[Callable], Callable]:
    """Logging decorator"""

    def my_decorator(func: Callable) -> Callable[..., Any]:
        logging_handler: logging.Handler = logging.StreamHandler(sys.stdout)
        if filename:
            logging_handler = logging.FileHandler(filename)
        logging_handler.setFormatter(formatter)
        logger.addHandler(logging_handler)

        def wrapper(*args: tuple, **kwargs: dict[str, Any]) -> Any:
            result = None
            try:
                result = func(*args, **kwargs)
                logger.debug("Function: %s ok", func.__name__)
            except Exception as e:
                logger.debug(f"Function: {func.__name__} -> error: {e.__class__.__name__} -> inputs: {args, kwargs}")
            return result

        return wrapper

    return my_decorator
