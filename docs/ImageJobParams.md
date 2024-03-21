# ImageJobParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt** | **str** |  | [optional] 
**negative_prompt** | **str** |  | [optional] 
**scheduler** | [**Scheduler**](Scheduler.md) |  | [optional] 
**steps** | **int** |  | [optional] 
**cfg_scale** | **float** |  | [optional] 
**width** | **int** |  | 
**height** | **int** |  | 
**seed** | **int** |  | [optional] 
**clip_skip** | **int** |  | [optional] 

## Example

```python
from civitai.models.image_job_params import ImageJobParams

# TODO update the JSON string below
json = "{}"
# create an instance of ImageJobParams from a JSON string
image_job_params_instance = ImageJobParams.from_json(json)
# print the JSON string representation of the object
print(ImageJobParams.to_json())

# convert the object into a dict
image_job_params_dict = image_job_params_instance.to_dict()
# create an instance of ImageJobParams from a dict
image_job_params_form_dict = image_job_params.from_dict(image_job_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


