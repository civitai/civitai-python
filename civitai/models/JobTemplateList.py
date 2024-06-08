from typing import *

from pydantic import BaseModel, Field

from .TextToImageJobRequest import TextToImageJobRequest
from .ImageResourceTrainingJobRequest import ImageResourceTrainingJobRequest
from .UploadBlobRequest import UploadBlobRequest
from .GetBlobRequest import GetBlobRequest
from .PinBlobRequest import PinBlobRequest
from .UnpinBlobRequest import UnpinBlobRequest
from .DeleteBlobRequest import DeleteBlobRequest
from .ImageTransformJobRequest import ImageTransformJobRequest
from .CopyAssetRequest import CopyAssetRequest
from .ClearAssetRequest import ClearAssetRequest
from .MovieRatingJobRequest import MovieRatingJobRequest
from .WDTaggingJobRequest import WDTaggingJobRequest
from .MediaTaggingJobRequest import MediaTaggingJobRequest
from .PrepareModelJobRequest import PrepareModelJobRequest
from .ComfyJobRequest import ComfyJobRequest
from .ImageEmbeddingJobRequest import ImageEmbeddingJobRequest
from .RebootWorkerJobRequest import RebootWorkerJobRequest


class JobTemplateList(BaseModel):
    """
    None model

    """

    jobs: Optional[
        List[
            Union[
                TextToImageJobRequest,
                ImageResourceTrainingJobRequest,
                UploadBlobRequest,
                GetBlobRequest,
                PinBlobRequest,
                UnpinBlobRequest,
                DeleteBlobRequest,
                ImageTransformJobRequest,
                CopyAssetRequest,
                ClearAssetRequest,
                MovieRatingJobRequest,
                WDTaggingJobRequest,
                MediaTaggingJobRequest,
                PrepareModelJobRequest,
                ComfyJobRequest,
                ImageEmbeddingJobRequest,
                RebootWorkerJobRequest,
            ]
        ]
    ] = Field(alias="jobs", default=None)
