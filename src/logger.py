from loguru import logger

try:
    from config import *
except ImportError:
    from src.config import *

configuracion = Config()
config_logger = configuracion.get_logger_config()

logger.add(config_logger["file"], format="{time:DD-MM-YYYY at HH:mm:ss} | {level: <8} | {name: ^15}:{line: >3}  | {function: ^15} | {message}", level=config_logger["level"], rotation="100 MB")
