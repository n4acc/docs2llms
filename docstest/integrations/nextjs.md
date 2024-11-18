# Add fal.ai to your Next.js app | fal.ai Docs


> Learn how to integrate fal.ai with your Next.js app, including installing libraries, adding a server proxy, and generating images using SDXL.


# Add fal.ai to your Next.js app

### You will learn how to:

- Install the fal.ai libraries

- Add a server proxy to protect your credentials

- Generate an image using SDXL

### Prerequisites

- Have an existing Next.js app or create a new one usingnpx create-next-app

- Have afal.aiaccount

- Have an API Key. You cancreate one here

### 1. Install the fal.ai libraries

Using your favorite package manager, install both the@fal-ai/clientand@fal-ai/server-proxylibraries.

- npm

- yarn

- pnpm

```
Terminal windownpminstall@fal-ai/client@fal-ai/server-proxy
```

```
npminstall@fal-ai/client@fal-ai/server-proxy
```

```
npminstall@fal-ai/client@fal-ai/server-proxy
```

```
Terminal windowyarnadd@fal-ai/client@fal-ai/server-proxy
```

```
yarnadd@fal-ai/client@fal-ai/server-proxy
```

```
yarnadd@fal-ai/client@fal-ai/server-proxy
```

```
Terminal windowpnpmadd@fal-ai/client@fal-ai/server-proxy
```

```
pnpmadd@fal-ai/client@fal-ai/server-proxy
```

```
pnpmadd@fal-ai/client@fal-ai/server-proxy
```

### 2. Setup the proxy

The proxy will protect your API Key and prevent it from being exposed to the client. Usually app implementation have to handle that integration themselves, but in order to make the integration as smooth as possible, we provide a drop-in proxy implementation that can be integrated with either thePage Routeror theApp Router.

#### 2.1. Page Router

If you are using thePage Router(i.e.src/pages/_app.js), create an API handler insrc/pages/api/fal/proxy.js(or.tsin case of TypeScript), and re-export the built-in proxy handler:

```
export{ handlerasdefault}from"@fal-ai/server-proxy/nextjs";
```

```
export{ handlerasdefault}from"@fal-ai/server-proxy/nextjs";
```

```
export{ handlerasdefault}from"@fal-ai/server-proxy/nextjs";
```

#### 2.2. App Router

If you are using theApp Router(i.e.src/app/page.jsx) create a route handler insrc/app/api/fal/proxy/route.js(or.tsin case of TypeScript), and re-export the route handler:

```
import{ route }from"@fal-ai/server-proxy/nextjs";export const {GET,POST} =route;
```

```
import{ route }from"@fal-ai/server-proxy/nextjs";export const {GET,POST} =route;
```

```
import{ route }from"@fal-ai/server-proxy/nextjs";
```

```
export const {GET,POST} =route;
```

#### 2.3. Setup the API Key

Make sure you have your API Key available as an environment variable. You can setup in your.env.localfile for development and also in your hosting provider for production, such asVercel.

```
Terminal windowFAL_KEY="key_id:key_secret"
```

```
FAL_KEY="key_id:key_secret"
```

```
FAL_KEY="key_id:key_secret"
```

#### 2.4. Custom proxy logic

It’s common for applications to execute custom logic before or after the proxy handler. For example, you may want to add a custom header to the request, or log the request and response, or apply some rate limit. The good news is that the proxy implementation is simply a standard Next.js API/route handler function, which means you can compose it with other handlers.

For example, let’s assume you want to add some analytics and apply some rate limit to the proxy handler:

```
import{ route }from"@fal-ai/server-proxy/nextjs";// Let's add some custom logic to POST requests - i.e. when the request is// submitted for processingexport constPOST=(req)=> {// Add some analyticsanalytics.track("fal.ai request", {targetUrl:req.headers["x-fal-target-url"],userId:req.user.id,});// Apply some rate limitif(rateLimiter.shouldLimit(req)){res.status(429).json({ error:"Too many requests"});}// If everything passed your custom logic, now execute the proxy handlerreturnroute.POST(req);};// For GET requests we will just use the built-in proxy handler// But you could also add some custom logic here if you needexport constGET=route.GET;
```

