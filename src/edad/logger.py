from loguru import logger
import os

log_path = "output/edad.log"
os.makedirs(os.path.dirname(log_path), exist_ok=True)
logger.add(log_path, rotation="500 KB")
