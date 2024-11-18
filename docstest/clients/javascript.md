# Client Library for JavaScript / TypeScript | fal.ai Docs


> Learn how to integrate fal with your JavaScript or TypeScript projects, including installation, calling endpoints, and managing requests with the fal client.


# Client Library for JavaScript / TypeScript

## Introduction

The client for JavaScript / TypeScript provides a seamless interface to interact with fal.

## Installation

First, add the client as a dependency in your project:

- npm

- yarn

- pnpm

- bun

```
Terminal windownpminstall--save@fal-ai/client
```

```
npminstall--save@fal-ai/client
```

```
npminstall--save@fal-ai/client
```

```
Terminal windowyarnadd@fal-ai/client
```

```
yarnadd@fal-ai/client
```

```
yarnadd@fal-ai/client
```

```
Terminal windowpnpmadd@fal-ai/client
```

```
pnpmadd@fal-ai/client
```

```
pnpmadd@fal-ai/client
```

```
Terminal windowbunadd@fal-ai/client
```

```
bunadd@fal-ai/client
```

```
bunadd@fal-ai/client
```

## Features

### 1. Call an endpoint

Endpoints requests are managed by a queue system. This allows fal to provide a reliable and scalable service.

Thesubscribemethod allows you to submit a request to the queue and wait for the result.

```
import{ fal }from"@fal-ai/client";constresult= awaitfal.subscribe("fal-ai/flux/dev", {input: {prompt:"a cat",seed:6252023,image_size:"landscape_4_3",num_images:4,},logs:true,onQueueUpdate:(update)=> {if(update.status==="IN_PROGRESS"){update.logs.map((log)=>log.message).forEach(console.log);}},});console.log(result.data);console.log(result.requestId);
```

```
import{ fal }from"@fal-ai/client";constresult= awaitfal.subscribe("fal-ai/flux/dev", {input: {prompt:"a cat",seed:6252023,image_size:"landscape_4_3",num_images:4,},logs:true,onQueueUpdate:(update)=> {if(update.status==="IN_PROGRESS"){update.logs.map((log)=>log.message).forEach(console.log);}},});console.log(result.data);console.log(result.requestId);
```

```
import{ fal }from"@fal-ai/client";
```

```
constresult= awaitfal.subscribe("fal-ai/flux/dev", {
```

```
input: {
```

```
prompt:"a cat",
```

```
seed:6252023,
```

```
image_size:"landscape_4_3",
```

```
num_images:4,
```

```
},
```

```
logs:true,
```

```
onQueueUpdate:(update)=> {
```

```
if(update.status==="IN_PROGRESS"){
```

```
update.logs.map((log)=>log.message).forEach(console.log);
```

```
}
```

```
},
```

```
});
```

```
console.log(result.data);
```

```
console.log(result.requestId);
```

### 2. Queue Management

You can manage the queue using the following methods:

#### Submit a Request

Submit a request to the queue using thequeue.submitmethod.

```
import{ fal }from"@fal-ai/client";const {request_id} = awaitfal.queue.submit("fal-ai/flux/dev", {input: {prompt:"a cat",seed:6252023,image_size:"landscape_4_3",num_images:4,},webhookUrl:"https://optional.webhook.url/for/results",});
```

```
import{ fal }from"@fal-ai/client";const {request_id} = awaitfal.queue.submit("fal-ai/flux/dev", {input: {prompt:"a cat",seed:6252023,image_size:"landscape_4_3",num_images:4,},webhookUrl:"https://optional.webhook.url/for/results",});
```

```
import{ fal }from"@fal-ai/client";
```

```
const {request_id} = awaitfal.queue.submit("fal-ai/flux/dev", {
```

```
input: {
```

```
prompt:"a cat",
```

```
seed:6252023,
```

```
image_size:"landscape_4_3",
```

```
num_images:4,
```

```
},
```

```
webhookUrl:"https://optional.webhook.url/for/results",
```

```
});
```

This is useful when you want to submit a request to the queue and retrieve the result later. You can save therequest_idand use it to retrieve the result later.

Webhooks

For long-running requests, such astraining jobs, you can use webhooks to receive the result asynchronously. You can specify the webhook URL when submitting a request.

#### Check Request Status

Retrieve the status of a specific request in the queue:

