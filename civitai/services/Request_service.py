import json
from typing import *

import httpx

from ..api_config import APIConfig, HTTPException
from ..models import *


def get_v1consumerrequests(
    cursor: Optional[str] = None, take: Optional[int] = None, api_config_override: Optional[APIConfig] = None
) -> QueryRequestsResult:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/v1/consumer/requests"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {"cursor": cursor, "take": take}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    with httpx.Client(base_url=base_path, verify=api_config.verify) as client:
        response = client.request(
            "get",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return QueryRequestsResult(**response.json()) if response.json() is not None else QueryRequestsResult()
