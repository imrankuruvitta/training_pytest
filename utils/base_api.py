import requests
from config.logger import get_logger

logger = get_logger(__name__)

def get_request(url, headers=None, params=None):
    logger.info(f"Sending GET request to: {url}")
    logger.debug(f"Headers: {headers}, Params: {params}")
    response = requests.get(url, headers=headers, params=params, verify=False)
    logger.info(f"GET request completed")
    return response

def post_request(url, payload=None, headers=None):
    logger.info(f"Sending POST request to: {url}")
    logger.debug(f"Payload: {payload}, Headers: {headers}")
    response = requests.post(url, json=payload, headers=headers, verify=False)
    logger.info(f"POST request completed")
    return response
