# RuntimeTypeHandle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **object** |  | [optional] 

## Example

```python
from civitai.models.runtime_type_handle import RuntimeTypeHandle

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimeTypeHandle from a JSON string
runtime_type_handle_instance = RuntimeTypeHandle.from_json(json)
# print the JSON string representation of the object
print(RuntimeTypeHandle.to_json())

# convert the object into a dict
runtime_type_handle_dict = runtime_type_handle_instance.to_dict()
# create an instance of RuntimeTypeHandle from a dict
runtime_type_handle_form_dict = runtime_type_handle.from_dict(runtime_type_handle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


