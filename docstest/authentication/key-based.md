# Key-Based Authentication | fal.ai Docs


> Learn how to use key-based authentication for fal, including generating keys, understanding scopes, and using keys in CI/CD and remote environments.


# Key-Based Authentication

There are two main reasons to use key-based authentication:

- When callingready-to-use models

- In headless remote environments or CI/CD (where GitHub authentication is not available)

### Generating the keys

Navigate to our dashboard keys page and generate a key from the UIfal.ai/dashboard/keys

### Scopes

Scopes provide a way to control the permissions and access level of a given key. By assigning scopes to keys, you can limit the operations that each key can perform. Currently there are only two scopes,ADMINandAPI. If you are just consumingready-to-use models, we recommend that you use theAPIscope.

#### API scope

- Grants access to ready-to-use models.

#### ADMIN scope

- Grants full access to private models.

- Grants full access to CLI operations.

- Grants access to ready-to-use models.