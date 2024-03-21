# QueryJobsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **str** |  | [optional] 
**jobs** | [**List[JobStatus]**](JobStatus.md) |  | [optional] 

## Example

```python
from civitai.models.query_jobs_result import QueryJobsResult

# TODO update the JSON string below
json = "{}"
# create an instance of QueryJobsResult from a JSON string
query_jobs_result_instance = QueryJobsResult.from_json(json)
# print the JSON string representation of the object
print(QueryJobsResult.to_json())

# convert the object into a dict
query_jobs_result_dict = query_jobs_result_instance.to_dict()
# create an instance of QueryJobsResult from a dict
query_jobs_result_form_dict = query_jobs_result.from_dict(query_jobs_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


