# TimeSpan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticks** | **int** |  | [optional] 
**days** | **int** |  | [optional] [readonly] 
**hours** | **int** |  | [optional] [readonly] 
**milliseconds** | **int** |  | [optional] [readonly] 
**microseconds** | **int** |  | [optional] [readonly] 
**nanoseconds** | **int** |  | [optional] [readonly] 
**minutes** | **int** |  | [optional] [readonly] 
**seconds** | **int** |  | [optional] [readonly] 
**total_days** | **float** |  | [optional] [readonly] 
**total_hours** | **float** |  | [optional] [readonly] 
**total_milliseconds** | **float** |  | [optional] [readonly] 
**total_microseconds** | **float** |  | [optional] [readonly] 
**total_nanoseconds** | **float** |  | [optional] [readonly] 
**total_minutes** | **float** |  | [optional] [readonly] 
**total_seconds** | **float** |  | [optional] [readonly] 

## Example

```python
from civitai.models.time_span import TimeSpan

# TODO update the JSON string below
json = "{}"
# create an instance of TimeSpan from a JSON string
time_span_instance = TimeSpan.from_json(json)
# print the JSON string representation of the object
print(TimeSpan.to_json())

# convert the object into a dict
time_span_dict = time_span_instance.to_dict()
# create an instance of TimeSpan from a dict
time_span_form_dict = time_span.from_dict(time_span_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


