# job_status_job.py

from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from civitai_py.models.comfy_job import ComfyJob
from civitai_py.models.image_embedding_job import ImageEmbeddingJob
from civitai_py.models.image_resource_training_job import ImageResourceTrainingJob
from civitai_py.models.image_transform_job import ImageTransformJob
from civitai_py.models.media_tagging_job import MediaTaggingJob
from civitai_py.models.pin_model_job import PinModelJob
from civitai_py.models.ping_job import PingJob
from civitai_py.models.prepare_model_job import PrepareModelJob
from civitai_py.models.reboot_worker_job import RebootWorkerJob
from civitai_py.models.text_to_image_job import TextToImageJob
from civitai_py.models.wd_tagging_job import WDTaggingJob
from civitai_py.models.job_event import JobEvent
from civitai_py.models.provider_job_status import ProviderJobStatus
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

JOBSTATUSJOB_ONE_OF_SCHEMAS = ["ComfyJob", "ImageEmbeddingJob", "ImageResourceTrainingJob", "ImageTransformJob",
                               "MediaTaggingJob", "PinModelJob", "PingJob", "PrepareModelJob", "RebootWorkerJob", "TextToImageJob", "WDTaggingJob"]


class JobStatusJob(BaseModel):
    """
    JobStatusJob
    """
    # data type: TextToImageJob
    oneof_schema_1_validator: Optional[TextToImageJob] = None
    # data type: PingJob
    oneof_schema_2_validator: Optional[PingJob] = None
    # data type: ImageResourceTrainingJob
    oneof_schema_3_validator: Optional[ImageResourceTrainingJob] = None
    # data type: ImageTransformJob
    oneof_schema_4_validator: Optional[ImageTransformJob] = None
    # data type: WDTaggingJob
    oneof_schema_5_validator: Optional[WDTaggingJob] = None
    # data type: MediaTaggingJob
    oneof_schema_6_validator: Optional[MediaTaggingJob] = None
    # data type: PrepareModelJob
    oneof_schema_7_validator: Optional[PrepareModelJob] = None
    # data type: ComfyJob
    oneof_schema_8_validator: Optional[ComfyJob] = None
    # data type: ImageEmbeddingJob
    oneof_schema_9_validator: Optional[ImageEmbeddingJob] = None
    # data type: PinModelJob
    oneof_schema_10_validator: Optional[PinModelJob] = None
    # data type: RebootWorkerJob
    oneof_schema_11_validator: Optional[RebootWorkerJob] = None
    actual_instance: Optional[Union[ComfyJob, ImageEmbeddingJob, ImageResourceTrainingJob, ImageTransformJob,
                                    MediaTaggingJob, PinModelJob, PingJob, PrepareModelJob, RebootWorkerJob, TextToImageJob, WDTaggingJob]] = None
    one_of_schemas: Set[str] = {"ComfyJob", "ImageEmbeddingJob", "ImageResourceTrainingJob", "ImageTransformJob",
                                "MediaTaggingJob", "PinModelJob", "PingJob", "PrepareModelJob", "RebootWorkerJob", "TextToImageJob", "WDTaggingJob"}

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError(
                    "If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError(
                    "If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        if v is None:
            return v

        instance = JobStatusJob.model_construct()
        error_messages = []
        match = 0
        # validate data type: TextToImageJob
        if not isinstance(v, TextToImageJob):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TextToImageJob`")
        else:
            match += 1
        # validate data type: PingJob
        if not isinstance(v, PingJob):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PingJob`")
        else:
            match += 1
        # validate data type: ImageResourceTrainingJob
        if not isinstance(v, ImageResourceTrainingJob):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ImageResourceTrainingJob`")
        else:
            match += 1
        # validate data type: ImageTransformJob
        if not isinstance(v, ImageTransformJob):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ImageTransformJob`")
        else:
            match += 1
        # validate data type: WDTaggingJob
        if not isinstance(v, WDTaggingJob):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WDTaggingJob`")
        else:
            match += 1
        # validate data type: MediaTaggingJob
        if not isinstance(v, MediaTaggingJob):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MediaTaggingJob`")
        else:
            match += 1
        # validate data type: PrepareModelJob
        if not isinstance(v, PrepareModelJob):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PrepareModelJob`")
        else:
            match += 1
        # validate data type: ComfyJob
        if not isinstance(v, ComfyJob):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ComfyJob`")
        else:
            match += 1
        # validate data type: ImageEmbeddingJob
        if not isinstance(v, ImageEmbeddingJob):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ImageEmbeddingJob`")
        else:
            match += 1
        # validate data type: PinModelJob
        if not isinstance(v, PinModelJob):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PinModelJob`")
        else:
            match += 1
        # validate data type: RebootWorkerJob
        if not isinstance(v, RebootWorkerJob):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RebootWorkerJob`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in JobStatusJob with oneOf schemas: ComfyJob, ImageEmbeddingJob, ImageResourceTrainingJob, ImageTransformJob, MediaTaggingJob, PinModelJob, PingJob, PrepareModelJob, RebootWorkerJob, TextToImageJob, WDTaggingJob. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in JobStatusJob with oneOf schemas: ComfyJob, ImageEmbeddingJob, ImageResourceTrainingJob, ImageTransformJob, MediaTaggingJob, PinModelJob, PingJob, PrepareModelJob, RebootWorkerJob, TextToImageJob, WDTaggingJob. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of JobStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "job": JobStatusJob.from_dict(obj["job"]) if obj.get("job") is not None else None,
            "jobId": obj.get("jobId"),
            "cost": obj.get("cost"),
            "properties": obj.get("properties"),
            "result": obj.get("result"),
            "lastEvent": JobEvent.from_dict(obj["lastEvent"]) if obj.get("lastEvent") is not None else None,
            "serviceProviders": dict(
                (_k, ProviderJobStatus.from_dict(_v))
                for _k, _v in obj["serviceProviders"].items()
            )
            if obj.get("serviceProviders") is not None
            else None,
            "scheduled": obj.get("scheduled")
        })
        return _obj

    @classmethod
    def from_json(cls, json_str: Optional[str]) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        if json_str is None:
            return instance

        error_messages = []
        match = 0

        # deserialize data into TextToImageJob
        try:
            instance.actual_instance = TextToImageJob.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PingJob
        try:
            instance.actual_instance = PingJob.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ImageResourceTrainingJob
        try:
            instance.actual_instance = ImageResourceTrainingJob.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ImageTransformJob
        try:
            instance.actual_instance = ImageTransformJob.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into WDTaggingJob
        try:
            instance.actual_instance = WDTaggingJob.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into MediaTaggingJob
        try:
            instance.actual_instance = MediaTaggingJob.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PrepareModelJob
        try:
            instance.actual_instance = PrepareModelJob.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ComfyJob
        try:
            instance.actual_instance = ComfyJob.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ImageEmbeddingJob
        try:
            instance.actual_instance = ImageEmbeddingJob.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PinModelJob
        try:
            instance.actual_instance = PinModelJob.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into RebootWorkerJob
        try:
            instance.actual_instance = RebootWorkerJob.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into JobStatusJob with oneOf schemas: ComfyJob, ImageEmbeddingJob, ImageResourceTrainingJob, ImageTransformJob, MediaTaggingJob, PinModelJob, PingJob, PrepareModelJob, RebootWorkerJob, TextToImageJob, WDTaggingJob. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into JobStatusJob with oneOf schemas: ComfyJob, ImageEmbeddingJob, ImageResourceTrainingJob, ImageTransformJob, MediaTaggingJob, PinModelJob, PingJob, PrepareModelJob, RebootWorkerJob, TextToImageJob, WDTaggingJob. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], ComfyJob, ImageEmbeddingJob, ImageResourceTrainingJob, ImageTransformJob, MediaTaggingJob, PinModelJob, PingJob, PrepareModelJob, RebootWorkerJob, TextToImageJob, WDTaggingJob]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())
