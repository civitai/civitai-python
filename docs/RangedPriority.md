# RangedPriority

A priority will be dynamically calculated between the min and max values.   The value will be calculated based on the number of recent requests that share the same properties.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **int** |  | [optional] 
**max** | **int** |  | [optional] 

## Example

```python
from civitai.models.ranged_priority import RangedPriority

# TODO update the JSON string below
json = "{}"
# create an instance of RangedPriority from a JSON string
ranged_priority_instance = RangedPriority.from_json(json)
# print the JSON string representation of the object
print(RangedPriority.to_json())

# convert the object into a dict
ranged_priority_dict = ranged_priority_instance.to_dict()
# create an instance of RangedPriority from a dict
ranged_priority_form_dict = ranged_priority.from_dict(ranged_priority_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


