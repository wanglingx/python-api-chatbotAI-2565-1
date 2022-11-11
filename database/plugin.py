import json
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
    sql = "SELECT groupjob_id FROM Job WHERE job_name = '{}';".format(job_name)
    mycursor.execute(sql)
    result = mycursor.fetchall()
    if len(result) > 0:
        for x in result:
            arr = {"groupjob_id": x[0]}
    
    js_str = json.dumps(arr)
    ans =  json.loads(js_str)  
    sql2 = "SELECT subject_name FROM Subject,Groupjob WHERE Groupjob.groupjob_id = %s AND Subject.groupjob_id = %s"
    val = (ans['groupjob_id'], ans['groupjob_id'])
    mycursor.execute(sql2,val)
    newSub = mycursor.fetchall()
    return newSub
    
#def findsubjectbytiming()
def getSubbyTime(time):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "SELECT subject_name time FROM Subject WHERE time = '{}';".format(time)
    mycursor.execute(sql)
    result = mycursor.fetchall()
    if len(result) > 0:
        for x in result:
            arr = {
                "subject_name": x[0],
                "time":x[1] 
            }
    return arr
