# Keeping fal API Secrets Safe | fal.ai Docs


> Learn how to securely manage fal API secrets for real-time models using WebSockets, including using JWT tokens and server-side proxies for authentication.


# Keeping fal API Secrets Safe

Real-time models using WebSockets present challenges in ensuring the security of API secrets.

The WebSocket connection is established directly from the browser or native mobile application, making it unsafe to embed API keys and secrets directly into the client. To address this, we have developed additional tools to enable secure authentication with our servers without introducing unnecessary intermediaries between the client and our GPU servers. Instead of using traditional API keys, we recommend utilizing short-livedJWTtokens for authentication.

Easiest way to communicate with fal using websockets is through ourjavascriptandswiftclients and aserver proxy.

Server Side Proxy

Checkout ourServer Side Integrationsection to learn more about using a ready made proxy with your Node.js or Next.js app or implement your own.

Whenfal.realtime.connectis invoked the fal client gets a short livedJWTtoken through a server proxy to authenticate with fal services. This token is refreshed automatically by the client when it is needed.

- Javascript

- SWIFT

```
import{ fal }from"@fal-ai/client";fal.config({proxyUrl:"/api/fal/proxy",});const {send} =fal.realtime.connect("fal-ai/fast-lcm-diffusion", {connectionKey:"realtime-demo",throttleInterval:128,onResult(result){// display},});
```

```
import{ fal }from"@fal-ai/client";fal.config({proxyUrl:"/api/fal/proxy",});const {send} =fal.realtime.connect("fal-ai/fast-lcm-diffusion", {connectionKey:"realtime-demo",throttleInterval:128,onResult(result){// display},});
```

```
import{ fal }from"@fal-ai/client";
```

```
fal.config({
```

```
proxyUrl:"/api/fal/proxy",
```

```
});
```

```
const {send} =fal.realtime.connect("fal-ai/fast-lcm-diffusion", {
```

```
connectionKey:"realtime-demo",
```

```
throttleInterval:128,
```

```
onResult(result){
```

```
// display
```

```
},
```

```
});
```

```
importFalClientletfal=FalClient.withProxy("http://localhost:3333/api/fal/proxy")letconnection=tryfal.realtime.connect(to: OptimizedLatentConsistency,connectionKey:"PencilKitDemo",throttleInterval: .milliseconds(128)) { (result: Result<LcmResponse,Error>)inifcaselet.success(data)=result,letimage=data.images.first{letdata=try?Data(contentsOf:URL(string: image.url)!)DispatchQueue.main.async{self.currentImage=data}}}
```

```
importFalClientletfal=FalClient.withProxy("http://localhost:3333/api/fal/proxy")letconnection=tryfal.realtime.connect(to: OptimizedLatentConsistency,connectionKey:"PencilKitDemo",throttleInterval: .milliseconds(128)) { (result: Result<LcmResponse,Error>)inifcaselet.success(data)=result,letimage=data.images.first{letdata=try?Data(contentsOf:URL(string: image.url)!)DispatchQueue.main.async{self.currentImage=data}}}
```

```
importFalClient
```

```
letfal=FalClient.withProxy("http://localhost:3333/api/fal/proxy")
```

```
letconnection=tryfal.realtime.connect(
```

```
to: OptimizedLatentConsistency,
```

```
connectionKey:"PencilKitDemo",
```

```
throttleInterval: .milliseconds(128)
```

```
) { (result: Result<LcmResponse,Error>)in
```

```
ifcaselet.success(data)=result,
```

```
letimage=data.images.first{
```

```
letdata=try?Data(contentsOf:URL(string: image.url)!)
```

```
DispatchQueue.main.async{
```

```
self.currentImage=data
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

Checkout theFalRealtimeSampleApp (swift)andrealtime demo (js)for more details.