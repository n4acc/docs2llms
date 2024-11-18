# Client Library for Dart (Flutter) | fal.ai Docs


> Learn how to integrate fal with your Dart (Flutter) projects, including installation, calling endpoints, and managing requests with the fal client.


# Client Library for Dart (Flutter)

## Introduction

The client for Dart (Flutter) provides a seamless interface to interact with fal.

## Installation

First, add the client as a dependency in your project:

```
Terminal windowflutterpubaddfal_client
```

```
flutterpubaddfal_client
```

```
flutterpubaddfal_client
```

## Features

### 1. Call an endpoint

Endpoints requests are managed by a queue system. This allows fal to provide a reliable and scalable service.

Thesubscribemethod allows you to submit a request to the queue and wait for the result.

```
import'package:fal_client/fal_client.dart';finalfal=FalClient.withCredentials("FAL_KEY");finaloutput=awaitfal.subscribe("fal-ai/flux/dev",input:{"prompt":"a cat","seed":6252023,"image_size":"landscape_4_3","num_images":4},logs:true,webhookUrl:"https://optional.webhook.url/for/results",onQueueUpdate:(update) {print(update); });print(output.requestId);print(output.data);
```

```
import'package:fal_client/fal_client.dart';finalfal=FalClient.withCredentials("FAL_KEY");finaloutput=awaitfal.subscribe("fal-ai/flux/dev",input:{"prompt":"a cat","seed":6252023,"image_size":"landscape_4_3","num_images":4},logs:true,webhookUrl:"https://optional.webhook.url/for/results",onQueueUpdate:(update) {print(update); });print(output.requestId);print(output.data);
```

```
import'package:fal_client/fal_client.dart';
```

```
finalfal=FalClient.withCredentials("FAL_KEY");
```

```
finaloutput=awaitfal.subscribe("fal-ai/flux/dev",
```

```
input:{
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
logs:true,
```

```
webhookUrl:"https://optional.webhook.url/for/results",
```

```
onQueueUpdate:(update) {print(update); }
```

```
);
```

```
print(output.requestId);
```

```
print(output.data);
```

### 2. Queue Management

You can manage the queue using the following methods:

#### Submit a Request

Submit a request to the queue using thequeue.submitmethod.

```
import'package:fal_client/fal_client.dart';finalfal=FalClient.withCredentials("FAL_KEY");finaljob=awaitfal.queue.submit("fal-ai/flux/dev",input:{"prompt":"a cat","seed":6252023,"image_size":"landscape_4_3","num_images":4},webhookUrl:"https://optional.webhook.url/for/results");print(job.requestId);
```

```
import'package:fal_client/fal_client.dart';finalfal=FalClient.withCredentials("FAL_KEY");finaljob=awaitfal.queue.submit("fal-ai/flux/dev",input:{"prompt":"a cat","seed":6252023,"image_size":"landscape_4_3","num_images":4},webhookUrl:"https://optional.webhook.url/for/results");print(job.requestId);
```

```
import'package:fal_client/fal_client.dart';
```

```
finalfal=FalClient.withCredentials("FAL_KEY");
```

```
finaljob=awaitfal.queue.submit("fal-ai/flux/dev",
```

```
input:{
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
webhookUrl:"https://optional.webhook.url/for/results"
```

```
);
```

```
print(job.requestId);
```

This is useful when you want to submit a request to the queue and retrieve the result later. You can save therequest_idand use it to retrieve the result later.

Webhooks

For long-running requests, such astraining jobs, you can use webhooks to receive the result asynchronously. You can specify the webhook URL when submitting a request.

#### Check Request Status

Retrieve the status of a specific request in the queue:

```
import'package:fal_client/fal_client.dart';finalfal=FalClient.withCredentials("FAL_KEY");finaljob=awaitfal.queue.status("fal-ai/flux/dev",requestId:"764cabcf-b745-4b3e-ae38-1200304cf45b",logs:true);print(job.requestId);print(job.status);
```

```
import'package:fal_client/fal_client.dart';finalfal=FalClient.withCredentials("FAL_KEY");finaljob=awaitfal.queue.status("fal-ai/flux/dev",requestId:"764cabcf-b745-4b3e-ae38-1200304cf45b",logs:true);print(job.requestId);print(job.status);
```

```
import'package:fal_client/fal_client.dart';
```

