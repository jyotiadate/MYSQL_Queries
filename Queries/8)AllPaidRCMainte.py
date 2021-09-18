import mysql.connector
from fpdf import FPDF
connection = mysql.connector.connect(host="localhost",
                                             user="root",
                                             password="root",
                                             database="Smart_Society_db")

cursor = connection.cursor()
cursor.execute(" select m.no,m.name,m.type,p.paid_date from member_register m join pay_maintenance p on m.no=p.no")

result = cursor.fetchall()
#print(result)
pdf=FPDF()
pdf.add_page()
pdf.set_font("Arial",size=8)

#print(result)
for i in range(len(result)):
    k=25
    for j in range(len(result[i])):
        print(result[i][j])
        data=str(result[i][j])
        pdf.cell(k,10,txt=data,align="C",border=1)
    pdf.ln()
pdf.output("AllPaidRCMain.pdf")

