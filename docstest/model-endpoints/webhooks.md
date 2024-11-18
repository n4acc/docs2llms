# Webhooks | fal.ai Docs


> Learn how to use webhooks with fal's queue system to receive notifications when requests are completed, enabling efficient asynchronous operations.


# Webhooks

Webhooks work in tandem with the queue system explained above, it is another way to interact with our queue. By providing us a webhook endpoint you get notified when the request is done as opposed to polling it.

Here is how this works in practice, it is very similar to submitting something to the queue but we require you to pass an extrafal_webhookquery parameter.

To utilize webhooks, your requests should be directed to thequeue.fal.runendpoint, instead of the standardfal.run. This distinction is crucial for enabling webhook functionality, as it ensures your request is handled by the queue system designed to support asynchronous operations and notifications.

```
Terminal windowcurl--requestPOST\--urlhttps://queue.fal.run/fal-ai/flux/dev\?fal_webhook\=https://url.to.your.app/api/fal/webhook\--header"Authorization: Key$FAL_KEY"\--header'Content-Type: application/json'\--data'{"prompt": "Photo of a cute dog"}'
```

```
curl--requestPOST\--urlhttps://queue.fal.run/fal-ai/flux/dev\?fal_webhook\=https://url.to.your.app/api/fal/webhook\--header"Authorization: Key$FAL_KEY"\--header'Content-Type: application/json'\--data'{"prompt": "Photo of a cute dog"}'
```

```
curl--requestPOST\
```

```
--urlhttps://queue.fal.run/fal-ai/flux/dev\?fal_webhook\=https://url.to.your.app/api/fal/webhook\
```

```
--header"Authorization: Key$FAL_KEY"\
```

```
--header'Content-Type: application/json'\
```

```
--data'{
```

```
"prompt": "Photo of a cute dog"
```

```
}'
```

The request will be queued and you will get a response with therequest_idandgateway_request_id:

```
{"request_id":"024ca5b1-45d3-4afd-883e-ad3abe2a1c4d","gateway_request_id":"024ca5b1-45d3-4afd-883e-ad3abe2a1c4d"}
```

```
{"request_id":"024ca5b1-45d3-4afd-883e-ad3abe2a1c4d","gateway_request_id":"024ca5b1-45d3-4afd-883e-ad3abe2a1c4d"}
```

```
{
```

```
"request_id":"024ca5b1-45d3-4afd-883e-ad3abe2a1c4d",
```

```
"gateway_request_id":"024ca5b1-45d3-4afd-883e-ad3abe2a1c4d"
```

```
}
```

These two will be mostly the same, but if the request failed and was retried,gateway_request_idwill have the value of the last tried request, whilerequest_idwill be the value used in the queue API.

Once the request is done processing in the queue, aPOSTrequest is made to the webhook URL, passing the request info and the resultingpayload. Thestatusindicates whether the request was successful or not.

When to use it?

Webhooks are particularly useful for requests that can take a while to process and/or the result is not needed immediately. For example, if you are training a model, which is a process than can take several minutes or even hours, webhooks could be the perfect tool for the job.

### Successful result

The following is an example of a successful request:

```
{"request_id":"123e4567-e89b-12d3-a456-426614174000","gateway_request_id":"123e4567-e89b-12d3-a456-426614174000","status":"OK","payload": {"images": [{"url":"https://url.to/image.png","content_type":"image/png","file_name":"image.png","file_size":1824075,"width":1024,"height":1024}],"seed":196619188014358660}}
```

```
{"request_id":"123e4567-e89b-12d3-a456-426614174000","gateway_request_id":"123e4567-e89b-12d3-a456-426614174000","status":"OK","payload": {"images": [{"url":"https://url.to/image.png","content_type":"image/png","file_name":"image.png","file_size":1824075,"width":1024,"height":1024}],"seed":196619188014358660}}
```

```
{
```

```
"request_id":"123e4567-e89b-12d3-a456-426614174000",
```

```
"gateway_request_id":"123e4567-e89b-12d3-a456-426614174000",
```

```
"status":"OK",
```

```
"payload": {
```

```
"images": [
```

```
{
```

```
"url":"https://url.to/image.png",
```

```
"content_type":"image/png",
```

```
"file_name":"image.png",
```

```
"file_size":1824075,
```

```
"width":1024,
```

```
"height":1024
```

```
}
```

```
],
```

```
"seed":196619188014358660
```

```
}
```

```
}
```

### Response errors

When an error happens, thestatuswill beERROR. Theerrorproperty will contain a message and thepayloadwill provide the error details. For example, if you forget to pass the requiredmodel_nameparameter, you will get the following response:

```
{"request_id":"123e4567-e89b-12d3-a456-426614174000","gateway_request_id":"123e4567-e89b-12d3-a456-426614174000","status":"ERROR","error":"Invalid status code: 422","payload": {"detail": [{"loc": ["body","prompt"],"msg":"field required","type":"value_error.missing"}]}}
```

```
{"request_id":"123e4567-e89b-12d3-a456-426614174000","gateway_request_id":"123e4567-e89b-12d3-a456-426614174000","status":"ERROR","error":"Invalid status code: 422","payload": {"detail": [{"loc": ["body","prompt"],"msg":"field required","type":"value_error.missing"}]}}
```

```
{
```

```
"request_id":"123e4567-e89b-12d3-a456-426614174000",
```

```
"gateway_request_id":"123e4567-e89b-12d3-a456-426614174000",
```

```
"status":"ERROR",
```

```
"error":"Invalid status code: 422",
```

```
"payload": {
```

```
"detail": [
```

```
{
```

```
"loc": ["body","prompt"],
```

```
"msg":"field required",
```

```
"type":"value_error.missing"
```

```
}
```

```
]
```

```
}
```

```
}
```

### Payload errors

For the webhook to include the payload, it must be valid JSON. So if there is an error serializing it,payloadis set tonulland apayload_errorwill include details about the error.

```
{"request_id":"123e4567-e89b-12d3-a456-426614174000","gateway_request_id":"123e4567-e89b-12d3-a456-426614174000","status":"OK","payload":null,"payload_error":"Response payload is not JSON serializable. Either return a JSON serializable object or use the queue endpoint to retrieve the response."}
```

```
{"request_id":"123e4567-e89b-12d3-a456-426614174000","gateway_request_id":"123e4567-e89b-12d3-a456-426614174000","status":"OK","payload":null,"payload_error":"Response payload is not JSON serializable. Either return a JSON serializable object or use the queue endpoint to retrieve the response."}
```

```
{
```

```
"request_id":"123e4567-e89b-12d3-a456-426614174000",
```

```
"gateway_request_id":"123e4567-e89b-12d3-a456-426614174000",
```

```
"status":"OK",
```

```
"payload":null,
```

```
"payload_error":"Response payload is not JSON serializable. Either return a JSON serializable object or use the queue endpoint to retrieve the response."
```

```
}
```