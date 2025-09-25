from flask import Flask, request, jsonify
from flask_cors import CORS
from api import get_data_from_url
from Sql import save_feedback_to_db
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer

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
    greeting_msg = url = base_url = query = chat_reponse = ''
    
    if question.lower() in ["hello", "hi", "who are you",  "how are you", "kese ho"]:
        greeting_msg = get_flan_response(question, filename='prompt_greeting.txt')
        chat_reponse = greeting_msg
    
    elif filename == "prompt_bom.txt":
        chat_reponse = get_flan_response(question, filename=filename)
        url = chat_reponse
        base_url = "https://slnxsaps4h19.marc.fr.ssg:44300/sap/opu/odata/sap/BILLOFMATERIALV2_SRV"
        url = url.replace("base_url", base_url)
    
    elif filename == "prompt_po.txt":
        chat_reponse = get_flan_response(question, filename=filename)
        url = chat_reponse
        base_url = "https://slnxsaps4h19.marc.fr.ssg:44300/sap/opu/odata/sap/C_PURCHASEORDER_FS_SRV"
        url = url.replace("base_url", base_url)
    
    elif filename == "prompt_query.txt":
        chat_reponse = get_flan_response(question, filename=filename)
        query = chat_reponse
        print(query)
    
    return greeting_msg, url, query, chat_reponse
@app.route('/api/generate-response', methods=['POST'])
def api_generate_response():
    data = request.json
    question = data.get('question')
    filename = data.get('filename')
    rating = data.get('rating')  # 👈 capture optional rating

    response_greet, response_url, response_query, chat_response = generate_response(question, filename)
    columns = []
    data_rows = []
    response_for_rating = ""

    if response_greet:
        response_for_rating = response_greet
    elif response_url:
        columns, data_rows = get_data_from_url(response_url, filename)
        response_for_rating = chat_response
    elif response_query:
        response_for_rating = chat_response
    else:
        response_for_rating = "Sorry, I couldn't understand the query. Please try again."

    # Save feedback if rating is sent
    if rating is not None:
        print("Saving feedback with rating:", rating)
        save_feedback_to_db(question, response_for_rating, rating)

    return jsonify({
        "greet": response_greet,
        "columns": columns,
        "data": data_rows,
        "url": response_url,
        "query": response_query,
        "response_for_rating": response_for_rating
    })   
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)