import sqlite3
import os
from Sql import set_db

def get_data_from_query(st,sql):
    db = 'MYdb.db'
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
    try:
       conn = sqlite3.connect(db)
       cur = conn.cursor()
       cur.execute(sql)
       rows = cur.fetchall()
    except Exception as e:
           st.write(str(e))
    column_names = []
    for description in cur.description:
        if desc.get(description[0]):
            column_names.append(desc.get(description[0]))
        else:
            column_names.append("Total Number of orders")
    conn.commit()
    conn.close()
    return  column_names , rows