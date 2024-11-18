# Optimizing Routing Behavior | fal.ai Docs


> Learn how to optimize routing behavior for applications with multiple replicas using semantically-aware routing hints to minimize cache misses.


# Optimizing Routing Behavior

When there are multiple available replicas of the same application, there isn’t a defined
behavior for picking which one to use for a particular request with the assumption that all
replicas would behave identically for the given set of inputs.

This might not be true for applications which hold state and might include an in-memory cache
for certain sets of parameters. For example, if you are serving an application that can run any
diffusion model but only can keep 3 distinct models in memory, you want to minimize the number of
cache misses (because loading that model from scratch incurs a significant performance penalty) depending
on a user provided input.

This is where the semantically-aware routing hints come into play. Instead of treating each replica equally, applications can provide hints for specialization and allow fal’s router to select the appropriate replica for a specific request. For this logic to work as efficiently, the user needs to provide aX-Fal-Runner-Hintheader
with a semantically identifying string hint and the application should implement aprovide_hints()method that returns a list
of hints. If there is a match in any of the replicas, fal’s router will send the request to that replica. However, if there is no match, it will fall back to the standard routing algorithm.

```
fromtypingimportAnyimportfalfromfal.toolkitimportImagefrompydanticimportBaseModelclassInput(BaseModel):model:str=Field()prompt:str=Field()classOutput(BaseModel):image: Image=Field()classAnyModelRunner(fal.App):defsetup(self)->None:self.models={}defprovide_hints(self)-> list[str]:# Choose to specialize on already loaded models; at first this will be empty# so we'll be picked for any request, but as slowly the cache builds up, the# replica will be more preferable compared to others.returnself.models.keys()defload_model(self,name:str)-> Any:fromdiffusersimportDiffusionPipelineifnameinself.models:returnself.models[name]pipeline=DiffusionPipeline.from_pretrained(name)pipeline.to("cuda")self.models[name]=pipelinereturnpipeline@fal.endpoint("/")defrun_model(self,input: Input)-> Output:model=self.load_model(input.model)result=model(input.prompt)returnOutput(image=Image.from_pil(result.images[0]))
```

```
fromtypingimportAnyimportfalfromfal.toolkitimportImagefrompydanticimportBaseModelclassInput(BaseModel):model:str=Field()prompt:str=Field()classOutput(BaseModel):image: Image=Field()classAnyModelRunner(fal.App):defsetup(self)->None:self.models={}defprovide_hints(self)-> list[str]:# Choose to specialize on already loaded models; at first this will be empty# so we'll be picked for any request, but as slowly the cache builds up, the# replica will be more preferable compared to others.returnself.models.keys()defload_model(self,name:str)-> Any:fromdiffusersimportDiffusionPipelineifnameinself.models:returnself.models[name]pipeline=DiffusionPipeline.from_pretrained(name)pipeline.to("cuda")self.models[name]=pipelinereturnpipeline@fal.endpoint("/")defrun_model(self,input: Input)-> Output:model=self.load_model(input.model)result=model(input.prompt)returnOutput(image=Image.from_pil(result.images[0]))
```

```
fromtypingimportAny
```

```
importfal
```

```
fromfal.toolkitimportImage
```

```
frompydanticimportBaseModel
```

```
classInput(BaseModel):
```

```
model:str=Field()
```

```
prompt:str=Field()
```

```
classOutput(BaseModel):
```

```
image: Image=Field()
```

```
classAnyModelRunner(fal.App):
```

```
defsetup(self)->None:
```

```
self.models={}
```

```
defprovide_hints(self)-> list[str]:
```

```
# Choose to specialize on already loaded models; at first this will be empty
```

```
# so we'll be picked for any request, but as slowly the cache builds up, the
```

```
# replica will be more preferable compared to others.
```

```
returnself.models.keys()
```

```
defload_model(self,name:str)-> Any:
```

```
fromdiffusersimportDiffusionPipeline
```

```
ifnameinself.models:
```

```
returnself.models[name]
```

```
pipeline=DiffusionPipeline.from_pretrained(name)
```

```
pipeline.to("cuda")
```

```
self.models[name]=pipeline
```

```
returnpipeline
```

```
@fal.endpoint("/")
```

```
defrun_model(self,input: Input)-> Output:
```

```
model=self.load_model(input.model)
```

```
result=model(input.prompt)
```

```
returnOutput(image=Image.from_pil(result.images[0]))
```