# MethodInfo


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
**attributes** | [**MethodAttributes**](MethodAttributes.md) |  | [optional] 
**method_implementation_flags** | [**MethodImplAttributes**](MethodImplAttributes.md) |  | [optional] 
**calling_convention** | [**CallingConventions**](CallingConventions.md) |  | [optional] 
**is_abstract** | **bool** |  | [optional] [readonly] 
**is_constructor** | **bool** |  | [optional] [readonly] 
**is_final** | **bool** |  | [optional] [readonly] 
**is_hide_by_sig** | **bool** |  | [optional] [readonly] 
**is_special_name** | **bool** |  | [optional] [readonly] 
**is_static** | **bool** |  | [optional] [readonly] 
**is_virtual** | **bool** |  | [optional] [readonly] 
**is_assembly** | **bool** |  | [optional] [readonly] 
**is_family** | **bool** |  | [optional] [readonly] 
**is_family_and_assembly** | **bool** |  | [optional] [readonly] 
**is_family_or_assembly** | **bool** |  | [optional] [readonly] 
**is_private** | **bool** |  | [optional] [readonly] 
**is_public** | **bool** |  | [optional] [readonly] 
**is_constructed_generic_method** | **bool** |  | [optional] [readonly] 
**is_generic_method** | **bool** |  | [optional] [readonly] 
**is_generic_method_definition** | **bool** |  | [optional] [readonly] 
**contains_generic_parameters** | **bool** |  | [optional] [readonly] 
**method_handle** | [**RuntimeMethodHandle**](RuntimeMethodHandle.md) |  | [optional] 
**is_security_critical** | **bool** |  | [optional] [readonly] 
**is_security_safe_critical** | **bool** |  | [optional] [readonly] 
**is_security_transparent** | **bool** |  | [optional] [readonly] 
**member_type** | [**MemberTypes**](MemberTypes.md) |  | [optional] 
**return_parameter** | [**ParameterInfo**](ParameterInfo.md) |  | [optional] 
**return_type** | [**Type**](Type.md) |  | [optional] 
**return_type_custom_attributes** | **object** |  | [optional] 

## Example

```python
from civitai.models.method_info import MethodInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MethodInfo from a JSON string
method_info_instance = MethodInfo.from_json(json)
# print the JSON string representation of the object
print(MethodInfo.to_json())

# convert the object into a dict
method_info_dict = method_info_instance.to_dict()
# create an instance of MethodInfo from a dict
method_info_form_dict = method_info.from_dict(method_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


