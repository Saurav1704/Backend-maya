# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from database import  get_data_from_query
# from api import get_data_from_url

# # from generate import generate_response, get_gemini_response, get_prompts
# import google.generativeai as genai
# app = Flask(__name__)
# app.config['prompt_file'] = ''
# CORS(app)

# def generate_response(question, filename ):
#     genai.configure(api_key="AIzaSyAFl6pYoPmFtP_0F_M0sfQ-HAJu-k5uk2M")
#     greeting_msg = url = base_url = query = ''
#     if question.lower() in ["hello", "hi", "who are you"]:
#         greeting_msg = get_gemini_response(question ,filename = 'prompt_greeting.txt')
#     elif filename == "prompt_bom.txt":
#         url = get_gemini_response(question ,filename = filename,)
#         base_url = "http://slnxsaps4h19.marc.fr.ssg:50000/sap/opu/odata/sap/BILLOFMATERIALV2_SRV"
#         url = url.replace("base_url", base_url)
#     elif filename == "prompt_po.txt":
#         url = get_gemini_response(question ,filename = filename,)
#         base_url = "http://slnxsaps4h19.marc.fr.ssg:50000/sap/opu/odata/sap"
#         url = url.replace("base_url", base_url)
#     elif filename == "prompt_query.txt":
#         query  = get_gemini_response(question ,filename = filename)
#     return greeting_msg ,url ,query

# def get_prompts(file_name):
#     # To set file name of the file  
#     with open(file_name , 'r') as file:
#         prompts = file.read().strip()
#         # print(prompts)
#     return prompts


# def get_gemini_response(question,filename):
#     # To set file name of the file
#     prompts = get_prompts(file_name = filename)
#     #generate gemini response
#     model = genai.GenerativeModel('gemini-1.5-pro')
#     response = model.generate_content([prompts,question])
#     print(response.text)
#     return response.text or ""


# @app.route('/api/generate-response', methods=['POST'])
# def api_generate_response():
#     # columns = data = []
#     data = request.json
#     # print(data)
#     question = data.get('question')
#     filename = data.get('filename')
#     columns = data = []
#     response_greet , response_url ,response_query = generate_response(question, filename)
#     if response_greet =="" and response_url != "":
#         columns , data = get_data_from_url(response_url  , filename)
#     elif response_greet =="" and response_query !="":
#         columns , data = get_data_from_query(response_query)

#     return jsonify({"greet": response_greet , "columns" : columns , "data" : data})


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)

# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from database import get_data_from_query
# from api import get_data_from_url
# from transformers import AutoModelForCausalLM, AutoTokenizer
# from huggingface_hub import login
# import torch

# app = Flask(__name__)
# app.config['prompt_file'] = ''
# CORS(app)

# access_token = "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"
# login(token=access_token)
# # Load the Meta-Llama model and tokenizer
# model_name = "meta-llama/Meta-Llama-3.1-8B-Instruct"
# tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=access_token)
# model = AutoModelForCausalLM.from_pretrained(model_name, use_auth_token=access_token)

# def generate_llama_response(question, filename):
#     greeting_msg = url = base_url = query = ''
#     if question.lower() in ["hello", "hi", "who are you"]:
#         greeting_msg = get_llama_response(question, filename='prompt_greeting.txt')
#     elif filename == "prompt_bom.txt":
#         url = get_llama_response(question, filename=filename)
#         base_url = "http://slnxsaps4h15.marc.fr.ssg:50000/sap/opu/odata/sap/BILLOFMATERIALV2_SRV"
#         url = url.replace("base_url", base_url)
#     elif filename == "prompt_po.txt":
#         url = get_llama_response(question, filename=filename)
#         base_url = "http://slnxsaps4h15.marc.fr.ssg:50000/sap/opu/odata/sap"
#         url = url.replace("base_url", base_url)
#     elif filename == "prompt_query.txt":
#         query = get_llama_response(question, filename=filename)
#     return greeting_msg, url, query

# def get_prompts(file_name):
#     # To set file name of the file  
#     with open(file_name, 'r') as file:
#         prompts = file.read().strip()
#     return prompts

# def get_llama_response(question, filename):
#     # To set file name of the file
#     prompts = get_prompts(file_name=filename)
#     input_text = f"{prompts}\n{question}"
    
#     # Tokenize input and generate response from LLaMA model
#     inputs = tokenizer(input_text, return_tensors="pt")
#     outputs = model.generate(**inputs, max_length=512, num_return_sequences=1)
    
#     # Decode and return response text
#     response = tokenizer.decode(outputs[0], skip_special_tokens=True)
#     print(response)
#     return response or ""

# @app.route('/api/generate-response', methods=['POST'])
# def api_generate_response():
#     data = request.json
#     question = data.get('question')
#     filename = data.get('filename')
#     columns = data = []
#     response_greet, response_url, response_query = generate_llama_response(question, filename)
    
#     if response_greet == "" and response_url != "":
#         columns, data = get_data_from_url(response_url, filename)
#     elif response_greet == "" and response_query != "":
#         columns, data = get_data_from_query(response_query)

#     return jsonify({"greet": response_greet, "columns": columns, "data": data})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)



from flask import Flask, request, jsonify
from flask_cors import CORS
from database import get_data_from_query
from api import get_data_from_url
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer
import requests

app = Flask(__name__)
app.config['prompt_file'] = ''
CORS(app, supports_credentials=True)

