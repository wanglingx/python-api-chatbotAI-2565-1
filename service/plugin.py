import json
<<<<<<< HEAD
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
=======
from database.config import Connector as db
>>>>>>> 480b72e32e452e5611cea53b4b7bd550ad67f28c
    
#def findsubjectbyjob() *
def getSubbyJOb(job_name):
    mydb = db.ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "SELECT groupjob_id FROM Job WHERE job_name = '{}';".format(job_name)
    mycursor.execute(sql)
    result = mycursor.fetchall()
    arr=''
    if len(result) > 0:
        for x in result:
            arr = {"groupjob_id": x[0]}
    js_str = json.dumps(arr)
    ans =  json.loads(js_str)  
    return ans

#def getsub by job and period
def getSubbyJobnPeriod(groupjob_id,period):
    mydb = db.ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "SELECT subject_id,subject_name ,time FROM Subject WHERE groupjob_id = %s AND period = %s "
    val = (groupjob_id, period)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    arr = {}
    if len(result) > 0:
        for x in range(len(result)):
            print(str(x))
            arr["subject" + str(x)] = {"subject_id": result[x][0],
                                       "subject_name": result[x][1], "time": result[x][2]}
    return arr
    
#def findsubjectbytiming() *
def getSubbyTime(groupjob_id,time,day):
    mydb = db.ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "SELECT subject_id,subject_name ,time FROM Subject WHERE groupjob_id = %s AND period = %s AND day = %s"
    val = (groupjob_id,time,day)
    mycursor.execute(sql,val)
    result = mycursor.fetchall()
    arr = {}
    if len(result) > 0:
        for x in range(len(result)):
            print(str(x))
            arr["subject" + str(x)] = {"subject_id": result[x][0],
                                       "subject_name": result[x][1], "time": result[x][2]}
    return arr

#get data by groupjob only *
def getSubbyGroupjob(groupjob_id):
    mydb = db.ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "SELECT subject_id,subject_name ,time,day FROM Subject WHERE groupjob_id = '{}';".format(groupjob_id)
    mycursor.execute(sql)
    result = mycursor.fetchall()
    arr = {}
    if len(result) > 0:
        for x in range(len(result)):
            arr["subject" + str(x)] = {"subject_id": result[x][0], "subject_name": result[x][1], "time": result[x][2],"day": result[x][3]}
    return arr

#use for get subjectby time only *
def getSubbyTimeNG(time, day):
    mydb = db.ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "SELECT subject_id,subject_name ,time FROM Subject WHERE period = %s AND day = %s"
    val = (time, day)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    arr = {}
    if len(result) > 0:
        for x in range(len(result)):
            arr["subject" + str(x)] = {"subject_id": result[x][0],
                                       "subject_name": result[x][1], "time": result[x][2]}
    return arr        

#get all subject in that semester
def getAllSub():
    mydb = db.ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "SELECT subject_id,subject_name,time,day FROM Subject "
    mycursor.execute(sql)
    result = mycursor.fetchall()
    arr = {}
    if len(result) > 0:
        for x in range(len(result)):
            arr["subject" + str(x)] = {"subject_id": result[x][0],"subject_name": result[x][1], "time": result[x][2]}
    return arr        
