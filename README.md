# Civitai Generator Python Client

A Python client for Civitai's generator to run Civitai models from your Python code.

## Quick Start

To get started with the Civitai Generator Python Client, you can use the following resources:

- **Google Colab Notebook**: Jump into a pre-configured environment with a live notebook to try out the Civitai SDK.

  <a target="_blank" href="https://colab.research.google.com/github/civitai/civitai-python/blob/main/examples/text2img.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

- **Streamlit Demo**: See the Civitai SDK in action with a live Streamlit app demo. [View Streamlit Demo](https://civitai.streamlit.app/)

## Installation

```python
pip install civitai-py
```

## Authenticate

Before running any Python scripts that use the API, you need to set your Civitai API token in your environment.

Grab your token from [your Civitai account](https://civitai.com/user/account) and set it as an environment variable:

```bash
export CIVITAI_API_TOKEN=<your token>
```

## Requirements

- Python 3.7+

## Usage

#### Import the Civitai SDK:

```python
import civitai
```

#### Create a txt2img job:

```python
input = {
    "model": "urn:air:sd1:checkpoint:civitai:4384@128713",
    "params": {
        "prompt": "RAW photo, face portrait photo of woman, wearing black dress, happy face, hard shadows, cinematic shot, dramatic lighting",
        "negativePrompt": "(deformed, distorted, disfigured:1.3)",
        "scheduler": "EulerA",
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
response = civitai.image.create(input)
```

Then, fetch the result later:

```python
response = civitai.jobs.get(token=response.token)
```

Or wait for the job to finish by running the generation in the background a.k.a long polling. You can add the `wait=True` flag to the method. It has a default timeout of 5 minutes.

```python
response = civitai.image.create(input, wait=True)
```

### Using Additional Networks

The SDK supports additional networks: LoRA, VAE, Hypernetwork, Textual Inversion, LyCORIS, Checkpoint, and LoCon.

To use any of the networks availabe on Civitai, simply add the `additionalNetworks` field into the input:

```python
input = {
    "model": "urn:air:sd1:checkpoint:civitai:4384@128713",
    "params": {
        "prompt": "masterpiece, best quality, 1girl, IncrsAhri, multiple tails, fox tail, korean clothes, skirt, braid, arms behind back",
        "negativePrompt": "(worst quality:1.4), (low quality:1.4), simple background, bad anatomy",
        "scheduler": "EulerA",
        "steps": 25,
        "cfgScale": 7,
        "width": 512,
        "height": 768,
        "seed": -1,
        "clipSkip": 2
    },
    "additionalNetworks": {
        # Detail enhancer LoRA: https://civitai.com/models/82098/add-more-details-detail-enhancer-tweaker-lora
        "urn:air:sd1:lora:civitai:82098@87153": {
            "strength": 1.0
        }
    }
}
```

In the case of `Lora` and `LoCon` networks, set the `strength` of the network; for `TextualInversion`, set the `triggerWord` of the network.

<br/>

### `civitai.image.create`

Run a model with inputs you provide.

```python
response = civitai.image.create(options)
```

| name                    | type                                                                      | description                                                                                                                                                                                                                                                                                                                               |
| ----------------------- | ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `model`                 | string \| null                                                            | **Required**. The Civitai model to use for generation.                                                                                                                                                                                                                                                                                    |
| `params.prompt`         | string \| null                                                            | **Required**. The main prompt for the image generation.                                                                                                                                                                                                                                                                                   |
| `params.negativePrompt` | string \| null                                                            | Optional. The negative prompt for the image generation.                                                                                                                                                                                                                                                                                   |
| `params.scheduler`      | [Scheduler](civitai/models/Scheduler.py) \| null                          | Optional. The scheduler algorithm to use. <br/> <br/>Possible values are: `EulerA`, `Euler`, `LMS`, `Heun`, `DPM2`, `DPM2A`, `DPM2SA`, `DPM2M`, `DPMSDE`, `DPMFast`, `DPMAdaptive`, `LMSKarras`, `DPM2Karras`, `DPM2AKarras`, `DPM2SAKarras`, `DPM2MKarras`, `DPMSDEKarras`, `DDIM`, `PLMS`, `UniPC`, `Undefined`, `LCM`, `DDPM`, `DEIS`. |
| `params.steps`          | number \| null                                                            | Optional. The number of steps for the image generation process.                                                                                                                                                                                                                                                                           |
| `params.cfgScale`       | number \| null                                                            | Optional. The CFG scale for the image generation.                                                                                                                                                                                                                                                                                         |
| `params.width`          | number                                                                    | **Required**. The width of the generated image.                                                                                                                                                                                                                                                                                           |
| `params.height`         | number                                                                    | **Required**. The height of the generated image.                                                                                                                                                                                                                                                                                          |
| `params.seed`           | number \| null                                                            | Optional. The seed for the image generation process.                                                                                                                                                                                                                                                                                      |
| `params.clipSkip`       | number \| null                                                            | Optional. The number of CLIP skips for the image generation.                                                                                                                                                                                                                                                                              |
| `callbackUrl`           | string \| null                                                            | Optional. URL that will be invoked upon completion of this job                                                                                                                                                                                                                                                                            |
| `additionalNetworks`    | [ImageJobNetworkParams](civitai/models/ImageJobNetworkParams.py) \| null  | Optional. An associative list of additional networks, keyed by the AIR of the network. Each network is of type [AssetType](civitai/models/asset_type.py).                                                                                                                                                                                 |
| `controlNets`           | Array<[ImageJobControlNet](civitai/models/ImageJobControlNet.py)> \| null | Optional. An associative list of additional networks.                                                                                                                                                                                                                                                                                     |

#### Additional Networks

| `additionalNetworks` | Record<string, [ImageJobNetworkParams](civitai/models/ImageJobNetworkParams.py)> | Optional. An associative list of additional networks, keyed by the AIR of the network. Each network is described by an `ImageJobNetworkParams` object. |
| -------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `strength`           | number                                                                           | Optional. In case of Lora and LoCon, set the strength of the network.                                                                                  |
| `triggerWord`        | string                                                                           | Optional. In case of a TextualInversion, set the trigger word of the network.                                                                          |

#### ControlNets

| `controlNets`  | Array<[ImageJobControlNet](civitai/models/ImageJobControlNet.py)> | Optional. An array of control networks that can be applied to the image generation process. <br/><br/>Each `ImageJobControlNet` object in the array can have the following properties: |
| -------------- | ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `preprocessor` | [ImageTransformer](civitai/models/ImageTransformer.py) \| null    | Optional. Specifies the image transformer to be applied as a preprocessor. <br/><br/>Possible values are `Canny`, `DepthZoe`, `SoftedgePidinet`, `Rembg`.                              |
| `weight`       | number \| null                                                    | Optional. The weight of the control net.                                                                                                                                               |
| `startStep`    | number \| null                                                    | Optional. The step at which the control net starts to apply.                                                                                                                           |
| `endStep`      | number \| null                                                    | Optional. The step at which the control net stops applying.                                                                                                                            |
| `imageUrl`     | string \| null                                                    | Optional. The URL of the image associated with the controlnet.                                                                                                                         |

### `civitai.jobs.get`

Fetches job details based on a provided token or job ID. If both are provided, the token takes precedence.

```python
job_id = "your_job_id_here"
response = civitai.jobs.get(job_id=job_id)

# OR

token = "your_token_here"
response = civitai.jobs.get(token=token)

# OR

response = civitai.jobs.get(token=token, job_id=job_id)
```

### `civitai.jobs.query`

Retrieve a collection of jobs by querying properties, e.g., userId. You can optionally include a `detailed` boolean flag to get detailed information about the jobs.

```python
query = {
    "properties": {
        "userId": 4  # Querying by userId
    }
}

detailed = False  # Optional boolean flag to get detailed job definitions. False by default.

response = civitai.jobs.query(detailed=detailed, query_jobs_request=query)
```

### `civitai.jobs.cancel`

Cancel a job by its jobId.

```python
response = civitai.jobs.cancel(job_id)

```

This method cancels a job that is currently scheduled or running. It requires the `jobId` of the job you wish to cancel. On successful cancellation, it returns a response object indicating the cancellation status.

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
