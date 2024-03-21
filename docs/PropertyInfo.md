# PropertyInfo


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
**property_type** | [**Type**](Type.md) |  | [optional] 
**attributes** | [**PropertyAttributes**](PropertyAttributes.md) |  | [optional] 
**is_special_name** | **bool** |  | [optional] [readonly] 
**can_read** | **bool** |  | [optional] [readonly] 
**can_write** | **bool** |  | [optional] [readonly] 
**get_method** | [**MethodInfo**](MethodInfo.md) |  | [optional] 
**set_method** | [**MethodInfo**](MethodInfo.md) |  | [optional] 

## Example

```python
from civitai.models.property_info import PropertyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyInfo from a JSON string
property_info_instance = PropertyInfo.from_json(json)
# print the JSON string representation of the object
print(PropertyInfo.to_json())

# convert the object into a dict
property_info_dict = property_info_instance.to_dict()
# create an instance of PropertyInfo from a dict
property_info_form_dict = property_info.from_dict(property_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


