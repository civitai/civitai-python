# coding: utf-8

from typing import List, Dict, Union, Optional
from civitai.api.jobs_api import JobsApi
from civitai.api.coverage_api import CoverageApi
from civitai.models import AIR, ProviderAssetAvailability, JobStatusCollection, QueryJobsRequest, QueryJobsResult, ProblemDetails, JobStatus
from civitai.rest import ApiException
import time


class Civitai:
    """
    A Python client for interacting with Civitai services.
    """

    def __init__(self, config: Dict):
        """
        Initializes the Civitai client with configuration.

        Parameters:
        - config (Dict): Configuration dictionary containing 'env' and 'auth' keys.
        """
        self.config = config
        self.jobs_api = JobsApi()
        self.coverage_api = CoverageApi()

        base_url = "https://orchestration-dev.civitai.com" if config.get(
            "env") == "dev" else "https://orchestration.civitai.com"
        self.jobs_api.api_client.configuration.host = base_url
        self.coverage_api.api_client.configuration.host = base_url
        self.jobs_api.api_client.configuration.api_key["Authorization"] = f"Bearer {
            config['auth']}"
        self.coverage_api.api_client.configuration.api_key["Authorization"] = f"Bearer {
            config['auth']}"

    def from_text(self, input: Dict, wait: bool = False) -> Union[JobStatusCollection, ProblemDetails]:
        """
        Submits a text-to-image job to Civitai and optionally waits for completion.

        Parameters:
        - input (Dict): Input dictionary containing job parameters.
        - wait (bool, optional): Whether to wait for job completion. Defaults to False.

        Returns:
        Union[JobStatusCollection, ProblemDetails]: The job status collection or problem details on failure.
        """
        base_model = "SDXL" if "sdxl" in input["model"] else "SD_1_5"
        job_input = {
            "$type": "textToImage",
            "baseModel": base_model,
            **input
        }
        response = self.jobs_api.post_v1_consumer_jobs(
            wait=wait, detailed=False, job_request=job_input)

        if wait:
            job_result = self._poll_for_job_completion(response.token)
            if job_result and response.jobs:
                response.jobs[0].result = job_result

        return response

    def from_comfy(self, input: Dict, wait: bool = False) -> Union[JobStatusCollection, ProblemDetails]:
        """
        Submits a comfy job to Civitai and optionally waits for completion.

        Parameters:
        - input (Dict): Input dictionary containing job parameters.
        - wait (bool, optional): Whether to wait for job completion. Defaults to False.

        Returns:
        Union[JobStatusCollection, ProblemDetails]: The job status collection or problem details on failure.
        """
        job_input = {
            "$type": "comfy",
            **input
        }
        response = self.jobs_api.post_v1_consumer_jobs(
            wait=wait, detailed=False, job_request=job_input)

        if wait:
            job_result = self._poll_for_job_completion(response.token)
            if job_result and response.jobs:
                response.jobs[0].result = job_result

        return response

    def get_models(self, models: List[Union[AIR, str]]) -> Dict[str, ProviderAssetAvailability]:
        """
        Retrieves the availability of specified models.

        Parameters:
        - models (List[Union[AIR, str]]): A list of models to query.

        Returns:
        Dict[str, ProviderAssetAvailability]: A dictionary mapping models to their availability.
        """
        return self.coverage_api.get_v1_consumer_coverage(models=models)

    def get_job_by_id(self, job_id: str) -> JobStatus:
        """
        Retrieves a job's status by its ID.

        Parameters:
        - job_id (str): The job ID.

        Returns:
        JobStatus: The status of the job.
        """
        return self.jobs_api.get_v1_consumer_jobs_1(job_id=job_id)

    def get_jobs_by_token(self, token: str) -> JobStatusCollection:
        """
        Retrieves jobs associated with a given token.

        Parameters:
        - token (str): The token associated with the jobs.

        Returns:
        JobStatusCollection: The collection of jobs associated with the token.
        """
        return self.jobs_api.get_v1_consumer_jobs(token=token)

    def get_jobs_by_query(self, query: QueryJobsRequest, detailed: bool = False) -> QueryJobsResult:
        """
        Retrieves jobs based on a query.

        Parameters:
        - query (QueryJobsRequest): The query parameters.
        - detailed (bool, optional): Whether to include detailed information. Defaults to False.

        Returns:
        QueryJobsResult: The result of the query.
        """
        return self.jobs_api.post_v1_consumer_jobs_query(detailed=detailed, query_jobs_request=query)

    def cancel_job(self, job_id: str) -> Optional[ProblemDetails]:
        """
        Cancels a job by its ID.

        Parameters:
        - job_id (str): The ID of the job to cancel.

        Returns:
        Optional[ProblemDetails]: Problem details if the cancellation failed, None otherwise.
        """
        return self.jobs_api.delete_v1_consumer_jobs_1(job_id=job_id, force=True)

    def _poll_for_job_completion(self, token: str, interval: int = 30, timeout: int = 600) -> Optional[Dict]:
        """
        Polls for job completion within a specified timeout.

        Parameters:
        - token (str): The token associated with the job.
        - interval (int, optional): The polling interval in seconds. Defaults to 30.
        - timeout (int, optional): The polling timeout in seconds. Defaults to 600.

        Returns:
        Optional[Dict]: The job result if completed, None otherwise.

        Raises:
        - Exception: If polling exceeds the timeout or the job is not scheduled.
        """
        start_time = time.time()

        while time.time() - start_time < timeout:
            response = self.get_jobs_by_token(token)
            job = response.jobs[0] if response.jobs else None

            if job and job.result and job.result.blob_url:
                return job.result
            elif job and not job.scheduled:
                raise Exception(
                    f"Job {job.job_id} is not scheduled and has no result. Stopping polling.")

            time.sleep(interval)

        raise Exception(f"Polling timeout exceeded for token {token}")
