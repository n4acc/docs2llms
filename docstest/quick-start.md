# Quickstart with fal | fal.ai Docs


> Learn how to quickly get started with fal, including setting up API keys and using popular model endpoints for Stable Diffusion models.


# Quickstart with fal

In this example, we’ll be using one of our most popular modelendpoints.

Before we proceed, you need to create anAPI key.

This key will be used to authenticate your requests to the fal API.

- Javascript

- Python

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
Terminal windowpipinstallfal-client
```

```
pipinstallfal-client
```

```
pipinstallfal-client
```

- Javascript

- Python

```
fal.config({credentials:"PASTE_YOUR_FAL_KEY_HERE",});
```

```
fal.config({credentials:"PASTE_YOUR_FAL_KEY_HERE",});
```

```
fal.config({
```

```
credentials:"PASTE_YOUR_FAL_KEY_HERE",
```

```
});
```

```
Terminal windowexportFAL_KEY="PASTE_YOUR_FAL_KEY_HERE"
```

```
exportFAL_KEY="PASTE_YOUR_FAL_KEY_HERE"
```

```
exportFAL_KEY="PASTE_YOUR_FAL_KEY_HERE"
```

Now you can call our Model API endpoint using the falclient:

- Javascript

- Python

```
import{ fal }from"@fal-ai/client";constresult= awaitfal.subscribe("fal-ai/flux/dev", {input: {prompt:"Photo of a rhino dressed suit and tie sitting at a table in a bar with a bar stools, award winning photography, Elke vogelsang",},});
```

```
import{ fal }from"@fal-ai/client";constresult= awaitfal.subscribe("fal-ai/flux/dev", {input: {prompt:"Photo of a rhino dressed suit and tie sitting at a table in a bar with a bar stools, award winning photography, Elke vogelsang",},});
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
prompt:
```

```
"Photo of a rhino dressed suit and tie sitting at a table in a bar with a bar stools, award winning photography, Elke vogelsang",
```

```
},
```

```
});
```

```
importfal_clienthandler=fal_client.submit("fal-ai/flux/dev",arguments={"prompt":"photo of a rhino dressed suit and tie sitting at a table in a bar with a bar stools, award winning photography, Elke vogelsang"},)result=handler.get()print(result)
```

```
importfal_clienthandler=fal_client.submit("fal-ai/flux/dev",arguments={"prompt":"photo of a rhino dressed suit and tie sitting at a table in a bar with a bar stools, award winning photography, Elke vogelsang"},)result=handler.get()print(result)
```

```
importfal_client
```

```
handler=fal_client.submit(
```

```
"fal-ai/flux/dev",
```

```
arguments={
```

```
"prompt":"photo of a rhino dressed suit and tie sitting at a table in a bar with a bar stools, award winning photography, Elke vogelsang"
```

```
},
```

```
)
```

```
result=handler.get()
```

```
print(result)
```

We have made other popular models such as Flux Realism, Flux Lora Training SDXL Finetunes, Stable Video Diffusion, ControlNets, Whisper and more available as ready-to-use APIs so that you can easily integrate them into your applications.

FLUX.1 [schnell] is a 12 billion parameter flow transformer that generates high-quality images from text in 1 to 4 steps, suitable for personal and commercial use.

FLUX1.1 [pro] ultra is the newest version of FLUX1.1 [pro], maintaining professional-grade image quality while delivering up to 2K resolution with improved photo realism.

Check out ourModel Playgroundsto tinker with these models and let us know on ourDiscordif you want to see other ones listed.

Once you find a model that you want to use, you can grab its URL from the “API” tab. The API tab provides some important information about the model including its source code and examples of how you can call it.