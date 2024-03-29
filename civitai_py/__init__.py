# __init__.py file for the Civitai SDK package.

# flake8: noqa

"""
    Civitai Orchestration Consumer API
"""  # noqa: E501


__version__ = "1.0.0"

import os

# import apis into sdk package
from civitai_py.api.consumption_api import ConsumptionApi
from civitai_py.api.coverage_api import CoverageApi
from civitai_py.api.jobs_api import JobsApi

# import ApiClient
from civitai_py.api_response import ApiResponse
from civitai_py.api_client import ApiClient
from civitai_py.configuration import Configuration
from civitai_py.exceptions import OpenApiException
from civitai_py.exceptions import ApiTypeError
from civitai_py.exceptions import ApiValueError
from civitai_py.exceptions import ApiKeyError
from civitai_py.exceptions import ApiAttributeError
from civitai_py.exceptions import ApiException

# import models into sdk package
from civitai_py.models.air import AIR
from civitai_py.models.assembly import Assembly
from civitai_py.models.asset_type import AssetType
from civitai_py.models.base_model import SDBaseModel
from civitai_py.models.calling_conventions import CallingConventions
from civitai_py.models.clear_asset_request import ClearAssetRequest
from civitai_py.models.comfy_job import ComfyJob
from civitai_py.models.comfy_job_request import ComfyJobRequest
from civitai_py.models.constructor_info import ConstructorInfo
from civitai_py.models.consumption_details import ConsumptionDetails
from civitai_py.models.copy_asset_request import CopyAssetRequest
from civitai_py.models.custom_attribute_data import CustomAttributeData
from civitai_py.models.custom_attribute_named_argument import CustomAttributeNamedArgument
from civitai_py.models.custom_attribute_typed_argument import CustomAttributeTypedArgument
from civitai_py.models.delete_blob_request import DeleteBlobRequest
from civitai_py.models.event_attributes import EventAttributes
from civitai_py.models.event_info import EventInfo
from civitai_py.models.exception import Exception
from civitai_py.models.field_attributes import FieldAttributes
from civitai_py.models.field_info import FieldInfo
from civitai_py.models.fixed_priority import FixedPriority
from civitai_py.models.generic_parameter_attributes import GenericParameterAttributes
from civitai_py.models.get_blob_request import GetBlobRequest
from civitai_py.models.image_embedding_job import ImageEmbeddingJob
from civitai_py.models.image_embedding_job_request import ImageEmbeddingJobRequest
from civitai_py.models.image_job_control_net import ImageJobControlNet
from civitai_py.models.image_job_network_params import ImageJobNetworkParams
from civitai_py.models.image_job_params import ImageJobParams
from civitai_py.models.image_resource_training_job import ImageResourceTrainingJob
from civitai_py.models.image_resource_training_job_request import ImageResourceTrainingJobRequest
from civitai_py.models.image_transform_job import ImageTransformJob
from civitai_py.models.image_transform_job_request import ImageTransformJobRequest
from civitai_py.models.image_transformer import ImageTransformer
from civitai_py.models.job import Job
from civitai_py.models.job_event import JobEvent
from civitai_py.models.job_event_type import JobEventType
from civitai_py.models.job_request import JobRequest
from civitai_py.models.job_request_priority import JobRequestPriority
from civitai_py.models.job_status import JobStatus
from civitai_py.models.job_status_collection import JobStatusCollection
from civitai_py.models.job_status_job import JobStatusJob
from civitai_py.models.job_support import JobSupport
from civitai_py.models.job_template_list import JobTemplateList
from civitai_py.models.job_template_list_jobs_inner import JobTemplateListJobsInner
from civitai_py.models.layout_kind import LayoutKind
from civitai_py.models.media_tagging_job import MediaTaggingJob
from civitai_py.models.media_tagging_job_request import MediaTaggingJobRequest
from civitai_py.models.member_info import MemberInfo
from civitai_py.models.member_types import MemberTypes
from civitai_py.models.method_attributes import MethodAttributes
from civitai_py.models.method_base import MethodBase
from civitai_py.models.method_impl_attributes import MethodImplAttributes
from civitai_py.models.method_info import MethodInfo
from civitai_py.models.model_error import ModelError
from civitai_py.models.model_state_entry import ModelStateEntry
from civitai_py.models.model_validation_state import ModelValidationState
from civitai_py.models.module import Module
from civitai_py.models.module_handle import ModuleHandle
from civitai_py.models.parameter_attributes import ParameterAttributes
from civitai_py.models.parameter_info import ParameterInfo
from civitai_py.models.pin_blob_request import PinBlobRequest
from civitai_py.models.pin_model_job import PinModelJob
from civitai_py.models.ping_job import PingJob
from civitai_py.models.prepare_model_action import PrepareModelAction
from civitai_py.models.prepare_model_job import PrepareModelJob
from civitai_py.models.prepare_model_job_request import PrepareModelJobRequest
from civitai_py.models.problem_details import ProblemDetails
from civitai_py.models.property_attributes import PropertyAttributes
from civitai_py.models.property_info import PropertyInfo
from civitai_py.models.provider import Provider
from civitai_py.models.provider_asset_availability import ProviderAssetAvailability
from civitai_py.models.provider_job_queue_position import ProviderJobQueuePosition
from civitai_py.models.provider_job_status import ProviderJobStatus
from civitai_py.models.query_jobs_request import QueryJobsRequest
from civitai_py.models.query_jobs_result import QueryJobsResult
from civitai_py.models.ranged_priority import RangedPriority
from civitai_py.models.read_only_span1 import ReadOnlySpan1
from civitai_py.models.reboot_worker_job import RebootWorkerJob
from civitai_py.models.reboot_worker_job_request import RebootWorkerJobRequest
from civitai_py.models.runtime_field_handle import RuntimeFieldHandle
from civitai_py.models.runtime_method_handle import RuntimeMethodHandle
from civitai_py.models.runtime_type_handle import RuntimeTypeHandle
from civitai_py.models.scheduler import Scheduler
from civitai_py.models.security_rule_set import SecurityRuleSet
from civitai_py.models.struct_layout_attribute import StructLayoutAttribute
from civitai_py.models.taint_job_request import TaintJobRequest
from civitai_py.models.taint_jobs_request import TaintJobsRequest
from civitai_py.models.taint_jobs_result import TaintJobsResult
from civitai_py.models.text_to_image_job import TextToImageJob
from civitai_py.models.text_to_image_job_request import TextToImageJobRequest
from civitai_py.models.time_span import TimeSpan
from civitai_py.models.type import Type
from civitai_py.models.type_attributes import TypeAttributes
from civitai_py.models.type_info import TypeInfo
from civitai_py.models.unpin_blob_request import UnpinBlobRequest
from civitai_py.models.upload_blob_request import UploadBlobRequest
from civitai_py.models.wd_tagging_job import WDTaggingJob
from civitai_py.models.wd_tagging_job_request import WDTaggingJobRequest
from civitai_py.models.worker_asset_availability import WorkerAssetAvailability


