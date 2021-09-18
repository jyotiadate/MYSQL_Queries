import mysql.connector
connection = mysql.connector.connect(host="localhost",
                                             user="root",
                                             password="root",
                                             database="Smart_Society_db")

cursor = connection.cursor()
# styr="-01-01"
# endyear='-12-31'
# startyear=str(yy)+styr
# endyear=str(yy)+endyr
cursor.execute("select sum(amt) from set_expenses")
amt = cursor.fetchall()
#print(amt)
for x in range(len(amt)):
    result=(amt[x])
    #print(result)
    obj=(list(result))
    print(*obj)

cursor.execute("select year(date) from set_expenses")
year = cursor.fetchall()
print(year)
cursor.execute("select month(date) from set_expenses")
date = cursor.fetchall()
print(date)
