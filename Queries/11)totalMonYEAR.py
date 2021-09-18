import mysql.connector
connection = mysql.connector.connect(host="localhost",
                                             user="root",
                                             password="root",
                                             database="Smart_Society_db")

cursor = connection.cursor()
# cursor.execute("select count(*) from set_maintenance")
# cursor.execute("desc set_maintenance")
#cursor.execute("select * from set_maintenance")
#cursor.execute("SELECT date(2020-01-27) as MONTHNAME SUM(sq_ft) FROM member_register")
#cursor.execute("select EXTRACT('2020-01') from set_maintenance where 'name' ")
cursor.execute(" select year(paid_date) from pay_maintenance")
result = cursor.fetchall()
print(result)
cursor.execute("select month(paid_date)from pay_maintenance")
result = cursor.fetchall()
print(result)

