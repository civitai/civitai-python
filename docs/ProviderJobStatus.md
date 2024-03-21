# ProviderJobStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**support** | [**JobSupport**](JobSupport.md) |  | [optional] 
**queue_position** | [**ProviderJobQueuePosition**](ProviderJobQueuePosition.md) |  | [optional] 

## Example

```python
from civitai.models.provider_job_status import ProviderJobStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderJobStatus from a JSON string
provider_job_status_instance = ProviderJobStatus.from_json(json)
# print the JSON string representation of the object
print(ProviderJobStatus.to_json())

# convert the object into a dict
provider_job_status_dict = provider_job_status_instance.to_dict()
# create an instance of ProviderJobStatus from a dict
provider_job_status_form_dict = provider_job_status.from_dict(provider_job_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


