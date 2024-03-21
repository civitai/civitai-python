# ImageResourceTrainingJobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | The primary model to train upon | [optional] 
**training_data** | **str** | A url referring data that needs to be trained upon | [optional] 
**params** | **Dict[str, object]** | A untyped set of parameters that are associated with this job | [optional] 

## Example

```python
from civitai.models.image_resource_training_job_request import ImageResourceTrainingJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImageResourceTrainingJobRequest from a JSON string
image_resource_training_job_request_instance = ImageResourceTrainingJobRequest.from_json(json)
# print the JSON string representation of the object
print(ImageResourceTrainingJobRequest.to_json())

# convert the object into a dict
image_resource_training_job_request_dict = image_resource_training_job_request_instance.to_dict()
# create an instance of ImageResourceTrainingJobRequest from a dict
image_resource_training_job_request_form_dict = image_resource_training_job_request.from_dict(image_resource_training_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


