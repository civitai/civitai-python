import streamlit as st
import civitai

st.set_page_config(layout="wide")


def generate_image(input_data):
    """
    Generate an image using the Civitai SDK.

    :param input_data: The input parameters for the image generation.
    :return: The job result
    """
    try:
        output = civitai.image.create(input_data, wait=True)
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
        model = st.text_input(
            "Model URN", value="urn:air:sdxl:checkpoint:civitai:101055@128078")
        prompt = st.text_area("Prompt", value="A cat")
        negative_prompt = st.text_area("Negative Prompt", value="A dog")
        scheduler = st.selectbox(
            "Scheduler", ["EulerA", "HeunC", "Dopri5", "Bosh3"], index=0)
        steps = st.slider("Steps", min_value=1, max_value=100, value=30)
        cfg_scale = st.slider("CFG Scale", min_value=1, max_value=20, value=10)
        width = st.number_input("Width", min_value=1,
                                max_value=1024, value=768)
        height = st.number_input(
            "Height", min_value=1, max_value=1024, value=512)
        seed = st.number_input("Seed", value=-1)
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

    result = generate_image(input_data)

    if result:
        if 'jobs' in result and result['jobs'][0].get('result'):
            with col_image:
                st.image(result['jobs'][0]['result']['blobUrl'],
                         caption="Generated Image", use_column_width=True)
        else:
            with col_image:
                st.error("Failed to retrieve the generated image.")
