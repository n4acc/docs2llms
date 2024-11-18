# Setting secrets | fal.ai Docs


> Learn how to set and manage sensitive information like API keys and database credentials in fal functions using the fal secrets CLI interface.


# Setting secrets

For setting sensitive information (such as API keys or database credentials) to be accessed within your fal functions you can use thefal secretsCLI interface.

```
$fal secretssetMY_API_TOKEN=tokenMY_IDENTITY_KEY=identity
```

```
$fal secretssetMY_API_TOKEN=tokenMY_IDENTITY_KEY=identity
```

```
$fal secretssetMY_API_TOKEN=tokenMY_IDENTITY_KEY=identity
```

Any secret that is set will be exposed to all functions running from your user, and can be accessible as if they are regular environment variables.

```
importosimportfal@fal.function()defprint_secrets():print(os.getenv("MY_API_TOKEN"))print(os.getenv("MY_IDENTITY_KEY"))if__name__=="__main__":print_secrets()
```

```
importosimportfal@fal.function()defprint_secrets():print(os.getenv("MY_API_TOKEN"))print(os.getenv("MY_IDENTITY_KEY"))if__name__=="__main__":print_secrets()
```

```
importos
```

```
importfal
```

```
@fal.function()
```

```
defprint_secrets():
```

```
print(os.getenv("MY_API_TOKEN"))
```

```
print(os.getenv("MY_IDENTITY_KEY"))
```

```
if__name__=="__main__":
```

```
print_secrets()
```

You can also list the secrets you have through the CLI, but the values will be hidden for security reasons.

```
$fal secretslist┏━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓┃ Secret Name             ┃ Created At                 ┃┡━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩│MY_API_TOKEN│2023-09-0515:17:39.279347││MY_IDENTITY_KEY│2023-09-0515:17:41.444478│└─────────────────────────┴────────────────────────────┘
```

```
$fal secretslist┏━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓┃ Secret Name             ┃ Created At                 ┃┡━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩│MY_API_TOKEN│2023-09-0515:17:39.279347││MY_IDENTITY_KEY│2023-09-0515:17:41.444478│└─────────────────────────┴────────────────────────────┘
```

```
$fal secretslist
```

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
```

```
┃ Secret Name             ┃ Created At                 ┃
```

```
┡━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
```

```
│MY_API_TOKEN│2023-09-0515:17:39.279347│
```

```
│MY_IDENTITY_KEY│2023-09-0515:17:41.444478│
```

```
└─────────────────────────┴────────────────────────────┘
```

To omit a secret from being present in new runs, you can simply delete it through the CLI:

```
$fal secrets unsetMY_API_TOKEN
```

```
$fal secrets unsetMY_API_TOKEN
```

```
$fal secrets unsetMY_API_TOKEN
```