import pytest
from utils.base_api import get_request, post_request
from config.logger import get_logger

logger = get_logger(__name__)


@pytest.mark.smoke
def test_get_users(base_url):
    logger.info("Test: test_get_users - fetching a post from JSONPlaceholder")
    url = f"{base_url}/posts/1"
    logger.debug(f"URL: {url}")

    response = get_request(url)
    logger.info(f"Response status: {response.status_code}")

    logger.debug("Asserting status code equals 200")
    assert response.status_code == 200
    logger.info("✓ Status code assertion passed")
    
    logger.debug("Asserting 'id' field exists in response")
    assert "id" in response.json()
    logger.info("✓ 'id' field assertion passed")
    
    logger.debug("Asserting title length > 0")
    assert len(response.json()["title"]) > 0
    logger.info("✓ Title length assertion passed")


@pytest.mark.regression
def test_create_user(base_url):
    logger.info("Test: test_create_user - creating a new post")
    url = f"{base_url}/posts"
    logger.debug(f"URL: {url}")

    payload = {"title":"foo","body":"bar","userId":1}
    logger.info(f"Payload: {payload}")

    response = post_request(url, payload)
    logger.info(f"Response status: {response.status_code}")
    
    resp_json = response.json()
    logger.debug(f"Response JSON: {resp_json}")

    logger.debug("Asserting status code equals 201")
    assert response.status_code == 201
    logger.info("✓ Status code assertion passed")
    
    logger.debug("Asserting response title equals 'foo'")
    assert resp_json["title"] == "foo"
    logger.info("✓ Title assertion passed")
    
    logger.debug("Asserting response body equals 'bar'")
    assert resp_json["body"] == "bar"
    logger.info("✓ Body assertion passed")