```
import{ route }from"@fal-ai/server-proxy/nextjs";// Let's add some custom logic to POST requests - i.e. when the request is// submitted for processingexport constPOST=(req)=> {// Add some analyticsanalytics.track("fal.ai request", {targetUrl:req.headers["x-fal-target-url"],userId:req.user.id,});// Apply some rate limitif(rateLimiter.shouldLimit(req)){res.status(429).json({ error:"Too many requests"});}// If everything passed your custom logic, now execute the proxy handlerreturnroute.POST(req);};// For GET requests we will just use the built-in proxy handler// But you could also add some custom logic here if you needexport constGET=route.GET;
```

```
import{ route }from"@fal-ai/server-proxy/nextjs";
```

```
// Let's add some custom logic to POST requests - i.e. when the request is
```

```
// submitted for processing
```

```
export constPOST=(req)=> {
```

```
// Add some analytics
```

```
analytics.track("fal.ai request", {
```

```
targetUrl:req.headers["x-fal-target-url"],
```

```
userId:req.user.id,
```

```
});
```

```
// Apply some rate limit
```

```
if(rateLimiter.shouldLimit(req)){
```

```
res.status(429).json({ error:"Too many requests"});
```

```
}
```

```
// If everything passed your custom logic, now execute the proxy handler
```

```
returnroute.POST(req);
```

```
};
```

```
// For GET requests we will just use the built-in proxy handler
```

```
// But you could also add some custom logic here if you need
```

```
export constGET=route.GET;
```

Note that the URL that will be forwarded to server is available as a header namedx-fal-target-url. Also, keep in mind the example above is just an example,rateLimiterandanalyticsare just placeholders.

The example above used the app router, but the same logic can be applied to the page router and itshandlerfunction.

### 3. Configure the client

On your main file (i.e.src/pages/_app.jsxorsrc/app/page.jsx), configure the client to use the proxy:

```
import{ fal }from"@fal-ai/client";fal.config({proxyUrl:"/api/fal/proxy",});
```

```
import{ fal }from"@fal-ai/client";fal.config({proxyUrl:"/api/fal/proxy",});
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

Protect your API Key

Although the client can be configured with credentials, use that only for rapid prototyping. We recommend you always use the proxy to avoid exposing your API Key in the client before you deploy your web application. See theserver-side guidefor more details.

### 4. Generate an image

Now that the client is configured, you can generate an image usingfal.subscribeand pass the model id and the input parameters:

```
constresult= awaitfal.subscribe("fal-ai/flux/dev", {input: {prompt,image_size:"square_hd",},pollInterval:5000,logs:true,onQueueUpdate(update){console.log("queue update",update);},});constimageUrl=result.images[0].url;
```

```
constresult= awaitfal.subscribe("fal-ai/flux/dev", {input: {prompt,image_size:"square_hd",},pollInterval:5000,logs:true,onQueueUpdate(update){console.log("queue update",update);},});constimageUrl=result.images[0].url;
```

```
constresult= awaitfal.subscribe("fal-ai/flux/dev", {
```

```
input: {
```

```
prompt,
```

```
image_size:"square_hd",
```

```
},
```

```
pollInterval:5000,
```

```
logs:true,
```

```
onQueueUpdate(update){
```

```
console.log("queue update",update);
```

```
},
```

```
});
```

```
constimageUrl=result.images[0].url;
```

See more about SD with LoRA used in this example onfal.ai/models/sd-loras

### What’s next?

Image generation is just one of the many cool things you can do with fal. Make sure you:

- Check our demo application atgithub.com/fal-ai/serverless-js/apps/demo-nextjs-app-router

- Check all the availableModel APIs

- Learn how to write your own model APIs onIntroduction to serverless functions

- Read more about function endpoints onServing functions

- Check the next page to learn how todeploy your app to Vercel