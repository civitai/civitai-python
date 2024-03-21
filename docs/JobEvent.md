# JobEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | [optional] 
**type** | [**JobEventType**](JobEventType.md) |  | [optional] 
**date_time** | **datetime** | Get the absolute datetime on which this event got created | [optional] 
**provider** | [**Provider**](Provider.md) |  | [optional] 
**worker_id** | **str** | Get or set the workerId that is associated with this event | [optional] 
**context** | **Dict[str, object]** | An optional set of key/value pairs that can be used to provide additional context. | [optional] 
**claim_duration** | [**TimeSpan**](TimeSpan.md) |  | [optional] 
**job_duration** | [**TimeSpan**](TimeSpan.md) |  | [optional] 
**retry_attempt** | **int** | The retry attempt of this job | [optional] 
**cost** | **float** | The cost of the job associated with this event | [optional] 
**job_properties** | **Dict[str, object]** | The properties of the job associated with this event | [optional] 
**job_type** | **str** | Get the type of the job | [optional] 
**job_priority** | **int** | The priority that is associated with this job | [optional] 
**claim_has_completed** | **bool** | Get wether this event marks the completion of a claim | [optional] [readonly] 
**job_has_completed** | **bool** | Get wether this event marks the completion of a job  This is determined based on the Civitai.Orchestration.Grains.Jobs.JobEvent.Type of this event | [optional] [readonly] 

## Example

```python
from civitai.models.job_event import JobEvent

# TODO update the JSON string below
json = "{}"
# create an instance of JobEvent from a JSON string
job_event_instance = JobEvent.from_json(json)
# print the JSON string representation of the object
print(JobEvent.to_json())

# convert the object into a dict
job_event_dict = job_event_instance.to_dict()
# create an instance of JobEvent from a dict
job_event_form_dict = job_event.from_dict(job_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


