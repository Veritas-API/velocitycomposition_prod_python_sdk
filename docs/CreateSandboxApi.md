# swagger_client.CreateSandboxApi

All URIs are relative to *https://veritas-prod-prod.apigee.net/velocity-sandbox/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sandbox**](CreateSandboxApi.md#create_sandbox) | **POST** /oraclesandbox | 


# **create_sandbox**
> Sandbox create_sandbox(velocity_token, body)



Create Velocity Template , PointinTime and  Sandbox

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CreateSandboxApi()
velocity_token = 'velocity_token_example' # str | Token received from Velocity Oauth API call
body = swagger_client.ComposedObject() # ComposedObject | ComposedObject

try: 
    # 
    api_response = api_instance.create_sandbox(velocity_token, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateSandboxApi->create_sandbox: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **velocity_token** | **str**| Token received from Velocity Oauth API call | 
 **body** | [**ComposedObject**](ComposedObject.md)| ComposedObject | 

### Return type

[**Sandbox**](Sandbox.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

