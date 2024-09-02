from flask import Flask, request, jsonify
from flask_cors import CORS
from Database import  get_data_from_query
from api import get_data_from_url

# from generate import generate_response, get_gemini_response, get_prompts
import google.generativeai as genai
app = Flask(__name__)
CORS(app)

prompt_set = False # Status to check if prompt file is selected or not
greeting_set = False # Status to check if greeting is shown or not
def generate_response(question, filename ):
    genai.configure(api_key="AIzaSyA4wedlllm0xX9r7ERgbGQjQhM1Q3cIk6Y")

    if question.lower() in ["hello", "hi", "who are you"]:
        greeting_msg = get_gemini_response(question ,filename = 'prompt_greeting.txt')
    elif filename == 'prompt_bom.txt':
        url = get_gemini_response(question ,filename = filename,)
        base_url = "http://slnxsaps4h15.marc.fr.ssg:50000/sap/opu/odata/sap/BILLOFMATERIALV2_SRV"
    elif filename == 'prompt_po.txt':
        url = get_gemini_response(question ,filename = filename,)
        base_url = "po_url"
    elif filename == 'prompt_sql.txt':
        query  = get_gemini_response(question ,filename = filename)

    url = url.replace("base_url", base_url)
    return greeting_msg ,url ,query

def get_prompts(file_name):
    # To set file name of the file  
    with open(file_name , 'r') as file:
        prompts = file.read().strip()
        # print(prompts)
    return prompts


def get_gemini_response(question,filename):
    # To set file name of the file
    prompts = get_prompts(file_name = filename)
    #generate gemini response
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompts,question])
    print(response.text)
    return response.text


@app.route('/api/generate-response', methods=['POST'])
def api_generate_response():
    data = request.json
    # print(data)
    question = data.get('question')
    filename = data.get('filename')
    print(question)
    response_greet , response_url ,response_query = generate_response(question, filename)
    if response_greet is None and response_url is not None:
        columns , data = get_data_from_url(response_url)
    elif response_greet is not None and response_query is None:
        columns , data = get_data_from_query(response_query)

    return jsonify({"greet": response_greet , "columns" : columns , "data" : data})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
