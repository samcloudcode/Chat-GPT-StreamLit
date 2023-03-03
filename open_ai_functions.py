import openai
import streamlit as st


def get_one_shot_response(system_message, user_message):
    openai.api_key = st.secrets['SECRET_KEY']
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message},
        ]
    )
    return response['choices'][0]['message']['content']
