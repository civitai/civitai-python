# DeleteBlobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Get or set the key of the blob to pin | [optional] 

## Example

```python
from civitai.models.delete_blob_request import DeleteBlobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteBlobRequest from a JSON string
delete_blob_request_instance = DeleteBlobRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteBlobRequest.to_json())

# convert the object into a dict
delete_blob_request_dict = delete_blob_request_instance.to_dict()
# create an instance of DeleteBlobRequest from a dict
delete_blob_request_form_dict = delete_blob_request.from_dict(delete_blob_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


