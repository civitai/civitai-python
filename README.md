# Civitai Generator Python Client

A Python client for Civitai's generator to run Civitai models from your Python code.

## Installation

```python
pip install civitai
```

## Requirements

- Python 3.8+

## Usage

#### Create the client:

```python
from civitai import Civitai

civitai = Civitai(auth="YOUR_API_TOKEN")
```

#### Create a txt2img job:

```python
from civitai import Scheduler

input = {
    "model": "urn:air:sd1:checkpoint:civitai:4201@130072",
    "params": {
        "prompt": "RAW photo, face portrait photo of 26 y.o woman, wearing black dress, happy face, hard shadows, cinematic shot, dramatic lighting",
        "negativePrompt": "(deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime, mutated hands and fingers:1.4), (deformed, distorted, disfigured:1.3)",
        "scheduler": Scheduler.EULER_A,
        "steps": 20,
        "cfgScale": 7,
        "width": 512,
        "height": 512,
        "clipSkip": 2
    }
}
```

Run a model:

```python
response = civitai.image.from_text(input)
```

Then fetch the result later:

```python
output = civitai.jobs.get_by_token(response["token"])
```

Or wait for the job to finish by running the generation in the background a.k.a long polling:

```python
response = civitai.image.from_text(input, wait=True)  # Add wait flag
```

_Note: Jobs timeout after 10 minutes._

### Using Additional Networks

The SDK supports additional networks: LoRA, VAE, Hypernetwork, Textual Inversion, LyCORIS, Checkpoint, and LoCon.

To use any of the networks availabe on Civitai, simply the `additionNetworks` field into the input:

```python
from civitai import Scheduler, AssetType

input = {
    "model": "urn:air:sd1:checkpoint:civitai:4384@128713",
    "params": {
        "prompt": "masterpiece, best quality, 1girl, IncrsAhri, multiple tails, fox tail, korean clothes, skirt, braid, arms behind back",
        "negativePrompt": "(worst quality:1.4), (low quality:1.4), simple background, bad anatomy",
        "scheduler": Scheduler.EULER_A,
        "steps": 25,
        "cfgScale": 7,
        "width": 512,
        "height": 768,
        "seed": -1,
        "clipSkip": 2
    },
    "additional_networks": {
        "urn:air:sd1:lora:civitai:162141@182559": {
            "type": AssetType.LORA,
            "strength": 1.0
        }
    }
}
```

In the case of `Lora` and `LoCon` networks, set the `strength` of the network; for `TextualInversion`, set the `triggerWord` of the network.

<br/>

## API

### Constructor

```python
civitai = Civitai(options)
```

| name   | type                  | description                                                |
| ------ | --------------------- | ---------------------------------------------------------- |
| `auth` | string                | **Required**. API access token                             |
| `env`  | `dev` \| `production` | Optional. The environment to use. Default is `production`. |

### `civitai.image.from_text`

Run a model with inputs you provide.

```python
response = civitai.image.from_text(options)
```

| name                    | type                                                                  | description                                                                                                                                                                                                                                                                                                                               |
| ----------------------- | --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `model`                 | string \| null                                                        | **Required**. The Civitai model to use for generation.                                                                                                                                                                                                                                                                                    |
| `params.prompt`         | string \| null                                                        | **Required**. The main prompt for the image generation.                                                                                                                                                                                                                                                                                   |
| `params.negativePrompt` | string \| null                                                        | Optional. The negative prompt for the image generation.                                                                                                                                                                                                                                                                                   |
| `params.scheduler`      | [Scheduler](src/models/Scheduler.ts) \| null                          | Optional. The scheduler algorithm to use. <br/> <br/>Possible values are: `EulerA`, `Euler`, `LMS`, `Heun`, `DPM2`, `DPM2A`, `DPM2SA`, `DPM2M`, `DPMSDE`, `DPMFast`, `DPMAdaptive`, `LMSKarras`, `DPM2Karras`, `DPM2AKarras`, `DPM2SAKarras`, `DPM2MKarras`, `DPMSDEKarras`, `DDIM`, `PLMS`, `UniPC`, `Undefined`, `LCM`, `DDPM`, `DEIS`. |
| `params.steps`          | number \| null                                                        | Optional. The number of steps for the image generation process.                                                                                                                                                                                                                                                                           |
| `params.cfgScale`       | number \| null                                                        | Optional. The CFG scale for the image generation.                                                                                                                                                                                                                                                                                         |
| `params.width`          | number                                                                | **Required**. The width of the generated image.                                                                                                                                                                                                                                                                                           |
| `params.height`         | number                                                                | **Required**. The height of the generated image.                                                                                                                                                                                                                                                                                          |
| `params.seed`           | number \| null                                                        | Optional. The seed for the image generation process.                                                                                                                                                                                                                                                                                      |
| `params.clipSkip`       | number \| null                                                        | Optional. The number of CLIP skips for the image generation.                                                                                                                                                                                                                                                                              |
| `callbackUrl`           | string \| null                                                        | Optional. URL that will be invoked upon completion of this job                                                                                                                                                                                                                                                                            |
| `additionalNetworks`    | [ImageJobNetworkParams](src/models/ImageJobNetworkParams.ts) \| null  | Optional. An associative list of additional networks, keyed by the AIR of the network. Each network is of type [AssetType](src/models/AssetType.ts).                                                                                                                                                                                      |
| `controlNets`           | Array<[ImageJobControlNet](src/models/ImageJobControlNet.ts)> \| null | Optional. An associative list of additional networks.                                                                                                                                                                                                                                                                                     |

