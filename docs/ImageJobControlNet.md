# ImageJobControlNet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preprocessor** | [**ImageTransformer**](ImageTransformer.md) |  | [optional] 
**weight** | **float** |  | [optional] 
**start_step** | **float** |  | [optional] 
**end_step** | **float** |  | [optional] 
**blob_key** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 

## Example

```python
from civitai.models.image_job_control_net import ImageJobControlNet

# TODO update the JSON string below
json = "{}"
# create an instance of ImageJobControlNet from a JSON string
image_job_control_net_instance = ImageJobControlNet.from_json(json)
# print the JSON string representation of the object
print(ImageJobControlNet.to_json())

# convert the object into a dict
image_job_control_net_dict = image_job_control_net_instance.to_dict()
# create an instance of ImageJobControlNet from a dict
image_job_control_net_form_dict = image_job_control_net.from_dict(image_job_control_net_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


