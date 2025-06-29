import pathlib
import logging
from logging.handlers import RotatingFileHandler

logging_file = pathlib.Path.joinpath(pathlib.Path(__file__).parent.parent, "data", "password_generator_logs.log")
logging_file.parent.mkdir(parents=True, exist_ok=True)

def get_logger() -> logging.Logger:
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s() - %(message)s')
    handler = RotatingFileHandler(logging_file, mode="a", encoding="utf-8", maxBytes=5 * 1024 * 1024, backupCount=1)
    handler.setFormatter(formatter)
    logger = logging.getLogger(pathlib.Path(__name__).name)
    logger.setLevel(logging.WARNING)
    if not logger.hasHandlers():
        logger.addHandler(handler)
    return logger