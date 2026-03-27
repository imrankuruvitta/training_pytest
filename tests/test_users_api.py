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

    assert response.status_code == 200
    assert "id" in response.json()
    assert len(response.json()["title"]) > 0
    logger.info("✓ test_get_users passed all assertions")


@pytest.mark.regression
def test_create_user(base_url):
    logger.info("Test: test_create_user - creating a new post")
    url = f"{base_url}/posts"
    logger.debug(f"URL: {url}")

    payload = {"title":"foo","body":"bar","userId":1}
    logger.info(f"Payload: {payload}")

    response = post_request(url, payload)
    resp_json = response.json()

    assert response.status_code == 201
    assert resp_json["title"] == "foo"
    assert resp_json["body"] == "bar"
    logger.info("✓ test_create_user passed all assertions")

