from loguru import logger

try:
    from config import *
except ImportError:
    from src.config import *

configuracion = Config()

try:
    config_logger = configuracion.get_logger_config()
    logger.add(config_logger["file"], format=config_logger["format"], rotation=config_logger["rotation"])
except TypeError:
    config_logger = configuracion.get_logger_default_config() #Si las variables de entorno no son correctas, usar configuracion por defecto
    logger.add(config_logger["file"], format=config_logger["format"], rotation=config_logger["rotation"])
