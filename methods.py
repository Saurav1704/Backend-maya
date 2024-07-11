import streamlit as st
import sqlite3
import google.generativeai as genai
from hdbcli import dbapi  
# Import SAP HANA client

# Call Gemini API 
genai.configure(api_key="AIzaSyA4wedlllm0xX9r7ERgbGQjQhM1Q3cIk6Y")

# function  to load google gemini model and takes prompt as input 

def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt,question])
    return response.text
# Below function takes query and db and return datarecords as rows
def read_sql_query(sql, db):
    desc = {
        "EBELN" :"Document Number",
        "MATNR" :"Material",
        "MAKTX" :"Material Description",
        "BUKRS" :"Company code",
        "AEDAT" :"Document Creation Date",
        "BSTYP" :"Document Type",
        "MTART" :"Material Type",
        "ERSDA" :"Material Creation Date",
    }
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    column_names = [desc[description[0]] for description in cur.description]  # Get column names
    conn.commit()
    conn.close()
    # for row in rows:
    #     print(row)
    return rows, column_names

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