# Load the FLAN-T5 model and tokenizer
model_name = "google/flan-t5-large"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def get_prompts(file_name):
    # To read the prompt from the file
    try:
        with open(file_name, 'r') as file:
            prompts = file.read().strip()
        return prompts
    except FileNotFoundError:
        return "Prompt file not found."

def get_flan_response(question, filename):
    prompts = get_prompts(file_name=filename)
    input_text = f"{prompts} {question}"
    inputs = tokenizer(input_text, return_tensors="pt")
    # inputs = tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True)
    inputs = {k: v.to(device) for k, v in inputs.items()}
    outputs = model.generate(**inputs, max_length=512)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

# If the response starts with 'Output:', clean it up
    if response.startswith("Output:"):
        response = response.replace("Output:", "").strip()

    return response

def generate_response(question, filename):
    greeting_msg = url = base_url = query = ''
    
    if question.lower() in ["hello", "hi", "who are you",  "how are you", "kese ho"]:
        greeting_msg = get_flan_response(question, filename='prompt_greeting.txt')
    
    elif filename == "prompt_bom.txt":
        url = get_flan_response(question, filename=filename)
        base_url = "https://slnxsaps4h19.marc.fr.ssg:44300/sap/opu/odata/sap/BILLOFMATERIALV2_SRV"
        url = url.replace("base_url", base_url)
    
    elif filename == "prompt_po.txt":
        url = get_flan_response(question, filename=filename)
        base_url = "https://slnxsaps4h19.marc.fr.ssg:44300/sap/opu/odata/sap/C_PURCHASEORDER_FS_SRV"
        url = url.replace("base_url", base_url)
    
    elif filename == "prompt_query.txt":
        
        query = get_flan_response(question, filename=filename)
        print(query)
    
    return greeting_msg, url, query

@app.route('/api/generate-response', methods=['POST'])
def api_generate_response():
    data = request.json
    question = data.get('question')
    filename = data.get('filename')
    
    # Generate the response based on the question and filename
    response_greet, response_url, response_query = generate_response(question, filename)
    
    columns = data = []
    
    if response_greet == "" and response_url != "":
        columns, data = get_data_from_url(response_url, filename)
    
    elif response_greet == "" and response_query != "":
        columns, data = get_data_from_query(response_query)
    
    return jsonify({
        "greet": response_greet, 
        "columns": columns, 
        "data": data,
        "url": response_url,  # Include URL for debugging
        "query": response_query  # Include query for debugging
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from database import get_data_from_query
# from api import get_data_from_url
# from transformers import AutoTokenizer, AutoModelForCausalLM, LlamaConfig
# import torch

# app = Flask(__name__)
# CORS(app)

# # Load the LLaMA 3.1 model and tokenizer
# model_name = "meta-llama/Llama-3.1-8B"  # Ensure this model exists on Hugging Face
# config = LlamaConfig.from_pretrained(model_name)
# config.rope_scaling = {"type": "dynamic", "factor": 1.0}
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(model_name, config=config)
# # model = AutoModelForCausalLM.from_pretrained(
# #     model_name,
# #     device_map="auto",
# #     torch_dtype=torch.float16
# # )

# def get_prompts(file_name):
#     try:
#         with open(file_name, 'r') as file:
#             return file.read().strip()
#     except FileNotFoundError:
#         return "Prompt file not found."

# def get_llama_response(question, filename):
#     prompts = get_prompts(file_name=filename)
#     input_text = f"{prompts}\n{question}"
    
#     inputs = tokenizer(input_text, return_tensors="pt", truncation=True, max_length=2048)
#     inputs = {k: v.to(model.device) for k, v in inputs.items()}
    
#     outputs = model.generate(
#         **inputs,
#         max_new_tokens=2048,  # Adjust for your required response length
#         do_sample=True,
#         top_p=0.9,
#         temperature=0.7
#     )
#     response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
#     # Extract and clean the response
#     response = response.replace(prompts, "").strip()
#     return response

# def generate_response(question, filename):
#     greeting_msg = url = query = ''
    
#     if question.lower() in ["hello", "hi", "who are you", "how are you", "kese ho"]:
#         greeting_msg = get_llama_response(question, filename="prompt_greeting.txt")
    
#     elif filename == "prompt_bom.txt":
#         url = get_llama_response(question, filename=filename)
#         base_url = "https://slnxsaps4h19.marc.fr.ssg:44300/sap/opu/odata/sap/BILLOFMATERIALV2_SRV"
#         url = url.replace("base_url", base_url)
    
#     elif filename == "prompt_po.txt":
#         url = get_llama_response(question, filename=filename)
#         base_url = "https://slnxsaps4h19.marc.fr.ssg:44300/sap/opu/odata/sap"
#         url = url.replace("base_url", base_url)
    
#     elif filename == "prompt_query.txt":
#         query = get_llama_response(question, filename=filename)
    
#     return greeting_msg, url, query

# @app.route('/api/generate-response', methods=['POST'])
# def api_generate_response():

#     data = request.json
#     question = data.get('question')
#     filename = data.get('filename')
    
#     # Generate response
#     response_greet, response_url, response_query = generate_response(question, filename)
    
#     columns = data = []
    
#     if response_greet == "" and response_url:
#         columns, data = get_data_from_url(response_url, filename)
#     elif response_greet == "" and response_query:
#         columns, data = get_data_from_query(response_query)
    
#     return jsonify({
#         "greet": response_greet, 
#         "columns": columns, 
#         "data": data,
#         "url": response_url,  # For debugging purposes
#         "query": response_query  # For debugging purposes
#     })

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080)

