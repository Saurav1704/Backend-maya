from flask import Flask, request, jsonify
from flask_cors import CORS
# from generate import generate_response, get_gemini_response, get_prompts
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app)



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

def get_prompts():

    with open('prompt_service.txt', 'r') as file:
        prompts = file.read().strip()
        print(prompts)
    with open('prompt_greeting.txt', 'r') as file_greet:
        greet = file_greet.read().strip()
        print(greet)
    return prompts,greet


def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt,question])
    print(response)
    return response.text




@app.route('/api/generate-response', methods=['POST'])
def api_generate_response():
    data = request.json
    question = data.get('question')
    response_text = generate_response(question)
    print(response_text)
    return jsonify({"response": response_text})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
