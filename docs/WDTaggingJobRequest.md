# WDTaggingJobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | 
**media_url** | **str** |  | 
**threshold** | **float** |  | [optional] 

## Example

```python
from civitai.models.wd_tagging_job_request import WDTaggingJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WDTaggingJobRequest from a JSON string
wd_tagging_job_request_instance = WDTaggingJobRequest.from_json(json)
# print the JSON string representation of the object
print(WDTaggingJobRequest.to_json())

# convert the object into a dict
wd_tagging_job_request_dict = wd_tagging_job_request_instance.to_dict()
# create an instance of WDTaggingJobRequest from a dict
wd_tagging_job_request_form_dict = wd_tagging_job_request.from_dict(wd_tagging_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


