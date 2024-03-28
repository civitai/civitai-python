import streamlit as st
import civitai


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

with st.form("image_gen_form"):
    model = st.text_input("Model URN", value="urn:air:sd1:checkpoint:civitai:4201@130072")
    prompt = st.text_area("Prompt", value="A cat")
    wait_for_completion = st.checkbox("Wait for completion", value=True)
    submit_button = st.form_submit_button("Generate Image")

if submit_button:
    input_data = {
        "model": model,
        "params": {
            "prompt": prompt,
            # Add other parameters as needed
        },
    }

    result = generate_image(input_data, wait_for_completion)

    if result:
        if wait_for_completion:
            if 'jobs' in result and result['jobs'][0].get('result'):
                st.image(result['jobs'][0]['result']['blobUrl'], caption="Generated Image")
            else:
                st.error("Failed to retrieve the generated image.")
        else:
            st.success(f"Job submitted. Token: {result.get('token')}")
