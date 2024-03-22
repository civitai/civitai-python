# coding: utf-8

from typing import List, Dict, Union, Optional
from civitai.api.jobs_api import JobsApi
from civitai.api.coverage_api import CoverageApi
from civitai.models import AIR, ProviderAssetAvailability, JobStatusCollection, QueryJobsRequest, QueryJobsResult, ProblemDetails, JobStatus
from civitai.rest import ApiException
import time

class Civitai:
    def __init__(self, config: Dict):
        self.config = config
        self.jobs_api = JobsApi()
        self.coverage_api = CoverageApi()

        base_url = "https://orchestration-dev.civitai.com" if config.get("env") == "dev" else "https://orchestration.civitai.com"
        self.jobs_api.api_client.configuration.host = base_url
        self.coverage_api.api_client.configuration.host = base_url
        self.jobs_api.api_client.configuration.api_key["Authorization"] = f"Bearer {config['auth']}"
        self.coverage_api.api_client.configuration.api_key["Authorization"] = f"Bearer {config['auth']}"

    def from_text(self, input: Dict, wait: bool = False) -> Union[JobStatusCollection, ProblemDetails]:
        base_model = "SDXL" if "sdxl" in input["model"] else "SD_1_5"
        job_input = {
            "$type": "textToImage", 
            "baseModel": base_model,
            **input
        }
        response = self.jobs_api.post_v1_consumer_jobs(wait=wait, detailed=False, job_request=job_input)
        
        if wait:
            job_result = self._poll_for_job_completion(response.token)
            if job_result and response.jobs:
                response.jobs[0].result = job_result
        
        return response

    def from_comfy(self, input: Dict, wait: bool = False) -> Union[JobStatusCollection, ProblemDetails]:
        job_input = {
            "$type": "comfy",
            **input
        }
        response = self.jobs_api.post_v1_consumer_jobs(wait=wait, detailed=False, job_request=job_input)

        if wait:
            job_result = self._poll_for_job_completion(response.token)
            if job_result and response.jobs:
                response.jobs[0].result = job_result
        
        return response

    def get_models(self, models: List[Union[AIR, str]]) -> Dict[str, ProviderAssetAvailability]:
        return self.coverage_api.get_v1_consumer_coverage(models=models)

    def get_job_by_id(self, job_id: str) -> JobStatus:
        return self.jobs_api.get_v1_consumer_jobs_1(job_id=job_id)

    def get_jobs_by_token(self, token: str) -> JobStatusCollection:
        return self.jobs_api.get_v1_consumer_jobs(token=token)

    def get_jobs_by_query(self, query: QueryJobsRequest, detailed: bool = False) -> QueryJobsResult:
        return self.jobs_api.post_v1_consumer_jobs_query(detailed=detailed, query_jobs_request=query)

    def cancel_job(self, job_id: str) -> Optional[ProblemDetails]:
        return self.jobs_api.delete_v1_consumer_jobs_1(job_id=job_id, force=True)

    def _poll_for_job_completion(self, token: str, interval: int = 30, timeout: int = 600) -> Optional[Dict]:
        start_time = time.time()

        while time.time() - start_time < timeout:
            response = self.get_jobs_by_token(token)
            job = response.jobs[0] if response.jobs else None
            
            if job and job.result and job.result.blob_url:
                return job.result
            elif job and not job.scheduled:
                raise Exception(f"Job {job.job_id} is not scheduled and has no result. Stopping polling.")
            
            time.sleep(interval)
        
        raise Exception(f"Polling timeout exceeded for token {token}")