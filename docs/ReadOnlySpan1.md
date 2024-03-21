# ReadOnlySpan1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**length** | **int** |  | [optional] [readonly] 
**is_empty** | **bool** |  | [optional] [readonly] 

## Example

```python
from civitai.models.read_only_span1 import ReadOnlySpan1

# TODO update the JSON string below
json = "{}"
# create an instance of ReadOnlySpan1 from a JSON string
read_only_span1_instance = ReadOnlySpan1.from_json(json)
# print the JSON string representation of the object
print(ReadOnlySpan1.to_json())

# convert the object into a dict
read_only_span1_dict = read_only_span1_instance.to_dict()
# create an instance of ReadOnlySpan1 from a dict
read_only_span1_form_dict = read_only_span1.from_dict(read_only_span1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


