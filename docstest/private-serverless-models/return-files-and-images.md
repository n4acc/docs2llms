# Returning files and images from functions | fal.ai Docs


> Learn how to return files and images from fal functions, including using fal's file and image classes for simplified handling and secure access.


# Returning files and images from functions

Saving images to your persistent directory is not always a convenient way to access them (you can use the File Explorer provided by the fal Web UI.) Alternatively, when dealing with image inputs and outputs, you can use fal’s file and image classes to simplify the process.

```
importfalfromfal.toolkitimportImageMODEL_NAME="google/ddpm-cat-256"@fal.function(requirements=["diffusers[torch]","transformers","pydantic",],machine_type="GPU-A100",)defgenerate_image():fromdiffusersimportDDPMPipelinepipe=DDPMPipeline.from_pretrained(MODEL_NAME,use_safetensors=True)pipe=pipe.to("cuda")result=pipe(num_inference_steps=25)returnImage.from_pil(result.images[0])if__name__=="__main__":cat_image=generate_image()print(f"Here is your cat:{cat_image.url}")
```

```
importfalfromfal.toolkitimportImageMODEL_NAME="google/ddpm-cat-256"@fal.function(requirements=["diffusers[torch]","transformers","pydantic",],machine_type="GPU-A100",)defgenerate_image():fromdiffusersimportDDPMPipelinepipe=DDPMPipeline.from_pretrained(MODEL_NAME,use_safetensors=True)pipe=pipe.to("cuda")result=pipe(num_inference_steps=25)returnImage.from_pil(result.images[0])if__name__=="__main__":cat_image=generate_image()print(f"Here is your cat:{cat_image.url}")
```

```
importfal
```

```
fromfal.toolkitimportImage
```

```
MODEL_NAME="google/ddpm-cat-256"
```

```
@fal.function(
```

```
requirements=[
```

```
"diffusers[torch]",
```

```
"transformers",
```

```
"pydantic",
```

```
],
```

```
machine_type="GPU-A100",
```

```
)
```

```
defgenerate_image():
```

```
fromdiffusersimportDDPMPipeline
```

```
pipe=DDPMPipeline.from_pretrained(MODEL_NAME,use_safetensors=True)
```

```
pipe=pipe.to("cuda")
```

```
result=pipe(num_inference_steps=25)
```

```
returnImage.from_pil(result.images[0])
```

```
if__name__=="__main__":
```

```
cat_image=generate_image()
```

```
print(f"Here is your cat:{cat_image.url}")
```

Constructing anImageobject on a serverless function automatically uploads it to fal’s block storage system and gives you a signed link for 2 days in which you can view or download it securely to have a copy of it as long as you need.

There's more...

Check out the reference forFilewhen doing more generic file I/O, and other
methods ofImageto see all supported formats.