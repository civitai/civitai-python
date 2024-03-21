# TaintJobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 
**context** | **Dict[str, object]** | An optional set of key/value pairs that can be used to provide additional context. | [optional] 

## Example

```python
from civitai.models.taint_job_request import TaintJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TaintJobRequest from a JSON string
taint_job_request_instance = TaintJobRequest.from_json(json)
# print the JSON string representation of the object
print(TaintJobRequest.to_json())

# convert the object into a dict
taint_job_request_dict = taint_job_request_instance.to_dict()
# create an instance of TaintJobRequest from a dict
taint_job_request_form_dict = taint_job_request.from_dict(taint_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


