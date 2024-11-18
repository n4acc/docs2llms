# Server-side integration | fal.ai Docs


> Learn how to securely integrate fal API with your server-side code, including ready-to-use proxy implementations and custom proxy guidelines.


# Server-side integration

Although the endpoints are designed to be called directly from the client, it is not safe to keep API Keys in client side code. Most cases require developer to create their own server-side APIs, that call a 3rd party service, fal, and then return the result to the client. It is a straightforward process, but always get in the way of developers and teams trying to focus on their own business, their own idea.

Therefore, we implemented the client libraries to support a proxy mode, which allows you to use the client libraries in the client, while keeping the API Keys in your own server-side code.

### Ready-to-use proxy implementations

We provide ready-to-use proxy implementations for the following languages/frameworks:

- Node.js with Next.js: a Next.js API route handler that can be used in any Next.js app. it supports both Page and App routers. We use it ourselves in all of our apps in production.

- Node.js with Express: an Express route handler that can be used in any Express app. You can also implement custom logic and compose together with your own handlers.

That’s it for now, but we are looking out for our community needs and will add more implementations in the future. If you have any requests, join our community in ourDiscord server.

### The proxy formula

In case fal doesn’t provide a plug-and-play proxy implementation for your language/framework, you can use the following formula to implement your own proxy:

- Provide a single endpoint that will ingest all requests from the client (e.g./api/fal/proxyis commonly used as the default route path).

- The endpoint must support bothGETandPOSTrequests. When an unsupported HTTP method is used, the proxy must return status code405, Method Not Allowed.

- The URL the proxy needs to call is provided by thex-fal-target-urlheader. If the header is missing, the proxy must return status code400, Bad Request. In case it doesn’t point to a valid URL, or the URL’s domain is not*.fal.aior*.fal.run, the proxy must return status code412, Precondition Failed.

- The request body, when present, is always in the JSON format - i.e.content-typeheader isapplication/json. Any other type of content must be rejected with status code415, Unsupported Media Type.

- The proxy must add theauthorizationheader in the format ofKey <your-api-key>to the request it sends to the target URL. Your API key should be resolved from the environment variableFAL_KEY.

- The response from the target URL will always be in the JSON format, the proxy must return the same response to the client.

- The proxy must return the same HTTP status code as the target URL.

- The proxy must return the same headers as the target URL, except for thecontent-lengthandcontent-encodingheaders, which should be set by the your own server/framework automatically.

Use the power of LLMs

The formula above was written in a way that should be easy to follow, including by LLMs. Try using ChatGPT or Co-pilot with the formula above and your should get a good starting point for your own implementation. Let us know if you try that!

### Configure the client

To use the proxy, you need to configure the client to use the proxy endpoint. You can do that by setting theproxyUrloption in the client configuration:

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

### Example implementation

You can find a reference implementation of the proxy formula using TypeScript, which supports both Express and Next.js, inserverless-js/libs/proxy/src/index.ts.