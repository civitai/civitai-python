# FieldInfo


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
**attributes** | [**FieldAttributes**](FieldAttributes.md) |  | [optional] 
**field_type** | [**Type**](Type.md) |  | [optional] 
**is_init_only** | **bool** |  | [optional] [readonly] 
**is_literal** | **bool** |  | [optional] [readonly] 
**is_pinvoke_impl** | **bool** |  | [optional] [readonly] 
**is_special_name** | **bool** |  | [optional] [readonly] 
**is_static** | **bool** |  | [optional] [readonly] 
**is_assembly** | **bool** |  | [optional] [readonly] 
**is_family** | **bool** |  | [optional] [readonly] 
**is_family_and_assembly** | **bool** |  | [optional] [readonly] 
**is_family_or_assembly** | **bool** |  | [optional] [readonly] 
**is_private** | **bool** |  | [optional] [readonly] 
**is_public** | **bool** |  | [optional] [readonly] 
**is_security_critical** | **bool** |  | [optional] [readonly] 
**is_security_safe_critical** | **bool** |  | [optional] [readonly] 
**is_security_transparent** | **bool** |  | [optional] [readonly] 
**field_handle** | [**RuntimeFieldHandle**](RuntimeFieldHandle.md) |  | [optional] 

## Example

```python
from civitai.models.field_info import FieldInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FieldInfo from a JSON string
field_info_instance = FieldInfo.from_json(json)
# print the JSON string representation of the object
print(FieldInfo.to_json())

# convert the object into a dict
field_info_dict = field_info_instance.to_dict()
# create an instance of FieldInfo from a dict
field_info_form_dict = field_info.from_dict(field_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


