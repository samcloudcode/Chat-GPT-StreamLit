import openai
import streamlit as st

# def generate_response(prompt):
#     completions = openai.Completion.create(
#         engine='text-davinci-003',
#         prompt=prompt,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.8,
#     )
#
#     message = completions.choices[0].text
#     return message


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

# {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
# {"role": "user", "content": "Where was it played?"}