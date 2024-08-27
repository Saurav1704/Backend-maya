import pandas as pd
from generate import generate_response
from database import get_data_from_service

def show_output(question, session_state):
    response_md = generate_response(question)
    
    if question.lower() in ["hello", "hi", "who are you"]:
        message = {'role': "assistant", 'content': response_md}
        session_state["messages"].append(message)
        return response_md, None
    
    try:
        service_data, error = get_data_from_service(response_md)
        response_df = pd.DataFrame(service_data)
        message = {'role': "assistant", 'content': service_data}
        if not response_df.empty:
            message['data'] = response_df.to_dict()
        session_state["messages"].append(message)
        return service_data, response_df
    except Exception as e:
        error = str(e)
        message = {'role': "assistant", 'content': error}
        session_state["messages"].append(message)
        return error, None
