# ImageJobNetworkParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AssetType**](AssetType.md) |  | [optional] 
**strength** | **float** | In case of Lora and LoCon, set the strength of the network | [optional] 
**trigger_word** | **str** | In case of a TextualInversion, set the trigger word of the network | [optional] 

## Example

```python
from civitai.models.image_job_network_params import ImageJobNetworkParams

# TODO update the JSON string below
json = "{}"
# create an instance of ImageJobNetworkParams from a JSON string
image_job_network_params_instance = ImageJobNetworkParams.from_json(json)
# print the JSON string representation of the object
print(ImageJobNetworkParams.to_json())

# convert the object into a dict
image_job_network_params_dict = image_job_network_params_instance.to_dict()
# create an instance of ImageJobNetworkParams from a dict
image_job_network_params_form_dict = image_job_network_params.from_dict(image_job_network_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


