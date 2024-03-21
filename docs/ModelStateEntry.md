# ModelStateEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw_value** | **object** |  | [optional] 
**attempted_value** | **str** |  | [optional] 
**errors** | [**List[ModelError]**](ModelError.md) |  | [optional] [readonly] 
**validation_state** | [**ModelValidationState**](ModelValidationState.md) |  | [optional] 
**is_container_node** | **bool** |  | [optional] [readonly] 
**children** | [**List[ModelStateEntry]**](ModelStateEntry.md) |  | [optional] [readonly] 

## Example

```python
from civitai.models.model_state_entry import ModelStateEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ModelStateEntry from a JSON string
model_state_entry_instance = ModelStateEntry.from_json(json)
# print the JSON string representation of the object
print(ModelStateEntry.to_json())

# convert the object into a dict
model_state_entry_dict = model_state_entry_instance.to_dict()
# create an instance of ModelStateEntry from a dict
model_state_entry_form_dict = model_state_entry.from_dict(model_state_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


