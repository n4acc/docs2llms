# Client Library for Python | fal.ai Docs


> Learn how to integrate fal with your Python projects, including installation, calling endpoints, and managing requests with the fal client.


# Client Library for Python

## Introduction

The client for Python provides a seamless interface to interact with fal.

## Installation

First, add the client as a dependency in your project:

```
Terminal windowpipinstallfal-client
```

```
pipinstallfal-client
```

```
pipinstallfal-client
```

## Features

### 1. Call an endpoint

Endpoints requests are managed by a queue system. This allows fal to provide a reliable and scalable service.

Thesubscribemethod allows you to submit a request to the queue and wait for the result.

- Python

- Python (async)

```
importfal_clientdefon_queue_update(update):ifisinstance(update,fal_client.InProgress):forloginupdate.logs:print(log["message"])result=fal_client.subscribe("fal-ai/flux/dev",arguments={"prompt":"a cat","seed":6252023,"image_size":"landscape_4_3","num_images":4},with_logs=True,on_queue_update=on_queue_update,)print(result)
```

```
importfal_clientdefon_queue_update(update):ifisinstance(update,fal_client.InProgress):forloginupdate.logs:print(log["message"])result=fal_client.subscribe("fal-ai/flux/dev",arguments={"prompt":"a cat","seed":6252023,"image_size":"landscape_4_3","num_images":4},with_logs=True,on_queue_update=on_queue_update,)print(result)
```

```
importfal_client
```

```
defon_queue_update(update):
```

```
ifisinstance(update,fal_client.InProgress):
```

```
forloginupdate.logs:
```

```
print(log["message"])
```

```
result=fal_client.subscribe(
```

```
"fal-ai/flux/dev",
```

```
arguments={
```

```
"prompt":"a cat",
```

```
"seed":6252023,
```

```
"image_size":"landscape_4_3",
```

```
"num_images":4
```

```
},
```

```
with_logs=True,
```

```
on_queue_update=on_queue_update,
```

```
)
```

```
print(result)
```

```
importasyncioimportfal_clientasyncdefsubscribe():defon_queue_update(update):ifisinstance(update,fal_client.InProgress):forloginupdate.logs:print(log["message"])result=awaitfal_client.subscribe_async("fal-ai/flux/dev",arguments={"prompt":"a cat","seed":6252023,"image_size":"landscape_4_3","num_images":4},on_queue_update=on_queue_update,)print(result)if__name__=="__main__":asyncio.run(subscribe())
```

```
importasyncioimportfal_clientasyncdefsubscribe():defon_queue_update(update):ifisinstance(update,fal_client.InProgress):forloginupdate.logs:print(log["message"])result=awaitfal_client.subscribe_async("fal-ai/flux/dev",arguments={"prompt":"a cat","seed":6252023,"image_size":"landscape_4_3","num_images":4},on_queue_update=on_queue_update,)print(result)if__name__=="__main__":asyncio.run(subscribe())
```

```
importasyncio
```

```
importfal_client
```

```
asyncdefsubscribe():
```

```
defon_queue_update(update):
```

```
ifisinstance(update,fal_client.InProgress):
```

```
forloginupdate.logs:
```

```
print(log["message"])
```

```
result=awaitfal_client.subscribe_async(
```

```
"fal-ai/flux/dev",
```

```
arguments={
```

```
"prompt":"a cat",
```

```
"seed":6252023,
```

```
"image_size":"landscape_4_3",
```

```
"num_images":4
```

```
},
```

```
on_queue_update=on_queue_update,
```

```
)
```

```
print(result)
```

```
if__name__=="__main__":
```

```
asyncio.run(subscribe())
```

### 2. Queue Management

You can manage the queue using the following methods:

#### Submit a Request

Submit a request to the queue using thequeue.submitmethod.

- Python

- Python (async)

```
importfal_clienthandler=fal_client.submit("fal-ai/flux/dev",arguments={"prompt":"a cat","seed":6252023,"image_size":"landscape_4_3","num_images":4},)request_id=handler.request_id
```

```
importfal_clienthandler=fal_client.submit("fal-ai/flux/dev",arguments={"prompt":"a cat","seed":6252023,"image_size":"landscape_4_3","num_images":4},)request_id=handler.request_id
```

