# Cache-Efficient Dockerfile Guidelines with docker buildx (or buildKit) | fal.ai Docs


> Learn how to create cache-efficient Dockerfiles using Docker Buildx and BuildKit to improve build times and reduce resource consumption.


# Cache-Efficient Dockerfile Guidelines with docker buildx (or buildKit)

Under the hood, we usebuildkit(ordocker buildx) to build docker images. This allows us to take advantage of advanced caching mechanisms to improve build times and reduce resource consumption. In this guide, we’ll provide some guidelines for creating cache-efficient Dockerfiles.

### Introduction

Building a cache-efficient Dockerfile is crucial for improving the build time and reducing resource consumption. Docker Buildx and BuildKit provide advanced features that enhance caching mechanisms. This document provides guidelines for creating such Dockerfiles.

Note

Ensure you have Docker Buildx and BuildKit enabled in your Docker environment
if you want to test your containers locally. Otherwise, you don’t need to
worry about it. fal platform takes care of it for you when you deploy your
application using container support.

Check out theDocker buildx documentationfor more information.

### General Guidelines

Note

Please also refer to theDockerfile best
practicesfor detailed
information on Dockerfile best practices.

#### 1. Minimize Layers

EachRUN,COPY, orADDinstruction creates a new layer. Minimize the number of layers by combining commands.

Bad Example:

```
RUNapt-get updateRUNapt-get install -y curl
```

```
RUNapt-get updateRUNapt-get install -y curl
```

```
RUNapt-get update
```

```
RUNapt-get install -y curl
```

Good Example:

```
RUNapt-get update && apt-get install -y curl
```

```
RUNapt-get update && apt-get install -y curl
```

```
RUNapt-get update && apt-get install -y curl
```

#### 2. Leverage Layer Caching

Order instructions from least to most frequently changing to maximize layer caching.

Example:

```
# Install dependencies (changes less frequently)COPYrequirements.txt /app/RUNpip install -r requirements.txt# Copy application code (changes more frequently)COPY. /app
```

```
# Install dependencies (changes less frequently)COPYrequirements.txt /app/RUNpip install -r requirements.txt# Copy application code (changes more frequently)COPY. /app
```

```
# Install dependencies (changes less frequently)
```

```
COPYrequirements.txt /app/
```

```
RUNpip install -r requirements.txt
```

```
# Copy application code (changes more frequently)
```

```
COPY. /app
```

#### 3. Use--mount=type=cache

Utilize BuildKit’s--mount=type=cacheto cache directories across builds.

Example:

```
1.3-labsFROMpython:3.9# Use BuildKit cache for pipRUN--mount=type=cache,target=/root/.cache/pip \pip install --upgrade pipCOPYrequirements.txt /app/RUN--mount=type=cache,target=/root/.cache/pip \pip install -r requirements.txtCOPY. /app
```

```
FROMpython:3.9# Use BuildKit cache for pipRUN--mount=type=cache,target=/root/.cache/pip \pip install --upgrade pipCOPYrequirements.txt /app/RUN--mount=type=cache,target=/root/.cache/pip \pip install -r requirements.txtCOPY. /app
```

```
FROMpython:3.9
```

```
# Use BuildKit cache for pip
```

```
RUN--mount=type=cache,target=/root/.cache/pip \
```

```
pip install --upgrade pip
```

```
COPYrequirements.txt /app/
```

```
RUN--mount=type=cache,target=/root/.cache/pip \
```

```
pip install -r requirements.txt
```

```
COPY. /app
```

#### 4. Multi-Stage Builds

Use multi-stage builds to reduce the final image size by copying only the necessary artifacts from intermediate stages.

Example:

```
1.3FROMpython:3.9ASbuilderWORKDIR/appCOPY. .RUNpip install --upgrade pip \&& pip install -r requirements.txtFROMpython:3.9-slimCOPY--from=builder /app /appWORKDIR/appENTRYPOINT["python","app.py"]
```

```
FROMpython:3.9ASbuilderWORKDIR/appCOPY. .RUNpip install --upgrade pip \&& pip install -r requirements.txtFROMpython:3.9-slimCOPY--from=builder /app /appWORKDIR/appENTRYPOINT["python","app.py"]
```

```
FROMpython:3.9ASbuilder
```

```
WORKDIR/app
```

```
COPY. .
```

```
RUNpip install --upgrade pip \
```

```
&& pip install -r requirements.txt
```

```
FROMpython:3.9-slim
```

```
COPY--from=builder /app /app
```

```
WORKDIR/app
```

```
ENTRYPOINT["python","app.py"]
```

#### 5. Clean Up After Installations

Remove unnecessary files and caches after installing packages to keep the image size small.

Example:

```
RUNapt-get update && apt-get install -y \build-essential \&& rm -rf /var/lib/apt/lists/*
```

