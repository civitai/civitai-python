import json
import logging
from typing import *

import httpx

from ..api_config import APIConfig, HTTPException
from ..models import *


async def get_v1consumerjobs(
    token: str,
    wait: Optional[bool] = None,
    detailed: Optional[bool] = None,
    api_config_override: Optional[APIConfig] = None,
) -> JobStatusCollection:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/v1/consumer/jobs"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_config.get_access_token()}",
    }
    query_params: Dict[str, Any] = {
        "token": token, "wait": wait, "detailed": detailed}

    query_params = {key: value for (
        key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=api_config.verify) as client:
        response = await client.request(
            "get",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code not in [200, 202]:
        raise HTTPException(response.status_code, f"Request to {path} failed with status code: {response.status_code}")

    return JobStatusCollection(**response.json()) if response.json() is not None else JobStatusCollection()


async def post_v1consumerjobs(
    data: Union[JobTemplateList, dict],
    wait: Optional[bool] = None,
    detailed: Optional[bool] = None,
    whatif: Optional[bool] = None,
    charge: Optional[bool] = None,
    api_config_override: Optional[APIConfig] = None,
) -> JobStatusCollection:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/v1/consumer/jobs"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_config.get_access_token()}",
    }
    query_params: Dict[str, Any] = {"wait": wait,
                                    "detailed": detailed, "whatif": whatif, "charge": charge}

    query_params = {key: value for (
        key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=True) as client:
        response = await client.request("post", httpx.URL(path), headers=headers, params=query_params, json=data if isinstance(data, dict) else data.dict())

    if response.status_code not in [200, 202]:
        raise HTTPException(response.status_code, f"Request failed with status code: {response.status_code}")

    return JobStatusCollection(**response.json()) if response.json() is not None else JobStatusCollection()


async def put_v1consumerjobs(
    data: TaintJobsRequest, token: Optional[str] = None, api_config_override: Optional[APIConfig] = None
) -> TaintJobsResult:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/v1/consumer/jobs"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_config.get_access_token()}",
    }
    query_params: Dict[str, Any] = {"token": token}

    query_params = {key: value for (
        key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=api_config.verify) as client:
        response = await client.request("put", httpx.URL(path), headers=headers, params=query_params, json=data.dict())

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return TaintJobsResult(**response.json()) if response.json() is not None else TaintJobsResult()


async def delete_v1consumerjobs(
    token: str, force: Optional[bool] = None, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/v1/consumer/jobs"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_config.get_access_token()}",
    }
    query_params: Dict[str, Any] = {"token": token, "force": force}

    query_params = {key: value for (
        key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=api_config.verify) as client:
        response = await client.request(
            "delete",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return None


async def get_v1consumerjobsjobId(
    jobId: str, detailed: Optional[bool] = None, api_config_override: Optional[APIConfig] = None
) -> JobStatusCollection:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/v1/consumer/jobs/{jobId}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_config.get_access_token()}",
    }
    query_params: Dict[str, Any] = {"detailed": detailed}

    query_params = {key: value for (
        key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=api_config.verify) as client:
        response = await client.request(
            "get",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return JobStatusCollection(**response.json()) if response.json() is not None else JobStatusCollection()


async def put_v1consumerjobsjobId(
    jobId: str, data: TaintJobRequest, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/v1/consumer/jobs/{jobId}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_config.get_access_token()}",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (
        key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=api_config.verify) as client:
        response = await client.request("put", httpx.URL(path), headers=headers, params=query_params, json=data.dict())

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return None


async def delete_v1consumerjobsjobId(
    jobId: str, force: Optional[bool] = None, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/v1/consumer/jobs/{jobId}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_config.get_access_token()}",
    }
    query_params: Dict[str, Any] = {"force": force}

    query_params = {key: value for (
        key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=api_config.verify) as client:
        response = await client.request(
            "delete",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return None


async def post_v1consumerjobsquery(
    data: QueryJobsRequest, detailed: Optional[bool] = None, api_config_override: Optional[APIConfig] = None
) -> QueryJobsResult:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/v1/consumer/jobs/query"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_config.get_access_token()}",
    }
    query_params: Dict[str, Any] = {"detailed": detailed}

    query_params = {key: value for (
        key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=api_config.verify) as client:
        response = await client.request("post", httpx.URL(path), headers=headers, params=query_params, json=data)

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return QueryJobsResult(**response.json()) if response.json() is not None else QueryJobsResult()
