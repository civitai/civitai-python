# Civitai Image Generator Streamlit Demo

This Streamlit application demonstrates how to use the Civitai SDK to generate images based on user input.

## Installation

Before running the application, ensure you have Python installed on your system. This application has been tested with Python 3.7 and above.

To set up and run the application, follow these steps:

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Before running the application, you need to set up the `CIVITAI_API_TOKEN` environment variable. This token is required for authenticating requests to the Civitai API.

### For Unix/Linux/macOS:

```bash
export CIVITAI_API_TOKEN="your_civitai_api_token"
```

### For Windows:

```bash
set CIVITAI_API_TOKEN="your_civitai_api_token"
```

## Running the Application

To run the application, use the following command:

```bash
streamlit run app.py
```

Open your web browser and go to `http://localhost:8501` to view the app.
