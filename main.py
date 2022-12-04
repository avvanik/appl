import sqlite3

'''command = """CREATE TABLE edi867 (
            unique_identification text,
            esi_id text,
            cr_name text,
            meter_role text,
            meter_type text,
            quantity text
            )"""
cursor.execute(command)'''

#connect db    
conn = sqlite3.connect('edi.db')
cursor = conn.cursor()

measures = []
x = "gistfile2.txt"
u_id = "BPT~"
esi_id = "REF~Q"
cr_name = "CR NAME"
meter_role = "REF~JH"
meter_type = "REF~MT"
quantity = "QTY~QD"

#read file and convert to list
def readFile(f):
    file = open(f, "r")
    
    for x in file.readlines():
        measures.append(x)

#iterate through list and insert into dataframe if condition true
def extract(measure, column):
    for data in measures:
        if measure in data:
            cursor.execute(f"INSERT INTO edi867 ({column}) VALUES ('{data}')")

def run(file):

    #read
    readFile(file)

    #extract
    extract(u_id, "unique_identification")
    extract(esi_id, "esi_id")
    extract(cr_name, "cr_name")
    extract(meter_role, "meter_role")
    extract(meter_type, "meter_type")
    extract(quantity, "quantity")

    conn.commit()
    conn.close()

run("gistfile3.txt")






