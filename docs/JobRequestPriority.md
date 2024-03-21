# JobRequestPriority

Get or set a priority where lower values have priority over higher values

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** |  | [optional] 
**min** | **int** |  | [optional] 
**max** | **int** |  | [optional] 

## Example

```python
from civitai.models.job_request_priority import JobRequestPriority

# TODO update the JSON string below
json = "{}"
# create an instance of JobRequestPriority from a JSON string
job_request_priority_instance = JobRequestPriority.from_json(json)
# print the JSON string representation of the object
print(JobRequestPriority.to_json())

# convert the object into a dict
job_request_priority_dict = job_request_priority_instance.to_dict()
# create an instance of JobRequestPriority from a dict
job_request_priority_form_dict = job_request_priority.from_dict(job_request_priority_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


