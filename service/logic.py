import app
class Logic:
    def reply(intent, text, reply_token, id, disname, req):  # function reply
        if intent == 'testdodo':  # จับว่าเป็น intent ไหน
            text = Logic.test1()
        elif intent == 'finalsubject':
            jobsubject=Logic.setSubject(req)
            time = Logic.setTime(req)
            day=Logic.setDay(req)
            Logic.getdata_Subject(jobsubject , time)


            text = 'วิชา = '+jobsubject+' เวลา = '+time + 'วัน = '+day

        elif intent == 'classroom':
            Logic.test1()
            # if intent == 'test2':
        # elif intent == 'time':
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
        return day
    
    def getdata_Subject(job , time): #เข้า database
        print(job + time)

