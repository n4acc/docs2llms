# Workflow endpoints | fal.ai Docs


> Learn how to chain multiple models together using fal's workflow endpoints to create complex pipelines, enabling efficient multi-step AI tasks.


# Workflow endpoints

Workflows are a way to chain multiple models together to create a more complex pipeline. This allows you to create a single endpoint that can take an input and pass it through multiple models in sequence. This is useful for creating more complex models that require multiple steps, or for creating a single endpoint that can handle multiple tasks.

Beta alert

Workflows are currently in beta, join ourDiscordto get the latest updates and also share any issues or feedback you might have.

### Workflow as an API

Workflow APIs work the same way as other model endpoints, you can simply send a request and get a response back. However, it is common for workflows to contain multiple steps and produce intermediate results, as each step contains their own response that could be relevant in your use-case.

Therefore, workflows benefit from thestreamingfeature, which allows you to get partial results as they are being generated.

### Workflow events

The workflow API will trigger a few events during its execution, these events can be used to monitor the progress of the workflow and get intermediate results. Below are the events that you can expect from a workflow stream:

#### Thesubmitevent

This events is triggered every time a new step has been submitted to execution. It contains theapp_id,request_idand thenode_id.

```
{"type":"submit","node_id":"stable_diffusion_xl","app_id":"fal-ai/fast-sdxl","request_id":"d778bdf4-0275-47c2-9f23-16c27041cbeb"}
```

```
{"type":"submit","node_id":"stable_diffusion_xl","app_id":"fal-ai/fast-sdxl","request_id":"d778bdf4-0275-47c2-9f23-16c27041cbeb"}
```

```
{
```

```
"type":"submit",
```

```
"node_id":"stable_diffusion_xl",
```

```
"app_id":"fal-ai/fast-sdxl",
```

```
"request_id":"d778bdf4-0275-47c2-9f23-16c27041cbeb"
```

```
}
```

#### Thecompletionevent

This event is triggered upon the completion of a specific step.

```
{"type":"completion","node_id":"stable_diffusion_xl","output": {"images": [{"url":"https://fal.media/result.jpeg","width":1024,"height":1024,"content_type":"image/jpeg"}],"timings": {"inference":2.1733},"seed":6252023,"has_nsfw_concepts": [false],"prompt":"a cute puppy"}}
```

```
{"type":"completion","node_id":"stable_diffusion_xl","output": {"images": [{"url":"https://fal.media/result.jpeg","width":1024,"height":1024,"content_type":"image/jpeg"}],"timings": {"inference":2.1733},"seed":6252023,"has_nsfw_concepts": [false],"prompt":"a cute puppy"}}
```

```
{
```

```
"type":"completion",
```

```
"node_id":"stable_diffusion_xl",
```

```
"output": {
```

```
"images": [
```

```
{
```

```
"url":"https://fal.media/result.jpeg",
```

```
"width":1024,
```

```
"height":1024,
```

```
"content_type":"image/jpeg"
```

```
}
```

```
],
```

```
"timings": {"inference":2.1733},
```

```
"seed":6252023,
```

```
"has_nsfw_concepts": [false],
```

```
"prompt":"a cute puppy"
```

```
}
```

```
}
```

#### Theoutputevent

Theoutputevent means that the workflow has completed and the final result is ready.

```
{"type":"output","output": {"images": [{"url":"https://fal.media/result.jpeg","width":1024,"height":1024,"content_type":"image/jpeg"}]}}
```

```
{"type":"output","output": {"images": [{"url":"https://fal.media/result.jpeg","width":1024,"height":1024,"content_type":"image/jpeg"}]}}
```

```
{
```

```
"type":"output",
```

```
"output": {
```

```
"images": [
```

```
{
```

```
"url":"https://fal.media/result.jpeg",
```

```
"width":1024,
```

```
"height":1024,
```

