# Add fal.ai to your Next.js app | fal.ai Docs


> Learn how to connect a Next.js app deployed on Vercel to fal.ai, including using the official integration and manual setup of credentials.


# Add fal.ai to your Next.js app

### You will learn how to:

- Connect a Next.js app deployed on Vercel to fal.ai

### Prerequisites

- Afal.aiaccount

- AVercel account

- A Next.js app. Check theNext.js guideif you don’t have one yet.

- App deployed on Vercel. Runnpx vercelin your app directory to deploy it in case you haven’t done it yet.

### Vercel official integration

The recommended way to add fal.ai to your app deployed on Vercel is to use the official integration. You can find it in theVercel marketplace.

Click onAdd integrationand follow the steps. After you’re done, re-deploy your app and you’re good to go!

### Manual setup

You can also manually add fal credentials to your Vercel environment manually.

- Go to yourfal.ai dashboard, create anAPI-scopedkey and copy it. Make sure you create an alias do identify which app is using it.

- Go to your app settings in Vercel and add a new environment variable calledFAL_KEYwith the value of the key you just copied. You can choose other names, but keep in mind that the default convention of fal-provided libraries isFAL_KEY.

- Re-deploy your app and you’re good to go!