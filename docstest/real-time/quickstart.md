# Real Time Models Quickstart | fal.ai Docs


> Get started quickly with fal by following this guide, including setup, installation, and basic usage to begin leveraging fal's capabilities.


# Real Time Models Quickstart

In this example, we’ll be using our most popularoptimized ultra fast latent consistency model.

All our Model Endpoint’s support HTTP/REST. Additionally our real-time models support WebSockets. You can use the HTTP/REST endpoint for any real time model but if you are sending back to back requests using websockets gives the best results.

Run SDXL at the speed of light

Run SDXL at the speed of light

Before we proceed, you need to create yourAPI key.

```
import{ fal }from"@fal-ai/client";fal.config({credentials:"PASTE_YOUR_FAL_KEY_HERE",});constconnection=fal.realtime.connect("fal-ai/fast-lcm-diffusion", {onResult:(result)=> {console.log(result);},onError:(error)=> {console.error(error);},});connection.send({prompt:"an island near sea, with seagulls, moon shining over the sea, light house, boats int he background, fish flying over the sea",sync_mode:true,image_url:"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg==",});
```

```
import{ fal }from"@fal-ai/client";fal.config({credentials:"PASTE_YOUR_FAL_KEY_HERE",});constconnection=fal.realtime.connect("fal-ai/fast-lcm-diffusion", {onResult:(result)=> {console.log(result);},onError:(error)=> {console.error(error);},});connection.send({prompt:"an island near sea, with seagulls, moon shining over the sea, light house, boats int he background, fish flying over the sea",sync_mode:true,image_url:"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg==",});
```

```
import{ fal }from"@fal-ai/client";
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
constconnection=fal.realtime.connect("fal-ai/fast-lcm-diffusion", {
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
prompt:
```

```
"an island near sea, with seagulls, moon shining over the sea, light house, boats int he background, fish flying over the sea",
```

```
sync_mode:true,
```

```
image_url:
```

```
"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg==",
```

```
});
```

You can read more about the real time clients in ourreal time client docssection.

Note

For the fastest inference speed use512x512input dimensions forimage_url.

To get the best performance from this model:

- Make sure the image is provided as a base64 encoded data url.

- Make sure the image_url is exactly512x512.

- Make sure sync*mode is true, this will make sure you also get a base64 encoded data url back from our API.

You can also use768x768or1024x1024as your image dimensions, the inference will be faster for this configuration compared to random dimensions but wont be as fast as512x512.

Video Tutorial:Latent Consistency - Build a Real-Time AI Image App with WebSockets, Next.js, and fal.ai byNader Dabit