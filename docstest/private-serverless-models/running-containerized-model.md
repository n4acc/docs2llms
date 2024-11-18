# Running a containerized application | fal.ai Docs


> Learn how to run a containerized application with fal, including converting existing examples into containerized applications for better scalability.


# Running a containerized application

The easiest way to understand how to run a containerized application is to see an example.
Let’s convert the example from theprevious sectioninto a containerized application.

Container support basics

Check out therunning a fal function in a
containerexample for understanding the
basics of running a containerized application.

```
importfalimportfal.toolkitfromfal.containerimportContainerImagefromfal.toolkitimportImagefrompydanticimportBaseModel, Fielddockerfile_str="""FROM python:3.11RUN apt-get update && apt-get install -y ffmpegRUN pip install "accelerate" "transformers>=4.30.2" "diffusers>=0.26" "torch>=2.2.0""""classInput(BaseModel):prompt:str=Field(description="The prompt to generate an image from.",examples=["A cinematic shot of a baby racoon wearing an intricate italian priest robe.",],)classOutput(BaseModel):image: Image=Field(description="The generated image.",)classFalModel(fal.App,image=ContainerImage.from_dockerfile_str(dockerfile_str),kind="container",):machine_type="GPU"defsetup(self)->None:importtorchfromdiffusersimportAutoPipelineForText2Image# Load SDXLself.pipeline=AutoPipelineForText2Image.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0",torch_dtype=torch.float16,variant="fp16",)self.pipeline.to("cuda")# Apply fal's spatial optimizer to the pipeline.self.pipeline.unet=fal.toolkit.optimize(self.pipeline.unet)self.pipeline.vae=fal.toolkit.optimize(self.pipeline.vae)# Warm up the model.self.pipeline(prompt="a cat",num_inference_steps=30,)@fal.endpoint("/")deftext_to_image(self,input: Input)-> Output:result=self.pipeline(prompt=input.prompt,num_inference_steps=30,)[image]=result.imagesreturnOutput(image=Image.from_pil(image))
```

```
importfalimportfal.toolkitfromfal.containerimportContainerImagefromfal.toolkitimportImagefrompydanticimportBaseModel, Fielddockerfile_str="""FROM python:3.11RUN apt-get update && apt-get install -y ffmpegRUN pip install "accelerate" "transformers>=4.30.2" "diffusers>=0.26" "torch>=2.2.0""""classInput(BaseModel):prompt:str=Field(description="The prompt to generate an image from.",examples=["A cinematic shot of a baby racoon wearing an intricate italian priest robe.",],)classOutput(BaseModel):image: Image=Field(description="The generated image.",)classFalModel(fal.App,image=ContainerImage.from_dockerfile_str(dockerfile_str),kind="container",):machine_type="GPU"defsetup(self)->None:importtorchfromdiffusersimportAutoPipelineForText2Image# Load SDXLself.pipeline=AutoPipelineForText2Image.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0",torch_dtype=torch.float16,variant="fp16",)self.pipeline.to("cuda")# Apply fal's spatial optimizer to the pipeline.self.pipeline.unet=fal.toolkit.optimize(self.pipeline.unet)self.pipeline.vae=fal.toolkit.optimize(self.pipeline.vae)# Warm up the model.self.pipeline(prompt="a cat",num_inference_steps=30,)@fal.endpoint("/")deftext_to_image(self,input: Input)-> Output:result=self.pipeline(prompt=input.prompt,num_inference_steps=30,)[image]=result.imagesreturnOutput(image=Image.from_pil(image))
```

```
importfal
```

```
importfal.toolkit
```

```
fromfal.containerimportContainerImage
```

```
fromfal.toolkitimportImage
```

```
frompydanticimportBaseModel, Field
```

```
dockerfile_str="""
```

```
FROM python:3.11
```

```
RUN apt-get update && apt-get install -y ffmpeg
```

```
RUN pip install "accelerate" "transformers>=4.30.2" "diffusers>=0.26" "torch>=2.2.0"
```

```
"""
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
classFalModel(
```

```
fal.App,
```

```
image=ContainerImage.from_dockerfile_str(dockerfile_str),
```

```
kind="container",
```

```
):
```

```
machine_type="GPU"
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

Voila! 🎉 The highlighted changes are the only modifications you need to make; the rest remains your familiar fal application.

Dockerfile Keywords

Please check ourDockerfile best practicesfor
more information on how to optimize your Dockerfile.