# Keeping fal API Secrets Safe | fal.ai Docs


> Learn how to use fal's queue system for handling long-running AI requests, including adding, monitoring, and canceling requests efficiently.


# Keeping fal API Secrets Safe

For requests that take longer than several seconds, as it is usually the case with AI applications, we have built a queue system.

Utilizing our queue system offers you a more granulated control to handle unexpected surges in traffic. It further provides you with the capability to cancel requests if needed and grants you the observability to monitor your current position within the queue. Besides that using the queue system spares you from the headache of keeping around long running https requests.

### Queue endpoints

You can interact with all queue features through a set of endpoints added to you function URL via thequeuesubdomain. The endpoints are as follows:

For instance, should you want to use the curl command to submit a request to the aforementioned endpoint and add it to the queue, your command would appear as follows:

```
Terminal windowcurl-XPOSThttps://queue.fal.run/fal-ai/fast-sdxl\-H"Authorization: Key$FAL_KEY"\-d'{"prompt": "a cat"}'
```

```
curl-XPOSThttps://queue.fal.run/fal-ai/fast-sdxl\-H"Authorization: Key$FAL_KEY"\-d'{"prompt": "a cat"}'
```

```
curl-XPOSThttps://queue.fal.run/fal-ai/fast-sdxl\
```

```
-H"Authorization: Key$FAL_KEY"\
```

```
-d'{"prompt": "a cat"}'
```

Here’s an example of a response with therequest_id:

```
{"request_id":"80e732af-660e-45cd-bd63-580e4f2a94cc","response_url":"https://queue.fal.run/fal-ai/fast-sdxl/requests/80e732af-660e-45cd-bd63-580e4f2a94cc","status_url":"https://queue.fal.run/fal-ai/fast-sdxl/requests/80e732af-660e-45cd-bd63-580e4f2a94cc/status","cancel_url":"https://queue.fal.run/fal-ai/fast-sdxl/requests/80e732af-660e-45cd-bd63-580e4f2a94cc/cancel"}
```

```
{"request_id":"80e732af-660e-45cd-bd63-580e4f2a94cc","response_url":"https://queue.fal.run/fal-ai/fast-sdxl/requests/80e732af-660e-45cd-bd63-580e4f2a94cc","status_url":"https://queue.fal.run/fal-ai/fast-sdxl/requests/80e732af-660e-45cd-bd63-580e4f2a94cc/status","cancel_url":"https://queue.fal.run/fal-ai/fast-sdxl/requests/80e732af-660e-45cd-bd63-580e4f2a94cc/cancel"}
```

```
{
```

```
"request_id":"80e732af-660e-45cd-bd63-580e4f2a94cc",
```

```
"response_url":"https://queue.fal.run/fal-ai/fast-sdxl/requests/80e732af-660e-45cd-bd63-580e4f2a94cc",
```

```
"status_url":"https://queue.fal.run/fal-ai/fast-sdxl/requests/80e732af-660e-45cd-bd63-580e4f2a94cc/status",
```

```
"cancel_url":"https://queue.fal.run/fal-ai/fast-sdxl/requests/80e732af-660e-45cd-bd63-580e4f2a94cc/cancel"
```

```
}
```

The payload helps you to keep track of your request with therequest_id, and provides you with the necessary information to get the status of your request, cancel it or get the response once it’s ready, so you don’t have to build these endpoints yourself.

### Request status

Once you have the request id you may use this request id to get the status of the request. This endpoint will give you information about your request’s status, it’s position in the queue or the response itself if the response is ready.

```
Terminal windowcurl-XGEThttps://queue.fal.run/fal-ai/fast-sdxl/requests/{request_id}/status
```

```
curl-XGEThttps://queue.fal.run/fal-ai/fast-sdxl/requests/{request_id}/status
```

```
curl-XGEThttps://queue.fal.run/fal-ai/fast-sdxl/requests/{request_id}/status
```

Here’s an example of a response with theIN_QUEUEstatus:

```
{"status":"IN_QUEUE","queue_position":0,"response_url":"https://queue.fal.run/fal-ai/fast-sdxl/requests/80e732af-660e-45cd-bd63-580e4f2a94cc"}
```

```
{"status":"IN_QUEUE","queue_position":0,"response_url":"https://queue.fal.run/fal-ai/fast-sdxl/requests/80e732af-660e-45cd-bd63-580e4f2a94cc"}
```

