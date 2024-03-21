# ParameterInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ParameterAttributes**](ParameterAttributes.md) |  | [optional] 
**member** | [**MemberInfo**](MemberInfo.md) |  | [optional] 
**name** | **str** |  | [optional] [readonly] 
**parameter_type** | [**Type**](Type.md) |  | [optional] 
**position** | **int** |  | [optional] [readonly] 
**is_in** | **bool** |  | [optional] [readonly] 
**is_lcid** | **bool** |  | [optional] [readonly] 
**is_optional** | **bool** |  | [optional] [readonly] 
**is_out** | **bool** |  | [optional] [readonly] 
**is_retval** | **bool** |  | [optional] [readonly] 
**default_value** | **object** |  | [optional] [readonly] 
**raw_default_value** | **object** |  | [optional] [readonly] 
**has_default_value** | **bool** |  | [optional] [readonly] 
**custom_attributes** | [**List[CustomAttributeData]**](CustomAttributeData.md) |  | [optional] [readonly] 
**metadata_token** | **int** |  | [optional] [readonly] 

## Example

```python
from civitai.models.parameter_info import ParameterInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ParameterInfo from a JSON string
parameter_info_instance = ParameterInfo.from_json(json)
# print the JSON string representation of the object
print(ParameterInfo.to_json())

# convert the object into a dict
parameter_info_dict = parameter_info_instance.to_dict()
# create an instance of ParameterInfo from a dict
parameter_info_form_dict = parameter_info.from_dict(parameter_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


