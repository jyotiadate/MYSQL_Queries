import mysql.connector
from  fpdf import FPDF
connection = mysql.connector.connect(host="localhost",
                                             user="root",
                                             password="root",
                                             database="Smart_Society_db")



cursor = connection.cursor()
cursor.execute("select count(*) from member_register where type='Residential'")
result1 = cursor.fetchall()
print(result1)
cursor.execute("select count(*) from member_register where type='Commercial'")
result = cursor.fetchall()
print(result)
pdf=FPDF()
pdf.add_page()
pdf.set_font("Arial",size=8)

#print(result)
for i in range(len(result1)):

    for j in range(len(result1[i])):
        print(result1[i][j])
        data=str(result1[i][j])
for i in range(len(result)):

    for j in range(len(result[i])):
                print(result[i][j])
                data1 = str(result[i][j])

pdf.cell(20,10,txt=data,align="C",border=1)
pdf.cell(20,10,txt=data1,align="C",border=1)
pdf.ln()
pdf.output("AccRC.pdf")

