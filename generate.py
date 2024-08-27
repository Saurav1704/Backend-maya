import google.generativeai as genai

 
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
    base_url = "http://slnxsaps4h15.marc.fr.ssg:50000/sap/opu/odata/sap/BILLOFMATERIALV2_SRV"
    with open('prompts_service.txt', 'r') as file:
        prompts = file.read().strip()
    with open('prompt_greeting.txt', 'r') as file_greet:
        greet = file_greet.read().strip()
    prompts = prompts.replace("base_url", base_url)
    # print(prompts)
    return prompts,greet

def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt,question])
    print(response.text)
    return response.text