```
{
```

```
"status":"IN_QUEUE",
```

```
"queue_position":0,
```

```
"response_url":"https://queue.fal.run/fal-ai/fast-sdxl/requests/80e732af-660e-45cd-bd63-580e4f2a94cc"
```

```
}
```

#### Status types

Queuestatuscan have one of the following types and their respective properties:

- IN_QUEUE:queue_position: The current position of the task in the queue.response_url: The URL where the response will be available once the task is processed.

- IN_PROGRESS:logs: An array of logs related to the request. Note that it needs to be enabled, as explained in the previous section.response_url: The URL where the response will be available.

- COMPLETED:logs: An array of logs related to the request. Note that it needs to be enabled, as explained in the previous section.response_url: The URL where the response is available.

IN_QUEUE:

- queue_position: The current position of the task in the queue.

- response_url: The URL where the response will be available once the task is processed.

IN_PROGRESS:

- logs: An array of logs related to the request. Note that it needs to be enabled, as explained in the previous section.

- response_url: The URL where the response will be available.

COMPLETED:

- logs: An array of logs related to the request. Note that it needs to be enabled, as explained in the previous section.

- response_url: The URL where the response is available.

#### Logs

Logs are disabled by default. In order to enable logs for your request, you need to send thelogs=1query parameter when getting the status of your request. For example:

```
Terminal windowcurl-XGEThttps://queue.fal.run/fal-ai/fast-sdxl/requests/{request_id}/status?logs=1
```

```
curl-XGEThttps://queue.fal.run/fal-ai/fast-sdxl/requests/{request_id}/status?logs=1
```

```
curl-XGEThttps://queue.fal.run/fal-ai/fast-sdxl/requests/{request_id}/status?logs=1
```

When enabled, thelogsattribute in the queue status contains an array of log entries, each represented by theRequestLogtype. ARequestLogobject has the following attributes:

- message: a string containing the log message.

- level: the severity of the log, it can be one of the following:STDERR|STDOUT|ERROR|INFO|WARN|DEBUG

- source: indicates the source of the log.

- timestamp: a string representing the time when the log was generated.

- STDERR|STDOUT|ERROR|INFO|WARN|DEBUG

These logs offer valuable insights into the status and progress of your queued tasks, facilitating effective monitoring and debugging.

### Cancelling a request

If your request is still in the queue and not already being processed you may still cancel it.

```
Terminal windowcurl-XPUThttps://queue.fal.run/fal-ai/fast-sdxl/requests/{request_id}/cancel
```

```
curl-XPUThttps://queue.fal.run/fal-ai/fast-sdxl/requests/{request_id}/cancel
```

```
curl-XPUThttps://queue.fal.run/fal-ai/fast-sdxl/requests/{request_id}/cancel
```

### Getting the response

Once you get theCOMPLETEDstatus, theresponsewill be available along with itslogs.

```
Terminal windowcurl-XGEThttps://queue.fal.run/fal-ai/fast-sdxl/requests/{request_id}
```

```
curl-XGEThttps://queue.fal.run/fal-ai/fast-sdxl/requests/{request_id}
```

```
curl-XGEThttps://queue.fal.run/fal-ai/fast-sdxl/requests/{request_id}
```

Here’s an example of a response with theCOMPLETEDstatus:

```
{"status":"COMPLETED","logs": [{"message":"2020-05-04 14:00:00.000000","level":"INFO","source":"stdout","timestamp":"2020-05-04T14:00:00.000000Z"}],"response": {"message":"Hello World!"}}
```

```
{"status":"COMPLETED","logs": [{"message":"2020-05-04 14:00:00.000000","level":"INFO","source":"stdout","timestamp":"2020-05-04T14:00:00.000000Z"}],"response": {"message":"Hello World!"}}
```

```
{
```

```
"status":"COMPLETED",
```

```
"logs": [
```

```
{
```

```
"message":"2020-05-04 14:00:00.000000",
```

```
"level":"INFO",
```

```
"source":"stdout",
```

```
"timestamp":"2020-05-04T14:00:00.000000Z"
```

```
}
```

```
],
```

```
"response": {
```

```
"message":"Hello World!"
```

```
}
```

```
}
```

A simple queue recipe

Submit your request and let our client handle the status tracking for you. The next section details how the fal client simplifies building apps with fal functions.