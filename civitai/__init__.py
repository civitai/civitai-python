import os
import asyncio
import time
import logging
from .schemas import FromTextSchema
from .services.async_Jobs_service import (
    get_v1consumerjobs,
    post_v1consumerjobs,
    put_v1consumerjobs,
    delete_v1consumerjobs,
    get_v1consumerjobsjobId,
    put_v1consumerjobsjobId,
    delete_v1consumerjobsjobId,
    post_v1consumerjobsquery
)


class Civitai:
    def __init__(self, env="prod"):
        self.api_token = os.getenv("CIVITAI_API_TOKEN")
        if not self.api_token:
            raise ValueError(
                "API token not provided. Please set the 'CIVITAI_API_TOKEN' environment variable.")

        self.base_path = "https://orchestration-dev.civitai.com" if env == "dev" else "https://orchestration.civitai.com"
        self.verify = True
        self.headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }

        self.image = self.Image(self)
        self.jobs = self.Jobs(self)

    def get_access_token(self):
        return self.api_token

    class Image:
        def __init__(self, civitai):
            self.civitai = civitai

        def create(self, input, wait=False):
            async def async_create():
                try:
                    validated_input = FromTextSchema(**input)
                except ValueError as e:
                    raise ValueError(f"Validation error: {str(e)}")

                base_model = "SDXL" if "sdxl" in validated_input.model else "SD_1_5"
                job_input = {"$type": "textToImage",
                             "baseModel": base_model, **validated_input.model_dump(exclude_unset=True)}

                response = await post_v1consumerjobs(job_input, wait=False, api_config_override=self.civitai)
                modified_response = {
                    "token": response.token,
                    "jobs": [{
                        "jobId": job.jobId,
                        "cost": job.cost,
                        "result": job.result,
                        "scheduled": job.scheduled,
                    } for job in response.jobs]
                }

                if wait:
                    response = await self._poll_for_job_completion(response.token)
                    return response

                return modified_response

            try:
                loop = asyncio.get_running_loop()
            except RuntimeError:
                loop = None

            if loop and loop.is_running():
                return asyncio.ensure_future(async_create())
            else:
                return asyncio.run(async_create())

        async def _poll_for_job_completion(self, token, interval=1, timeout=300):
            start_time = time.time()
            last_response = None
            completed_jobs = {}
            while time.time() - start_time < timeout:
                response = await get_v1consumerjobs(
                    token, api_config_override=self.civitai
                )
                if response and response.jobs:
                    last_response = response
                    logging.info(f"Job status: {last_response}")
                    for job in response.jobs:
                        if job.jobId not in completed_jobs:
                            if job.result and job.result.get("blobUrl"):
                                completed_jobs[job.jobId] = {
                                    "jobId": job.jobId,
                                    "cost": job.cost,
                                    "result": job.result,
                                    "scheduled": job.scheduled,
                                }
                    if len(completed_jobs) >= len(response.jobs):
                        break
                await asyncio.sleep(interval)

            if completed_jobs:
                return {"token": response.token, "jobs": list(completed_jobs.values())}

            if last_response:
                logging.warning(
                    f"Job {token} did not complete within {timeout // 60} minutes."
                )
                return {
                    "token": last_response.token,
                    "jobs": [
                        {
                            "jobId": job.jobId,
                            "cost": job.cost,
                            "result": job.result,
                            "scheduled": job.scheduled,
                        }
                        for job in last_response.jobs
                    ],
                }

    class Jobs:
        def __init__(self, civitai):
            self.civitai = civitai

        def get(self, token=None, job_id=None):
            async def async_get():
                if token:
                    response = await get_v1consumerjobs(token, api_config_override=self.civitai)
                    modified_response = {
                        "token": response.token,
                        "jobs": [{
                            "jobId": job.jobId,
                            "cost": job.cost,
                            "result": job.result,
                            "scheduled": job.scheduled,
                        } for job in response.jobs]
                    }
                elif job_id:
                    response = await get_v1consumerjobsjobId(job_id, api_config_override=self.civitai)
                    modified_response = {
                        "jobId": response.jobId,
                        "cost": response.cost,
                        "result": response.result,
                        "scheduled": response.scheduled,
                    }
                else:
                    raise ValueError(
                        "Either token or job_id must be provided.")

                return modified_response

            try:
                loop = asyncio.get_running_loop()
            except RuntimeError:
                loop = None

            if loop and loop.is_running():
                return asyncio.ensure_future(async_get())
            else:
                return asyncio.run(async_get())

        def query(self, query, detailed=False):
            async def async_query():
                response = await post_v1consumerjobsquery(query, detailed=detailed, api_config_override=self.civitai)
                return response

            try:
                loop = asyncio.get_running_loop()
            except RuntimeError:
                loop = None

            if loop and loop.is_running():
                return asyncio.ensure_future(async_query())
            else:
                return asyncio.run(async_query())

        def cancel(self, job_id):
            async def async_cancel():
                response = await delete_v1consumerjobsjobId(job_id, api_config_override=self.civitai)
                return response

            try:
                loop = asyncio.get_running_loop()
            except RuntimeError:
                loop = None

            if loop and loop.is_running():
                return asyncio.ensure_future(async_cancel())
            else:
                return asyncio.run(async_cancel())


# Expose the 'Civitai' class at the module level
civitai = Civitai()
image = civitai.image
jobs = civitai.jobs
