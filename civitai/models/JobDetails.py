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


class JobDetails(BaseModel):
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

    lastEvent: Optional[JobEvent] = Field(alias="lastEvent", default=None)
