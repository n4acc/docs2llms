# Passing arguments and leveraging Pydantic | fal.ai Docs


> Learn how to use Pydantic for data validation in fal applications, including setting optional parameters, default values, and applying constraints.


# Passing arguments and leveraging Pydantic

fal Applications and FAST API are fully compatible with Pydantic. Any features of Pydantic used in fal endpoint arguments will also work.

Pydantic features can be used for data validation in your endpoint. In the example below, you can set some of the parameters as optional, set default values, and apply other types of validation such as constraints and types.

```
importfalfrompydanticimportBaseModelfromfal.toolkitimportImageclassImageModelInput(BaseModel):seed:int|None=Field(default=None,description="""The same seed and the same prompt given to the same version of Stable Diffusionwill output the same image every time.""",examples=[176400],)num_inference_steps:int=Field(default=25,description="""Increasing the amount of steps tell the model that it should take more stepsto generate your final result which can increase the amount of detail in your image.""",gt=0,le=100,)classMyApp(fal.App(keep_alive=300)):machine_type="GPU-A100"requirements=["diffusers==0.28.0","torch==2.3.0","accelerate","transformers",]defsetup(self):importtorchfromdiffusersimportStableDiffusionXLPipeline, DPMSolverSinglestepSchedulerself.pipe=StableDiffusionXLPipeline.from_pretrained("sd-community/sdxl-flash",torch_dtype=torch.float16,).to("cuda")self.pipe.scheduler=DPMSolverSinglestepScheduler.from_config(self.pipe.scheduler.config,timestep_spacing="trailing",)@fal.endpoint("/")defgenerate_image(self,request: ImageModelInput)-> Image:result=self.pipe(request.prompt,num_inference_steps=7,guidance_scale=3)image=Image.from_pil(result.images[0])returnimage
```

```
importfalfrompydanticimportBaseModelfromfal.toolkitimportImageclassImageModelInput(BaseModel):seed:int|None=Field(default=None,description="""The same seed and the same prompt given to the same version of Stable Diffusionwill output the same image every time.""",examples=[176400],)num_inference_steps:int=Field(default=25,description="""Increasing the amount of steps tell the model that it should take more stepsto generate your final result which can increase the amount of detail in your image.""",gt=0,le=100,)classMyApp(fal.App(keep_alive=300)):machine_type="GPU-A100"requirements=["diffusers==0.28.0","torch==2.3.0","accelerate","transformers",]defsetup(self):importtorchfromdiffusersimportStableDiffusionXLPipeline, DPMSolverSinglestepSchedulerself.pipe=StableDiffusionXLPipeline.from_pretrained("sd-community/sdxl-flash",torch_dtype=torch.float16,).to("cuda")self.pipe.scheduler=DPMSolverSinglestepScheduler.from_config(self.pipe.scheduler.config,timestep_spacing="trailing",)@fal.endpoint("/")defgenerate_image(self,request: ImageModelInput)-> Image:result=self.pipe(request.prompt,num_inference_steps=7,guidance_scale=3)image=Image.from_pil(result.images[0])returnimage
```

```
importfal
```

```
frompydanticimportBaseModel
```

```
fromfal.toolkitimportImage
```

```
classImageModelInput(BaseModel):
```

```
seed:int|None=Field(
```

```
default=None,
```

```
description="""
```

```
The same seed and the same prompt given to the same version of Stable Diffusion
```

```
will output the same image every time.
```

```
""",
```

```
examples=[176400],
```

```
)
```

```
num_inference_steps:int=Field(
```

```
default=25,
```

```
description="""
```

```
Increasing the amount of steps tell the model that it should take more steps
```

```
to generate your final result which can increase the amount of detail in your image.
```

```
""",
```

```
gt=0,
```

```
le=100,
```

```
)
```

```
classMyApp(fal.App(keep_alive=300)):
```

```
machine_type="GPU-A100"
```

```
requirements=[
```

```
"diffusers==0.28.0",
```

```
"torch==2.3.0",
```

```
"accelerate",
```

```
"transformers",
```

```
]
```

```
defsetup(self):
```

```
importtorch
```

```
fromdiffusersimportStableDiffusionXLPipeline, DPMSolverSinglestepScheduler
```

```
self.pipe=StableDiffusionXLPipeline.from_pretrained(
```

```
"sd-community/sdxl-flash",
```

```
torch_dtype=torch.float16,
```

```
).to("cuda")
```

```
self.pipe.scheduler=DPMSolverSinglestepScheduler.from_config(
```

```
self.pipe.scheduler.config,
```

```
timestep_spacing="trailing",
```

```
)
```

```
@fal.endpoint("/")
```

```
defgenerate_image(self,request: ImageModelInput)-> Image:
```

```
result=self.pipe(request.prompt,num_inference_steps=7,guidance_scale=3)
```

```
image=Image.from_pil(result.images[0])
```

```
returnimage
```