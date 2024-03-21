# CustomAttributeData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_type** | [**Type**](Type.md) |  | [optional] 
**constructor** | [**ConstructorInfo**](ConstructorInfo.md) |  | [optional] 
**constructor_arguments** | [**List[CustomAttributeTypedArgument]**](CustomAttributeTypedArgument.md) |  | [optional] [readonly] 
**named_arguments** | [**List[CustomAttributeNamedArgument]**](CustomAttributeNamedArgument.md) |  | [optional] [readonly] 

## Example

```python
from civitai.models.custom_attribute_data import CustomAttributeData

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttributeData from a JSON string
custom_attribute_data_instance = CustomAttributeData.from_json(json)
# print the JSON string representation of the object
print(CustomAttributeData.to_json())

# convert the object into a dict
custom_attribute_data_dict = custom_attribute_data_instance.to_dict()
# create an instance of CustomAttributeData from a dict
custom_attribute_data_form_dict = custom_attribute_data.from_dict(custom_attribute_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


