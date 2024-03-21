# TaintJobsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 
**context** | **Dict[str, object]** |  | [optional] 
**properties** | **Dict[str, Optional[object]]** |  | [optional] 

## Example

```python
from civitai.models.taint_jobs_request import TaintJobsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TaintJobsRequest from a JSON string
taint_jobs_request_instance = TaintJobsRequest.from_json(json)
# print the JSON string representation of the object
print(TaintJobsRequest.to_json())

# convert the object into a dict
taint_jobs_request_dict = taint_jobs_request_instance.to_dict()
# create an instance of TaintJobsRequest from a dict
taint_jobs_request_form_dict = taint_jobs_request.from_dict(taint_jobs_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


