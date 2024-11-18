# Real-time endpoints & WebSockets | fal.ai Docs


> Learn how to implement real-time endpoints and WebSockets in fal applications for low-latency and stateful real-time communication.


# Real-time endpoints & WebSockets

For applications deployed on fal runtime; in addition to regular HTTP endpoints,
developers might choose to implement auxiliary interfaces on top of raw WebSockets
or fal’s (stateless) real-time application framework.

Under afal.App, for any endpoint that deal with real-time connectivity,@fal.realtime()decorator
can be used instead of@fal.endpointto automatically make the interface compatible withfal’s real-time clients. The
functions do not provide any session state, and are meant to be used for reducing the overall latency (with fal’s binary protocol)
and eliminating fixed connection establishing overheads.

For power users who want to build stateful applications with their own real-time protocol, a@fal.endpointcan
be initialized withis_websocket=Trueflag and the underlying function will receive the raw WebSocket connection and
can choose to use it however it wants.

```
importfalfrompydanticimportBaseModelclassInput(BaseModel):prompt:str=Field()classOutput(BaseModel):output:str=Field()classRealtimeApp(fal.App):@fal.endpoint("/")defgenerate(self,input: Input)-> Output:returnOutput(output=input.prompt)@fal.endpoint("/ws",is_websocket=True)asyncdefgenerate_ws(self,websocket: WebSocket)->None:awaitwebsocket.accept()for_inrange(3):awaitwebsocket.send_json({"message":"Hello world!"})awaitwebsocket.close()@fal.realtime("/realtime")defgenerate_rt(self,input: Input)-> Output:returnOutput(output=input.prompt)
```

```
importfalfrompydanticimportBaseModelclassInput(BaseModel):prompt:str=Field()classOutput(BaseModel):output:str=Field()classRealtimeApp(fal.App):@fal.endpoint("/")defgenerate(self,input: Input)-> Output:returnOutput(output=input.prompt)@fal.endpoint("/ws",is_websocket=True)asyncdefgenerate_ws(self,websocket: WebSocket)->None:awaitwebsocket.accept()for_inrange(3):awaitwebsocket.send_json({"message":"Hello world!"})awaitwebsocket.close()@fal.realtime("/realtime")defgenerate_rt(self,input: Input)-> Output:returnOutput(output=input.prompt)
```

```
importfal
```

```
frompydanticimportBaseModel
```

```
classInput(BaseModel):
```

```
prompt:str=Field()
```

```
classOutput(BaseModel):
```

```
output:str=Field()
```

```
classRealtimeApp(fal.App):
```

```
@fal.endpoint("/")
```

```
defgenerate(self,input: Input)-> Output:
```

```
returnOutput(output=input.prompt)
```

```
@fal.endpoint("/ws",is_websocket=True)
```

```
asyncdefgenerate_ws(self,websocket: WebSocket)->None:
```

```
awaitwebsocket.accept()
```

```
for_inrange(3):
```

```
awaitwebsocket.send_json({"message":"Hello world!"})
```

```
awaitwebsocket.close()
```

```
@fal.realtime("/realtime")
```

```
defgenerate_rt(self,input: Input)-> Output:
```

```
returnOutput(output=input.prompt)
```