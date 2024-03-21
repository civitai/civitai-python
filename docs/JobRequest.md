# JobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** | Get or set the name of this job so that it can be referenced by other jobs | [optional] 
**priority** | [**JobRequestPriority**](JobRequestPriority.md) |  | [optional] 
**providers** | [**List[Provider]**](Provider.md) | Get or set a list of service providers to target with this job  If not specified then all providers will be targeted | [optional] 
**expire_at** | **datetime** | An optional expiration date for this job | [optional] 
**properties** | **Dict[str, Optional[object]]** | A dictionary of user defined properties that are associated with this job template | [optional] 
**callback_url** | **str** | Get or set a url that will be invoked upon completion of this job | [optional] 
**timeout** | [**TimeSpan**](TimeSpan.md) |  | [optional] 
**retries** | **int** | The max number of retries before we give up | [optional] 
**dependencies** | **List[str]** | Get or set a list of dependencies that this job has  These are the names of jobs that this job is dependent upon | [optional] 

## Example

```python
from civitai.models.job_request import JobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JobRequest from a JSON string
job_request_instance = JobRequest.from_json(json)
# print the JSON string representation of the object
print(JobRequest.to_json())

# convert the object into a dict
job_request_dict = job_request_instance.to_dict()
# create an instance of JobRequest from a dict
job_request_form_dict = job_request.from_dict(job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


