from loguru import logger

try:
    from config import *
except ImportError:
    from src.config import *

configuracion = Config()
config_logger = configuracion.get_logger_config()

logger.add(config_logger["file"], format=config_logger["format"], level=config_logger["level"], rotation="100 MB")
