# ComfyJobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**params** | **Dict[str, object]** | A untyped set of parameters that are associated with this job | [optional] 

## Example

```python
from civitai.models.comfy_job_request import ComfyJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ComfyJobRequest from a JSON string
comfy_job_request_instance = ComfyJobRequest.from_json(json)
# print the JSON string representation of the object
print(ComfyJobRequest.to_json())

# convert the object into a dict
comfy_job_request_dict = comfy_job_request_instance.to_dict()
# create an instance of ComfyJobRequest from a dict
comfy_job_request_form_dict = comfy_job_request.from_dict(comfy_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


