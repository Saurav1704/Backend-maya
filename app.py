# from dotenv import load_dotenv
# load_dotenv() # load all the environment variables

import streamlit as st
from langchain import prompts
import pandas as pd
from streamlit_feedback  import streamlit_feedback
# # import os
# import sqlite3
# import google.generativeai as genai
# import json
import methods
# Configure our api key

# with open('prompt.json', 'r') as jsonfile:
#     json_data = json.load(jsonfile)
#     print(json_data)



# genai.configure(api_key="AIzaSyA4wedlllm0xX9r7ERgbGQjQhM1Q3cIk6Y")

# # function  to load google gemini model and provide sql query as resposne 

# def get_gemini_response(question,prompt):
#     model = genai.GenerativeModel('gemini-pro')
#     response = model.generate_content([prompt[0],question])
#     return response.text

# function to retrieve the query from sql database

# def read_sql_query(sql, db):
#     conn = sqlite3.connect(db)
#     cur = conn.cursor()
#     cur.execute(sql)
#     rows=cur.fetchall()
#     conn.commit()
#     conn.close()
#     for row in rows:
#         print(row)
#     return rows

# Define Your prompt
# load the prompt from txt file
with open('prompts.txt', 'r') as file:
    prompts = file.read().strip()
# prompt=[
#     """You are an expert in converting English questions to SQL query!
#     The SQL database has the table name EKKO and has the following columns - EBELN(Purchase order), BUKRS(Company code), BSTYP(document type), AEDAT(document creation date), MATNR,
#     The SQL database has the table name MARA and has the following columns - MATNR(Material), MTART(material type), ERSDA(creation date), 
#     The SQL database has the table name EKKO and has the following columns - MATNR(Material), MAKTX(Material description),
#     SECTION \n\nFor example,\nExample 1 - How many entries of records are present?,
#     the SQL command will be something like this SELECT COUNT(*) FROM EKKO ;\n\nExample 2 - What are the records present in the table?,
#     the SQL command will be something like this SELECT * FROM EKKO ;\n\nExample 3 - What are the records where BUKRS is 5710?,
#     the SQL command will be something like this SELECT * FROM EKKO WHERE BUKRS = '5710';\n\nExample 4 - What are the records where BUKRS is 5710 and AEDAT is 20.12.2021?,
#     the SQL command will be something like this SELECT * FROM EKKO WHERE BUKRS = '5710' AND AEDAT = '20.12.2021';\n\n Example 5 - what is the creation date of the material used in the purchase order = '400000000',
#     the SQL command will be something like this SELECT MARA.ERSDA FROM EKKO INNER JOIN MARA ON EKKO.MATNR = MARA.MATNR WHERE EKKO.EBELN = '400000000';\n\n Example 6 - what is the description of the material used in the purchase order = '400000000',
#     the SQL command will be something like this SELECT MAKT.MATKX FROM EKKO INNER JOIN MARA ON EKKO.MATNR = MARA.MATNR AND INNER JOIN MAKT ON MARA.MATNR = MAKT.MATNR WHERE EKKO.EBELN = '400000000';
#     also the sql code should not have ``` in beginning or end and sql word in output  
#     """
# ]

## Streamlit App

# If __name__ == "__main__" :



# st.set_page_config(page_title="I can Retrieve Any SQL query")
# st.header("Local chatgpt")

# question=st.text_input("Input: ",key="input")

# submit=st.button("Ask the question")

# if submit is clicked
# if submit:
#     response= methods.get_gemini_response(question,prompt[0])
#     print(response)
#     try:
#         # response=read_sql_query(response,"EKKO.db")
#         # response=read_sql_query(response,"MARA.db")
#         response=methods.read_sql_query(response,"MAKT.db")
#         st.subheader("The Response is")
#         for row in response:
#             print(row)
#             st.header(row)
#     except :
#         # print('Sorry, I am not trained for the above question')
#         st.header('Sorry, I am not trained for the above question')

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to generate AI response (replace with your actual logic)
def generate_response(question):
    # ... (Your AI model or logic here)
    response_gemini = methods.get_gemini_response(question,prompts)
    
    try:
        query_result ,columns_names =  methods.read_sql_query(response_gemini,"Mydb.db")
        # response=read_sql_query(response,"EKKO.db")
        # response=read_sql_query(response,"MARA.db")
        df = pd.DataFrame(query_result, columns = columns_names)
        response = df.to_markdown(index=False)

        # if dtype(response) == 

        # st.subheader("The Response is")
        # for row in response:
            # print(row)
            # st.header(row)
    except :
        response = 'Sorry, I am not trained for the above question'
    return response

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if question := st.chat_input("Your message"):  
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": question})
    
    # Display user message in chat
    with st.chat_message("user"):
        st.markdown(question )

    # Generate AI response
    response = generate_response(question)

    # Add AI message to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
#     buttons = [
#                 {   "label": "👍",
#                     "value": "like",
#                     "style": { "border-radius": "22px", "padding": "1px" }
#                 },
#                 {   "label": "👎",
#                     "value": "dislike",
#                     "style": { "border-radius": "22px", "padding": "1px" }
#    }
# ]

# col = st.columns([92, 8])
# with col[1]:
#   returned = st_btn_group(buttons=buttons, key=message["query_id"], mode='radio',
#                           return_value=True)
    

    # Display AI message in chat
    with st.chat_message("assistant"):
        st.markdown(response)
    feedback = streamlit_feedback(feedback_type="thumbs")
