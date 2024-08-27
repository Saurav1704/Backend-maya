import requests
from requests.auth import HTTPBasicAuth 

def get_data_from_service(service):
    odata_username = "Jchand" 
    odata_password = "Bakzee@123"    
    try:
        auth = HTTPBasicAuth(odata_username, odata_password)
        response = requests.get(service , auth = auth)
        response.raise_for_status()
        service_data = response.json()

 
        if 'd' in service_data and 'results' in service_data['d']:
            return_data = service_data['d']['results']
            return return_data, None
        else:
            return None, "No BOM data found."
    except requests.exceptions.RequestException as e:
        return None, str(e)