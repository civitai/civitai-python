# MemberInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_type** | [**MemberTypes**](MemberTypes.md) |  | [optional] 
**name** | **str** |  | [optional] [readonly] 
**declaring_type** | [**Type**](Type.md) |  | [optional] 
**reflected_type** | [**Type**](Type.md) |  | [optional] 
**module** | [**Module**](Module.md) |  | [optional] 
**custom_attributes** | [**List[CustomAttributeData]**](CustomAttributeData.md) |  | [optional] [readonly] 
**is_collectible** | **bool** |  | [optional] [readonly] 
**metadata_token** | **int** |  | [optional] [readonly] 

## Example

```python
from civitai.models.member_info import MemberInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MemberInfo from a JSON string
member_info_instance = MemberInfo.from_json(json)
# print the JSON string representation of the object
print(MemberInfo.to_json())

# convert the object into a dict
member_info_dict = member_info_instance.to_dict()
# create an instance of MemberInfo from a dict
member_info_form_dict = member_info.from_dict(member_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


