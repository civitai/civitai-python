# civitai.JobsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_consumer_jobs_delete**](JobsApi.md#v1_consumer_jobs_delete) | **DELETE** /v1/consumer/jobs | Cancel all jobs associated with a token
[**v1_consumer_jobs_get**](JobsApi.md#v1_consumer_jobs_get) | **GET** /v1/consumer/jobs | Get the status of a previous submitted request by looking up the token
[**v1_consumer_jobs_job_id_delete**](JobsApi.md#v1_consumer_jobs_job_id_delete) | **DELETE** /v1/consumer/jobs/{jobId} | Cancels a specific job by looking it up by jobId
[**v1_consumer_jobs_job_id_get**](JobsApi.md#v1_consumer_jobs_job_id_get) | **GET** /v1/consumer/jobs/{jobId} | Get the status of a job by looking up the jobId
[**v1_consumer_jobs_job_id_put**](JobsApi.md#v1_consumer_jobs_job_id_put) | **PUT** /v1/consumer/jobs/{jobId} | Taint a specific job by its id
[**v1_consumer_jobs_post**](JobsApi.md#v1_consumer_jobs_post) | **POST** /v1/consumer/jobs | Submits a new job for processing
[**v1_consumer_jobs_put**](JobsApi.md#v1_consumer_jobs_put) | **PUT** /v1/consumer/jobs | Taint all jobs that match particular properties or belong to a token
[**v1_consumer_jobs_query_post**](JobsApi.md#v1_consumer_jobs_query_post) | **POST** /v1/consumer/jobs/query | Query for previously submitted jobs by looking up the properties


# **v1_consumer_jobs_delete**
> v1_consumer_jobs_delete(token, force=force)

Cancel all jobs associated with a token

### Example

* Api Key Authentication (ApiKey):

```python
import civitai
from civitai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = civitai.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with civitai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = civitai.JobsApi(api_client)
    token = 'token_example' # str | The token that was returned when requesting jobs
    force = True # bool | Force cancellation of jobs, even when jobs are currently being worked on (optional) (default to True)

    try:
        # Cancel all jobs associated with a token
        api_instance.v1_consumer_jobs_delete(token, force=force)
    except Exception as e:
        print("Exception when calling JobsApi->v1_consumer_jobs_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The token that was returned when requesting jobs | 
 **force** | **bool**| Force cancellation of jobs, even when jobs are currently being worked on | [optional] [default to True]

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_consumer_jobs_get**
> JobStatusCollection v1_consumer_jobs_get(token, wait=wait, detailed=detailed)

Get the status of a previous submitted request by looking up the token

### Example

* Api Key Authentication (ApiKey):

```python
import civitai
from civitai.models.job_status_collection import JobStatusCollection
from civitai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = civitai.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with civitai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = civitai.JobsApi(api_client)
    token = 'token_example' # str | The token that got returned as a result of submitting a requeset
    wait = True # bool | Whether to wait for the job to complete before returning or to return immediatly  The request may return a 202 if the clients waits for the job to complete and the job does not complete within the requested timeout.   In which case the client should use the token to query the status of the job. (optional)
    detailed = True # bool | Whether to include the job definition (optional)

    try:
        # Get the status of a previous submitted request by looking up the token
        api_response = api_instance.v1_consumer_jobs_get(token, wait=wait, detailed=detailed)
        print("The response of JobsApi->v1_consumer_jobs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->v1_consumer_jobs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The token that got returned as a result of submitting a requeset | 
 **wait** | **bool**| Whether to wait for the job to complete before returning or to return immediatly  The request may return a 202 if the clients waits for the job to complete and the job does not complete within the requested timeout.   In which case the client should use the token to query the status of the job. | [optional] 
 **detailed** | **bool**| Whether to include the job definition | [optional] 

### Return type

[**JobStatusCollection**](JobStatusCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**202** | Accepted |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_consumer_jobs_job_id_delete**
> v1_consumer_jobs_job_id_delete(job_id, force=force)

Cancels a specific job by looking it up by jobId

### Example

* Api Key Authentication (ApiKey):

```python
import civitai
from civitai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = civitai.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with civitai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = civitai.JobsApi(api_client)
    job_id = 'job_id_example' # str | The id of the job to cancel
    force = True # bool | Force cancellation, even when the job is currently being worked on (optional) (default to True)

    try:
        # Cancels a specific job by looking it up by jobId
        api_instance.v1_consumer_jobs_job_id_delete(job_id, force=force)
    except Exception as e:
        print("Exception when calling JobsApi->v1_consumer_jobs_job_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The id of the job to cancel | 
 **force** | **bool**| Force cancellation, even when the job is currently being worked on | [optional] [default to True]

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_consumer_jobs_job_id_get**
> JobStatusCollection v1_consumer_jobs_job_id_get(job_id, detailed=detailed)

Get the status of a job by looking up the jobId

### Example

* Api Key Authentication (ApiKey):

```python
import civitai
from civitai.models.job_status_collection import JobStatusCollection
from civitai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = civitai.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with civitai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = civitai.JobsApi(api_client)
    job_id = 'job_id_example' # str | 
    detailed = True # bool |  (optional)

    try:
        # Get the status of a job by looking up the jobId
        api_response = api_instance.v1_consumer_jobs_job_id_get(job_id, detailed=detailed)
        print("The response of JobsApi->v1_consumer_jobs_job_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->v1_consumer_jobs_job_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 
 **detailed** | **bool**|  | [optional] 

### Return type

[**JobStatusCollection**](JobStatusCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_consumer_jobs_job_id_put**
> v1_consumer_jobs_job_id_put(job_id, taint_job_request=taint_job_request)

Taint a specific job by its id

### Example

* Api Key Authentication (ApiKey):

```python
import civitai
from civitai.models.taint_job_request import TaintJobRequest
from civitai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = civitai.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with civitai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = civitai.JobsApi(api_client)
    job_id = 'job_id_example' # str | 
    taint_job_request = civitai.TaintJobRequest() # TaintJobRequest |  (optional)

    try:
        # Taint a specific job by its id
        api_instance.v1_consumer_jobs_job_id_put(job_id, taint_job_request=taint_job_request)
    except Exception as e:
        print("Exception when calling JobsApi->v1_consumer_jobs_job_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 
 **taint_job_request** | [**TaintJobRequest**](TaintJobRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_consumer_jobs_post**
> JobStatusCollection v1_consumer_jobs_post(wait=wait, detailed=detailed, job_template_list=job_template_list)

Submits a new job for processing

Sample request:                    POST /v1/consumer/jobs      {        \"$type\": \"textToImage\",        \"model\": \"urn:air:sdxl:model:civitai:4201@130072\",        \"params\": {            \"prompt\": \"A cat\",            \"negativePrompt\": \"A dog\",            \"scheduler\": \"EulerA\",            \"steps\": 30,            \"cfgScale\": 10,            \"width\": 1216,            \"height\": 832,            \"seed\": -1,            \"clipSkip\": 1        },        \"additionalNetworks\": {          \"civitai:58390@62833\": {            \"type\": \"Lora\",            \"strength\": 1          }        },        \"quantity\": 1,        \"priority\": {            \"min\": 2,            \"max\": 8        }      }

### Example

* Api Key Authentication (ApiKey):

```python
import civitai
from civitai.models.job_status_collection import JobStatusCollection
from civitai.models.job_template_list import JobTemplateList
from civitai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = civitai.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with civitai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = civitai.JobsApi(api_client)
    wait = True # bool | Whether to wait for the job to complete before returning or to return immediatly  The request may return a 202 if the clients waits for the job to complete and the job does not complete within the requested timeout.   In which case the client should use the token to query the status of the job. (optional)
    detailed = True # bool | Wether to include the job specification upon response (optional)
    job_template_list = {"quantity":1,"model":"urn:air:sdxl:model:civitai:101055@128078","additionalNetworks":{},"controlNets":[],"params":{"prompt":"A curious cat","negativePrompt":"Blurred","scheduler":"LMS","steps":30,"cfgScale":10,"width":1216,"height":832,"seed":-1,"clipSkip":2},"priority":5,"providers":[]} # JobTemplateList |  (optional)

    try:
        # Submits a new job for processing
        api_response = api_instance.v1_consumer_jobs_post(wait=wait, detailed=detailed, job_template_list=job_template_list)
        print("The response of JobsApi->v1_consumer_jobs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->v1_consumer_jobs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wait** | **bool**| Whether to wait for the job to complete before returning or to return immediatly  The request may return a 202 if the clients waits for the job to complete and the job does not complete within the requested timeout.   In which case the client should use the token to query the status of the job. | [optional] 
 **detailed** | **bool**| Wether to include the job specification upon response | [optional] 
 **job_template_list** | [**JobTemplateList**](JobTemplateList.md)|  | [optional] 

### Return type

[**JobStatusCollection**](JobStatusCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_consumer_jobs_put**
> TaintJobsResult v1_consumer_jobs_put(token=token, taint_jobs_request=taint_jobs_request)

Taint all jobs that match particular properties or belong to a token

### Example

* Api Key Authentication (ApiKey):

```python
import civitai
from civitai.models.taint_jobs_request import TaintJobsRequest
from civitai.models.taint_jobs_result import TaintJobsResult
from civitai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = civitai.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with civitai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = civitai.JobsApi(api_client)
    token = 'token_example' # str |  (optional)
    taint_jobs_request = civitai.TaintJobsRequest() # TaintJobsRequest |  (optional)

    try:
        # Taint all jobs that match particular properties or belong to a token
        api_response = api_instance.v1_consumer_jobs_put(token=token, taint_jobs_request=taint_jobs_request)
        print("The response of JobsApi->v1_consumer_jobs_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->v1_consumer_jobs_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | [optional] 
 **taint_jobs_request** | [**TaintJobsRequest**](TaintJobsRequest.md)|  | [optional] 

### Return type

[**TaintJobsResult**](TaintJobsResult.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_consumer_jobs_query_post**
> QueryJobsResult v1_consumer_jobs_query_post(detailed=detailed, query_jobs_request=query_jobs_request)

Query for previously submitted jobs by looking up the properties

### Example

* Api Key Authentication (ApiKey):

```python
import civitai
from civitai.models.query_jobs_request import QueryJobsRequest
from civitai.models.query_jobs_result import QueryJobsResult
from civitai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = civitai.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with civitai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = civitai.JobsApi(api_client)
    detailed = True # bool | Wether to include the original job definition (optional)
    query_jobs_request = civitai.QueryJobsRequest() # QueryJobsRequest |  (optional)

    try:
        # Query for previously submitted jobs by looking up the properties
        api_response = api_instance.v1_consumer_jobs_query_post(detailed=detailed, query_jobs_request=query_jobs_request)
        print("The response of JobsApi->v1_consumer_jobs_query_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->v1_consumer_jobs_query_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **detailed** | **bool**| Wether to include the original job definition | [optional] 
 **query_jobs_request** | [**QueryJobsRequest**](QueryJobsRequest.md)|  | [optional] 

### Return type

[**QueryJobsResult**](QueryJobsResult.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