```
importfal_client
```

```
handler=fal_client.submit(
```

```
"fal-ai/flux/dev",
```

```
arguments={
```

```
"prompt":"a cat",
```

```
"seed":6252023,
```

```
"image_size":"landscape_4_3",
```

```
"num_images":4
```

```
},
```

```
)
```

```
request_id=handler.request_id
```

```
importasyncioimportfal_clientasyncdefsubmit():handler=awaitfal_client.submit_async("fal-ai/flux/dev",arguments={"prompt":"a cat","seed":6252023,"image_size":"landscape_4_3","num_images":4},)request_id=handler.request_idprint(request_id)
```

```
importasyncioimportfal_clientasyncdefsubmit():handler=awaitfal_client.submit_async("fal-ai/flux/dev",arguments={"prompt":"a cat","seed":6252023,"image_size":"landscape_4_3","num_images":4},)request_id=handler.request_idprint(request_id)
```

```
importasyncio
```

```
importfal_client
```

```
asyncdefsubmit():
```

```
handler=awaitfal_client.submit_async(
```

```
"fal-ai/flux/dev",
```

```
arguments={
```

```
"prompt":"a cat",
```

```
"seed":6252023,
```

```
"image_size":"landscape_4_3",
```

```
"num_images":4
```

```
},
```

```
)
```

```
request_id=handler.request_id
```

```
print(request_id)
```

This is useful when you want to submit a request to the queue and retrieve the result later. You can save therequest_idand use it to retrieve the result later.

Webhooks

For long-running requests, such astraining jobs, you can use webhooks to receive the result asynchronously. You can specify the webhook URL when submitting a request.

#### Check Request Status

Retrieve the status of a specific request in the queue:

- Python

- Python (async)

```
status=fal_client.status("fal-ai/flux/dev",request_id,with_logs=True)
```

```
status=fal_client.status("fal-ai/flux/dev",request_id,with_logs=True)
```

```
status=fal_client.status("fal-ai/flux/dev",request_id,with_logs=True)
```

```
status=awaitfal_client.status_async("fal-ai/flux/dev",request_id,with_logs=True)
```

```
status=awaitfal_client.status_async("fal-ai/flux/dev",request_id,with_logs=True)
```

```
status=awaitfal_client.status_async("fal-ai/flux/dev",request_id,with_logs=True)
```

#### Retrieve Request Result

Get the result of a specific request from the queue:

- Python

- Python (async)

```
result=fal_client.result("fal-ai/flux/dev",request_id)
```

```
result=fal_client.result("fal-ai/flux/dev",request_id)
```

```
result=fal_client.result("fal-ai/flux/dev",request_id)
```

```
result=awaitfal_client.result_async("fal-ai/flux/dev",request_id)
```

```
result=awaitfal_client.result_async("fal-ai/flux/dev",request_id)
```

```
result=awaitfal_client.result_async("fal-ai/flux/dev",request_id)
```

### 3. File Uploads

Some endpoints require files as input. However, since the endpoints run asynchronously, processed by the queue, you will need to provide URLs to the files instead of the actual file content.

Luckily, the client library provides a way to upload files to the server and get a URL to use in the request.

- Python

- Python (async)

```
url=fal_client.upload_file("path/to/file")
```

```
url=fal_client.upload_file("path/to/file")
```

```
url=fal_client.upload_file("path/to/file")
```

```
url=fal_client.upload_file_async("path/to/file")
```

```
url=fal_client.upload_file_async("path/to/file")
```

```
url=fal_client.upload_file_async("path/to/file")
```

### 4. Streaming

Some endpoints support streaming:

- Python

- Python (async)

```
importfal_clientdefstream():stream=fal_client.stream("fal-ai/flux/dev",arguments={"prompt":"a cat","seed":6252023,"image_size":"landscape_4_3","num_images":4},)foreventinstream:print(event)if__name__=="__main__":stream()
```

```
importfal_clientdefstream():stream=fal_client.stream("fal-ai/flux/dev",arguments={"prompt":"a cat","seed":6252023,"image_size":"landscape_4_3","num_images":4},)foreventinstream:print(event)if__name__=="__main__":stream()
```