```
RUNapt-get update && apt-get install -y \build-essential \&& rm -rf /var/lib/apt/lists/*
```

```
RUNapt-get update && apt-get install -y \
```

```
build-essential \
```

```
&& rm -rf /var/lib/apt/lists/*
```

#### 6. Use.dockerignore

Specify files and directories to ignore during the build process to avoid unnecessary files in the build context.

Caution

As of now, fal does not support.dockerignorefiles. Since we don’t allow usingCOPYandADDfrom the host filesystem, you can ignore this step. However, we plan to add support for this in the near future. Stay tuned!

Seebelowfor more information.

Example:

```
__pycache__*.pyc*.pyo
```

```
__pycache__*.pyc*.pyo
```

```
__pycache__
```

```
*.pyc
```

```
*.pyo
```

### Example Dockerfile

Here is an example of a cache-efficient Dockerfile using the principles outlined above:

```
1.3FROMpython:3.9ASbaseWORKDIR/app# Install dependenciesCOPYrequirements.txt ./RUN--mount=type=cache,target=/root/.cache/pip \pip install --upgrade pip \&& pip install -r requirements.txt# Copy source filesCOPY. .# Build the applicationRUNpython setup.py build# Production imageFROMpython:3.9-slimCOPY--from=base /app /appWORKDIR/appENTRYPOINT["python","app.py"]
```

```
FROMpython:3.9ASbaseWORKDIR/app# Install dependenciesCOPYrequirements.txt ./RUN--mount=type=cache,target=/root/.cache/pip \pip install --upgrade pip \&& pip install -r requirements.txt# Copy source filesCOPY. .# Build the applicationRUNpython setup.py build# Production imageFROMpython:3.9-slimCOPY--from=base /app /appWORKDIR/appENTRYPOINT["python","app.py"]
```

```
FROMpython:3.9ASbase
```

```
WORKDIR/app
```

```
# Install dependencies
```

```
COPYrequirements.txt ./
```

```
RUN--mount=type=cache,target=/root/.cache/pip \
```

```
pip install --upgrade pip \
```

```
&& pip install -r requirements.txt
```

```
# Copy source files
```

```
COPY. .
```

```
# Build the application
```

```
RUNpython setup.py build
```

```
# Production image
```

```
FROMpython:3.9-slim
```

```
COPY--from=base /app /app
```

```
WORKDIR/app
```

```
ENTRYPOINT["python","app.py"]
```

### fal Platform Specific Gotchas

When deploying your application on the fal platform, you don’t need to worry about enabling Docker Buildx or BuildKit. We take care of it for you. However, you can follow the guidelines mentioned above to create efficient Dockerfiles that will help speed up the build process and reduce resource consumption.

#### 1. Interacting with the local filesystem

COPYandADD(from local filesystem) are not supported as of now to copy files into the container
from the host. Instead you can use fal’sfal.toolkitto upload files and
refer them in the container using links.

Note

If you are curious about the differences betweenCOPYandADD, check out
thefollowing link.

```
json_url=File.from_path("my-file.json",repository="cdn").urldockerfile_str=f"""FROM python:3.11-slimRUN apt-get update && apt-get install -y curlRUN curl '{json_url}' > my-file.json"""
```

```
json_url=File.from_path("my-file.json",repository="cdn").urldockerfile_str=f"""FROM python:3.11-slimRUN apt-get update && apt-get install -y curlRUN curl '{json_url}' > my-file.json"""
```

```
json_url=File.from_path("my-file.json",repository="cdn").url
```

```
dockerfile_str=f"""
```

```
FROM python:3.11-slim
```

```
RUN apt-get update && apt-get install -y curl
```

```
RUN curl '{json_url}' > my-file.json
```

```
"""
```

or you can useADDto directly download the file from the URL:

```
json_url=File.from_path("requirements.txt",repository="cdn").urldockerfile_str=f"""FROM python:3.11-slimADD{json_url}/app/requirements.txtWORKDIR /appRUN pip install -r requirements.txt"""
```

```
json_url=File.from_path("requirements.txt",repository="cdn").urldockerfile_str=f"""FROM python:3.11-slimADD{json_url}/app/requirements.txtWORKDIR /appRUN pip install -r requirements.txt"""
```

```
json_url=File.from_path("requirements.txt",repository="cdn").url
```

```
dockerfile_str=f"""
```

```
FROM python:3.11-slim
```

```
ADD{json_url}/app/requirements.txt
```

```
WORKDIR /app
```

```
RUN pip install -r requirements.txt
```

```
"""
```

### Conclusion

By following these guidelines, you can create Dockerfiles that build efficiently and take full advantage of Docker Buildx and BuildKit’s caching capabilities. This will lead to faster build times and reduced resource usage.

For more detailed information, refer to theDocker documentation.