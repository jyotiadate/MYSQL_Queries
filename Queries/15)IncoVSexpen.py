import mysql.connector
connection = mysql.connector.connect(host="localhost",
                                             user="root",
                                             password="root",
                                             database="Smart_Society_db")

cursor = connection.cursor()
cursor.execute("select sum(Amt) from Income")
result = cursor.fetchall()
print(result)
cursor.execute("select sum(amt) from set_expenses")
result = cursor.fetchall()
print(result)
Income=2000
Expenses=20000
if (Income<=0):
     print("profit")
else:
     (Expenses>=0)
     print("loss")


