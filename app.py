# from generate import generate_response
from speech import recognize_speech
from utils import set_front_page
from output import show_output  


import streamlit as st

#This is the session state of streamlit to control streamlit flow and variable initialization
if "messages" not in st.session_state:
    st.session_state.messages = []
if "greeting_shown" not in st.session_state:
    st.session_state.greeting_shown = False
if "front_loaded" not in st.session_state:
    st.session_state.greeting_shown = False

# load front_end
set_front_page(st)

#Get user input
question = st.chat_input("")
if st.button("🎙️", help='Click this button to perform an action'):
    question = recognize_speech(st)
# elif st.chat_input(""):
#     question = st.chat_input("")

# generate content
if question:
# display content
    show_output(st , question)
