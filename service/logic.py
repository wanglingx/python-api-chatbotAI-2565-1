import app
import service.plugin as db
from flask import jsonify
import json

class Logic:
    def reply(intent, text, reply_token, id, disname, req):  # function reply
        # if intent == 'job':  # จับว่าเป็น intent ไหน
        #     text = Logic.test1()
        #
        if intent == 'final-subject':
            jobsubject=Logic.setSubject(req)
            time = Logic.setTime(req)
            day=Logic.setDay(req)
            #result = Logic.getdata_SubjectbyTime(time,day)
           
            text = 'วิชา = '+jobsubject + ' เวลา = '+time + 'วัน = '+day
            #text = 'วิชา = '+jobsubject+' เวลา = '+time+ 'วัน = '+day

        elif intent == 'classroom':
            Logic.test1()
           
        text_message = app.TextSendMessage(text)
        app.line_bot_api.reply_message(reply_token, text_message) # ส่งข้อความตอบกลับไป

    def test1():
        return 'ทดสอบสำเร็จ'     

    def setSubject(req) :
        jobsubject = req["queryResult"]["outputContexts"][0]["parameters"]["job"]
        jobsubject = jobsubject.upper()
        return jobsubject
    
    def setTime(req) : 
        time=req["queryResult"]["outputContexts"][0]["parameters"]["time.original"]
        if time == 'เช้า' or time == 'ช่วงเช้า':
            time = 'morning'
        elif time == 'บ่าย'or time == 'ช่วงบ่าย':
            time = 'afternoon'
        elif time == 'เย็น'or time == 'ช่วงเย็น':
            time = 'evening'
        return time
    
    def setDay(req) : 
        day = req["queryResult"]["outputContexts"][0]["parameters"]["day.original"]
        if day == 'พฤหัส' or day == 'พฤหัสบดี' or day == 'วันพฤหัส' or day == 'วันพฤหัสบดี' or day == 'thursday' or day == 'Thursday':
            day = 'พฤหัสบดี'
        elif day == 'ศุกร์' or day == 'ศุก' or day == 'วันศุกร์' or day == 'วันศุก' or day == 'friday' or day == 'Friday':
            day = 'ศุกร์'  
        else :
            return 'เสียใจด้วยน้า เทอมนี้ยังไม่มี แต่ยังมีวิชาอื่นนะ ว่าแต่เทอมนี้มีวิชาไรบ้างน้า'  
        return day
    
    
    #เข้า database by job 
    def getdata_SubjectbyJob(job_name):
        ans = db.getSubbyTime(job_name)  
        return ans
    
    #เข้า database by group_job
    def getdata_SubjectbyGroupjob(groupjob_id):
        ans = db.getSubbyGroupjob(groupjob_id)
        return ans
    
    #เข้า database by job and period
    def getdata_SubjectbyJob(groupjob_id, period):
        ans = db.getSubbyJobnPeriod(groupjob_id, period)
        return ans

    #เข้า database by job and period and time 
    def getdata_SubjectbyTime(groupjob_id,period,day): 
        ans = db.getSubbyTime(groupjob_id,period,day)
        return ans
    
    #เข้า database by time only
    def getdata_SubjectbyTime(period, day):
        ans = db.getSubbyTimeNG(period, day)
        return ans
    
    #เข้า database เมื่อมันไม่มีวันที่กำหนด โดยมันเก็บค่าวิชาทั้งหมดในเทอมนั้นออกจาก database
    def getdata_SubAll():
        ans = db.getAllSub()
        return ans
    
    #scene 1.1 job only by groupjob when not day or show all by job
    def answerbyJobOnly(job,groupjob_id):
        ans = Logic.getdata_SubjectbyGroupjob(groupjob_id)
        subject = ''
        if len(ans) > 0 :
            for x in range(len(ans)):
                subject += "วัน : " + \
                    ans["subject"+str(x)]["day"] + " เวลา : " + \
                    ans["subject"+str(x)]["time"]+" วิชา : " + \
                    ans["subject"+str(x)]["subject_id"]+" " + \
                    ans["subject"+str(x)]["subject_name"]+"\n"
        replyMgs = "วิชาเลือกที่เปิดในเทอมนี้ตามอาชีพ "+job+" มีดังนี้"+"\n"+subject+"เลือกลงได้เลยนะครับผมม" 
        return replyMgs
    
    #scence 1.2 by job and period (group_job,period)
    def answerbyJobnPeriod(job,groupjob_id,period):
        resualt = Logic.getdata_SubjectbyJob(groupjob_id, period)
        subject = ''
        temp = []
        ans = dict()
        if len(resualt) > 0:
            for key, val in resualt.items():
                if val not in temp:
                    temp.append(val)
                    ans[key] = val
                    subject += "เวลา : " + \
                        ans[str(key)]["time"] + " วิชา : " + \
                        ans[str(key)]["subject_id"]+" " + \
                        ans[str(key)]["subject_name"]+"\n"
        if period == 'morning':
            period = "เช้า"
        if period == 'afternoon':
            period = "บ่าย"
        if period == 'evening':
            period = "เย็น"

        replyMgs = "วิชาเลือกที่เปิดในเทอมนี้ตามอาชีพ "+job+" ช่วง"+period+" มีดังนี้" + \
            "\n"+subject+"เลือกลงได้เลยนะครับผมม"
        if len(ans) <= 0:
            allsub = Logic.answerbyJobOnly(job, groupjob_id)
            replyMgs = "เทอมนี้ไม่มีช่วงที่คุณได้เลือก คุณสามารถดู"+allsub
        return replyMgs
    
    #scence 1.3 by job and period (group_job,period,day)
    def answerbyJobnPeriodnDay(job,groupjob_id,period,day):
        ans = Logic.getdata_SubjectbyTime(groupjob_id, period, day)
        subject = ''
        if len(ans) > 0:
            for x in range(len(ans)):
                subject += "เวลา : " + \
                    ans["subject"+str(x)]["time"] + " วิชา : " + \
                    ans["subject"+str(x)]["subject_id"]+" "+ \
                    ans["subject"+str(x)]["subject_name"]+"\n"
        if period == 'morning':
            period = "เช้า"
        if period == 'afternoon':
            period = "บ่าย"
        if period == 'evening':
            period = "เย็น"

        replyMgs = "วิชาเลือกที่เปิดในเทอมนี้ตามอาชีพ "+job+" ช่วง"+period+" ของวัน"+day+" มีดังนี้" + \
            "\n"+subject+"เลือกลงได้เลยนะครับผมม"

        if len(ans) <= 0:
            allsub = Logic.answerbyJobOnly(job, groupjob_id)
            replyMgs = "เทอมนี้ไม่มีช่วงที่คุณได้เลือก คุณสามารถดู"+allsub
        return replyMgs
    
    #scene 2.1 only time
    def answerbyTimeOnly(period,day):
        result = Logic.getdata_SubjectbyTime(period, day)
        subject = ''
        temp = []
        ans = dict()
        if len(result) > 0:
            for key, val in result.items():
                if val not in temp:
                    temp.append(val)
                    ans[key] = val
                    subject += "เวลา : " + \
                        ans[str(key)]["time"] + " วิชา : " + \
                        ans[str(key)]["subject_id"]+" "+ \
                        ans[str(key)]["subject_name"]+"\n"
        if period == 'morning':
            period = "เช้า"
        if period == 'afternoon':
            period = "บ่าย"
        if period == 'evening':
            period = "เย็น"

        replyMgs = "สำหรับวิชาเลือกที่เปิดในเทอมนี้ช่วง"+period+"ของวัน" + \
            day+"มีดังนี้"+"\n"+subject+"เลือกลงได้เลยนะครับผมม"
        return replyMgs
    
    #scene 2.2 all of semester not job not period not day
    def answerAllSub():
        result = Logic.getdata_SubAll()
        subject = ''
        temp = []
        ans = dict()
        if len(result) > 0:
                for key, val in result.items():
                    if val not in temp:
                        temp.append(val)
                        ans[key] = val
                        subject += "เวลา : " + \
                            ans[str(key)]["time"] + " วิชา : " + ans[str(key)]["subject_id"]+" "\
                            +ans[str(key)]["subject_name"]+"\n"

        replyMgs = "วิชาเลือกที่เปิดในเทอมนี้ทั้งหมดมีดังนี้" + \
                "\n"+"วันพฤหัสบดีและวันศุกร์มีวันเวลาช่วงเดียวกัน"+"\n"+subject+"เลือกลงได้เลยนะครับผมม"
        return replyMgs

    
#validate job -> groupjob -> time and day
#                         -> All

#validate time and day = subject
