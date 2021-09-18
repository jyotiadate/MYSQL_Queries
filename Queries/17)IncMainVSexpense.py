import mysql.connector
from fpdf import FPDF
connection = mysql.connector.connect(host="localhost",
                                             user="root",
                                             password="root",
                                             database="Smart_Society_db")

cursor = connection.cursor()
cursor.execute("select sum(Amt) from Income")
result = cursor.fetchall()
#print("i",result)
cursor.execute("select sum(Amt) from set_maintenance")
result1 = cursor.fetchall()
#print("m",result1)
x=(result+result1)
print(x)
pdf=FPDF()
pdf.add_page()
pdf.set_font("Arial",size=8)



#r=result[0]
#print(r)
for i in range (len(result1)):
    r1=(result1[i])
    # print(type(r1))
    # print(r1)
for x in range (len(result)):
     r=(result[x])
     #print(r)
     ob=list((r1+r))
     print(ob)
     obj=(round(sum(r1+r)))
     print(obj)

#     print(type(obj))
#      rr=int(obj/10)
#      print(type(rr))

cursor = connection.cursor()
cursor.execute("select sum(Amt) from set_expenses")
Expenses = cursor.fetchall()
#print(Expenses)


for i in range(len(Expenses)):
    x=Expenses[i]
    #print(x)
   # print(type(x))
    obj1=list(x)
    print(*obj1)
    print(type(obj1))

    # obj1=str+(x)
    # print(obj1)
IE=55000
Expenses=45000

if (IE<=0):

     print("profit")
else:
     (Expenses>=0)
     print("loss")

pdf.cell(200,10,txt="Smart_Society_Maintenance",align="C",border=1)
for i in range(len(result)):
    k=25
    for j in range(len(result[i])):
        print(result[i][j])
        data=str(result[i][j])
        pdf.cell(k,10,txt=data,align="C",border=1)
    pdf.ln()
pdf.output("IncMainExp.pdf")