from .schemas import FromTextSchema

import time
import json
import asyncio


class Civitai:
    def __init__(self, api_token=None):
        self.api_token = api_token or os.getenv('CIVITAI_API_TOKEN', '')
        config = Configuration(host="https://orchestration.civitai.com")
        api_client = ApiClient(configuration=config)
        api_client.default_headers['Authorization'] = f"Bearer {self.api_token}"
        self.jobs_api = JobsApi(api_client=api_client)
        self.coverage_api = CoverageApi(api_client=api_client)

    @property
    def jobs(self):
        return self.Jobs(self)

    @property
    def image(self):
        return self.Image(self)

    class Jobs:
        def __init__(self, civitai_py):
            self.civitai_py = civitai_py

        def get(self, token=None, id=None):
            """
            Retrieves job details based on a provided token or job ID.

            This method allows for fetching job details by either specifying a token or a job ID. 
            If both are provided, token takes precedence -- it fetches the job associated with that token.
            At least one of the parameters must be provided, or a ValueError is raised.

            :param token: The token associated with a job.
            :type token: str, optional
            :param id: The unique identifier of the job.
            :type id: str, optional
            :return: A filtered response containing job details such as job ID, cost, result, and scheduled time.
            :rtype: dict
            """
            response = None
            if token:
                full_response = self.civitai_py.jobs_api.v1_consumer_jobs_get(token=token)
                response = self._filter_response(full_response)
            elif id:
                full_response = self.civitai_py.jobs_api.v1_consumer_jobs_job_id_get(job_id=id)
                response = self._filter_response(full_response)
            else:
                raise ValueError("Either 'token' or 'id' must be provided.")

            return json.dumps(response)

        @staticmethod
        def _filter_response(full_response):
            filtered_jobs = []
            for job in full_response.jobs:
                filtered_job = {
                    "jobId": job.job_id,
                    "cost": job.cost,
                    "result": job.result,
                    "scheduled": job.scheduled,
                }
                filtered_jobs.append(filtered_job)
            filtered_response = {
                "token": full_response.token,
                "jobs": filtered_jobs,
            }

            return filtered_response

        def query(self, detailed=False, query_jobs_request=None):
            """
            Query for previously submitted jobs based on properties.

            :param detailed: Whether to include the original job definition.
            :param query_jobs_request: The request object containing query criteria.
            :return: A filtered response based on the query.
            """
            # Call the API method with the provided parameters.
            response = self.civitai_py.jobs_api.v1_consumer_jobs_query_post(
                detailed=detailed,
                query_jobs_request=query_jobs_request
            )
            return response.to_json()

        def cancel(self, job_id, force=False):
            """
            Cancels a job based on the provided job ID.

            :param job_id: The unique identifier of the job to cancel.
            :type job_id: str
            :param force: Force cancellation, even when the job is currently being worked on.
            :type force: bool, optional
            :return: None
            """
            try:
                self.civitai_py.jobs_api.v1_consumer_jobs_job_id_delete(job_id=job_id, force=force)
                print(f"Job {job_id} cancelled successfully.")
            except ApiException as e:
                print(f"Failed to cancel job {job_id}. Error: {e}")

    # @property
    # def models(self):
    #     return self.Models(self)

    # class Models:
    #     def __init__(self, civitai_py):
    #         self.civitai_py = civitai_py

    #     def get(self, model):
    #         return self.civitai_py.coverage_api.v1_consumer_coverage_get(model=model)

    class Image:
        def __init__(self, civitai_py):
            self.civitai_py = civitai_py

        def create(self, input, timeout=None):
            """
            Submits a new image generation job and optionally waits for its completion.

            :param input: The input parameters for the image generation job, including the model.
            :param wait: If True, the method will wait for the job to complete and return the result.
            :return: A dictionary containing the job token and details, or the job result if `wait` is True.
            """

            # Validate input using Pydantic
            try:
                input_data = {
                    "model": input["model"],
                    "params": input["params"],
                    "additionalNetworks": input.get("additionalNetworks", {}),
                    "controlNets": input.get("controlNets", []),
                    "callbackUrl": input.get("callbackUrl", ""),
                    "quantity": input.get("quantity", 1),
                    "properties": input.get("properties", {})
                }

                validated_input = FromTextSchema(**input_data)
            except ValueError as e:
                raise ValueError(f"Validation error: {str(e)}")

            # Infer the baseModel from the model value
            base_model = "SDXL" if "sdxl" in validated_input.model else "SD_1_5"

            # Prepare job input with default values
            job_input = {"$type": "textToImage",
                         "baseModel": base_model, **validated_input.model_dump()}

            try:
                # Submit job and process response
                response = self.civitai_py.jobs_api.v1_consumer_jobs_post(
                    wait=True,
                    detailed=False,
                    _request_timeout=timeout,
                    job_template_list=job_input
                )
            except ApiException as e:
                print(f"Failed to submit job: {e}")
                return None

            if isinstance(response, JobStatusCollection):
                if response:
                    # Return the modified response
                    modified_response = {
                        "token": response.token,
                        "jobs": [{
                            "jobId": job.job_id,
                            "cost": job.cost,
                            "result": job.result,
                            "scheduled": job.scheduled,
                        } for job in response.jobs]
                    }
                    return modified_response


# Create an instance of Civitai and assign it to the variable 'civitai_py'
civitai_py = Civitai()

# Expose the 'jobs', 'models', and 'image' attributes of the 'civitai_py' instance at the module level
jobs = civitai_py.jobs
image = civitai_py.image
# models = civitai_py.models
