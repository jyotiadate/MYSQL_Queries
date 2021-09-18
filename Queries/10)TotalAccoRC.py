import mysql.connector
from fpdf import FPDF

connection = mysql.connector.connect(host="localhost",
                                             user="root",
                                             password="root",
                                             database="Smart_Society_db")

cursor = connection.cursor()
# cursor.execute("select count(*) from set_maintenance")
# cursor.execute("desc set_maintenance")
cursor.execute("select m.no,m.name,m.type,sm.amt from member_register m  join set_maintenance sm on m.no=sm.no")
result = cursor.fetchall()
#print(result)
cursor.execute("  select sum(amt) from set_maintenance")
result1 = cursor.fetchall()
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
        for i in range(len(result1)):
            k = 25
            for j in range(len(result1[i])):
                print(result1[i][j])
                data1 = str(result1[i][j])
                pdf.cell(k, 10, txt=data1, align="C", border=1)

    pdf.ln()
pdf.output("TotalAccRC.pdf")
