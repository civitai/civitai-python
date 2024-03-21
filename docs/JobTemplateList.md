# JobTemplateList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobs** | [**List[JobTemplateListJobsInner]**](JobTemplateListJobsInner.md) |  | [optional] 

## Example

```python
from civitai.models.job_template_list import JobTemplateList

# TODO update the JSON string below
json = "{}"
# create an instance of JobTemplateList from a JSON string
job_template_list_instance = JobTemplateList.from_json(json)
# print the JSON string representation of the object
print(JobTemplateList.to_json())

# convert the object into a dict
job_template_list_dict = job_template_list_instance.to_dict()
# create an instance of JobTemplateList from a dict
job_template_list_form_dict = job_template_list.from_dict(job_template_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


