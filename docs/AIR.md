# AIR


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**legacy_id** | **str** |  | [optional] [readonly] 
**base_model** | [**BaseModel**](BaseModel.md) |  | [optional] 
**ecosystem** | [**ReadOnlySpan1**](ReadOnlySpan1.md) |  | [optional] 
**type** | [**ReadOnlySpan1**](ReadOnlySpan1.md) |  | [optional] 
**source** | [**ReadOnlySpan1**](ReadOnlySpan1.md) |  | [optional] 
**id** | [**ReadOnlySpan1**](ReadOnlySpan1.md) |  | [optional] 
**layer** | [**ReadOnlySpan1**](ReadOnlySpan1.md) |  | [optional] 
**format** | [**ReadOnlySpan1**](ReadOnlySpan1.md) |  | [optional] 

## Example

```python
from civitai.models.air import AIR

# TODO update the JSON string below
json = "{}"
# create an instance of AIR from a JSON string
air_instance = AIR.from_json(json)
# print the JSON string representation of the object
print(AIR.to_json())

# convert the object into a dict
air_dict = air_instance.to_dict()
# create an instance of AIR from a dict
air_form_dict = air.from_dict(air_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


