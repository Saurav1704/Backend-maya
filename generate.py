# import streamlit as st
# import sqlite3
import google.generativeai as genai
# from hdbcli import dbapi  
# import pandas as pd
# from st_aggrid import AgGrid, GridOptionsBuilder, AgGridTheme
# import speech_recognition as sr
# from pydub import AudioSegment
# from pydub.playback import play
 
def generate_response(question):
    prompts , greet  = get_prompts()
    genai.configure(api_key="AIzaSyA4wedlllm0xX9r7ERgbGQjQhM1Q3cIk6Y")

    if question.lower() in ["hello", "hi", "who are you"]:
        text = get_gemini_response(greet, question)
    else:
        text = get_gemini_response(prompts, question)
    base_url = "http://slnxsaps4h15.marc.fr.ssg:50000/sap/opu/odata/sap/BILLOFMATERIALV2_SRV"
    text = text.replace("base_url", base_url)
    return text

# function  to load google gemini model and takes prompt as input 
def get_prompts():
    
    with open('prompt_api.txt', 'r') as file:
        prompts = file.read().strip()
    with open('prompt_greeting.txt', 'r') as file_greet:
        greet = file_greet.read().strip()
    # prompts = prompts.replace("base_url", base_url)
    # print(prompts)
    return prompts,greet

def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt,question])
    return response.text



# import ctypes
# from transformers import BertTokenizer, BertForSequenceClassification
# import torch

# ctypes.windll.LoadLibrary("C://Users//nitiskumar//AppData//Local//anaconda3//Lib//site-packages//torch//lib//fbgemm.dll")
# # Load pre-trained model and tokenizer
# tokenizer = BertTokenizer.from_pretrained('huawei-noah/TinyBERT_General_4L_312D')
# model = BertForSequenceClassification.from_pretrained('huawei-noah/TinyBERT_General_4L_312D')

# def generate_response(question):
#     prompts, greet = get_prompts()

#     if question.lower() in ["hello", "hi", "who are you"]:
#         text = get_tinybert_response(greet, question)
#     else:
#         text = get_tinybert_response(prompts, question)
#     return text

# # function to load prompts from files
# def get_prompts():
#     with open('prompts_api.txt', 'r') as file:
#         prompts = file.read().strip()
#     with open('prompt_greeting.txt', 'r') as file_greet:
#         greet = file_greet.read().strip()
#     return prompts, greet

# def get_tinybert_response(prompt, question):
#     inputs = tokenizer(prompt + " " + question, return_tensors='pt')
#     outputs = model(**inputs)
#     logits = outputs.logits
#     predicted_class_id = torch.argmax(logits).item()
#     return tokenizer.decode(predicted_class_id)


   
    # query_result, column_names, error = read_sql_query(response_gemini, "MYdb.db")
    # if error:
    #     return pd.DataFrame(), f"An error occurred: {error}"
   
    # if query_result:
    #     df = pd.DataFrame(query_result, columns=column_names)
    #     response_df = df
    #     response_md = df.to_markdown(index=False)
    # else:
    #     response_df = pd.DataFrame()
    #     response_md = "No results found."
    # return response_df, response_md

# def recognize_speech():
#     recognizer = sr.Recognizer()
#     microphone = sr.Microphone()
 
#     with microphone as source:
#         st.write("Listening...")
#         audio = recognizer.listen(source)
 
#     try:
#         st.write("Recognizing...")
#         text = recognizer.recognize_google(audio)
#         st.write(f"Recognized text: {text}")
#         return text
#     except sr.UnknownValueError:
#         st.write("Sorry, I could not understand the audio.")
#         return ""
#     except sr.RequestError as e:
#         st.write(f"Could not request results; {e}")
#         return ""
    # r = sr.Recognizer()
    # with st.chat_message("user"):
    #     with sr.Microphone() as source:
    #         st.write("Listening...")
    #         audio = r.listen(source)

    #     try:
    #         text = r.recognize_google(audio)
    #         return text
    #     except sr.UnknownValueError:
    #         st.write("Sorry, could not understand audio")
    #     except sr.RequestError as e:
    #         st.write("Could not request results; {0}".format(e))



# def pagination_of_data(df):
#     gb = GridOptionsBuilder.from_dataframe(df)
#     gb.configure_pagination(paginationPageSize=10)
#     gb.configure_default_column(enablePivot=True, enableValue=True, enableRowGroup=True, filter=True)
#     grid_options = gb.build()
#     grid_response = AgGrid(
#                             df,
#                             gridOptions=grid_options,
#                             enable_enterprise_modules=True,
#                             theme=AgGridTheme.STREAMLIT,
#                             fit_columns_on_grid_load=True,
#                             update_mode='MODEL_CHANGED' )
    
# def assistant_response(st,df):
#     tab1, tab2 = st.tabs(["Tabular Data", "Graphical Representation"])
#     with tab1:
#             # Configure AgGrid options  
#             pagination_of_data(df = df)    
#     with tab2:
#             if not df.empty:
#                 if len(df.columns) == 2 and df.dtypes[1] in ['int64', 'float64']:
#                     st.bar_chart(data= df.set_index(df.columns[0]))
#                 else:
#                     st.write("The data is not suitable for a Bar chart.")
#             else:
#                 st.write("No data available to display.")


# def read_sql_query(sql, host, port, user, password, database):
#     conn = dbapi.connect(
#        address="dc3",
#         port=140,
#         user="DIT000071A",
#         password="SauravSopra@2023",
#         databaseName="MARA"
#     )
#     cur = conn.cursor()
#     cur.execute(sql)
#     rows = cur.fetchall()
#     column_names = [description[0] for description in cur.description]  # Get column names
#     conn.commit()
#     conn.close()
#     return rows, column_names