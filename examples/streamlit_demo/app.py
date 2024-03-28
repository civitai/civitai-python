import streamlit as st
import civitai_py as civitai

st.set_page_config(layout="wide")


def generate_image(input_data, wait_for_completion):
    """
    Generate an image using the Civitai SDK.

    :param input_data: The input parameters for the image generation.
    :param wait_for_completion: Whether to wait for the job to complete before returning the result.
    :return: The job result if wait_for_completion is True, otherwise the job token.
    """
    try:
        output = civitai.image.create(input_data, wait=wait_for_completion)
        return output
    except Exception as e:
        st.error(f"Failed to generate image: {str(e)}")
        return None


# Streamlit UI
st.title("Civitai Image Generator")

# Create two columns for inputs and image display
col_input, col_image = st.columns([2, 3])

with col_input:
    with st.form("image_gen_form"):
        model = st.text_input("Model URN", value="urn:air:sd1:checkpoint:civitai:4201@130072")
        prompt = st.text_area("Prompt", value="A cat")
        negative_prompt = st.text_area("Negative Prompt", value="A dog")
        scheduler = st.selectbox("Scheduler", ["EulerA", "HeunC", "Dopri5", "Bosh3"], index=0)
        steps = st.slider("Steps", min_value=1, max_value=100, value=30)
        cfg_scale = st.slider("CFG Scale", min_value=1, max_value=20, value=10)
        width = st.number_input("Width", min_value=1, max_value=1024, value=768)
        height = st.number_input("Height", min_value=1, max_value=1024, value=512)
        seed = st.number_input("Seed", value=-1)
        wait_for_completion = st.checkbox("Wait for completion", value=True)
        submit_button = st.form_submit_button("Generate Image")

if submit_button:
    input_data = {
        "model": model,
        "params": {
            "prompt": prompt,
            "negativePrompt": negative_prompt,
            "scheduler": scheduler,
            "steps": steps,
            "cfgScale": cfg_scale,
            "width": width,
            "height": height,
            "seed": seed,
        },
    }

    result = generate_image(input_data, wait_for_completion)

    if result and wait_for_completion:
        if 'jobs' in result and result['jobs'][0].get('result'):
            with col_image:
                st.image(result['jobs'][0]['result']['blobUrl'],
                         caption="Generated Image", use_column_width=True)
        else:
            with col_image:
                st.error("Failed to retrieve the generated image.")
    elif result and not wait_for_completion:
        with col_image:
            st.success(f"Job submitted. Token: {result.get('token')}")
