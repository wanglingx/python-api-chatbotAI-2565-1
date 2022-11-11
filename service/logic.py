import app
import service.plugin as db
from flask import jsonify
import json

class Logic:
    def reply(intent, text, reply_token, id, disname, req):  # function reply
        if intent == 'testdodo':  # จับว่าเป็น intent ไหน
            text = Logic.test1()
            
        elif intent == 'finalsubject':
            jobsubject=Logic.setSubject(req)
            time = Logic.setTime(req)
            day=Logic.setDay(req)
            result = Logic.getdata_SubjectbyTime(time,day)
            if(result > 0):
                js_str = json.dumps(result)
                ans = json.loads(js_str)

            text = 'วิชา = '+ans['subject_name'] + ' เวลา = '+ans['time'] + 'วัน = '+day
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
    
    
    #เข้า database by job *
    def getdata_SubjectbyJob(job_name):
        ans = db.getSubbyTime(job_name)
        print(ans)
        return ans
    
    #เข้า database by time *
    def getdata_SubjectbyTime(groupjob_id,period,day): 
        ans = db.getSubbyTime(groupjob_id,period,day)
        return jsonify({'message': ans})
    
    #เข้า database by group_job
    def getdata_SubjectbyTime(groupjob_id):
        ans = db.getSubbyTime(groupjob_id)
        return jsonify({'message': ans})
    
    #เข้า database by time only*
    def getdata_SubjectbyTime(period, day):
        ans = db.getSubbyTime(period, day)
        return jsonify({'message': ans})
       
    # def answerbyTimeOnly(period,day):
    #     result = Logic.getdata_SubjectbyTime(period, day)
    #     if(result > 0):
    #         for x in result:
    #             js_str = json.dumps(result)
    #             ans = json.loads(js_str)
    #             answer = 'วัน : '+day +' เวลา : '+ans['time']+' วิชา :'+ans['subject_name']
        
    
#validate job -> groupjob -> time and day
#                         -> All

#validate time and day = subject
