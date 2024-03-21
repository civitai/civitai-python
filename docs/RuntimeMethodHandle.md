# RuntimeMethodHandle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **object** |  | [optional] 

## Example

```python
from civitai.models.runtime_method_handle import RuntimeMethodHandle

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimeMethodHandle from a JSON string
runtime_method_handle_instance = RuntimeMethodHandle.from_json(json)
# print the JSON string representation of the object
print(RuntimeMethodHandle.to_json())

# convert the object into a dict
runtime_method_handle_dict = runtime_method_handle_instance.to_dict()
# create an instance of RuntimeMethodHandle from a dict
runtime_method_handle_form_dict = runtime_method_handle.from_dict(runtime_method_handle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


