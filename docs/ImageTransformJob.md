# ImageTransformJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_url** | **str** | The url of the image to transform | [optional] 
**transformer** | [**ImageTransformer**](ImageTransformer.md) |  | [optional] 
**destination_blob_key** | **str** | Get the key of the destination blob to upload the result to | [optional] 
**params** | **Dict[str, object]** | A untyped set of parameters that are associated with this job | [optional] 
**destination_url** | **str** | Get or set the URL where the transformed image will be uploaded to | [optional] 
**cost** | **float** | Get cost associated with this job | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**id** | **str** | A unique id for this job | [optional] 
**created_at** | **datetime** | The date when this job got created | [optional] 
**expire_at** | **datetime** | The date for when this job was set to expire | [optional] 
**webhook** | **str** | A webhook to be invoked when the job receives a status update | [optional] 
**properties** | **Dict[str, object]** | A set of user defined properties that can be used to index and partition this job | [optional] 
**max_retry_attempt** | **int** | The max number of retries before we give up | [optional] 
**dependencies** | **List[str]** | Get or set a list of dependencies that this job has | [optional] 
**issued_by** | **str** | Get or set the name of the consumer that issued this job | [optional] 
**claim_duration** | [**TimeSpan**](TimeSpan.md) |  | [optional] 

## Example

```python
from civitai.models.image_transform_job import ImageTransformJob

# TODO update the JSON string below
json = "{}"
# create an instance of ImageTransformJob from a JSON string
image_transform_job_instance = ImageTransformJob.from_json(json)
# print the JSON string representation of the object
print(ImageTransformJob.to_json())

# convert the object into a dict
image_transform_job_dict = image_transform_job_instance.to_dict()
# create an instance of ImageTransformJob from a dict
image_transform_job_form_dict = image_transform_job.from_dict(image_transform_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


