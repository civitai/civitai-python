# WDTaggingJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | [optional] 
**media_url** | **str** |  | [optional] 
**threshold** | **float** |  | [optional] 
**cost** | **float** |  | [optional] [readonly] 
**claim_duration** | [**TimeSpan**](TimeSpan.md) |  | [optional] 
**type** | **str** |  | [optional] [readonly] 
**id** | **str** | A unique id for this job | [optional] 
**created_at** | **datetime** | The date when this job got created | [optional] 
**expire_at** | **datetime** | The date for when this job was set to expire | [optional] 
**webhook** | **str** | A webhook to be invoked when the job receives a status update | [optional] 
**properties** | **Dict[str, object]** | A set of user defined properties that can be used to index and partition this job | [optional] 
**max_retry_attempt** | **int** | The max number of retries before we give up | [optional] 
**dependencies** | **List[str]** | Get or set a list of dependencies that this job has | [optional] 
**issued_by** | **str** | Get or set the name of the consumer that issued this job | [optional] 

## Example

```python
from civitai.models.wd_tagging_job import WDTaggingJob

# TODO update the JSON string below
json = "{}"
# create an instance of WDTaggingJob from a JSON string
wd_tagging_job_instance = WDTaggingJob.from_json(json)
# print the JSON string representation of the object
print(WDTaggingJob.to_json())

# convert the object into a dict
wd_tagging_job_dict = wd_tagging_job_instance.to_dict()
# create an instance of WDTaggingJob from a dict
wd_tagging_job_form_dict = wd_tagging_job.from_dict(wd_tagging_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


