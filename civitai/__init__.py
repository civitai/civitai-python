# __init__.py file for the Civitai SDK package.

# flake8: noqa

"""
    Civitai Orchestration Consumer API
"""  # noqa: E501

import os

# import apis into sdk package
from civitai.api.consumption_api import ConsumptionApi
from civitai.api.coverage_api import CoverageApi
from civitai.api.jobs_api import JobsApi

# import ApiClient
from civitai.api_response import ApiResponse
from civitai.api_client import ApiClient
from civitai.configuration import Configuration
from civitai.exceptions import OpenApiException
from civitai.exceptions import ApiTypeError
from civitai.exceptions import ApiValueError
from civitai.exceptions import ApiKeyError
from civitai.exceptions import ApiAttributeError
from civitai.exceptions import ApiException

# import models into sdk package
from civitai.models.air import AIR
from civitai.models.assembly import Assembly
from civitai.models.asset_type import AssetType
from civitai.models.base_model import SDBaseModel
from civitai.models.calling_conventions import CallingConventions
from civitai.models.clear_asset_request import ClearAssetRequest
from civitai.models.comfy_job import ComfyJob
from civitai.models.comfy_job_request import ComfyJobRequest
from civitai.models.constructor_info import ConstructorInfo
from civitai.models.consumption_details import ConsumptionDetails
from civitai.models.copy_asset_request import CopyAssetRequest
from civitai.models.custom_attribute_data import CustomAttributeData
from civitai.models.custom_attribute_named_argument import CustomAttributeNamedArgument
from civitai.models.custom_attribute_typed_argument import CustomAttributeTypedArgument
from civitai.models.delete_blob_request import DeleteBlobRequest
from civitai.models.event_attributes import EventAttributes
from civitai.models.event_info import EventInfo
from civitai.models.exception import Exception
from civitai.models.field_attributes import FieldAttributes
from civitai.models.field_info import FieldInfo
from civitai.models.fixed_priority import FixedPriority
from civitai.models.generic_parameter_attributes import GenericParameterAttributes
from civitai.models.get_blob_request import GetBlobRequest
from civitai.models.image_embedding_job import ImageEmbeddingJob
from civitai.models.image_embedding_job_request import ImageEmbeddingJobRequest
from civitai.models.image_job_control_net import ImageJobControlNet
from civitai.models.image_job_network_params import ImageJobNetworkParams
from civitai.models.image_job_params import ImageJobParams
from civitai.models.image_resource_training_job import ImageResourceTrainingJob
from civitai.models.image_resource_training_job_request import ImageResourceTrainingJobRequest
from civitai.models.image_transform_job import ImageTransformJob
from civitai.models.image_transform_job_request import ImageTransformJobRequest
from civitai.models.image_transformer import ImageTransformer
from civitai.models.job import Job
from civitai.models.job_event import JobEvent
from civitai.models.job_event_type import JobEventType
from civitai.models.job_request import JobRequest
from civitai.models.job_request_priority import JobRequestPriority
from civitai.models.job_status import JobStatus
from civitai.models.job_status_collection import JobStatusCollection
from civitai.models.job_status_job import JobStatusJob
from civitai.models.job_support import JobSupport
from civitai.models.job_template_list import JobTemplateList
from civitai.models.job_template_list_jobs_inner import JobTemplateListJobsInner
from civitai.models.layout_kind import LayoutKind
from civitai.models.media_tagging_job import MediaTaggingJob
from civitai.models.media_tagging_job_request import MediaTaggingJobRequest
from civitai.models.member_info import MemberInfo
from civitai.models.member_types import MemberTypes
from civitai.models.method_attributes import MethodAttributes
from civitai.models.method_base import MethodBase
from civitai.models.method_impl_attributes import MethodImplAttributes
from civitai.models.method_info import MethodInfo
from civitai.models.model_error import ModelError
from civitai.models.model_state_entry import ModelStateEntry
from civitai.models.model_validation_state import ModelValidationState
from civitai.models.module import Module
from civitai.models.module_handle import ModuleHandle
from civitai.models.parameter_attributes import ParameterAttributes
from civitai.models.parameter_info import ParameterInfo
from civitai.models.pin_blob_request import PinBlobRequest
from civitai.models.pin_model_job import PinModelJob
from civitai.models.ping_job import PingJob
from civitai.models.prepare_model_action import PrepareModelAction
from civitai.models.prepare_model_job import PrepareModelJob
from civitai.models.prepare_model_job_request import PrepareModelJobRequest
from civitai.models.problem_details import ProblemDetails
from civitai.models.property_attributes import PropertyAttributes
from civitai.models.property_info import PropertyInfo
from civitai.models.provider import Provider
from civitai.models.provider_asset_availability import ProviderAssetAvailability
from civitai.models.provider_job_queue_position import ProviderJobQueuePosition
from civitai.models.provider_job_status import ProviderJobStatus
from civitai.models.query_jobs_request import QueryJobsRequest
from civitai.models.query_jobs_result import QueryJobsResult
from civitai.models.ranged_priority import RangedPriority
from civitai.models.read_only_span1 import ReadOnlySpan1
from civitai.models.reboot_worker_job import RebootWorkerJob
from civitai.models.reboot_worker_job_request import RebootWorkerJobRequest
from civitai.models.runtime_field_handle import RuntimeFieldHandle
from civitai.models.runtime_method_handle import RuntimeMethodHandle
from civitai.models.runtime_type_handle import RuntimeTypeHandle
from civitai.models.scheduler import Scheduler
from civitai.models.security_rule_set import SecurityRuleSet
from civitai.models.struct_layout_attribute import StructLayoutAttribute
from civitai.models.taint_job_request import TaintJobRequest
from civitai.models.taint_jobs_request import TaintJobsRequest
from civitai.models.taint_jobs_result import TaintJobsResult
from civitai.models.text_to_image_job import TextToImageJob
from civitai.models.text_to_image_job_request import TextToImageJobRequest
from civitai.models.time_span import TimeSpan
from civitai.models.type import Type
from civitai.models.type_attributes import TypeAttributes
from civitai.models.type_info import TypeInfo
from civitai.models.unpin_blob_request import UnpinBlobRequest
from civitai.models.upload_blob_request import UploadBlobRequest
from civitai.models.wd_tagging_job import WDTaggingJob
from civitai.models.wd_tagging_job_request import WDTaggingJobRequest
from civitai.models.worker_asset_availability import WorkerAssetAvailability


