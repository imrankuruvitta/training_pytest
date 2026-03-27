import pytest
from config.config import BASE_URL
from config.logger import get_logger

logger = get_logger(__name__)

@pytest.fixture(scope="session")
def base_url():
    logger.info("Initializing base_url fixture")
    logger.info(f"Base URL: {BASE_URL}")
    return BASE_URL

@pytest.fixture(autouse=True)
def log_test_info(request):
    """Log test information at the start and end of each test."""
    logger.info(f"Starting test: {request.node.name}")
    yield
    logger.info(f"Completed test: {request.node.name}")
