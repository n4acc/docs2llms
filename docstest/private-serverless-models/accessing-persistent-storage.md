# Introduction to Private Serverless Models | fal.ai Docs


> Learn how to use fal's persistent storage for serverless functions, enabling data persistence across isolated environments for various use cases.


# Introduction to Private Serverless Models

As mentioned earlier, each fal function runs in an isolated environment that gets voided right after their invocation (unlesskeep_aliveis set). But for certain use cases, it may be important to persist certain results after the run is over. In such scenarios, you can use the/datavolume, which is mounted on each machine and is shared across all your functions running at any point in time linked to your FAL account.

```
importfalfrompathlibimportPathDATA_DIR=Path("/data/mnist")@fal.function("virtualenv",requirements=["torch>=2.0.0","torchvision"],machine_type="M",)deftrain_fashion_model():importtorchfromtorchvisionimportdatasetsalready_present=DATA_DIR.exists()ifalready_present:print("Test data is already downloaded, skipping download!")test_data=datasets.FashionMNIST(root=DATA_DIR,train=False,download=notalready_present,)...if__name__=="__main__":train_fashion_model()
```

```
importfalfrompathlibimportPathDATA_DIR=Path("/data/mnist")@fal.function("virtualenv",requirements=["torch>=2.0.0","torchvision"],machine_type="M",)deftrain_fashion_model():importtorchfromtorchvisionimportdatasetsalready_present=DATA_DIR.exists()ifalready_present:print("Test data is already downloaded, skipping download!")test_data=datasets.FashionMNIST(root=DATA_DIR,train=False,download=notalready_present,)...if__name__=="__main__":train_fashion_model()
```

```
importfal
```

```
frompathlibimportPath
```

```
DATA_DIR=Path("/data/mnist")
```

```
@fal.function(
```

```
"virtualenv",
```

```
requirements=["torch>=2.0.0","torchvision"],
```

```
machine_type="M",
```

```
)
```

```
deftrain_fashion_model():
```

```
importtorch
```

```
fromtorchvisionimportdatasets
```

```
already_present=DATA_DIR.exists()
```

```
ifalready_present:
```

```
print("Test data is already downloaded, skipping download!")
```

```
test_data=datasets.FashionMNIST(
```

```
root=DATA_DIR,
```

```
train=False,
```

```
download=notalready_present,
```

```
)
```

```
...
```

```
if__name__=="__main__":
```

```
train_fashion_model()
```

When you invoke this function for the first time, you will notice that Torch downloads the test dataset. However, subsequent invocations - even those not covered by the invocation’skeep_alive- will skip the download and proceed directly to your logic.

Implementation note

For HF-related libraries, fal ensures all downloaded models are persisted to
avoid re-downloads when running ML inference workloads. No need to customize
the output path fortransformersordiffusers.