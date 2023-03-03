import streamlit as st
from open_ai_functions import get_one_shot_response
import data

st.title("AI Career Advisor")

# Store chat
if 'prompt' not in st.session_state:
    st.session_state['prompt'] = {}

if 'feedback' not in st.session_state:
    st.session_state['feedback'] = ""


st.session_state.prompt['name'] = st.text_input("What's your name?")

st.session_state.prompt['strengths'] = st.multiselect('Please share some of your strengths, '
                                                      'either from CliftonStrengths, or others you relate to:',
                                                      data.clifton_strengths_list)

st.session_state.prompt['experience'] = st.text_input("Please share your work experience in a few lines, "
                                                      "if you are currently working include this:")

st.session_state.prompt['skills'] = st.text_input("Please share any skills you want to highlight: ")

st.session_state.prompt['education'] = st.text_input("What did you study and to what level of Education? ",
                                                     placeholder="e.g. Masters in Chemistry at University")

st.session_state.prompt['requests'] = st.text_input("Please share any general requests, for example "
                                                    "things you like or dislike doing, or specific "
                                                    "areas that interest you.", placeholder="e.g. I really don't "
                                                    "like spreadsheets, but I love the idea of going to space.")

st.session_state.prompt['impact'] = st.checkbox("Careers with positive impact")
st.session_state.prompt['future'] = st.checkbox("Careers that are future proof")
st.session_state.prompt['novel'] = st.checkbox("Unusual suggestions I may not have thought of")
st.session_state.prompt['count'] = st.slider("How many suggestions would you like? "
                                             "Fewer will give more detailed responses.", min_value=1, max_value=10)

print(st.session_state.prompt['impact'], st.session_state.prompt['future'], st.session_state.prompt['novel'])

system_message = "You are an expert, friendly and professional career advisor called Sam."
user_input = "My name is " + st.session_state.prompt['name'] + ". This my background:" \
             + "\n" + "CliftonStrengths: " + ", ".join(st.session_state.prompt['strengths']) \
             + "\n" + "Education: " + st.session_state.prompt['education'] \
             + "\n" + "Career experience: " + st.session_state.prompt['experience'] \
             + "\n" + "Skills: " + st.session_state.prompt['skills'] + "." + "\n" \
             + st.session_state.prompt['requests'] + "." + "\n" \
             + "Suggest " + str(st.session_state.prompt['count']) \
             + " of the most interesting and relevant careers I could consider, ranked by personal fit, " \
               "with detailed reasoning for each. The suggestions should make use " \
               "of my strengths, education, career experience and skills. "

if st.session_state.prompt['impact']:
    user_input = user_input + "The career suggestions should make a positive impact on the world. "

if st.session_state.prompt['future']:
    user_input = user_input + "The career suggestions should be future proof. "

if st.session_state.prompt['novel']:
    user_input = user_input + "The career suggestions should be unusual and ones I have not thought of. "


user_input = user_input + "Include a brief introduction and format simply using Github-flavored Markdown. " \


print(user_input)

if st.button("Submit"):
    output = get_one_shot_response(system_message, user_input)
    st.session_state.feedback = output

if st.session_state['feedback']:
    st.markdown(st.session_state.feedback)
