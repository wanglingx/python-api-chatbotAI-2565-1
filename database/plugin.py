import mysql.connector

def ConnectorMysql():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="AI-Chatbot",
        auth_plugin='mysql_native_password'
    )
    print("Connection Success !")
    return mydb


def insert_data(name, age, address):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "INSERT INTO user (name,age,address) VALUES (%s ,%s, %s)"
    val = (name, age, address)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
    mydb.close()

#def findsubjectbyjob()
#require job find groupjob
#groupjob find subject

#def findsubjectbytiming()
#require timing and finding groupjob