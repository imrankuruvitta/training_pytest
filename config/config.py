from config.logger import get_logger

logger = get_logger(__name__)

BASE_URL = "https://jsonplaceholder.typicode.com"
logger.debug(f"Configuration loaded - BASE_URL: {BASE_URL}")