```
finalfal=FalClient.withCredentials("FAL_KEY");
```

```
finaljob=awaitfal.queue.status("fal-ai/flux/dev",
```

```
requestId:"764cabcf-b745-4b3e-ae38-1200304cf45b",
```

```
logs:true
```

```
);
```

```
print(job.requestId);
```

```
print(job.status);
```

#### Retrieve Request Result

Get the result of a specific request from the queue:

```
import'package:fal_client/fal_client.dart';finalfal=FalClient.withCredentials("FAL_KEY");finaloutput=awaitfal.queue.result("fal-ai/flux/dev",requestId:"764cabcf-b745-4b3e-ae38-1200304cf45b");print(output.requestId);print(output.data);
```

```
import'package:fal_client/fal_client.dart';finalfal=FalClient.withCredentials("FAL_KEY");finaloutput=awaitfal.queue.result("fal-ai/flux/dev",requestId:"764cabcf-b745-4b3e-ae38-1200304cf45b");print(output.requestId);print(output.data);
```

```
import'package:fal_client/fal_client.dart';
```

```
finalfal=FalClient.withCredentials("FAL_KEY");
```

```
finaloutput=awaitfal.queue.result("fal-ai/flux/dev",
```

```
requestId:"764cabcf-b745-4b3e-ae38-1200304cf45b"
```

```
);
```

```
print(output.requestId);
```

```
print(output.data);
```

### 3. File Uploads

Some endpoints require files as input. However, since the endpoints run asynchronously, processed by the queue, you will need to provide URLs to the files instead of the actual file content.

Luckily, the client library provides a way to upload files to the server and get a URL to use in the request.

```
import'package:cross_file/cross_file.dart';import'package:fal_client/fal_client.dart';finalfal=FalClient.withCredentials("FAL_KEY");finalfile=XFile("path/to/file");finalurl=awaitfal.storage.upload(file);
```

```
import'package:cross_file/cross_file.dart';import'package:fal_client/fal_client.dart';finalfal=FalClient.withCredentials("FAL_KEY");finalfile=XFile("path/to/file");finalurl=awaitfal.storage.upload(file);
```

```
import'package:cross_file/cross_file.dart';
```

```
import'package:fal_client/fal_client.dart';
```

```
finalfal=FalClient.withCredentials("FAL_KEY");
```

```
finalfile=XFile("path/to/file");
```

```
finalurl=awaitfal.storage.upload(file);
```

### 4. Streaming

Some endpoints support streaming:

Not implemented yet

This functionality is not available on this client yet.

### 5. Realtime Communication

For the endpoints that support real-time inference via WebSockets, you can use the realtime client that abstracts the WebSocket connection, re-connection, serialization, and provides a simple interface to interact with the endpoint:

Not implemented yet

This functionality is not available on this client yet.

### 6. Run

The endpoints can also be called directly instead of using the queue system.

Prefer the queue

Wedo not recommendthis use most use cases as it will block the client
until the response is received. Moreover, if the connection is closed before
the response is received, the request will be lost.

```
import'package:fal_client/fal_client.dart';finalfal=FalClient.withCredentials("FAL_KEY");finaloutput=awaitfal.run("fal-ai/flux/dev",input:{"prompt":"a cat","seed":6252023,"image_size":"landscape_4_3","num_images":4});print(output.requestId);print(output.data);
```

```
import'package:fal_client/fal_client.dart';finalfal=FalClient.withCredentials("FAL_KEY");finaloutput=awaitfal.run("fal-ai/flux/dev",input:{"prompt":"a cat","seed":6252023,"image_size":"landscape_4_3","num_images":4});print(output.requestId);print(output.data);
```

```
import'package:fal_client/fal_client.dart';
```

```
finalfal=FalClient.withCredentials("FAL_KEY");
```

```
finaloutput=awaitfal.run("fal-ai/flux/dev",
```

```
input:{
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
});
```

```
print(output.requestId);
```

```
print(output.data);
```

## API Reference

For a complete list of available methods and their parameters, please refer toDart (Flutter) API Reference documentation.

## Examples

Check out some of the examples below to see real-world use cases of the client library:

- Simple Flutter app using fal image inference:https://pub.dev/packages/fal_client/example

## Support

If you encounter any issues or have questions, please visit theGitHub repositoryor join ourDiscord Community.