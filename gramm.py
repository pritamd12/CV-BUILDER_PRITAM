import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

st.set_page_config(
    page_title="AI Grammar Corrector",
    page_icon="✍️"
)

st.title("✍️ AI Grammar Corrector")
st.write("Enter an English sentence and correct its grammar.")

text = st.text_area(
    "Enter your sentence:",
    placeholder="She go to college every day."
)

if st.button("Correct Grammar"):

    if text.strip() == "":
        st.warning("Please enter a sentence.")

    elif not api_key:
        st.error("GROQ_API_KEY is missing from the .env file.")

    else:
        try:
            client = Groq(api_key=api_key)

            with st.spinner("Correcting..."):
                response = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "Correct the grammar, spelling and punctuation "
                                "of the user's English sentence. Keep the original "
                                "meaning. Return only the corrected sentence."
                            )
                        },
                        {
                            "role": "user",
                            "content": text
                        }
                    ],
                    temperature=0
                )

            corrected_text = response.choices[0].message.content

            st.success("Corrected Sentence:")
            st.write(corrected_text)

        except Exception as error:
            st.error(f"Error: {error}")