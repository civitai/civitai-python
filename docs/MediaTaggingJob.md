# MediaTaggingJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_id** | **int** |  | [optional] 
**media_url** | **str** |  | [optional] 
**cost** | **float** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**id** | **str** | A unique id for this job | [optional] 
**created_at** | **datetime** | The date when this job got created | [optional] 
**expire_at** | **datetime** | The date for when this job was set to expire | [optional] 
**webhook** | **str** | A webhook to be invoked when the job receives a status update | [optional] 
**properties** | **Dict[str, object]** | A set of user defined properties that can be used to index and partition this job | [optional] 
**max_retry_attempt** | **int** | The max number of retries before we give up | [optional] 
**dependencies** | **List[str]** | Get or set a list of dependencies that this job has | [optional] 
**issued_by** | **str** | Get or set the name of the consumer that issued this job | [optional] 
**claim_duration** | [**TimeSpan**](TimeSpan.md) |  | [optional] 

## Example

```python
from civitai.models.media_tagging_job import MediaTaggingJob

# TODO update the JSON string below
json = "{}"
# create an instance of MediaTaggingJob from a JSON string
media_tagging_job_instance = MediaTaggingJob.from_json(json)
# print the JSON string representation of the object
print(MediaTaggingJob.to_json())

# convert the object into a dict
media_tagging_job_dict = media_tagging_job_instance.to_dict()
# create an instance of MediaTaggingJob from a dict
media_tagging_job_form_dict = media_tagging_job.from_dict(media_tagging_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