#### Additional Networks

| `additionalNetworks` | Record<string, [ImageJobNetworkParams](src/models/ImageJobNetworkParams.ts)> | Optional. An associative list of additional networks, keyed by the AIR of the network. Each network is described by an `ImageJobNetworkParams` object. |
| -------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `type`               | [`AssetType`](src/models/AssetType.ts)                                       | Optional. The type of the asset. <br/><br/>Can be one of `Lora`, `Hypernetwork`, `TextualInversion`, `Lycoris`, `Checkpoint`, `Vae`, `LoCon`.          |
| `strength`           | number                                                                       | Optional. In case of Lora and LoCon, set the strength of the network.                                                                                  |
| `triggerWord`        | string                                                                       | Optional. In case of a TextualInversion, set the trigger word of the network.                                                                          |

#### ControlNets

| `controlNets`  | Array<[ImageJobControlNet](src/models/ImageJobControlNet.ts)> | Optional. An array of control networks that can be applied to the image generation process. <br/><br/>Each `ImageJobControlNet` object in the array can have the following properties: |
| -------------- | ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `preprocessor` | [ImageTransformer](src/models/ImageTransformer.ts) \| null    | Optional. Specifies the image transformer to be applied as a preprocessor. <br/><br/>Possible values are `Canny`, `DepthZoe`, `SoftedgePidinet`, `Rembg`.                              |
| `weight`       | number \| null                                                | Optional. The weight of the control net.                                                                                                                                               |
| `startStep`    | number \| null                                                | Optional. The step at which the control net starts to apply.                                                                                                                           |
| `endStep`      | number \| null                                                | Optional. The step at which the control net stops applying.                                                                                                                            |
| `imageUrl`     | string \| null                                                | Optional. The URL of the image associated with the controlnet.                                                                                                                         |

### `civitai.jobs.get_by_id`

Fetches the status of a job by its unique jobId.

```python
response = civitai.jobs.get_by_id(job_id)
```

### `civitai.jobs.get_by_query`

Retrieve a collection of jobs by querying properties, e.g., userId. You can optionally include a `detailed` boolean flag to get detailed information about the jobs.

```python
query = {
    "properties": {
        "userId": 4  # Querying by userId
    }
}
detailed = False  # Optional boolean flag to get detailed job definitions. False by default.
response = civitai.jobs.get_by_query(query, detailed)
```

### `civitai.jobs.cancel`

Cancel a job by its jobId.

```python
response = civitai.jobs.cancel(job_id)
```

This method cancels a job that is currently scheduled or running. It requires the `jobId` of the job you wish to cancel. On successful cancellation, it returns a response object indicating the cancellation status.

### `civitai.models.get`

To check the coverage of specific models, you can use the `civitai.models.get` method. This method retrieves the availability of the requested models.

```python
models = [
    "urn:air:sd1:checkpoint:civitai:107842@275408",
    "urn:air:sd1:lora:civitai:162141@182559"
]
coverage = civitai.models.get(models)
print("Model coverage:", coverage)
```

### Contributing Your Changes

After making your changes:

1. Push your changes to your fork.
2. Open a pull request against the main repository.
3. Describe your changes and how they improve the project or fix issues.

Your contributions will be reviewed, and if accepted, merged into the project.

### Additional Guidelines

- Include unit tests for new features or bug fixes.
- Update the documentation if necessary.

Thank you for contributing to the Civitai Generator Python Client! 🥹🤭
