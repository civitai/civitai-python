# RuntimeFieldHandle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **object** |  | [optional] 

## Example

```python
from civitai.models.runtime_field_handle import RuntimeFieldHandle

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimeFieldHandle from a JSON string
runtime_field_handle_instance = RuntimeFieldHandle.from_json(json)
# print the JSON string representation of the object
print(RuntimeFieldHandle.to_json())

# convert the object into a dict
runtime_field_handle_dict = runtime_field_handle_instance.to_dict()
# create an instance of RuntimeFieldHandle from a dict
runtime_field_handle_form_dict = runtime_field_handle.from_dict(runtime_field_handle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


