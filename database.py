import sqlite3
import os
from sql import set_db
# import requests
# from requests.auth import HTTPBasicAuth 

# def get_data_from_service(service):
#     odata_username = "Jchand" 
#     odata_password = "Bakzee@123"    
#     try:
#         auth = HTTPBasicAuth(odata_username, odata_password)
#         response = requests.get(service , auth = auth)
#         response.raise_for_status()
#         service_data = response.json()
#         # st.write("Raw OData response:", data)  # Debugging line
 
#         if 'd' in service_data and 'results' in service_data['d']:
#             return_data = service_data['d']['results']
#             return return_data, None
#         else:
#             return None, "No BOM data found."
#     except requests.exceptions.RequestException as e:
#         return None, str(e)






def read_sql_query(sql):
    db = 'Mydb.db'
    if not os.path.isfile(db):
        set_db()

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
    column_names = []
    for description in cur.description:
        if desc.get(description[0]):
            column_names.append(desc.get(description[0]))
        else:
            column_names.append("Total Number of orders")
    conn.commit()
    conn.close()
    return rows, column_names