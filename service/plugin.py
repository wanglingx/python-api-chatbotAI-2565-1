import json
import mysql.connector

def ConnectorMysql():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="1234",
        database="duckbot",
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

#get data by groupjob only
def getSubbyGroupjob(groupjob_id):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "SELECT subject_name ,time FROM Subject WHERE groupjob_id = %s"
    val = (groupjob_id)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    arr = {}
    if len(result) > 0:
        for x in range(len(result)):
            arr["subject" +
                str(x)] = {"subject_name": result[x][0], "time": result[x][1]}
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