```
import{ fal }from"@fal-ai/client";conststatus= awaitfal.queue.status("fal-ai/flux/dev", {requestId:"764cabcf-b745-4b3e-ae38-1200304cf45b",logs:true,});
```

```
import{ fal }from"@fal-ai/client";conststatus= awaitfal.queue.status("fal-ai/flux/dev", {requestId:"764cabcf-b745-4b3e-ae38-1200304cf45b",logs:true,});
```

```
import{ fal }from"@fal-ai/client";
```

```
conststatus= awaitfal.queue.status("fal-ai/flux/dev", {
```

```
requestId:"764cabcf-b745-4b3e-ae38-1200304cf45b",
```

```
logs:true,
```

```
});
```

#### Retrieve Request Result

Get the result of a specific request from the queue:

```
import{ fal }from"@fal-ai/client";constresult= awaitfal.queue.result("fal-ai/flux/dev", {requestId:"764cabcf-b745-4b3e-ae38-1200304cf45b",});console.log(result.data);console.log(result.requestId);
```

```
import{ fal }from"@fal-ai/client";constresult= awaitfal.queue.result("fal-ai/flux/dev", {requestId:"764cabcf-b745-4b3e-ae38-1200304cf45b",});console.log(result.data);console.log(result.requestId);
```

```
import{ fal }from"@fal-ai/client";
```

```
constresult= awaitfal.queue.result("fal-ai/flux/dev", {
```

```
requestId:"764cabcf-b745-4b3e-ae38-1200304cf45b",
```

```
});
```

```
console.log(result.data);
```

```
console.log(result.requestId);
```

### 3. File Uploads

Some endpoints require files as input. However, since the endpoints run asynchronously, processed by the queue, you will need to provide URLs to the files instead of the actual file content.

Luckily, the client library provides a way to upload files to the server and get a URL to use in the request.

```
import{ fal }from"@fal-ai/client";constfile=newFile(["Hello, World!"],"hello.txt", { type:"text/plain"});consturl= awaitfal.storage.upload(file);
```

```
import{ fal }from"@fal-ai/client";constfile=newFile(["Hello, World!"],"hello.txt", { type:"text/plain"});consturl= awaitfal.storage.upload(file);
```

```
import{ fal }from"@fal-ai/client";
```

```
constfile=newFile(["Hello, World!"],"hello.txt", { type:"text/plain"});
```

```
consturl= awaitfal.storage.upload(file);
```

### 4. Streaming

Some endpoints support streaming:

```
import{ fal }from"@fal-ai/client";conststream= awaitfal.stream("fal-ai/flux/dev", {input: {prompt:"a cat",seed:6252023,image_size:"landscape_4_3",num_images:4,},});forawait(consteventofstream) {console.log(event);}constresult= awaitstream.done();
```

```
import{ fal }from"@fal-ai/client";conststream= awaitfal.stream("fal-ai/flux/dev", {input: {prompt:"a cat",seed:6252023,image_size:"landscape_4_3",num_images:4,},});forawait(consteventofstream) {console.log(event);}constresult= awaitstream.done();
```

```
import{ fal }from"@fal-ai/client";
```

```
conststream= awaitfal.stream("fal-ai/flux/dev", {
```

```
input: {
```

```
prompt:"a cat",
```

```
seed:6252023,
```

```
image_size:"landscape_4_3",
```

```
num_images:4,
```

```
},
```

```
});
```

```
forawait(consteventofstream) {
```

```
console.log(event);
```

```
}
```

```
constresult= awaitstream.done();
```

### 5. Realtime Communication

For the endpoints that support real-time inference via WebSockets, you can use the realtime client that abstracts the WebSocket connection, re-connection, serialization, and provides a simple interface to interact with the endpoint:

```
import{ fal }from"@fal-ai/client";constconnection=fal.realtime.connect("fal-ai/flux/dev", {onResult:(result)=> {console.log(result);},onError:(error)=> {console.error(error);},});connection.send({prompt:"a cat",seed:6252023,image_size:"landscape_4_3",num_images:4,});
```

```
import{ fal }from"@fal-ai/client";constconnection=fal.realtime.connect("fal-ai/flux/dev", {onResult:(result)=> {console.log(result);},onError:(error)=> {console.error(error);},});connection.send({prompt:"a cat",seed:6252023,image_size:"landscape_4_3",num_images:4,});
```

