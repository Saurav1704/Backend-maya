import requests
import pandas as pd
from requests.auth import HTTPBasicAuth 
import xml.etree.ElementTree as ET # to parse XML

def get_data_from_url(url , type ):
    odata_username = "Jchand" 
    odata_password = "Bakzee@123"
    try:
        auth = HTTPBasicAuth(odata_username, odata_password)
        response = requests.get(url , auth = auth)
        response.raise_for_status()
        # get data from url 
        service_response = response.json()
        # metadata_url = url.rsplit('/' , 1)
        # print(service_data)
        if 'd' in service_response and 'results' in service_response['d']:
            service_data = service_response['d']['results']
            #GET data from url
            # metadata_url = url + '/' + '$metadata'
            # metadata_xml = requests.get(metadata_url , auth = auth)

            #get column name and row data from service response
            column , data = convert_data_to_json( service_data  , type) 

            # columns = parse_xml_data( metadata_xml , column )

            return column, data
        else:
            return None,[ "No data found."]
        
    except requests.exceptions.RequestException as e:
        return None, str(e)



def convert_data_to_json(json_data , type ):
    df = pd.DataFrame(json_data)
    columns = df.columns.to_list()
    rows  = []
    if type == 'prompt_bom.txt':
        columns_needed = ["BillOfMaterial","BillOfMaterialCategory","BillOfMaterialVariant","Material","Plant"]
        columns_to_return = ['BOM' ,'Category' , 'BOM variant' , 'Material' , 'Plant']
    elif type == 'prompt_po.txt':
        columns_needed = ["PurchaseOrder","PurchaseOrderType","PurchasingDocumentCategory","CompanyCode","Supplier"]
        columns_to_return = ['Purchase order' ,'Order Type' , 'Document Category' , 'Company Code' , 'Supplier']
    columns_to_drop = [ col for col in columns if col not in columns_needed]
    # columns_to_drop = ['__metadata']
    # # remove checks from the column names
    # for col in columns:
    #     if col.endswith('_ac') or col.endswith('_fc') or col.startswith('to_'):
    #         #  checks from the column names
    #         columns_to_drop.append(col)
    # df = df.drop(columns=columns_to_drop, axis=1)
    df = df.drop(columns=columns_to_drop, axis=1)
    # final_columns = df.columns.to_list()        
    for index ,row in df.iterrows():
        # print(row)
        rows.append(row.to_list())
    return columns_to_return, rows


    # columns = data[0].keys()
    # json_data = []
    # for row in data:
    #     json_data.append(dict(zip(columns, row.values())))
    # print( columns, json_data )
    # return columns, json_data




def parse_xml_data(xml ):
    # Get the root element
    root = xml.getroot()

    # Print the tag name of the root element
    print(root.tag)

    # Iterate over the child elements of the root element
    for child in root:
        # Print the tag name of the child element
        print(child.tag)

        # Print the attributes of the child element
        for key, value in child.attrib.items():
            print(f'{key}={value}')

        # Print the text content of the child element
        print(child.text)
