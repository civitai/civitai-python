# Assembly


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defined_types** | [**List[TypeInfo]**](TypeInfo.md) |  | [optional] [readonly] 
**exported_types** | [**List[Type]**](Type.md) |  | [optional] [readonly] 
**entry_point** | [**MethodInfo**](MethodInfo.md) |  | [optional] 
**full_name** | **str** |  | [optional] [readonly] 
**image_runtime_version** | **str** |  | [optional] [readonly] 
**is_dynamic** | **bool** |  | [optional] [readonly] 
**location** | **str** |  | [optional] [readonly] 
**reflection_only** | **bool** |  | [optional] [readonly] 
**is_collectible** | **bool** |  | [optional] [readonly] 
**is_fully_trusted** | **bool** |  | [optional] [readonly] 
**custom_attributes** | [**List[CustomAttributeData]**](CustomAttributeData.md) |  | [optional] [readonly] 
**manifest_module** | [**Module**](Module.md) |  | [optional] 
**modules** | [**List[Module]**](Module.md) |  | [optional] [readonly] 
**host_context** | **int** |  | [optional] [readonly] 
**security_rule_set** | [**SecurityRuleSet**](SecurityRuleSet.md) |  | [optional] 

## Example

```python
from civitai.models.assembly import Assembly

# TODO update the JSON string below
json = "{}"
# create an instance of Assembly from a JSON string
assembly_instance = Assembly.from_json(json)
# print the JSON string representation of the object
print(Assembly.to_json())

# convert the object into a dict
assembly_dict = assembly_instance.to_dict()
# create an instance of Assembly from a dict
assembly_form_dict = assembly.from_dict(assembly_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


