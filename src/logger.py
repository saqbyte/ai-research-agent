import logging
import os


LOG_LEVEL = os.getenv(
    "LOG_LEVEL",
    "INFO"
).upper()


def get_logger(name: str) -> logging.Logger:
    """
    Create and return a configured application logger.
    """

    logger = logging.getLogger(name)

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    logger.setLevel(LOG_LEVEL)

    handler = logging.StreamHandler()

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger