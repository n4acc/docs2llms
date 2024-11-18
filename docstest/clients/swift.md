# Client Library for Swift (iOS) | fal.ai Docs


> Learn how to integrate fal with your Swift (iOS) projects, including installation, calling endpoints, and managing requests with the fal client.


# Client Library for Swift (iOS)

## Introduction

The client for Swift (iOS) provides a seamless interface to interact with fal.

## Installation

First, add the client as a dependency in your project:

```
.package(url:"https://github.com/fal-ai/fal-swift.git",from:"0.5.6")
```

```
.package(url:"https://github.com/fal-ai/fal-swift.git",from:"0.5.6")
```

```
.package(url:"https://github.com/fal-ai/fal-swift.git",from:"0.5.6")
```

## Features

### 1. Call an endpoint

Endpoints requests are managed by a queue system. This allows fal to provide a reliable and scalable service.

Thesubscribemethod allows you to submit a request to the queue and wait for the result.

```
importFalClientletresult=tryawaitfal.subscribe(to:"fal-ai/flux/dev",input: ["prompt":"a cat","seed":6252023,"image_size":"landscape_4_3","num_images":4],includeLogs:true) { updateinifcaselet.inProgress(logs)=update {print(logs)}}
```

```
importFalClientletresult=tryawaitfal.subscribe(to:"fal-ai/flux/dev",input: ["prompt":"a cat","seed":6252023,"image_size":"landscape_4_3","num_images":4],includeLogs:true) { updateinifcaselet.inProgress(logs)=update {print(logs)}}
```

```
importFalClient
```

```
letresult=tryawaitfal.subscribe(
```

```
to:"fal-ai/flux/dev",
```

```
input: [
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
],
```

```
includeLogs:true
```

```
) { updatein
```

```
ifcaselet.inProgress(logs)=update {
```

```
print(logs)
```

```
}
```

```
}
```

### 2. Queue Management

You can manage the queue using the following methods:

#### Submit a Request

Submit a request to the queue using thequeue.submitmethod.

```
importFalClientletjob=tryawaitfal.queue.submit("fal-ai/flux/dev",input: ["prompt":"a cat","seed":6252023,"image_size":"landscape_4_3","num_images":4],webhookUrl:"https://optional.webhook.url/for/results")
```

```
importFalClientletjob=tryawaitfal.queue.submit("fal-ai/flux/dev",input: ["prompt":"a cat","seed":6252023,"image_size":"landscape_4_3","num_images":4],webhookUrl:"https://optional.webhook.url/for/results")
```

```
importFalClient
```

```
letjob=tryawaitfal.queue.submit(
```

```
"fal-ai/flux/dev",
```

```
input: [
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
],
```

```
webhookUrl:"https://optional.webhook.url/for/results"
```

```
)
```

This is useful when you want to submit a request to the queue and retrieve the result later. You can save therequest_idand use it to retrieve the result later.

Webhooks

For long-running requests, such astraining jobs, you can use webhooks to receive the result asynchronously. You can specify the webhook URL when submitting a request.

#### Check Request Status

Retrieve the status of a specific request in the queue:

```
importFalClientletstatus=tryawaitfal.queue.status("fal-ai/flux/dev",of:"764cabcf-b745-4b3e-ae38-1200304cf45b",includeLogs:true)
```

```
importFalClientletstatus=tryawaitfal.queue.status("fal-ai/flux/dev",of:"764cabcf-b745-4b3e-ae38-1200304cf45b",includeLogs:true)
```

```
importFalClient
```

```
letstatus=tryawaitfal.queue.status(
```

```
"fal-ai/flux/dev",
```

```
of:"764cabcf-b745-4b3e-ae38-1200304cf45b",
```

```
includeLogs:true
```

```
)
```

#### Retrieve Request Result

Get the result of a specific request from the queue:

```
importFalClientletresult=tryawaitfal.queue.response("fal-ai/flux/dev",of:"764cabcf-b745-4b3e-ae38-1200304cf45b")
```

```
importFalClientletresult=tryawaitfal.queue.response("fal-ai/flux/dev",of:"764cabcf-b745-4b3e-ae38-1200304cf45b")
```

```
importFalClient
```

```
letresult=tryawaitfal.queue.response(
```

```
"fal-ai/flux/dev",
```

```
of:"764cabcf-b745-4b3e-ae38-1200304cf45b"
```

```
)
```

### 3. File Uploads

Some endpoints require files as input. However, since the endpoints run asynchronously, processed by the queue, you will need to provide URLs to the files instead of the actual file content.

Luckily, the client library provides a way to upload files to the server and get a URL to use in the request.

```
importFalClientletdata=tryawaitData(contentsOf:URL(fileURLWithPath:"/path/to/file"))leturl=tryawaitfal.storage.upload(data)
```

```
importFalClientletdata=tryawaitData(contentsOf:URL(fileURLWithPath:"/path/to/file"))leturl=tryawaitfal.storage.upload(data)
```

```
importFalClient
```

```
letdata=tryawaitData(contentsOf:URL(fileURLWithPath:"/path/to/file"))
```

```
leturl=tryawaitfal.storage.upload(data)
```

### 4. Streaming

Some endpoints support streaming:

Not implemented yet

This functionality is not available on this client yet.

### 5. Realtime Communication

For the endpoints that support real-time inference via WebSockets, you can use the realtime client that abstracts the WebSocket connection, re-connection, serialization, and provides a simple interface to interact with the endpoint:

```
importFalClientletconnection=tryfal.realtime.connect(to:"fal-ai/flux/dev") { resultinswitchresult {caselet.success(data):print(data)caselet.failure(error):print(error)}}connection.send(["prompt":"a cat","seed":6252023,"image_size":"landscape_4_3","num_images":4])
```

```
importFalClientletconnection=tryfal.realtime.connect(to:"fal-ai/flux/dev") { resultinswitchresult {caselet.success(data):print(data)caselet.failure(error):print(error)}}connection.send(["prompt":"a cat","seed":6252023,"image_size":"landscape_4_3","num_images":4])
```

```
importFalClient
```

```
letconnection=tryfal.realtime.connect(to:"fal-ai/flux/dev") { resultin
```

```
switchresult {
```

```
caselet.success(data):
```

```
print(data)
```

```
caselet.failure(error):
```

```
print(error)
```

```
}
```

```
}
```

```
connection.send([
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
])
```

### 6. Run

The endpoints can also be called directly instead of using the queue system.

Prefer the queue

Wedo not recommendthis use most use cases as it will block the client
until the response is received. Moreover, if the connection is closed before
the response is received, the request will be lost.

```
importFalClientletresult=tryawaitfal.run("fal-ai/flux/dev",input: ["prompt":"a cat","seed":6252023,"image_size":"landscape_4_3","num_images":4])
```

```
importFalClientletresult=tryawaitfal.run("fal-ai/flux/dev",input: ["prompt":"a cat","seed":6252023,"image_size":"landscape_4_3","num_images":4])
```

```
importFalClient
```

```
letresult=tryawaitfal.run(
```

```
"fal-ai/flux/dev",
```

```
input: [
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
])
```

## API Reference

For a complete list of available methods and their parameters, please refer toSwift (iOS) API Reference documentation.

## Support

If you encounter any issues or have questions, please visit theGitHub repositoryor join ourDiscord Community.