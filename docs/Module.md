# Module


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assembly** | [**Assembly**](Assembly.md) |  | [optional] 
**fully_qualified_name** | **str** |  | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 
**md_stream_version** | **int** |  | [optional] [readonly] 
**module_version_id** | **str** |  | [optional] [readonly] 
**scope_name** | **str** |  | [optional] [readonly] 
**module_handle** | [**ModuleHandle**](ModuleHandle.md) |  | [optional] 
**custom_attributes** | [**List[CustomAttributeData]**](CustomAttributeData.md) |  | [optional] [readonly] 
**metadata_token** | **int** |  | [optional] [readonly] 

## Example

```python
from civitai.models.module import Module

# TODO update the JSON string below
json = "{}"
# create an instance of Module from a JSON string
module_instance = Module.from_json(json)
# print the JSON string representation of the object
print(Module.to_json())

# convert the object into a dict
module_dict = module_instance.to_dict()
# create an instance of Module from a dict
module_form_dict = module.from_dict(module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


