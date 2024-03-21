# ProviderJobQueuePosition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preceding_jobs** | **int** | The exact position in the queue | [optional] 
**preceding_cost** | **float** | The exact cost that is preceding | [optional] 
**throughput_rate** | **float** | The estimated throughput rate of the queue | [optional] 
**worker_id** | **str** | The id of the worker that this job is queued with | [optional] 
**estimated_start_duration** | [**TimeSpan**](TimeSpan.md) |  | [optional] 
**estimated_start_date** | **datetime** | The date before the job is estimated to be started. Null if we do not have an estimate yet | [optional] [readonly] 

## Example

```python
from civitai.models.provider_job_queue_position import ProviderJobQueuePosition

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderJobQueuePosition from a JSON string
provider_job_queue_position_instance = ProviderJobQueuePosition.from_json(json)
# print the JSON string representation of the object
print(ProviderJobQueuePosition.to_json())

# convert the object into a dict
provider_job_queue_position_dict = provider_job_queue_position_instance.to_dict()
# create an instance of ProviderJobQueuePosition from a dict
provider_job_queue_position_form_dict = provider_job_queue_position.from_dict(provider_job_queue_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


