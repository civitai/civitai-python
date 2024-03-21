# CopyAssetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | The ID of the original job to copy | [optional] 
**asset_name** | **str** | The name of the asset to copy | [optional] 
**destination_uri** | **str** | The destination URI to copy the asset to | [optional] 

## Example

```python
from civitai.models.copy_asset_request import CopyAssetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CopyAssetRequest from a JSON string
copy_asset_request_instance = CopyAssetRequest.from_json(json)
# print the JSON string representation of the object
print(CopyAssetRequest.to_json())

# convert the object into a dict
copy_asset_request_dict = copy_asset_request_instance.to_dict()
# create an instance of CopyAssetRequest from a dict
copy_asset_request_form_dict = copy_asset_request.from_dict(copy_asset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


