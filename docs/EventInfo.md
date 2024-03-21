# EventInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] [readonly] 
**declaring_type** | [**Type**](Type.md) |  | [optional] 
**reflected_type** | [**Type**](Type.md) |  | [optional] 
**module** | [**Module**](Module.md) |  | [optional] 
**custom_attributes** | [**List[CustomAttributeData]**](CustomAttributeData.md) |  | [optional] [readonly] 
**is_collectible** | **bool** |  | [optional] [readonly] 
**metadata_token** | **int** |  | [optional] [readonly] 
**member_type** | [**MemberTypes**](MemberTypes.md) |  | [optional] 
**attributes** | [**EventAttributes**](EventAttributes.md) |  | [optional] 
**is_special_name** | **bool** |  | [optional] [readonly] 
**add_method** | [**MethodInfo**](MethodInfo.md) |  | [optional] 
**remove_method** | [**MethodInfo**](MethodInfo.md) |  | [optional] 
**raise_method** | [**MethodInfo**](MethodInfo.md) |  | [optional] 
**is_multicast** | **bool** |  | [optional] [readonly] 
**event_handler_type** | [**Type**](Type.md) |  | [optional] 

## Example

```python
from civitai.models.event_info import EventInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EventInfo from a JSON string
event_info_instance = EventInfo.from_json(json)
# print the JSON string representation of the object
print(EventInfo.to_json())

# convert the object into a dict
event_info_dict = event_info_instance.to_dict()
# create an instance of EventInfo from a dict
event_info_form_dict = event_info.from_dict(event_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


