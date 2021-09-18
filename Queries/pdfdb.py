import mysql.connector


connection = mysql.connector.connect(host="localhost",
                                             user="root",
                                             password="root",
                                             database="Smart_Society_db")

cursor = connection.cursor()
cursor.execute("select count(*) from member_register")
result = cursor.fetchall()
#print(result)
txt=result
print(txt)