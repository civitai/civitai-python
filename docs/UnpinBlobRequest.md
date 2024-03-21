# UnpinBlobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Get or set the key of the blob to pin | [optional] 

## Example

```python
from civitai.models.unpin_blob_request import UnpinBlobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnpinBlobRequest from a JSON string
unpin_blob_request_instance = UnpinBlobRequest.from_json(json)
# print the JSON string representation of the object
print(UnpinBlobRequest.to_json())

# convert the object into a dict
unpin_blob_request_dict = unpin_blob_request_instance.to_dict()
# create an instance of UnpinBlobRequest from a dict
unpin_blob_request_form_dict = unpin_blob_request.from_dict(unpin_blob_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


