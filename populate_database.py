# NOT PART OF THE APPLICATION;USED TO POPULATE THE MYSQL DATABASE
import mysql.connector

host = 'jtb9ia3h1pgevwb1.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
username='fwchtxhm4yyl2zm8'
password = 'hotcpncj2aymful3'
database = 'i6od8rz9wvzh7zwz'

cnx = mysql.connector.connect(host=host, database=database, user=username, password=password)
cursor = cnx.cursor()

add_muscles = ("INSERT INTO stretches"
               "(stretch_desc, group_name) "
               "VALUES (%s, %s)")

f=open("data.txt","r")
for line in f:
    values=line.split(',')
    data_muscles=""
    try:
        if line.index("\n") != -1:
            values[1]=values[1][0:len(values[1])-1]
        print(values)
        data_muscles = (str(values[0]), str(values[1]))
    except Exception as e:
        print("Last Line")
        print(values)
        data_muscles = (str(values[0]), str(values[1]))
    cursor.execute(add_muscles, data_muscles)
    cnx.commit()

# Insert new employee


cursor.close()
cnx.close()