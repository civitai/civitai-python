# TextToImageJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | [optional] 
**params** | [**ImageJobParams**](ImageJobParams.md) |  | [optional] 
**image_hash** | **str** |  | [optional] 
**additional_networks** | [**Dict[str, ImageJobNetworkParams]**](ImageJobNetworkParams.md) | Get or set a associative list of additional networks. Each network is identified by a hash code | [optional] 
**destination_url** | **str** | Get or set the URL where the image will be uploaded to | [optional] 
**base_model** | [**BaseModel**](BaseModel.md) |  | [optional] 
**store_as_blob** | **bool** | Wether to store the image as a blob or as a legacy image | [optional] 
**control_nets** | [**List[ImageJobControlNet]**](ImageJobControlNet.md) | Get or set a list of control nets that should be applied with this textToImage job | [optional] 
**cost** | **float** |  | [optional] [readonly] 
**claim_duration** | [**TimeSpan**](TimeSpan.md) |  | [optional] 
**type** | **str** |  | [optional] [readonly] 
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
from civitai.models.text_to_image_job import TextToImageJob

# TODO update the JSON string below
json = "{}"
# create an instance of TextToImageJob from a JSON string
text_to_image_job_instance = TextToImageJob.from_json(json)
# print the JSON string representation of the object
print(TextToImageJob.to_json())

# convert the object into a dict
text_to_image_job_dict = text_to_image_job_instance.to_dict()
# create an instance of TextToImageJob from a dict
text_to_image_job_form_dict = text_to_image_job.from_dict(text_to_image_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


