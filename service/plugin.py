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
    
#def findsubjectbyjob() *
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
    return ans

#def getsub by job and period
def getSubbyJobnPeriod(groupjob_id,period):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "SELECT subject_name ,time FROM Subject WHERE groupjob_id = %s AND period = %s "
    val = (groupjob_id, period)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    arr = {}
    if len(result) > 0:
        for x in range(len(result)):
            print(str(x))
            arr["subject" +
                str(x)] = {"subject_name": result[x][0], "time": result[x][1]}
    return arr
    
#def findsubjectbytiming() *
def getSubbyTime(groupjob_id,time,day):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "SELECT subject_name ,time FROM Subject WHERE groupjob_id = %s AND period = %s AND day = %s"
    val = (groupjob_id,time,day)
    mycursor.execute(sql,val)
    result = mycursor.fetchall()
    arr = {}
    if len(result) > 0:
        for x in range(len(result)):
            print(str(x))
            arr["subject" +
                str(x)] = {"subject_name": result[x][0], "time": result[x][1]}
    return arr

#get data by groupjob only *
def getSubbyGroupjob(groupjob_id):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "SELECT subject_name ,time,day FROM Subject WHERE groupjob_id = '{}';".format(groupjob_id)
    mycursor.execute(sql)
    result = mycursor.fetchall()
    arr = {}
    if len(result) > 0:
        for x in range(len(result)):
            arr["subject" +
                str(x)] = {"subject_name": result[x][0], "time": result[x][1],"day":result[x][2]}
    return arr

#use for get subjectby time only *
def getSubbyTimeNG(time, day):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "SELECT subject_name ,time FROM Subject WHERE period = %s AND day = %s"
    val = (time, day)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    arr = {}
    if len(result) > 0:
        for x in range(len(result)):
            arr["subject"+ str(x)] = {"subject_name": result[x][0],"time": result[x][1]}
    return arr        

#get all subject in that semester
def getAllSub():
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "SELECT subject_name,time,day FROM Subject "
    mycursor.execute(sql)
    result = mycursor.fetchall()
    arr = {}
    if len(result) > 0:
        for x in range(len(result)):
            arr["subject" + str(x)] = {"subject_name": result[x]
                                       [0], "time": result[x][1]}
    return arr        
