# JobStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job** | [**JobStatusJob**](JobStatusJob.md) |  | [optional] 
**job_id** | **str** |  | [optional] [readonly] 
**cost** | **float** |  | [optional] [readonly] 
**properties** | **Dict[str, object]** |  | [optional] [readonly] 
**result** | **object** | A optional result of the job | [optional] 
**last_event** | [**JobEvent**](JobEvent.md) |  | [optional] 
**service_providers** | [**Dict[str, ProviderJobStatus]**](ProviderJobStatus.md) | The position of this job in the different queues for different providers. If this is an empty object then this job remains unscheduled. | [optional] 
**scheduled** | **bool** | Wether | [optional] [readonly] 

## Example

```python
from civitai.models.job_status import JobStatus

# TODO update the JSON string below
json = "{}"
# create an instance of JobStatus from a JSON string
job_status_instance = JobStatus.from_json(json)
# print the JSON string representation of the object
print(JobStatus.to_json())

# convert the object into a dict
job_status_dict = job_status_instance.to_dict()
# create an instance of JobStatus from a dict
job_status_form_dict = job_status.from_dict(job_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


