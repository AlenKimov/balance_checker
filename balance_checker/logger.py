from loguru import logger
from datetime import datetime
from os import makedirs
import sys
from pathlib import Path

# Скрипты проекта
from definitions import LOG_DIR


LOG_FILE_FORMAT = "<white>{time:YYYY-MM-DD HH:mm:ss}</white> | <level>{level: <8}</level> | <white>{message}</white>"
CONSOLE_FORMAT = "<white>{time:HH:mm:ss}</white> | <level>{level: <8}</level> | <white>{message}</white>"


def set_up_logger():
    logger.remove()
    makedirs(LOG_DIR, exist_ok=True)
    log_file_name = f"{datetime.now().strftime('%d-%m-%Y')}.log"
    log_file_path = Path(LOG_DIR, log_file_name)
    logger.add(log_file_path, format=LOG_FILE_FORMAT, level="DEBUG", rotation='1 day')
    logger.add(sys.stderr, colorize=True, format=CONSOLE_FORMAT, level="DEBUG")


set_up_logger()
