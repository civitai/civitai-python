# ImageResourceTrainingJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | [optional] 
**training_data** | **str** | A url referring data that needs to be trained upon | [optional] 
**params** | **Dict[str, object]** | A untyped set of parameters that are associated with this job | [optional] 
**cost** | **float** | Get cost associated with this job | [optional] [readonly] 
**custom_cost** | **float** | Get or set a custom cost value for this job | [optional] 
**output** | **str** | An application provided output of the current status of this job | [optional] 
**type** | **str** |  | [optional] [readonly] 
**claim_duration** | [**TimeSpan**](TimeSpan.md) |  | [optional] 
**id** | **str** | A unique id for this job | [optional] 
**created_at** | **datetime** | The date when this job got created | [optional] 
**expire_at** | **datetime** | The date for when this job was set to expire | [optional] 
**webhook** | **str** | A webhook to be invoked when the job receives a status update | [optional] 
**properties** | **Dict[str, object]** | A set of user defined properties that can be used to index and partition this job | [optional] 
**max_retry_attempt** | **int** | The max number of retries before we give up | [optional] 
**dependencies** | **List[str]** | Get or set a list of dependencies that this job has | [optional] 
**issued_by** | **str** | Get or set the name of the consumer that issued this job | [optional] 

## Example

```python
from civitai.models.image_resource_training_job import ImageResourceTrainingJob

# TODO update the JSON string below
json = "{}"
# create an instance of ImageResourceTrainingJob from a JSON string
image_resource_training_job_instance = ImageResourceTrainingJob.from_json(json)
# print the JSON string representation of the object
print(ImageResourceTrainingJob.to_json())

# convert the object into a dict
image_resource_training_job_dict = image_resource_training_job_instance.to_dict()
# create an instance of ImageResourceTrainingJob from a dict
image_resource_training_job_form_dict = image_resource_training_job.from_dict(image_resource_training_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


