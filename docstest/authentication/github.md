# GitHub Authentication | fal.ai Docs


> Learn how to authenticate with fal using your GitHub account, including steps for logging in and handling enterprise features.


# GitHub Authentication

faluses GitHub authentication by default which means that you need to have aGitHub accountto use it.

### Logging in

Installing falPython library lets you use thefalCLI, which you can use to authenticate. In your terminal, you can run the following command:

```
fal auth login
```

```
fal auth login
```

```
fal auth login
```

Follow the instructions on your terminal to confirm your credentials. Once you’re done, you should get a success message in your terminal.

Beta alert!

fal sdk is an enterprise feature. Once you run the login command, you will get
an error that you should reach out tosupport@fal.ai. Shoot us an email with how
you are planning to use fal, and we will make sure to get you access asap.

Now you’re ready to write your first fal function!

Note:Your login credentials are persisted on your local machine and cannot be transferred to another machine. If you want to use fal in your CI/CD, you will need to usekey-based credentials.