from .schemas import FromTextSchema

import time
import json


class Civitai:
    def __init__(self, api_token=None):
        self.api_token = api_token or os.getenv('CIVITAI_API_TOKEN', '')
        if not self.api_token:
            raise ValueError(
                "API token not provided. Please set the 'CIVITAI_API_TOKEN' environment variable or pass the token directly.")

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
        def __init__(self, civitai):
            self.civitai = civitai

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
                full_response = self.civitai.jobs_api.v1_consumer_jobs_get(token=token)
                response = self._filter_response(full_response)
            elif id:
                full_response = self.civitai.jobs_api.v1_consumer_jobs_job_id_get(job_id=id)
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
            response = self.civitai.jobs_api.v1_consumer_jobs_query_post(
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
                self.civitai.jobs_api.v1_consumer_jobs_job_id_delete(job_id=job_id, force=force)
                print(f"Job {job_id} cancelled successfully.")
            except ApiException as e:
                print(f"Failed to cancel job {job_id}. Error: {e}")

    # @property
    # def models(self):
    #     return self.Models(self)

    # class Models:
    #     def __init__(self, civitai):
    #         self.civitai = civitai

    #     def get(self, model):
    #         return self.civitai.coverage_api.v1_consumer_coverage_get(model=model)

    class Image:
        def __init__(self, civitai):
            self.civitai = civitai

        def create(self, input, wait=False):
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
                response = self.civitai.jobs_api.v1_consumer_jobs_post(
                    wait=True,
                    detailed=False,
                    job_template_list=job_input
                )
            except ApiException as e:
                print(f"Failed to submit job: {e}")
                return None

            if response is None:
                print("No response received from the API.")
                return None

            # Poll until job is done
            job_result = self._poll_for_job_completion(response.token)
            if job_result and response.jobs:
                response.jobs[0].result = job_result

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

        # Helper methods
        def _get_job_token(self, token, timeout=10):
            """
            Retrieves the job token or raises a TimeoutError if the token is not available within the specified timeout.

            :param token: The token to retrieve.
            :param timeout: The maximum time (in seconds) to wait for the token.
            :return: The job token as a dictionary.
            """
            start_time = time.time()
            while time.time() - start_time < timeout:
                response = self.civitai.jobs_api.v1_consumer_jobs_get(token=token)
                if response and response.token:
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
                time.sleep(1)
            raise TimeoutError(f"Job token not available within {timeout} seconds.")

        def _poll_for_job_completion(self, token, interval=30, timeout=300):
            """
            Polls the job status until completion or timeout.

            :param token: The token of the job to poll.
            :param interval: The interval (in seconds) between status checks.
            :param timeout: The maximum time (in seconds) to wait for job completion.
            :return: The result of the job if completed, None otherwise.
            """
            start_time = time.time()
            while time.time() - start_time < timeout:
                response = self.civitai.jobs_api.v1_consumer_jobs_get(token=token)
                if response and response.jobs:
                    job = response.jobs[0]
                    if job.result and job.result.get("blobUrl"):
                        return job.result
                time.sleep(interval)
            raise TimeoutError(f"Job {token} did not complete within {timeout} seconds.")


# Create an instance of Civitai and assign it to the variable 'civitai'
civitai = Civitai()

# Expose the 'jobs', 'models', and 'image' attributes of the 'civitai' instance at the module level
jobs = civitai.jobs
image = civitai.image
# models = civitai.models
