# ImageEmbeddingJobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_url** | **str** | The url of the image to get embeddings for | [optional] 

## Example

```python
from civitai.models.image_embedding_job_request import ImageEmbeddingJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImageEmbeddingJobRequest from a JSON string
image_embedding_job_request_instance = ImageEmbeddingJobRequest.from_json(json)
# print the JSON string representation of the object
print(ImageEmbeddingJobRequest.to_json())

# convert the object into a dict
image_embedding_job_request_dict = image_embedding_job_request_instance.to_dict()
# create an instance of ImageEmbeddingJobRequest from a dict
image_embedding_job_request_form_dict = image_embedding_job_request.from_dict(image_embedding_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


