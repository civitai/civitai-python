# JobStatusJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | [optional] 
**params** | **Dict[str, object]** | A untyped set of parameters that are associated with this job | [optional] 
**image_hash** | **str** |  | [optional] 
**additional_networks** | [**Dict[str, ImageJobNetworkParams]**](ImageJobNetworkParams.md) | Get or set a associative list of additional networks. Each network is identified by a hash code | [optional] 
**destination_url** | **str** | Get or set the URL where the transformed image will be uploaded to | [optional] 
**base_model** | [**BaseModel**](BaseModel.md) |  | [optional] 
**store_as_blob** | **bool** | Wether to store the image as a blob or as a legacy image | [optional] 
**control_nets** | [**List[ImageJobControlNet]**](ImageJobControlNet.md) | Get or set a list of control nets that should be applied with this textToImage job | [optional] 
**cost** | **float** | Get a cost estimate for this job | [optional] [readonly] 
**claim_duration** | [**TimeSpan**](TimeSpan.md) |  | [optional] 
**type** | **str** | The type of this job as a string | [optional] [readonly] 
**id** | **str** | A unique id for this job | [optional] 
**created_at** | **datetime** | The date when this job got created | [optional] 
**expire_at** | **datetime** | The date for when this job was set to expire | [optional] 
**webhook** | **str** | A webhook to be invoked when the job receives a status update | [optional] 
**properties** | **Dict[str, object]** | A set of user defined properties that can be used to index and partition this job | [optional] 
**max_retry_attempt** | **int** | The max number of retries before we give up | [optional] 
**dependencies** | **List[str]** | Get or set a list of dependencies that this job has | [optional] 
**issued_by** | **str** | Get or set the name of the consumer that issued this job | [optional] 
**training_data** | **str** | A url referring data that needs to be trained upon | [optional] 
**custom_cost** | **float** | Get or set a custom cost value for this job | [optional] 
**output** | **str** | An application provided output of the current status of this job | [optional] 
**image_url** | **str** |  | [optional] 
**transformer** | [**ImageTransformer**](ImageTransformer.md) |  | [optional] 
**destination_blob_key** | **str** | Get the key of the destination blob to upload the result to | [optional] 
**media_url** | **str** |  | [optional] 
**threshold** | **float** |  | [optional] 
**model_id** | **int** |  | [optional] 
**action** | [**PrepareModelAction**](PrepareModelAction.md) |  | [optional] 
**assets** | [**Dict[str, ImageJobNetworkParams]**](ImageJobNetworkParams.md) |  | [optional] 

## Example

```python
from civitai.models.job_status_job import JobStatusJob

# TODO update the JSON string below
json = "{}"
# create an instance of JobStatusJob from a JSON string
job_status_job_instance = JobStatusJob.from_json(json)
# print the JSON string representation of the object
print(JobStatusJob.to_json())

# convert the object into a dict
job_status_job_dict = job_status_job_instance.to_dict()
# create an instance of JobStatusJob from a dict
job_status_job_form_dict = job_status_job.from_dict(job_status_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


