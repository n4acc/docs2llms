# Runtime Model Optimizations | fal.ai Docs


> Learn how to optimize runtime models with fal's inference engine, including dynamic compilation and quantization techniques for improved performance.


# Runtime Model Optimizations

fal’s inference engine bindings takes a torch module and applies all relevant dynamic compilation and
quantization techniques to make it faster out of the box without leaking any of the complexity to the user.

This API is currently experimental, and might be subject to change in the future.

Example usage:

```
importfalimportfal.toolkitfromfal.toolkitimportImagefrompydanticimportBaseModel, FieldclassInput(BaseModel):prompt:str=Field(description="The prompt to generate an image from.",examples=["A cinematic shot of a baby racoon wearing an intricate italian priest robe.",],)classOutput(BaseModel):image: Image=Field(description="The generated image.",)classFalModel(fal.App):machine_type="GPU"requirements=["accelerate","transformers>=4.30.2","diffusers>=0.26","torch>=2.2.0",]defsetup(self)->None:importtorchfromdiffusersimportAutoPipelineForText2Image# Load SDXLself.pipeline=AutoPipelineForText2Image.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0",torch_dtype=torch.float16,variant="fp16",)self.pipeline.to("cuda")# Apply fal's spatial optimizer to the pipeline.self.pipeline.unet=fal.toolkit.optimize(self.pipeline.unet)self.pipeline.vae=fal.toolkit.optimize(self.pipeline.vae)# Warm up the model.self.pipeline(prompt="a cat",num_inference_steps=30,)@fal.endpoint("/")deftext_to_image(self,input: Input)-> Output:result=self.pipeline(prompt=input.prompt,num_inference_steps=30,)[image]=result.imagesreturnOutput(image=Image.from_pil(image))
```

```
importfalimportfal.toolkitfromfal.toolkitimportImagefrompydanticimportBaseModel, FieldclassInput(BaseModel):prompt:str=Field(description="The prompt to generate an image from.",examples=["A cinematic shot of a baby racoon wearing an intricate italian priest robe.",],)classOutput(BaseModel):image: Image=Field(description="The generated image.",)classFalModel(fal.App):machine_type="GPU"requirements=["accelerate","transformers>=4.30.2","diffusers>=0.26","torch>=2.2.0",]defsetup(self)->None:importtorchfromdiffusersimportAutoPipelineForText2Image# Load SDXLself.pipeline=AutoPipelineForText2Image.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0",torch_dtype=torch.float16,variant="fp16",)self.pipeline.to("cuda")# Apply fal's spatial optimizer to the pipeline.self.pipeline.unet=fal.toolkit.optimize(self.pipeline.unet)self.pipeline.vae=fal.toolkit.optimize(self.pipeline.vae)# Warm up the model.self.pipeline(prompt="a cat",num_inference_steps=30,)@fal.endpoint("/")deftext_to_image(self,input: Input)-> Output:result=self.pipeline(prompt=input.prompt,num_inference_steps=30,)[image]=result.imagesreturnOutput(image=Image.from_pil(image))
```

```
importfal
```

```
importfal.toolkit
```

```
fromfal.toolkitimportImage
```

```
frompydanticimportBaseModel, Field
```

```
classInput(BaseModel):
```

```
prompt:str=Field(
```

```
description="The prompt to generate an image from.",
```

```
examples=[
```

```
"A cinematic shot of a baby racoon wearing an intricate italian priest robe.",
```

```
],
```

```
)
```

```
classOutput(BaseModel):
```

```
image: Image=Field(
```

```
description="The generated image.",
```

```
)
```

```
classFalModel(fal.App):
```

```
machine_type="GPU"
```

```
requirements=[
```

```
"accelerate",
```

```
"transformers>=4.30.2",
```

```
"diffusers>=0.26",
```

```
"torch>=2.2.0",
```

```
]
```

```
defsetup(self)->None:
```

```
importtorch
```

```
fromdiffusersimportAutoPipelineForText2Image
```

```
# Load SDXL
```

```
self.pipeline=AutoPipelineForText2Image.from_pretrained(
```

```
"stabilityai/stable-diffusion-xl-base-1.0",
```

```
torch_dtype=torch.float16,
```

```
variant="fp16",
```

```
)
```

```
self.pipeline.to("cuda")
```

```
# Apply fal's spatial optimizer to the pipeline.
```

```
self.pipeline.unet=fal.toolkit.optimize(self.pipeline.unet)
```

```
self.pipeline.vae=fal.toolkit.optimize(self.pipeline.vae)
```

```
# Warm up the model.
```

```
self.pipeline(
```

```
prompt="a cat",
```

```
num_inference_steps=30,
```

```
)
```

```
@fal.endpoint("/")
```

```
deftext_to_image(self,input: Input)-> Output:
```

```
result=self.pipeline(
```

```
prompt=input.prompt,
```

```
num_inference_steps=30,
```

```
)
```

```
[image]=result.images
```

```
returnOutput(image=Image.from_pil(image))
```