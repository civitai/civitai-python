import os
from typing import Optional, Union

from pydantic import BaseModel, Field


class APIConfig(BaseModel):
    base_path: str = "/"
    verify: Union[bool, str] = True

    def get_access_token(self) -> str:
        token = os.getenv("CIVITAI_API_TOKEN")
        if not token:
            raise ValueError(
                "API token not provided. Please set the 'CIVITAI_API_TOKEN' environment variable.")
        return token

    def set_access_token(self, value: str):
        raise Exception(
            "This client was generated with an environment variable for the access token. Please set the environment variable 'CIVITAI_API_TOKEN' to the access token."
        )


class HTTPException(Exception):
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
        super().__init__(f"{status_code} {message}")

    def __str__(self):
        return f"{self.status_code} {self.message}"
