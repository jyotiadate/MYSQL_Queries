import mysql.connector
connection = mysql.connector.connect(host="localhost",
                                             user="root",
                                             password="root",
                                             database="Smart_Society_db")

cursor = connection.cursor()
# cursor.execute(" select year(date) from Income")
# result = cursor.fetchall()
# print(result)
cursor.execute("select sum(Amt) from Income")
result = cursor.fetchall()
#print(result)
for x in range(len(result)):
    obj=result[0]
    #print(obj)
    obj1=list(obj)
    print(*obj1)
    #print(type(*obj1))