```
importfal_client
```

```
defstream():
```

```
stream=fal_client.stream(
```

```
"fal-ai/flux/dev",
```

```
arguments={
```

```
"prompt":"a cat",
```

```
"seed":6252023,
```

```
"image_size":"landscape_4_3",
```

```
"num_images":4
```

```
},
```

```
)
```

```
foreventinstream:
```

```
print(event)
```

```
if__name__=="__main__":
```

```
stream()
```

```
importasyncioimportfal_clientasyncdefstream():stream=fal_client.stream_async("fal-ai/flux/dev",arguments={"prompt":"a cat","seed":6252023,"image_size":"landscape_4_3","num_images":4},)asyncforeventinstream:print(event)if__name__=="__main__":asyncio.run(stream())
```

```
importasyncioimportfal_clientasyncdefstream():stream=fal_client.stream_async("fal-ai/flux/dev",arguments={"prompt":"a cat","seed":6252023,"image_size":"landscape_4_3","num_images":4},)asyncforeventinstream:print(event)if__name__=="__main__":asyncio.run(stream())
```

```
importasyncio
```

```
importfal_client
```

```
asyncdefstream():
```

```
stream=fal_client.stream_async(
```

```
"fal-ai/flux/dev",
```

```
arguments={
```

```
"prompt":"a cat",
```

```
"seed":6252023,
```

```
"image_size":"landscape_4_3",
```

```
"num_images":4
```

```
},
```

```
)
```

```
asyncforeventinstream:
```

```
print(event)
```

```
if__name__=="__main__":
```

```
asyncio.run(stream())
```

### 5. Realtime Communication

For the endpoints that support real-time inference via WebSockets, you can use the realtime client that abstracts the WebSocket connection, re-connection, serialization, and provides a simple interface to interact with the endpoint:

- Python

- Python (async)

Not implemented yet

This functionality is not available on this client yet.

Not implemented yet

This functionality is not available on this client yet.

### 6. Run

The endpoints can also be called directly instead of using the queue system.

Prefer the queue

Wedo not recommendthis use most use cases as it will block the client
until the response is received. Moreover, if the connection is closed before
the response is received, the request will be lost.

- Python

- Python (async)

```
importfal_clientresult=fal_client.run("fal-ai/flux/dev",arguments={"prompt":"a cat","seed":6252023,"image_size":"landscape_4_3","num_images":4},)print(result)
```

```
importfal_clientresult=fal_client.run("fal-ai/flux/dev",arguments={"prompt":"a cat","seed":6252023,"image_size":"landscape_4_3","num_images":4},)print(result)
```

```
importfal_client
```

```
result=fal_client.run(
```

```
"fal-ai/flux/dev",
```

```
arguments={
```

```
"prompt":"a cat",
```

```
"seed":6252023,
```

```
"image_size":"landscape_4_3",
```

```
"num_images":4
```

```
},
```

```
)
```

```
print(result)
```

```
importasyncioimportfal_clientasyncdefsubmit():result=awaitfal_client.run_async("fal-ai/flux/dev",arguments={"prompt":"a cat","seed":6252023,"image_size":"landscape_4_3","num_images":4},)print(result)if__name__=="__main__":asyncio.run(submit())
```

```
importasyncioimportfal_clientasyncdefsubmit():result=awaitfal_client.run_async("fal-ai/flux/dev",arguments={"prompt":"a cat","seed":6252023,"image_size":"landscape_4_3","num_images":4},)print(result)if__name__=="__main__":asyncio.run(submit())
```

```
importasyncio
```

```
importfal_client
```

```
asyncdefsubmit():
```

```
result=awaitfal_client.run_async(
```

```
"fal-ai/flux/dev",
```

```
arguments={
```

```
"prompt":"a cat",
```

```
"seed":6252023,
```

```
"image_size":"landscape_4_3",
```

```
"num_images":4
```

```
},
```

```
)
```

```
print(result)
```

```
if__name__=="__main__":
```

```
asyncio.run(submit())
```

## API Reference

For a complete list of available methods and their parameters, please refer toPython API Reference documentation.

## Support

If you encounter any issues or have questions, please visit theGitHub repositoryor join ourDiscord Community.