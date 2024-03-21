# ConsumptionDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**images** | **int** |  | [optional] 
**total_cost** | **float** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 

## Example

```python
from civitai.models.consumption_details import ConsumptionDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ConsumptionDetails from a JSON string
consumption_details_instance = ConsumptionDetails.from_json(json)
# print the JSON string representation of the object
print(ConsumptionDetails.to_json())

# convert the object into a dict
consumption_details_dict = consumption_details_instance.to_dict()
# create an instance of ConsumptionDetails from a dict
consumption_details_form_dict = consumption_details.from_dict(consumption_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


