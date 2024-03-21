# MediaTaggingJobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_id** | **int** |  | 
**media_url** | **str** |  | 

## Example

```python
from civitai.models.media_tagging_job_request import MediaTaggingJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MediaTaggingJobRequest from a JSON string
media_tagging_job_request_instance = MediaTaggingJobRequest.from_json(json)
# print the JSON string representation of the object
print(MediaTaggingJobRequest.to_json())

# convert the object into a dict
media_tagging_job_request_dict = media_tagging_job_request_instance.to_dict()
# create an instance of MediaTaggingJobRequest from a dict
media_tagging_job_request_form_dict = media_tagging_job_request.from_dict(media_tagging_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


