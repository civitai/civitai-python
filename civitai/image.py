import requests
from .api_config import API_BASE_URL, HEADERS


def create(input, wait=False):
    url = f"{API_BASE_URL}/v1/images"
    response = requests.post(url, json=input, headers=HEADERS)
    response.raise_for_status()
    return response.json()
