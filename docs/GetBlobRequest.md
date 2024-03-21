# GetBlobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Get or set the key of the blob to upload | [optional] 
**duration** | [**TimeSpan**](TimeSpan.md) |  | [optional] 

## Example

```python
from civitai.models.get_blob_request import GetBlobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetBlobRequest from a JSON string
get_blob_request_instance = GetBlobRequest.from_json(json)
# print the JSON string representation of the object
print(GetBlobRequest.to_json())

# convert the object into a dict
get_blob_request_dict = get_blob_request_instance.to_dict()
# create an instance of GetBlobRequest from a dict
get_blob_request_form_dict = get_blob_request.from_dict(get_blob_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


