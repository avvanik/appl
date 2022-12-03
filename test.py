#connect to sqlite
import sqlite3

'''command = """CREATE TABLE edi867 (
            unique_identification text,
            esi_id text,
            cr_name text,
            meter_role text,
            meter_type text,
            quantity text
            )"""'''
#cursor.execute(command)

def createTable(name):
    cursor.execute('CREATE TABLE IF NOT EXISTS {name} (unique_identification text)')

#connect to database    
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
    

#read textFile and convert to list
def readFile(f):
    file = open(f, "r")
    
    for x in file.readlines():
        measures.append(x)

#iterate through list and insert into dataframe if condition true
def extractData(measure, column):
    for data in measures:
        if measure in data:
            cursor.execute(f"INSERT INTO edi867 ({column}) VALUES ('{data}')")
            

def safeData(file):

    #read
    readFile(file)

    #extract
    extractData(u_id, "unique_identification")
    extractData(esi_id, "esi_id")
    extractData(cr_name, "cr_name")
    extractData(meter_role, "meter_role")
    extractData(meter_type, "meter_type")
    extractData(quantity, "quantity")

    conn.commit()
    conn.close()
    print("done")

createTable("test")
safeData("gistfile3.txt")






