import json
from database.config import Connector as db
    
#def findsubjectbyjob() *
def getSubbyJOb(groupjob_name):
    mydb = db.ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "SELECT groupjob_id FROM Groupjob WHERE groupjob_name = '{}';".format(groupjob_name)
    mycursor.execute(sql)
    result = mycursor.fetchall()
    arr=''
    if len(result) > 0:
        for x in result:
            arr = {"groupjob_id": x[0]}
    js_str = json.dumps(arr)
    ans =  json.loads(js_str) 
    groupjob_id = ans["groupjob_id"]
    return groupjob_id

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
            arr["subject" + str(x)] = {"subject_id": result[x][0],
                                       "subject_name": result[x][1],
                                       "time": result[x][2]}
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
            arr["subject" + str(x)] = {"subject_id": result[x][0],
                                       "subject_name": result[x][1],
                                       "time": result[x][2]}
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
                arr["subject" + str(x)]= {"subject_id": result[x][0],
                                           "subject_name": result[x][1],
                                           "time": result[x][2],
                                           "day":result[x][3]}
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
                                       "subject_name": result[x][1],
                                       "time": result[x][2]}
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
            arr["subject" + str(x)] = {"subject_id": result[x][0], 
                                       "subject_name": result[x][1],
                                       "time": result[x][2]}
    return arr     

#get classroom by subject section day
def getClassroom(subject,section,day):
    mydb = db.ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "SELECT classroom,time FROM SubjectClass WHERE SubjectName = %s AND section = %s AND day = %s "
    value = (subject,section,day)
    mycursor.execute(sql,value)
    result = mycursor.fetchall()   
    classroom = {}
    if len(result) > 0:
        for x in range(len(result)):
            classroom["classroom" + str(x)] = { "classroom": result[x][0],
                                                "time": result[x][1]}
    return classroom