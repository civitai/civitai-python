# FixedPriority

A fixed priority with a single value

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** |  | [optional] 

## Example

```python
from civitai.models.fixed_priority import FixedPriority

# TODO update the JSON string below
json = "{}"
# create an instance of FixedPriority from a JSON string
fixed_priority_instance = FixedPriority.from_json(json)
# print the JSON string representation of the object
print(FixedPriority.to_json())

# convert the object into a dict
fixed_priority_dict = fixed_priority_instance.to_dict()
# create an instance of FixedPriority from a dict
fixed_priority_form_dict = fixed_priority.from_dict(fixed_priority_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


