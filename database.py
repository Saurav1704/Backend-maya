import sqlite3
import os
from sql import set_db

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