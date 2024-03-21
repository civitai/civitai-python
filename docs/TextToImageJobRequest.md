# TextToImageJobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **int** | Get or sets the number of images to generate | [optional] 
**model** | **str** | The AIR of the checkpoint model to use for generation | [optional] 
**additional_networks** | [**Dict[str, ImageJobNetworkParams]**](ImageJobNetworkParams.md) | Get or set a associative list of additional networks. Use the AIR of the network as the key. | [optional] 
**control_nets** | [**List[ImageJobControlNet]**](ImageJobControlNet.md) | Get or set a associative list of additional networks. | [optional] 
**params** | [**ImageJobParams**](ImageJobParams.md) |  | [optional] 

## Example

```python
from civitai.models.text_to_image_job_request import TextToImageJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TextToImageJobRequest from a JSON string
text_to_image_job_request_instance = TextToImageJobRequest.from_json(json)
# print the JSON string representation of the object
print(TextToImageJobRequest.to_json())

# convert the object into a dict
text_to_image_job_request_dict = text_to_image_job_request_instance.to_dict()
# create an instance of TextToImageJobRequest from a dict
text_to_image_job_request_form_dict = text_to_image_job_request.from_dict(text_to_image_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


