# PrepareModelJobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_model** | [**BaseModel**](BaseModel.md) |  | [optional] 
**model** | **str** | Get or set the model to prepare | [optional] 
**action** | [**PrepareModelAction**](PrepareModelAction.md) |  | [optional] 

## Example

```python
from civitai.models.prepare_model_job_request import PrepareModelJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareModelJobRequest from a JSON string
prepare_model_job_request_instance = PrepareModelJobRequest.from_json(json)
# print the JSON string representation of the object
print(PrepareModelJobRequest.to_json())

# convert the object into a dict
prepare_model_job_request_dict = prepare_model_job_request_instance.to_dict()
# create an instance of PrepareModelJobRequest from a dict
prepare_model_job_request_form_dict = prepare_model_job_request.from_dict(prepare_model_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


