from pydantic import BaseModel, Field, validator
from typing import Optional, List, Dict, Any


class ControlNetSchema(BaseModel):
    preprocessor: Optional[str]
    weight: Optional[float]
    startStep: Optional[int]
    endStep: Optional[int]
    blobKey: Optional[str] = None
    imageUrl: Optional[str] = None

    @validator('preprocessor')
    def preprocessor_validator(cls, v):
        if v and v not in ["Canny", "DepthZoe", "SoftedgePidinet", "Rembg"]:
            raise ValueError("Invalid preprocessor value")
        return v


class FromTextSchema(BaseModel):
    model: str
    params: Dict[str, Any] = Field(..., example={"prompt": "A clear day"})
    additionalNetworks: Optional[Dict[str, Any]]
    controlNets: Optional[List[ControlNetSchema]]
    callbackUrl: Optional[str]
    quantity: Optional[int] = 1
    properties: Optional[Dict[str, Any]]

    @validator('params')
    def params_validator(cls, v):
        if 'width' in v and not (1 <= v['width'] <= 1024):
            raise ValueError("Width must be between 1 and 1024")
        if 'height' in v and not (1 <= v['height'] <= 1024):
            raise ValueError("Height must be between 1 and 1024")
        return v
