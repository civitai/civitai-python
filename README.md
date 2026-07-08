# Civitai Python Client — Retired

> [!WARNING]
> **This project is no longer maintained and has been retired.**
>
> `civitai-py` was a hand-written Python client for Civitai's image-generation (orchestration) API. It has not been updated since June 2024, does not track the current API, and will receive no further fixes or releases. The `civitai-py` package on PyPI is frozen at its last version — do not use it for new projects.

## Use the official API

Civitai's APIs are now fully documented at **[developer.civitai.com](https://developer.civitai.com)**. They are plain HTTPS + JSON and work from any language, so there's no need for a bespoke SDK. Point your code — or your coding agent — at the docs and call the API directly.

| You want to… | Go here |
| --- | --- |
| Generate images, video, audio, and more (what this client did) | [Orchestration API guide](https://developer.civitai.com/orchestration/guide/) |
| Browse & search models, images, creators, tags | [Site API guide](https://developer.civitai.com/site/guide/) |
| Ready-made request examples per model | [Recipes](https://developer.civitai.com/orchestration/recipes/) |
| Connect an AI agent / assistant | [MCP server](https://developer.civitai.com/orchestration/mcp/) |
| Sign in users with their Civitai account | [OAuth guide](https://developer.civitai.com/site/oauth/) |

## Prefer a typed client? Generate one from the OpenAPI spec

The orchestration API publishes a live **OpenAPI 3.1 spec** that stays in sync with the API on every deploy. Instead of depending on a stale hand-written SDK, generate a fresh, fully-typed client for your language directly from it:

```
https://orchestration.civitai.com/openapi/v2-consumers.json
```

**Python** ([openapi-python-client](https://github.com/openapi-generators/openapi-python-client)):

```bash
pipx run openapi-python-client generate \
  --url https://orchestration.civitai.com/openapi/v2-consumers.json
```

**Any language** ([openapi-generator](https://openapi-generator.tech/)):

```bash
openapi-generator-cli generate \
  -i https://orchestration.civitai.com/openapi/v2-consumers.json \
  -g python \
  -o ./civitai-orchestration-client
```

The generated client is always current, unlike this repo. A browsable reference built from the same spec lives at [developer.civitai.com/orchestration/reference](https://developer.civitai.com/orchestration/reference/).

## Quick start (raw HTTP)

1. Grab an API key from your [Civitai account settings](https://civitai.com/user/account).
2. Submit a workflow to the orchestration API with a bearer token:

```bash
curl -X POST "https://orchestration.civitai.com/v2/consumer/workflows?wait=60" \
  -H "Authorization: Bearer $CIVITAI_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "steps": [{
      "$type": "imageGen",
      "input": {
        "engine": "sdcpp",
        "ecosystem": "sd1",
        "operation": "createImage",
        "model": "urn:air:sd1:checkpoint:civitai:4384@128713",
        "prompt": "masterpiece, best quality, portrait, cinematic lighting",
        "negativePrompt": "worst quality, low quality, blurry",
        "width": 512,
        "height": 512,
        "steps": 20,
        "cfgScale": 7
      }
    }]
  }'
```

See the [recipes](https://developer.civitai.com/orchestration/recipes/) for per-model request bodies (Flux, SDXL, WAN video, upscalers, TTS, transcription) and [authentication](https://developer.civitai.com/orchestration/guide/authentication) for token handling.

## Building an AI agent?

Point it at the **[Civitai MCP server](https://developer.civitai.com/orchestration/mcp/)** rather than writing a client by hand. There's also a machine-readable index of the docs at [developer.civitai.com/llms.txt](https://developer.civitai.com/llms.txt) (and [llms-full.txt](https://developer.civitai.com/llms-full.txt)) for feeding into LLM tools.

---

The original SDK source remains in this repository's history for reference only. It is unsupported.
