import sqlite3

# Connect to sqlite3
# connection = sqlite3.connect("EKKO.db")
# connection = sqlite3.connect("MARA.db")
#To create a database with the following name 
connection = sqlite3.connect("MYdb.db")

# Create a cursor object to insert record, create table, retrieve

cursor = connection.cursor()

#create the table

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

cursor.execute('''Insert Into EKKO values('4000000002' , '5710' , 'F' , '17.12.2023' , 'OLDMAT58') ''')
cursor.execute('''Insert Into EKKO values('4000000003' , '5710' , 'F' , '17.12.2023' , 'OLDMAT58') ''')
cursor.execute('''Insert Into EKKO values('4000000004' , '5710' , 'F' , '20.12.2023' , 'OLDMAT59') ''')
cursor.execute('''Insert Into EKKO values('4000000005' , '5710' , 'F' , '20.12.2023' , 'OLDMAT59') ''')
cursor.execute('''Insert Into EKKO values('4000000008' , '5710' , 'F' , '20.12.2023' , 'OLDMAT58') ''')
cursor.execute('''Insert Into EKKO values('4000000009' , '5710' , 'F' , '20.12.2023' , 'OLDMAT58') ''')
cursor.execute('''Insert Into EKKO values('4000000098' , '5710' , 'F' , '18.12.2023' , 'OLDMAT60') ''')
cursor.execute('''Insert Into EKKO values('4000000099' , '5710' , 'F' , '18.12.2023' , 'OLDMAT60') ''')

# Insert some records in MARA 
cursor.execute('''Insert Into MARA values('OLDMAT58' , 'Z080' , '02.10.2023' ) ''')
cursor.execute('''Insert Into MARA values('OLDMAT59' , 'Z080' , '02.11.2023' ) ''')
cursor.execute('''Insert Into MARA values('OLDMAT60' , 'Z080' , '04.11.2023' ) ''')
# Insert Some records in MAKT
cursor.execute('''Insert Into MAKT values('OLDMAT58' , 'STONE' ) ''')
cursor.execute('''Insert Into MAKT values('OLDMAT59' , 'PAPER' ) ''')
cursor.execute('''Insert Into MAKT values('OLDMAT60' , 'SCISSORS' ) ''')
#Display all the records

# print("The inserted records are")

# data= cursor.execute('''Select * from EKKO''')

# for row in data:
    # print(row)
    
#close the connection

connection.commit()
connection.close()