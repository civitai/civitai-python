# TaintJobsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobs** | **int** |  | [optional] 

## Example

```python
from civitai.models.taint_jobs_result import TaintJobsResult

# TODO update the JSON string below
json = "{}"
# create an instance of TaintJobsResult from a JSON string
taint_jobs_result_instance = TaintJobsResult.from_json(json)
# print the JSON string representation of the object
print(TaintJobsResult.to_json())

# convert the object into a dict
taint_jobs_result_dict = taint_jobs_result_instance.to_dict()
# create an instance of TaintJobsResult from a dict
taint_jobs_result_form_dict = taint_jobs_result.from_dict(taint_jobs_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


