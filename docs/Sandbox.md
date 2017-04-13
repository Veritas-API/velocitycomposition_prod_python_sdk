# Sandbox

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_share_client_ips** | **list[str]** | A set of IP addresses of machines that are actively using this share. | [optional] 
**application_hosts** | [**list[ApplicationHostInfo]**](ApplicationHostInfo.md) | For automation releases, added a list of application hosts along with their URI&#39;s | [optional] 
**application_instance** | [**ApplicationInstance**](ApplicationInstance.md) |  | [optional] 
**copy_preparation** | **bool** | Flag which indicate Copy Preparation is enabled or not | [optional] 
**creation_time** | **int** | Sandbox creation time | 
**description** | **str** | Short description of the sandbox | [optional] 
**expiry_time** | **int** | Sandbox expiry time | 
**id** | **str** | A unique identifier of the sandbox object | 
**mounts** | [**list[Mount]**](Mount.md) |  | [optional] 
**name** | **str** | Name of the sandbox | 
**owner** | [**User**](User.md) |  | [optional] 
**point_in_time_creation_time** | **int** | Time the point-in-time this sandbox is based on was created | 
**point_in_time_id** | **str** | Id of pointInTime for which this sandbox was created | 
**properties** | [**HashMapstringobject**](HashMapstringobject.md) | Sandbox properties. To be used for any type specific sandbox properties | [optional] 
**sandbox_config** | [**SandboxConfig**](SandboxConfig.md) |  | [optional] 
**share_location** | [**ShareLocation**](ShareLocation.md) |  | [optional] 
**shares_op_state_update_batch_time** | **int** |  | [optional] 
**state** | **str** | Current state of the sandbox | 
**status_info** | [**StatusInfo**](StatusInfo.md) | More info about the state of the share and why it is in the state it is in | [optional] 
**storage_server_id** | **str** | A unique identifier of the storage server hosting the sandbox | 
**storage_server_record_id** | **str** | storage server supplied unique recordId for this sandbox | 
**target_hosts** | **list[str]** | a list of application hosts for the sandbox | [optional] 
**type** | **str** | The type of sandbox. | 
**workload_id** | **str** | Id of workload for which this sandbox was created | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


