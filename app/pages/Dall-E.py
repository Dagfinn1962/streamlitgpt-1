import openai
import streamlit as st
import json
import requests


st.title("Dall-E Prompt")

response = ""

prompt = st.text_input("Input Text", label_visibility="visible")
# submit prompt to openai
if st.button("Submit"):
    with st.spinner("Wait for it..."):
        response = generation_response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024",
            response_format="url",
        )

if response:
    response_image_url = response["data"][0]["url"]  # extract image URL from response
    generated_image = requests.get(response_image_url).content

    placeholder = st.image(
        generated_image,
        caption=prompt,
        width=None,
        use_column_width=None,
        clamp=False,
        channels="RGB",
        output_format="auto",
    )
    st.json(json.dumps(response.to_dict()))
else:
    placeholder = st.empty()
