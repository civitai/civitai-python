# PinBlobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Get or set the key of the blob to pin | [optional] 

## Example

```python
from civitai.models.pin_blob_request import PinBlobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PinBlobRequest from a JSON string
pin_blob_request_instance = PinBlobRequest.from_json(json)
# print the JSON string representation of the object
print(PinBlobRequest.to_json())

# convert the object into a dict
pin_blob_request_dict = pin_blob_request_instance.to_dict()
# create an instance of PinBlobRequest from a dict
pin_blob_request_form_dict = pin_blob_request.from_dict(pin_blob_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


