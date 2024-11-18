# Fastest FLUX Endpoint | fal.ai Docs


> Learn how to use fal's fastest FLUX endpoint, including setup, API key creation, and making API calls with the fal JavaScript client.


# Fastest FLUX Endpoint

We believe fal has the fastest FLUX endpoint in the planet. If you can find a faster one, we guarantee to beat it within one week. 🤝

FLUX.1 [schnell] is a 12 billion parameter flow transformer that generates high-quality images from text in 1 to 4 steps, suitable for personal and commercial use.

FLUX.1 [dev] is a 12 billion parameter flow transformer that generates high-quality images from text. It is suitable for personal and commercial use.

Here is a quick guide on how to use this model from an API in less than 1 minute.

Before we proceed, you need to create anAPI key.

This key secret will be used to authenticate your requests to the fal API.

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

Now you can call our Model API endpoint using thefal js client:

```
import{ fal }from"@fal-ai/client";constresult= awaitfal.subscribe("fal-ai/flux/dev", {input: {prompt:"photo of a rhino dressed suit and tie sitting at a table in a bar with a bar stools, award winning photography, Elke vogelsang",},});
```

```
import{ fal }from"@fal-ai/client";constresult= awaitfal.subscribe("fal-ai/flux/dev", {input: {prompt:"photo of a rhino dressed suit and tie sitting at a table in a bar with a bar stools, award winning photography, Elke vogelsang",},});
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
"photo of a rhino dressed suit and tie sitting at a table in a bar with a bar stools, award winning photography, Elke vogelsang",
```

```
},
```

```
});
```

Note

#### Image Uploads Should Not Waste GPU Cycles

We upload the output image in a background thread so we don’t charge any GPU
time for time spent on the GPU that is not directly inference.