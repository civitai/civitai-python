# ImageTransformJobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_url** | **str** | The url of the image to transform | [optional] 
**blob_key** | **str** | The key of the blob to transform | [optional] 
**replace** | **bool** | Get or set if existing blobs should be replaced. Otherwise the existing blob will be returned | [optional] 
**transformer** | [**ImageTransformer**](ImageTransformer.md) |  | [optional] 
**destination_url** | **str** | Get or set the URL where the transformed image will be uploaded to | [optional] 
**params** | **Dict[str, Optional[object]]** | A untyped set of parameters that are associated with this job | [optional] 

## Example

```python
from civitai.models.image_transform_job_request import ImageTransformJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImageTransformJobRequest from a JSON string
image_transform_job_request_instance = ImageTransformJobRequest.from_json(json)
# print the JSON string representation of the object
print(ImageTransformJobRequest.to_json())

# convert the object into a dict
image_transform_job_request_dict = image_transform_job_request_instance.to_dict()
# create an instance of ImageTransformJobRequest from a dict
image_transform_job_request_form_dict = image_transform_job_request.from_dict(image_transform_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


