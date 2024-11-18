# Container Support with fal | fal.ai Docs


> Learn how to run functions within custom Docker containers using fal, providing greater flexibility and control over your environment.


# Container Support with fal

fal now supports running functions within custom Docker containers, providing greater flexibility and control over your environment.

### Example: Using Custom Containers with fal functions

Here’s a complete example demonstrating how to use custom containers withfal.

```
importfalfromfal.containerimportContainerImagedockerfile_str="""FROM python:3.11RUN apt-get update && apt-get install -y ffmpegRUN pip install pyjokes ffmpeg-python"""@fal.function(kind="container",image=ContainerImage.from_dockerfile_str(dockerfile_str),)deftest_container():# A dependency that might have complex installation requirements.importffmpeg(ffmpeg.input("input.mp4").filter('thumbnail',n=300).output("thumbnail_filter_2.png").run())# And tell me a joke!importpyjokesprint(pyjokes.get_joke())print("done")if__name__=="__main__":test_container()
```

```
importfalfromfal.containerimportContainerImagedockerfile_str="""FROM python:3.11RUN apt-get update && apt-get install -y ffmpegRUN pip install pyjokes ffmpeg-python"""@fal.function(kind="container",image=ContainerImage.from_dockerfile_str(dockerfile_str),)deftest_container():# A dependency that might have complex installation requirements.importffmpeg(ffmpeg.input("input.mp4").filter('thumbnail',n=300).output("thumbnail_filter_2.png").run())# And tell me a joke!importpyjokesprint(pyjokes.get_joke())print("done")if__name__=="__main__":test_container()
```

```
importfal
```

```
fromfal.containerimportContainerImage
```

```
dockerfile_str="""
```

```
FROM python:3.11
```

```
RUN apt-get update && apt-get install -y ffmpeg
```

```
RUN pip install pyjokes ffmpeg-python
```

```
"""
```

```
@fal.function(
```

```
kind="container",
```

```
image=ContainerImage.from_dockerfile_str(dockerfile_str),
```

```
)
```

```
deftest_container():
```

```
# A dependency that might have complex installation requirements.
```

```
importffmpeg
```

```
(
```

```
ffmpeg.input("input.mp4")
```

```
.filter('thumbnail',n=300)
```

```
.output("thumbnail_filter_2.png")
```

```
.run()
```

```
)
```

```
# And tell me a joke!
```

```
importpyjokes
```

```
print(pyjokes.get_joke())
```

```
print("done")
```

```
if__name__=="__main__":
```

```
test_container()
```

#### Detailed Explanation

- Importing fal and ContainerImage:

```
importfalfromfal.containerimportContainerImage
```

```
importfalfromfal.containerimportContainerImage
```

```
importfal
```

```
fromfal.containerimportContainerImage
```

- Creating a Dockerfile String:
A multi-line string (dockerfile_str) is defined, specifying the base image aspython:3.11, and installingffmpegandpyjokespackages.

```
dockerfile_str="""FROM python:3.11RUN apt-get update && apt-get install -y ffmpegRUN pip install pyjokes ffmpeg-python"""
```

```
dockerfile_str="""FROM python:3.11RUN apt-get update && apt-get install -y ffmpegRUN pip install pyjokes ffmpeg-python"""
```

```
dockerfile_str="""
```

```
FROM python:3.11
```

```
RUN apt-get update && apt-get install -y ffmpeg
```

```
RUN pip install pyjokes ffmpeg-python
```

```
"""
```

Version mismatch

Ensure that the Python version in the Dockerfile matches the Python version in
your local environment that you use to run the function.

This is required to avoid any compatibility issues. We usepickleto serialize
the function under the hood, and the Python versions must match to avoid any
serialization issues.

That being said, we are constantly working on improving this experience.

Alternatively, you can use a Dockerfile path to specify the Dockerfile location:

```
importpathlibPWD=Path(__file__).resolve().parent@fal.function(kind="container",image=ContainerImage.from_dockerfile(f"{PWD}/Dockerfile"),)deftest_container():...
```

```
importpathlibPWD=Path(__file__).resolve().parent@fal.function(kind="container",image=ContainerImage.from_dockerfile(f"{PWD}/Dockerfile"),)deftest_container():...
```

```
importpathlib
```

```
PWD=Path(__file__).resolve().parent
```

```
@fal.function(
```

```
kind="container",
```

```
image=ContainerImage.from_dockerfile(f"{PWD}/Dockerfile"),
```

```
)
```

```
deftest_container():
```

```
...
```

- Defining the Container Function:
The@fal.functiondecorator specifies that this function runs in a container. Theimageparameter is set usingContainerImage.from_dockerfile_str(dockerfile_str), which builds the Docker image from the provided Dockerfile string.@fal.function(kind="container",image=ContainerImage.from_dockerfile_str(dockerfile_str),)

- Function Implementation:
Insidetest_container, theffmpeglibrary processes a video to create a thumbnail image. Then, it usespyjokesto print a random joke.deftest_container():importffmpeg(ffmpeg.input("input.mp4").filter('thumbnail',n=300).output("thumbnail_filter_2.png").run())importpyjokesprint(pyjokes.get_joke())print("done")

Defining the Container Function:
The@fal.functiondecorator specifies that this function runs in a container. Theimageparameter is set usingContainerImage.from_dockerfile_str(dockerfile_str), which builds the Docker image from the provided Dockerfile string.

```
@fal.function(kind="container",image=ContainerImage.from_dockerfile_str(dockerfile_str),)
```

```
@fal.function(kind="container",image=ContainerImage.from_dockerfile_str(dockerfile_str),)
```

```
@fal.function(
```

```
kind="container",
```

```
image=ContainerImage.from_dockerfile_str(dockerfile_str),
```

```
)
```

Function Implementation:
Insidetest_container, theffmpeglibrary processes a video to create a thumbnail image. Then, it usespyjokesto print a random joke.

```
deftest_container():importffmpeg(ffmpeg.input("input.mp4").filter('thumbnail',n=300).output("thumbnail_filter_2.png").run())importpyjokesprint(pyjokes.get_joke())print("done")
```

```
deftest_container():importffmpeg(ffmpeg.input("input.mp4").filter('thumbnail',n=300).output("thumbnail_filter_2.png").run())importpyjokesprint(pyjokes.get_joke())print("done")
```

```
deftest_container():
```

```
importffmpeg
```

```
(
```

```
ffmpeg.input("input.mp4")
```

```
.filter('thumbnail',n=300)
```

```
.output("thumbnail_filter_2.png")
```

```
.run()
```

```
)
```

```
importpyjokes
```

```
print(pyjokes.get_joke())
```

```
print("done")
```

#### Running the Function

To run the function, save the code to a file (e.g.,test_container.py) and execute it using thefal runcommand:

```
Terminal windowfalruntest_container.py
```

```
falruntest_container.py
```

```
falruntest_container.py
```

or directly from the Python interpreter:

```
python test_container.py
```

```
python test_container.py
```

```
python test_container.py
```

This example demonstrates how to leverage Docker containers in fal, enabling customized execution environments for your functions. For more details and advanced usage, refer to thefal Container Documentation.