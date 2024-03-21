# ModuleHandle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**md_stream_version** | **int** |  | [optional] [readonly] 

## Example

```python
from civitai.models.module_handle import ModuleHandle

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleHandle from a JSON string
module_handle_instance = ModuleHandle.from_json(json)
# print the JSON string representation of the object
print(ModuleHandle.to_json())

# convert the object into a dict
module_handle_dict = module_handle_instance.to_dict()
# create an instance of ModuleHandle from a dict
module_handle_form_dict = module_handle.from_dict(module_handle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


