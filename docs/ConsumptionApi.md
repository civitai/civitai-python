# civitai.ConsumptionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_consumer_consumption_get**](ConsumptionApi.md#v1_consumer_consumption_get) | **GET** /v1/consumer/consumption | 


# **v1_consumer_consumption_get**
> ConsumptionDetails v1_consumer_consumption_get(start_date=start_date, end_date=end_date)



### Example

* Api Key Authentication (ApiKey):

```python
import civitai
from civitai.models.consumption_details import ConsumptionDetails
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
    api_instance = civitai.ConsumptionApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        api_response = api_instance.v1_consumer_consumption_get(start_date=start_date, end_date=end_date)
        print("The response of ConsumptionApi->v1_consumer_consumption_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsumptionApi->v1_consumer_consumption_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 

### Return type

[**ConsumptionDetails**](ConsumptionDetails.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

