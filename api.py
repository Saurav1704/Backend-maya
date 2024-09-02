import requests
import pyodata
from requests.auth import HTTPBasicAuth 


def get_data_from_url(url):
    odata_username = "Jchand" 
    odata_password = "Bakzee@123"    
    try:
        auth = HTTPBasicAuth(odata_username, odata_password)
        response = requests.get(url , auth = auth)
        response.raise_for_status()
        service_data = response.json()
        print(service_data)
        if 'd' in service_data and 'results' in service_data['d']:
            return_data = service_data['d']['results']
            return return_data, None
        else:
            return None, "No BOM data found."
    except requests.exceptions.RequestException as e:
        return None, str(e)