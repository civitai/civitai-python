# ProviderAssetAvailability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability** | [**WorkerAssetAvailability**](WorkerAssetAvailability.md) |  | [optional] 
**workers** | **int** |  | [optional] 

## Example

```python
from civitai.models.provider_asset_availability import ProviderAssetAvailability

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderAssetAvailability from a JSON string
provider_asset_availability_instance = ProviderAssetAvailability.from_json(json)
# print the JSON string representation of the object
print(ProviderAssetAvailability.to_json())

# convert the object into a dict
provider_asset_availability_dict = provider_asset_availability_instance.to_dict()
# create an instance of ProviderAssetAvailability from a dict
provider_asset_availability_form_dict = provider_asset_availability.from_dict(provider_asset_availability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


