# UploadBlobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Get or set the key of the blob to upload. If no key is specified then a new unique key will be generated | [optional] 
**replace** | **bool** | Get or set if existing blobs should be replaced | [optional] 
**duration** | [**TimeSpan**](TimeSpan.md) |  | [optional] 

## Example

```python
from civitai.models.upload_blob_request import UploadBlobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UploadBlobRequest from a JSON string
upload_blob_request_instance = UploadBlobRequest.from_json(json)
# print the JSON string representation of the object
print(UploadBlobRequest.to_json())

# convert the object into a dict
upload_blob_request_dict = upload_blob_request_instance.to_dict()
# create an instance of UploadBlobRequest from a dict
upload_blob_request_form_dict = upload_blob_request.from_dict(upload_blob_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


