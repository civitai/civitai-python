from typing import *

from pydantic import BaseModel, Field

from .ApplyConfigurationJob import ApplyConfigurationJob
from .ComfyJob import ComfyJob
from .ImageEmbeddingJob import ImageEmbeddingJob
from .ImageResourceTrainingJob import ImageResourceTrainingJob
from .ImageTransformJob import ImageTransformJob
from .JobEvent import JobEvent
from .MediaTaggingJob import MediaTaggingJob
from .MovieRatingJob import MovieRatingJob
from .PingJob import PingJob
from .PinModelJob import PinModelJob
from .PrepareModelJob import PrepareModelJob
from .RebootWorkerJob import RebootWorkerJob
from .TextToImageJob import TextToImageJob
from .WDTaggingJob import WDTaggingJob


class JobStatus(BaseModel):
    """
    None model

    """

    job: Optional[
        Union[
            TextToImageJob,
            PingJob,
            ImageResourceTrainingJob,
            ImageTransformJob,
            MovieRatingJob,
            WDTaggingJob,
            MediaTaggingJob,
            PrepareModelJob,
            ComfyJob,
            ImageEmbeddingJob,
            PinModelJob,
            RebootWorkerJob,
            ApplyConfigurationJob,
        ]
    ] = Field(alias="job", default=None)

    jobId: Optional[str] = Field(alias="jobId", default=None)

    cost: Optional[float] = Field(alias="cost", default=None)

    properties: Optional[Dict[str, Any]] = Field(alias="properties", default=None)

    result: Optional[Any] = Field(alias="result", default=None)

    lastEvent: Optional[JobEvent] = Field(alias="lastEvent", default=None)

    serviceProviders: Optional[Dict[str, Any]] = Field(alias="serviceProviders", default=None)

    scheduled: Optional[bool] = Field(alias="scheduled", default=None)
