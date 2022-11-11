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

#def findsubjectbyjob()
def getSubbyJOb(job_name):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "SELECT groupjob_id FROM Job WHERE job_id = %s"
    val = job_name
    mycursor.execute(sql,val)
    result = mycursor.fetchall()
    for x in result:
        sql2 = "SELECT subject_name FROM Subject,Groupjob WHERE Groupjob.groupjob_id = %s AND Subject.groupjob_id = %s"
        val2 = (x,x)
        mycursor.execute(sql2,val2)
        newSub = mycursor.fetchall()
    mydb.commit()
    mycursor.close()
    mydb.close()    
    return newSub
    
#def findsubjectbytiming()
def getSubbyTime(time):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "SELECT subject_name FROM Subject WHERE time = %s"
    val = time
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    mydb.commit()
    mycursor.close()
    mydb.close()
    return result