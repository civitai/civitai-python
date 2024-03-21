# TypeInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] [readonly] 
**custom_attributes** | [**List[CustomAttributeData]**](CustomAttributeData.md) |  | [optional] [readonly] 
**is_collectible** | **bool** |  | [optional] [readonly] 
**metadata_token** | **int** |  | [optional] [readonly] 
**is_interface** | **bool** |  | [optional] [readonly] 
**member_type** | [**MemberTypes**](MemberTypes.md) |  | [optional] 
**namespace** | **str** |  | [optional] [readonly] 
**assembly_qualified_name** | **str** |  | [optional] [readonly] 
**full_name** | **str** |  | [optional] [readonly] 
**assembly** | [**Assembly**](Assembly.md) |  | [optional] 
**module** | [**Module**](Module.md) |  | [optional] 
**is_nested** | **bool** |  | [optional] [readonly] 
**declaring_type** | [**Type**](Type.md) |  | [optional] 
**declaring_method** | [**MethodBase**](MethodBase.md) |  | [optional] 
**reflected_type** | [**Type**](Type.md) |  | [optional] 
**underlying_system_type** | [**Type**](Type.md) |  | [optional] 
**is_type_definition** | **bool** |  | [optional] [readonly] 
**is_array** | **bool** |  | [optional] [readonly] 
**is_by_ref** | **bool** |  | [optional] [readonly] 
**is_pointer** | **bool** |  | [optional] [readonly] 
**is_constructed_generic_type** | **bool** |  | [optional] [readonly] 
**is_generic_parameter** | **bool** |  | [optional] [readonly] 
**is_generic_type_parameter** | **bool** |  | [optional] [readonly] 
**is_generic_method_parameter** | **bool** |  | [optional] [readonly] 
**is_generic_type** | **bool** |  | [optional] [readonly] 
**is_generic_type_definition** | **bool** |  | [optional] [readonly] 
**is_sz_array** | **bool** |  | [optional] [readonly] 
**is_variable_bound_array** | **bool** |  | [optional] [readonly] 
**is_by_ref_like** | **bool** |  | [optional] [readonly] 
**is_function_pointer** | **bool** |  | [optional] [readonly] 
**is_unmanaged_function_pointer** | **bool** |  | [optional] [readonly] 
**has_element_type** | **bool** |  | [optional] [readonly] 
**generic_type_arguments** | [**List[Type]**](Type.md) |  | [optional] [readonly] 
**generic_parameter_position** | **int** |  | [optional] [readonly] 
**generic_parameter_attributes** | [**GenericParameterAttributes**](GenericParameterAttributes.md) |  | [optional] 
**attributes** | [**TypeAttributes**](TypeAttributes.md) |  | [optional] 
**is_abstract** | **bool** |  | [optional] [readonly] 
**is_import** | **bool** |  | [optional] [readonly] 
**is_sealed** | **bool** |  | [optional] [readonly] 
**is_special_name** | **bool** |  | [optional] [readonly] 
**is_class** | **bool** |  | [optional] [readonly] 
**is_nested_assembly** | **bool** |  | [optional] [readonly] 
**is_nested_fam_and_assem** | **bool** |  | [optional] [readonly] 
**is_nested_family** | **bool** |  | [optional] [readonly] 
**is_nested_fam_or_assem** | **bool** |  | [optional] [readonly] 
**is_nested_private** | **bool** |  | [optional] [readonly] 
**is_nested_public** | **bool** |  | [optional] [readonly] 
**is_not_public** | **bool** |  | [optional] [readonly] 
**is_public** | **bool** |  | [optional] [readonly] 
**is_auto_layout** | **bool** |  | [optional] [readonly] 
**is_explicit_layout** | **bool** |  | [optional] [readonly] 
**is_layout_sequential** | **bool** |  | [optional] [readonly] 
**is_ansi_class** | **bool** |  | [optional] [readonly] 
**is_auto_class** | **bool** |  | [optional] [readonly] 
**is_unicode_class** | **bool** |  | [optional] [readonly] 
**is_com_object** | **bool** |  | [optional] [readonly] 
**is_contextful** | **bool** |  | [optional] [readonly] 
**is_enum** | **bool** |  | [optional] [readonly] 
**is_marshal_by_ref** | **bool** |  | [optional] [readonly] 
**is_primitive** | **bool** |  | [optional] [readonly] 
**is_value_type** | **bool** |  | [optional] [readonly] 
**is_signature_type** | **bool** |  | [optional] [readonly] 
**is_security_critical** | **bool** |  | [optional] [readonly] 
**is_security_safe_critical** | **bool** |  | [optional] [readonly] 
**is_security_transparent** | **bool** |  | [optional] [readonly] 
**struct_layout_attribute** | [**StructLayoutAttribute**](StructLayoutAttribute.md) |  | [optional] 
**type_initializer** | [**ConstructorInfo**](ConstructorInfo.md) |  | [optional] 
**type_handle** | [**RuntimeTypeHandle**](RuntimeTypeHandle.md) |  | [optional] 
**guid** | **str** |  | [optional] [readonly] 
**base_type** | [**Type**](Type.md) |  | [optional] 
**contains_generic_parameters** | **bool** |  | [optional] [readonly] 
**is_visible** | **bool** |  | [optional] [readonly] 
**generic_type_parameters** | [**List[Type]**](Type.md) |  | [optional] [readonly] 
**declared_constructors** | [**List[ConstructorInfo]**](ConstructorInfo.md) |  | [optional] [readonly] 
**declared_events** | [**List[EventInfo]**](EventInfo.md) |  | [optional] [readonly] 
**declared_fields** | [**List[FieldInfo]**](FieldInfo.md) |  | [optional] [readonly] 
**declared_members** | [**List[MemberInfo]**](MemberInfo.md) |  | [optional] [readonly] 
**declared_methods** | [**List[MethodInfo]**](MethodInfo.md) |  | [optional] [readonly] 
**declared_nested_types** | [**List[TypeInfo]**](TypeInfo.md) |  | [optional] [readonly] 
**declared_properties** | [**List[PropertyInfo]**](PropertyInfo.md) |  | [optional] [readonly] 
**implemented_interfaces** | [**List[Type]**](Type.md) |  | [optional] [readonly] 

## Example

```python
from civitai.models.type_info import TypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TypeInfo from a JSON string
type_info_instance = TypeInfo.from_json(json)
# print the JSON string representation of the object
print(TypeInfo.to_json())

# convert the object into a dict
type_info_dict = type_info_instance.to_dict()
# create an instance of TypeInfo from a dict
type_info_form_dict = type_info.from_dict(type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