```
import{ fal }from"@fal-ai/client";
```

```
constconnection=fal.realtime.connect("fal-ai/flux/dev", {
```

```
onResult:(result)=> {
```

```
console.log(result);
```

```
},
```

```
onError:(error)=> {
```

```
console.error(error);
```

```
},
```

```
});
```

```
connection.send({
```

```
prompt:"a cat",
```

```
seed:6252023,
```

```
image_size:"landscape_4_3",
```

```
num_images:4,
```

```
});
```

### 6. Run

The endpoints can also be called directly instead of using the queue system.

Prefer the queue

Wedo not recommendthis use most use cases as it will block the client
until the response is received. Moreover, if the connection is closed before
the response is received, the request will be lost.

```
import{ fal }from"@fal-ai/client";constresult= awaitfal.run("fal-ai/flux/dev", {input: {prompt:"a cat",seed:6252023,image_size:"landscape_4_3",num_images:4,},});console.log(result.data);console.log(result.requestId);
```

```
import{ fal }from"@fal-ai/client";constresult= awaitfal.run("fal-ai/flux/dev", {input: {prompt:"a cat",seed:6252023,image_size:"landscape_4_3",num_images:4,},});console.log(result.data);console.log(result.requestId);
```

```
import{ fal }from"@fal-ai/client";
```

```
constresult= awaitfal.run("fal-ai/flux/dev", {
```

```
input: {
```

```
prompt:"a cat",
```

```
seed:6252023,
```

```
image_size:"landscape_4_3",
```

```
num_images:4,
```

```
},
```

```
});
```

```
console.log(result.data);
```

```
console.log(result.requestId);
```

## API Reference

For a complete list of available methods and their parameters, please refer toJavaScript / TypeScript API Reference documentation.

## Examples

Check out some of the examples below to see real-world use cases of the client library:

- Seefal.realtimein action with SDXL Lightning:https://github.com/fal-ai/sdxl-lightning-demo-app

## Support

If you encounter any issues or have questions, please visit theGitHub repositoryor join ourDiscord Community.

## Migration fromserverless-clienttoclient

As fal no longer uses “serverless” as part of the AI provider branding, we also made sure that’s reflected in our libraries. However, that’s not the only thing that changed in the new client. There was lot’s of improvements that happened thanks to our community feedback.

So, if you were using the@fal-ai/serverless-clientpackage, you can upgrade to the new@fal-ai/clientpackage by following these steps:

- Remove the@fal-ai/serverless-clientpackage from your project:Terminal windownpmuninstall@fal-ai/serverless-client

- Install the new@fal-ai/clientpackage:Terminal windownpminstall--save@fal-ai/client

- Update your imports:import * as fal from "@fal-ai/serverless-client";import { fal } from "@fal-ai/client";

- Now APIs return aResult<Output>type that contains thedatawhich is the API output and therequestId. This is a breaking change from the previous version, that allows us to return extra data to the caller without future breaking changes.const data = fal.subscribe(endpointId, { input });const { data, requestId } = fal.subscribe(endpointId, { input });

```
Terminal windownpmuninstall@fal-ai/serverless-client
```

```
npmuninstall@fal-ai/serverless-client
```

```
npmuninstall@fal-ai/serverless-client
```

```
Terminal windownpminstall--save@fal-ai/client
```

```
npminstall--save@fal-ai/client
```

```
npminstall--save@fal-ai/client
```

```
import * as fal from "@fal-ai/serverless-client";import { fal } from "@fal-ai/client";
```

```
import * as fal from "@fal-ai/serverless-client";import { fal } from "@fal-ai/client";
```

```
import * as fal from "@fal-ai/serverless-client";
```

```
import { fal } from "@fal-ai/client";
```

```
const data = fal.subscribe(endpointId, { input });const { data, requestId } = fal.subscribe(endpointId, { input });
```

```
const data = fal.subscribe(endpointId, { input });const { data, requestId } = fal.subscribe(endpointId, { input });
```

```
const data = fal.subscribe(endpointId, { input });
```

```
const { data, requestId } = fal.subscribe(endpointId, { input });
```

Note

Thefalobject is now a named export from the package that represents a singleton instance of theFalClientand was added to make it as easy as possible to migrate from the old singleton-only client. However, starting in1.0.0you can create multiple instances of theFalClientwith thecreateFalClientfunction.