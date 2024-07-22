import sqlite3

# Connect to sqlite3
# connection = sqlite3.connect("EKKO.db")
# connection = sqlite3.connect("MARA.db")
#To create a database with the following name
def set_db(): 
    connection = sqlite3.connect("MYdb.db")
    # Create a cursor object to insert record, create table, retrieve
    cursor = connection.cursor()

    # create the table

    table_info_ekko = """
    Create table EKKO(EBELN CHAR(10), 
                    BUKRS CHAR(4),
                    BSTYP CHAR(1), 
                    AEDAT DATS,
                    MATNR CHAR(40)
                        );

    """
    table_info_mara = """
    Create table MARA(
            MATNR CHAR(40),
            MTART CHAR(4),
            ERSDA DATS
    );
    """
    table_info_makt = """
    Create table MAKT(
            MATNR CHAR(40),
            MAKTX CHAR(40)
    );
    """
    cursor.execute(table_info_ekko)
    cursor.execute(table_info_mara)
    cursor.execute(table_info_makt)

# Insert some more record IN EKKO

    cursor.execute('''Insert Into EKKO values('4000000002' , '5710' , 'F' , '17.11.2023' , 'OLDMAT58') ''')
    cursor.execute('''Insert Into EKKO values('4000000003' , '6952' , 'F' , '17.12.2023' , 'OLDMAT58') ''')
    cursor.execute('''Insert Into EKKO values('4000000004' , '5789' , 'F' , '20.10.2021' , 'NEW-MAT-189') ''')
    cursor.execute('''Insert Into EKKO values('4000000005' , '5796' , 'F' , '20.09.2024' , 'OLDMAT59') ''')
    cursor.execute('''Insert Into EKKO values('4000000008' , '5852' , 'F' , '20.07.2025' , 'OLDMAT58') ''')
    cursor.execute('''Insert Into EKKO values('4000000009' , '5218' , 'F' , '20.01.2020' , 'OLDMA-963-1569') ''')
    cursor.execute('''Insert Into EKKO values('4000000098' , '7411' , 'F' , '18.02.2019' , 'OLDMAT60') ''')
    cursor.execute('''Insert Into EKKO values('4000000099' , '9631' , 'F' , '18.12.2018' , 'OLDMAT60') ''')
    
    cursor.execute('''Insert Into EKKO values('4000000074' , '1258' , 'G' , '01.02.2018' , 'NEWMAT123') ''')
    cursor.execute('''Insert Into EKKO values('4000000085' , '9632' , 'B' , '07.11.2019' , 'MATERIAL159') ''')
    cursor.execute('''Insert Into EKKO values('4000000063' , '1489' , 'D' , '30.06.2020' , '392-597-41') ''')
    cursor.execute('''Insert Into EKKO values('4000000123' , '9621' , 'W' , '02.05.2026' , 'NEW-MAT-189') ''')
    cursor.execute('''Insert Into EKKO values('4000000741' , '7411' , 'R' , '10.05.2023' , 'OLD-963') ''')
    cursor.execute('''Insert Into EKKO values('4000000852' , '5710' , 'Q' , '11.04.2021' , 'OLDMA-963-1569') ''')
    cursor.execute('''Insert Into EKKO values('4000000963' , '5218' , 'H' , '08.03.2022' , '115-852-963') ''')
    cursor.execute('''Insert Into EKKO values('4000000456' , '6952' , 'K' , '19.02.2021' , 'A010-963') ''')
    
    cursor.execute('''Insert Into EKKO values('4000000741' , '6952' , 'G' , '14.01.2025' , 'C010-963') ''')
    cursor.execute('''Insert Into EKKO values('4000000147' , '9621' , 'F' , '06.07.2024' , 'A010-RECM-852') ''')
    cursor.execute('''Insert Into EKKO values('4000000469' , '7456' , 'E' , '05.08.2023' , 'A010OL') ''')
    cursor.execute('''Insert Into EKKO values('4000000753' , '1489' , 'F' , '07.08.2020' , 'ARSTYPE') ''')
    cursor.execute('''Insert Into EKKO values('4000000951' , '5710' , 'W' , '03.09.2021' , 'ARSTYPE') ''')
    cursor.execute('''Insert Into EKKO values('4000000456' , '1258' , 'F' , '08.08.2021' , 'OLUITH-852') ''')
    cursor.execute('''Insert Into EKKO values('4000007412' , '9632' , 'Q' , '16.10.2023' , 'OLDMPLM-9851') ''')
    cursor.execute('''Insert Into EKKO values('4000000963' , '6952' , 'F' , '21.11.2020' , 'OLEDC123') ''')
    
    cursor.execute('''Insert Into EKKO values('4000007412' , '7456' , 'Q' , '22.08.2017' , 'WSXRFT-852') ''')
    cursor.execute('''Insert Into EKKO values('4000008547' , '1489' , 'F' , '26.07.2019' , 'QWERT8520') ''')
    cursor.execute('''Insert Into EKKO values('4000008569' , '5710' , 'R' , '27.09.2020' , 'VBJKSF-852') ''')
    cursor.execute('''Insert Into EKKO values('4000005412' , '7562' , 'F' , '23.06.2023' , '7410-8520-8') ''')
    cursor.execute('''Insert Into EKKO values('4000000522' , '7896' , 'R' , '07.07.2025' , 'WSDCV-852') ''')
    cursor.execute('''Insert Into EKKO values('4000005236' , '9874' , 'F' , '09.07.2022' , 'PLVHJ-854') ''')
    cursor.execute('''Insert Into EKKO values('4000008569' , '1236' , 'T' , '01.05.2023' , 'OLDM-96-85') ''')
    cursor.execute('''Insert Into EKKO values('4000008544' , '7412' , 'F' , '13.04.2024' , '789-85-741') ''')
    
    cursor.execute('''Insert Into EKKO values('4000007458' , '6547' , 'U' , '11.03.2021' , 'ZXCV-852-74') ''')
    cursor.execute('''Insert Into EKKO values('4000008547' , '4569' , 'E' , '16.05.2018' , 'PLM-852-741') ''')
    cursor.execute('''Insert Into EKKO values('4000008569' , '7415' , 'C' , '28.02.2019' , '741-85-6') ''')
    cursor.execute('''Insert Into EKKO values('4000005236' , '9632' , 'S' , '29.01.2022' , 'RTYU-TYUIO') ''')
    cursor.execute('''Insert Into EKKO values('4000005214' , '8547' , 'A' , '31.04.2021' , 'VHJK-963-41') ''')
    cursor.execute('''Insert Into EKKO values('4000008569' , '8569' , 'Y' , '02.06.2026' , 'CVBNM-963-741') ''')
    cursor.execute('''Insert Into EKKO values('4000000045' , '6523' , 'U' , '17.08.2025' , 'NCS-74-85') ''')
    cursor.execute('''Insert Into EKKO values('4000000095' , '1254' , 'R' , '19.01.2024' , 'CVBN-85-74') ''')
    
    # Insert some records in MARA
    cursor.execute('''Insert Into MARA values('OLDMAT58' , 'Z080' , '02.10.2023' ) ''')
    cursor.execute('''Insert Into MARA values('OLDMAT59' , 'A010' , '02.11.2023' ) ''')
    cursor.execute('''Insert Into MARA values('OLDMAT60' , 'Z080' , '19.01.2024' ) ''')
    
    cursor.execute('''Insert Into MARA values('CVBN-85-74' , 'A080' , '28.02.2019' ) ''')
    cursor.execute('''Insert Into MARA values('NCS-74-85' , 'C080' , '02.11.2023' ) ''')
    cursor.execute('''Insert Into MARA values('CVBNM-963-741' , 'A010' , '04.11.2023' ) ''')
    
    cursor.execute('''Insert Into MARA values('ZXCV-852-74' , 'Z080' , '02.10.2023' ) ''')
    cursor.execute('''Insert Into MARA values('789-85-741' , 'Z080' , '02.11.2023' ) ''')
    cursor.execute('''Insert Into MARA values('WSXRFT-852' , 'Z080' , '23.06.2023' ) ''')
    
    cursor.execute('''Insert Into MARA values('OLEDC123' , 'Z080' , '02.10.2023' ) ''')
    cursor.execute('''Insert Into MARA values('CVBNM-963-741' , 'Z080' , '23.06.2023' ) ''')
    cursor.execute('''Insert Into MARA values('RTYU-TYUIO' , 'Z080' , '04.11.2023' ) ''')
    
    cursor.execute('''Insert Into MARA values('OLDM-96-85' , 'Z080' , '02.10.2023' ) ''')
    cursor.execute('''Insert Into MARA values('A010-RECM-852' , 'Z080' , '02.11.2023' ) ''')
    cursor.execute('''Insert Into MARA values('A010OL' , 'Z080' , '28.02.2019' ) ''')
    
    cursor.execute('''Insert Into MARA values('OLDMPLM-9851' , 'Z080' , '07.08.2020' ) ''')
    cursor.execute('''Insert Into MARA values('NEW-MAT-189' , 'Z080' , '02.11.2023' ) ''')
    cursor.execute('''Insert Into MARA values('OLDMAT60' , 'Z080' , '04.11.2023' ) ''')
    
    cursor.execute('''Insert Into MARA values('RTYU-TYUIO' , 'Z080' , '02.10.2023' ) ''')
    cursor.execute('''Insert Into MARA values('OLDMAT59' , 'Z080' , '02.11.2023' ) ''')
    cursor.execute('''Insert Into MARA values('OLEDC123' , 'Z080' , '07.08.2020' ) ''')
    cursor.execute('''Insert Into MARA values('115-852-963' , 'Z080' , '04.11.2023' ) ''')
    cursor.execute('''Insert Into MARA values('RTYU-TYUIO' , 'C080' , '02.11.2023' ) ''')
    cursor.execute('''Insert Into MARA values('OLEDC123' , 'A920' , '28.02.2019' ) ''')
    cursor.execute('''Insert Into MARA values('MATERIAL159' , 'A080-10' , '02.10.2023' ) ''')
    cursor.execute('''Insert Into MARA values('115-852-963' , 'Z080' , '11.04.2021' ) ''')
    cursor.execute('''Insert Into MARA values('OLDMAT58' , 'Z080' , '05.11.2024' ) ''')
    cursor.execute('''Insert Into MARA values('MATERIAL159' , 'Z080' , '02.11.2025' ) ''')
    cursor.execute('''Insert Into MARA values('OLDMAT60' , 'Z080' , '04.11.2023' ) ''')
    
    cursor.execute('''Insert Into MARA values('OLDMAT58' , 'Z080' , '02.10.2023' ) ''')
    cursor.execute('''Insert Into MARA values('RTYU-TYUIO' , 'Z080' , '02.11.2023' ) ''')
    cursor.execute('''Insert Into MARA values('OLDMAT60' , 'Z080' , '04.11.2023' ) ''')
    
    cursor.execute('''Insert Into MARA values('NEW-MAT-189' , 'X010' , '02.10.2023' ) ''')
    cursor.execute('''Insert Into MARA values('OLDMAT59' , 'A523' , '02.05.2026' ) ''')
    cursor.execute('''Insert Into MARA values('ARSTYPE' , 'D010' , '04.11.2023' ) ''')
    
    cursor.execute('''Insert Into MARA values('OLDMAT58' , 'A040' , '11.04.2021' ) ''')
    cursor.execute('''Insert Into MARA values('VBJKSF-852' , 'A010' , '02.11.2023' ) ''')
    cursor.execute('''Insert Into MARA values('OLDMAT60' , 'Z080' , '04.11.2023' ) ''')
    cursor.execute('''Insert Into MARA values('MATERIAL159' , 'Z080' , '19.02.2021' ) ''')
    cursor.execute('''Insert Into MARA values('OLEDC123' , 'Z080' , '19.02.2021' ) ''')
    cursor.execute('''Insert Into MARA values('OLDMAT58' , 'Z080' , '02.10.2023' ) ''')
    cursor.execute('''Insert Into MARA values('OLDMAT59' , 'Z080' , '02.11.2026' ) ''')
    cursor.execute('''Insert Into MARA values('NEW-MAT-189' , 'A010' , '04.11.2023' ) ''')
    cursor.execute('''Insert Into MARA values('OLDMAT58' , 'Z080' , '02.10.2023' ) ''')
    cursor.execute('''Insert Into MARA values('VBJKSF-852' , 'Z080' , '02.11.2026' ) ''')
    cursor.execute('''Insert Into MARA values('OLDMAT60' , 'A010' , '11.04.2021' ) ''')
    # Insert Some records in MAKT
    cursor.execute('''Insert Into MAKT values('OLEDC123' , 'MATERIAL TEST FOR OLEDC123' ) ''')
    cursor.execute('''Insert Into MAKT values('OLDMAT59' , 'MATERIAL TEST FOR OLDMAT59' ) ''')
    cursor.execute('''Insert Into MAKT values('392-597-41' , 'MATERIAL TEST FOR 392-597-41' ) ''') 
    cursor.execute('''Insert Into MAKT values('ARSTYPE' , 'MATERIAL TEST FOR ARSTYPE' ) ''')
    cursor.execute('''Insert Into MAKT values('OLDMA-963-1569' , 'MATERIAL TEST FOR OLDMA-963-1569 ' ) ''')
    cursor.execute('''Insert Into MAKT values('ARSTYPE' , 'MATERIAL TEST FOR ARSTYPE' ) ''')
    cursor.execute('''Insert Into MAKT values('OLDMAT59' , 'MATERIAL TEST FOR OLDMAT59' ) ''') 
    cursor.execute('''Insert Into MAKT values('OLDMA-963-1569' , 'MATERIAL TEST FOR OLDMA-963-1569' ) ''')
    cursor.execute('''Insert Into MAKT values('OLDMAT59' , 'MATERIAL TEST FOR OLDMAT59' ) ''')
    cursor.execute('''Insert Into MAKT values('NEW-MAT-189' , 'MATERIAL TEST FOR NEW-MAT-189' ) ''')
    cursor.execute('''Insert Into MAKT values('CVBN-85-74' , 'MATERIAL TEST FOR CVBN-85-74' ) ''')
    cursor.execute('''Insert Into MAKT values('392-597-41' , 'MATERIAL TEST FOR 392-597-41' ) ''')
    cursor.execute('''Insert Into MAKT values('ARSTYPE' , 'MATERIAL TEST FOR ARSTYPE' ) ''')
    cursor.execute('''Insert Into MAKT values('OLEDC123' , 'MATERIAL TEST FOR OLEDC123' ) ''')
    cursor.execute('''Insert Into MAKT values('ARSTYPE' , 'MATERIAL TEST FOR ARSTYPE' ) ''')
    cursor.execute('''Insert Into MAKT values('CVBN-85-74' , 'MATERIAL TEST FOR CVBN-85-74' ) ''')
    # print("The inserted records are")

    # data= cursor.execute('''Select * from EKKO''')

    # for row in data:
        # print(row)
        
    #close the connection

    connection.commit()
    connection.close()