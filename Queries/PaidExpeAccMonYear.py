import mysql.connector
yeartuple=[]
cntyeartuple=[]
connection = mysql.connector.connect(host="localhost",
                                             user="root",
                                             password="root",
                                             database="Smart_Society_db")

cursor = connection.cursor()
cursor.execute("select distinct year(date)   from set_expenses")
amt = cursor.fetchall()
for i in range(len(amt)) :
    dte=amt[i]
    yy=dte[0]
    yeartuple.append(yy)
    res=connection.cursor()
    styr="-01-01"
    endyr='-12-31'
    startyear=str(yy)+styr
    endyear=str(yy)+endyr

MonAnnu=("select count(date) from set_expenses where date between '"+startyear+"' and '"+endyear+"'")
res.execute(MonAnnu)
result=res.fetchall()
cntyeartuple.append(result[0])

countyytuple=[]
for i in range(len(cntyeartuple)):
    yy=cntyeartuple[i]
    cntyeartuple.append(yy[0])
print("",yeartuple)
print("",cntyeartuple)



#
print(amt)