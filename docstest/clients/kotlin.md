# Client Library for Kotlin | fal.ai Docs


> Learn how to integrate fal with your Kotlin projects, including installation, calling endpoints, and managing requests with the fal client.


# Client Library for Kotlin

## Introduction

The client for Kotlin provides a seamless interface to interact with fal.

## Installation

First, add the client as a dependency in your project:

- Gradle

- Maven

```
implementation'ai.fal.client:fal-client-kotlin:0.7.1'
```

```
implementation'ai.fal.client:fal-client-kotlin:0.7.1'
```

```
implementation'ai.fal.client:fal-client-kotlin:0.7.1'
```

```
<dependency><groupId>ai.fal.client</groupId><artifactId>fal-client-kotlin</artifactId><version>0.7.1</version></dependency>
```

```
<dependency><groupId>ai.fal.client</groupId><artifactId>fal-client-kotlin</artifactId><version>0.7.1</version></dependency>
```

```
<dependency>
```

```
<groupId>ai.fal.client</groupId>
```

```
<artifactId>fal-client-kotlin</artifactId>
```

```
<version>0.7.1</version>
```

```
</dependency>
```

## Features

### 1. Call an endpoint

Endpoints requests are managed by a queue system. This allows fal to provide a reliable and scalable service.

Thesubscribemethod allows you to submit a request to the queue and wait for the result.

```
importai.fal.client.ktvalfal=createFalClient()valinput=mapOf<String, Any>("prompt"to"a cat","seed"to6252023,"image_size"to"landscape_4_3","num_images"to4)valresult=fal.subscribe("fal-ai/flux/dev", input, options=SubscribeOptions(logs=true)) { update->if(updateisQueueStatus.InProgress) {println(update.logs)}}
```

```
importai.fal.client.ktvalfal=createFalClient()valinput=mapOf<String, Any>("prompt"to"a cat","seed"to6252023,"image_size"to"landscape_4_3","num_images"to4)valresult=fal.subscribe("fal-ai/flux/dev", input, options=SubscribeOptions(logs=true)) { update->if(updateisQueueStatus.InProgress) {println(update.logs)}}
```

```
importai.fal.client.kt
```

```
valfal=createFalClient()
```

```
valinput=mapOf<String, Any>(
```

```
"prompt"to"a cat",
```

```
"seed"to6252023,
```

```
"image_size"to"landscape_4_3",
```

```
"num_images"to4
```

```
)
```

```
valresult=fal.subscribe("fal-ai/flux/dev", input, options=SubscribeOptions(
```

```
logs=true
```

```
)) { update->
```

```
if(updateisQueueStatus.InProgress) {
```

```
println(update.logs)
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
importai.fal.client.ktvalfal=createFalClient()valinput=mapOf<String, Any>("prompt"to"a cat","seed"to6252023,"image_size"to"landscape_4_3","num_images"to4)valjob=fal.queue.submit("fal-ai/flux/dev", input, options=SubmitOptions(webhookUrl="https://optional.webhook.url/for/results"))
```

```
importai.fal.client.ktvalfal=createFalClient()valinput=mapOf<String, Any>("prompt"to"a cat","seed"to6252023,"image_size"to"landscape_4_3","num_images"to4)valjob=fal.queue.submit("fal-ai/flux/dev", input, options=SubmitOptions(webhookUrl="https://optional.webhook.url/for/results"))
```

```
importai.fal.client.kt
```

```
valfal=createFalClient()
```

```
valinput=mapOf<String, Any>(
```

```
"prompt"to"a cat",
```

```
"seed"to6252023,
```

```
"image_size"to"landscape_4_3",
```

```
"num_images"to4
```

```
)
```

```
valjob=fal.queue.submit("fal-ai/flux/dev", input, options=SubmitOptions(
```

```
webhookUrl="https://optional.webhook.url/for/results"
```

```
))
```

This is useful when you want to submit a request to the queue and retrieve the result later. You can save therequest_idand use it to retrieve the result later.

Webhooks

For long-running requests, such astraining jobs, you can use webhooks to receive the result asynchronously. You can specify the webhook URL when submitting a request.

#### Check Request Status

Retrieve the status of a specific request in the queue:

```
importai.fal.client.ktvalfal=createFalClient()valjob=fal.queue.status("fal-ai/flux/dev",requestId="764cabcf-b745-4b3e-ae38-1200304cf45b",options=StatusOptions(logs=true))
```

```
importai.fal.client.ktvalfal=createFalClient()valjob=fal.queue.status("fal-ai/flux/dev",requestId="764cabcf-b745-4b3e-ae38-1200304cf45b",options=StatusOptions(logs=true))
```

```
importai.fal.client.kt
```

```
valfal=createFalClient()
```

```
valjob=fal.queue.status("fal-ai/flux/dev",
```

```
requestId="764cabcf-b745-4b3e-ae38-1200304cf45b",
```

```
options=StatusOptions(
```

```
logs=true
```

```
)
```

```
)
```

#### Retrieve Request Result

Get the result of a specific request from the queue:

```
importai.fal.client.ktvalfal=createFalClient()valresult=fal.queue.result("fal-ai/flux/dev",requestId="764cabcf-b745-4b3e-ae38-1200304cf45b")
```

```
importai.fal.client.ktvalfal=createFalClient()valresult=fal.queue.result("fal-ai/flux/dev",requestId="764cabcf-b745-4b3e-ae38-1200304cf45b")
```

```
importai.fal.client.kt
```

```
valfal=createFalClient()
```

```
valresult=fal.queue.result("fal-ai/flux/dev",
```

```
requestId="764cabcf-b745-4b3e-ae38-1200304cf45b"
```

```
)
```

### 3. File Uploads

Some endpoints require files as input. However, since the endpoints run asynchronously, processed by the queue, you will need to provide URLs to the files instead of the actual file content.

Luckily, the client library provides a way to upload files to the server and get a URL to use in the request.

Not implemented yet

This functionality is not available on this client yet.

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
importai.fal.client.ktvalfal=createFalClient()valinput=mapOf<String, Any>("prompt"to"a cat","seed"to6252023,"image_size"to"landscape_4_3","num_images"to4)valresult=fal.run("fal-ai/flux/dev", input)
```

```
importai.fal.client.ktvalfal=createFalClient()valinput=mapOf<String, Any>("prompt"to"a cat","seed"to6252023,"image_size"to"landscape_4_3","num_images"to4)valresult=fal.run("fal-ai/flux/dev", input)
```

```
importai.fal.client.kt
```

```
valfal=createFalClient()
```

```
valinput=mapOf<String, Any>(
```

```
"prompt"to"a cat",
```

```
"seed"to6252023,
```

```
"image_size"to"landscape_4_3",
```

```
"num_images"to4
```

```
)
```

```
valresult=fal.run("fal-ai/flux/dev", input)
```

## API Reference

For a complete list of available methods and their parameters, please refer toKotlin API Reference documentation.

## Support

If you encounter any issues or have questions, please visit theGitHub repositoryor join ourDiscord Community.