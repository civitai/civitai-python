# JobTemplateListJobsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | Get or set the model to prepare | 
**training_data** | **str** | A url referring data that needs to be trained upon | [optional] 
**params** | **Dict[str, object]** | A untyped set of parameters that are associated with this job | [optional] 
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
**key** | **str** | Get or set the key of the blob to pin | [optional] 
**replace** | **bool** | Get or set if existing blobs should be replaced. Otherwise the existing blob will be returned | [optional] 
**duration** | [**TimeSpan**](TimeSpan.md) |  | [optional] 
**image_url** | **str** | The url of the image to get embeddings for | [optional] 
**blob_key** | **str** | The key of the blob to transform | [optional] 
**transformer** | [**ImageTransformer**](ImageTransformer.md) |  | [optional] 
**destination_url** | **str** | Get or set the URL where the transformed image will be uploaded to | [optional] 
**job_id** | **str** | The ID of the original job to clear | [optional] 
**asset_name** | **str** | The name of the asset to copy | [optional] 
**destination_uri** | **str** | The destination URI to copy the asset to | [optional] 
**media_url** | **str** |  | 
**threshold** | **float** |  | [optional] 
**model_id** | **int** |  | 
**base_model** | [**BaseModel**](BaseModel.md) |  | [optional] 
**action** | [**PrepareModelAction**](PrepareModelAction.md) |  | [optional] 

## Example

```python
from civitai.models.job_template_list_jobs_inner import JobTemplateListJobsInner

# TODO update the JSON string below
json = "{}"
# create an instance of JobTemplateListJobsInner from a JSON string
job_template_list_jobs_inner_instance = JobTemplateListJobsInner.from_json(json)
# print the JSON string representation of the object
print(JobTemplateListJobsInner.to_json())

# convert the object into a dict
job_template_list_jobs_inner_dict = job_template_list_jobs_inner_instance.to_dict()
# create an instance of JobTemplateListJobsInner from a dict
job_template_list_jobs_inner_form_dict = job_template_list_jobs_inner.from_dict(job_template_list_jobs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


