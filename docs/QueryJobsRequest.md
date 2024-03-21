# QueryJobsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **str** |  | [optional] 
**properties** | **Dict[str, object]** |  | [optional] 

## Example

```python
from civitai.models.query_jobs_request import QueryJobsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QueryJobsRequest from a JSON string
query_jobs_request_instance = QueryJobsRequest.from_json(json)
# print the JSON string representation of the object
print(QueryJobsRequest.to_json())

# convert the object into a dict
query_jobs_request_dict = query_jobs_request_instance.to_dict()
# create an instance of QueryJobsRequest from a dict
query_jobs_request_form_dict = query_jobs_request.from_dict(query_jobs_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


