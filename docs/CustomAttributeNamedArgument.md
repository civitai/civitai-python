# CustomAttributeNamedArgument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_info** | [**MemberInfo**](MemberInfo.md) |  | [optional] 
**typed_value** | [**CustomAttributeTypedArgument**](CustomAttributeTypedArgument.md) |  | [optional] 
**member_name** | **str** |  | [optional] [readonly] 
**is_field** | **bool** |  | [optional] [readonly] 

## Example

```python
from civitai.models.custom_attribute_named_argument import CustomAttributeNamedArgument

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttributeNamedArgument from a JSON string
custom_attribute_named_argument_instance = CustomAttributeNamedArgument.from_json(json)
# print the JSON string representation of the object
print(CustomAttributeNamedArgument.to_json())

# convert the object into a dict
custom_attribute_named_argument_dict = custom_attribute_named_argument_instance.to_dict()
# create an instance of CustomAttributeNamedArgument from a dict
custom_attribute_named_argument_form_dict = custom_attribute_named_argument.from_dict(custom_attribute_named_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