```
"content_type":"image/jpeg"
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

#### Theerrorevent

Theerrorevent is triggered when an error occurs during the execution of a step. Theerrorobject contains theerror.statuswith the HTTP status code, an errormessageas well aserror.bodywith the underlying error serialized.

```
{"type":"error","node_id":"stable_diffusion_xl","message":"Error while fetching the result of the request d778bdf4-0275-47c2-9f23-16c27041cbeb","error": {"status":422,"body": {"detail": [{"loc": ["body","num_images"],"msg":"ensure this value is less than or equal to 8","type":"value_error.number.not_le","ctx": {"limit_value":8}}]}}}
```

```
{"type":"error","node_id":"stable_diffusion_xl","message":"Error while fetching the result of the request d778bdf4-0275-47c2-9f23-16c27041cbeb","error": {"status":422,"body": {"detail": [{"loc": ["body","num_images"],"msg":"ensure this value is less than or equal to 8","type":"value_error.number.not_le","ctx": {"limit_value":8}}]}}}
```

```
{
```

```
"type":"error",
```

```
"node_id":"stable_diffusion_xl",
```

```
"message":"Error while fetching the result of the request d778bdf4-0275-47c2-9f23-16c27041cbeb",
```

```
"error": {
```

```
"status":422,
```

```
"body": {
```

```
"detail": [
```

```
{
```

```
"loc": ["body","num_images"],
```

```
"msg":"ensure this value is less than or equal to 8",
```

```
"type":"value_error.number.not_le",
```

```
"ctx": {"limit_value":8}
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

```
}
```

### Example

A cool and simple example of the power of workflows isworkflows/fal-ai/sdxl-sticker, which consists of three steps:

- Generates an image usingfal-ai/fast-sdxl.

- Remove the background of the image usingfal-ai/imageutils/rembg.

- Converts the image to a sticker usingfal-ai/face-to-sticker.

What could be a tedious process of running and coordinating three different models is now a single endpoint that you can call with a single request.

- Javascript

- python

- python (async)

- Swift

```
import{ fal }from"@fal-ai/client";conststream= awaitfal.stream("workflows/fal-ai/sdxl-sticker", {input: {prompt:"a face of a cute puppy, in the style of pixar animation",},});forawait(consteventofstream) {console.log("partial",event);}constresult= awaitstream.done();console.log("final result",result);
```

```
import{ fal }from"@fal-ai/client";conststream= awaitfal.stream("workflows/fal-ai/sdxl-sticker", {input: {prompt:"a face of a cute puppy, in the style of pixar animation",},});forawait(consteventofstream) {console.log("partial",event);}constresult= awaitstream.done();console.log("final result",result);
```

```
import{ fal }from"@fal-ai/client";
```

```
conststream= awaitfal.stream("workflows/fal-ai/sdxl-sticker", {
```

```
input: {
```

```
prompt:"a face of a cute puppy, in the style of pixar animation",
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
console.log("partial",event);
```

```
}
```

```
constresult= awaitstream.done();
```

```
console.log("final result",result);
```

```
importfal_clientstream=fal_client.stream("workflows/fal-ai/sdxl-sticker",arguments={"prompt":"a face of a cute puppy, in the style of pixar animation",},)foreventinstream:print(event)
```

```
importfal_clientstream=fal_client.stream("workflows/fal-ai/sdxl-sticker",arguments={"prompt":"a face of a cute puppy, in the style of pixar animation",},)foreventinstream:print(event)
```

```
importfal_client
```

```
stream=fal_client.stream(
```

```
"workflows/fal-ai/sdxl-sticker",
```

```
arguments={
```

```
"prompt":"a face of a cute puppy, in the style of pixar animation",
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
importasyncioimportfal_clientasyncdefmain():stream=awaitfal_client.stream_async("workflows/fal-ai/sdxl-sticker",arguments={"prompt":"a face of a cute puppy, in the style of pixar animation",},)asyncforeventinstream:print(event)if__name__=="__main__":asyncio.run(main())
```

```
importasyncioimportfal_clientasyncdefmain():stream=awaitfal_client.stream_async("workflows/fal-ai/sdxl-sticker",arguments={"prompt":"a face of a cute puppy, in the style of pixar animation",},)asyncforeventinstream:print(event)if__name__=="__main__":asyncio.run(main())
```

```
importasyncio
```

```
importfal_client
```

```
asyncdefmain():
```

```
stream=awaitfal_client.stream_async(
```

```
"workflows/fal-ai/sdxl-sticker",
```

```
arguments={
```

```
"prompt":"a face of a cute puppy, in the style of pixar animation",
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
asyncio.run(main())
```

Coming soon

The Swift client does not support streaming yet.

### Type definitions

Below are the type definition in TypeScript of events that you can expect from a workflow stream:

```
typeWorkflowBaseEvent={type:"submit"|"completion"|"error"|"output";node_id:string;};exporttypeWorkflowSubmitEvent=WorkflowBaseEvent&{type:"submit";app_id:string;request_id:string;};exporttypeWorkflowCompletionEvent<Output=any>=WorkflowBaseEvent&{type:"completion";app_id:string;output:Output;};exporttypeWorkflowDoneEvent<Output=any>=WorkflowBaseEvent&{type:"output";output:Output;};exporttypeWorkflowErrorEvent=WorkflowBaseEvent&{type:"error";message:string;error:any;};
```

```
typeWorkflowBaseEvent={type:"submit"|"completion"|"error"|"output";node_id:string;};exporttypeWorkflowSubmitEvent=WorkflowBaseEvent&{type:"submit";app_id:string;request_id:string;};exporttypeWorkflowCompletionEvent<Output=any>=WorkflowBaseEvent&{type:"completion";app_id:string;output:Output;};exporttypeWorkflowDoneEvent<Output=any>=WorkflowBaseEvent&{type:"output";output:Output;};exporttypeWorkflowErrorEvent=WorkflowBaseEvent&{type:"error";message:string;error:any;};
```

```
typeWorkflowBaseEvent={
```

```
type:"submit"|"completion"|"error"|"output";
```

```
node_id:string;
```

```
};
```

```
exporttypeWorkflowSubmitEvent=WorkflowBaseEvent&{
```

```
type:"submit";
```

```
app_id:string;
```

```
request_id:string;
```

```
};
```

```
exporttypeWorkflowCompletionEvent<Output=any>=WorkflowBaseEvent&{
```

```
type:"completion";
```

```
app_id:string;
```

```
output:Output;
```

```
};
```

```
exporttypeWorkflowDoneEvent<Output=any>=WorkflowBaseEvent&{
```

```
type:"output";
```

```
output:Output;
```

```
};
```

```
exporttypeWorkflowErrorEvent=WorkflowBaseEvent&{
```

```
type:"error";
```

```
message:string;
```

```
error:any;
```

```
};
```