# JobStatusCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | A token that can be used to get a status update on all the jobs in the collection | [optional] 
**jobs** | [**List[JobStatus]**](JobStatus.md) | A list of individual statuses for each generated job | [optional] 

## Example

```python
from civitai.models.job_status_collection import JobStatusCollection

# TODO update the JSON string below
json = "{}"
# create an instance of JobStatusCollection from a JSON string
job_status_collection_instance = JobStatusCollection.from_json(json)
# print the JSON string representation of the object
print(JobStatusCollection.to_json())

# convert the object into a dict
job_status_collection_dict = job_status_collection_instance.to_dict()
# create an instance of JobStatusCollection from a dict
job_status_collection_form_dict = job_status_collection.from_dict(job_status_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


