# ClearAssetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | The ID of the original job to clear | [optional] 

## Example

```python
from civitai.models.clear_asset_request import ClearAssetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClearAssetRequest from a JSON string
clear_asset_request_instance = ClearAssetRequest.from_json(json)
# print the JSON string representation of the object
print(ClearAssetRequest.to_json())

# convert the object into a dict
clear_asset_request_dict = clear_asset_request_instance.to_dict()
# create an instance of ClearAssetRequest from a dict
clear_asset_request_form_dict = clear_asset_request.from_dict(clear_asset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


