import app
import service.plugin as db


class Logic:
    def reply(intent, text, reply_token, id, disname, req):  # function reply
        if intent == 'testdodo':  # จับว่าเป็น intent ไหน
            text = Logic.test1()

        elif intent == 'show-all-subject':  # 1.1 แสดงอาชีพทั้งหมดในสายนั้น
            job = Logic.setjob(req)
            groupjob_id = Logic.getgroups_ID(job)
            text = Logic.answerbyJobOnly(job, groupjob_id)

        elif intent == 'choose-day-after - yes':  # 1.2 ใส่เวลา วัน อาชีพ
            job = Logic.setjob(req)
            time = Logic.setTime(req)
            day = Logic.setDay(req)
            groupjob_id = Logic.getgroups_ID(job)
            text = Logic.answerbyJobnPeriodnDay(job, groupjob_id, time, day)

        elif intent == 'select-from-time-choose-day - yes':  # 2.ช่วงเวลา วัน
            time = Logic.setTime(req)
            day = Logic.setDay(req)
            text = Logic.answerbyTimeOnly(time, day)

        elif intent == 'classroom':
            day = Logic.setDay(req)
            subject = Logic.setSubject(req)
            section = Logic.setSection(req)
            text = Logic.ansClassroom(subject, section, day)
            # print("day = ",day," sub = ",subject," section = ",section)

        text_message = app.TextSendMessage(text)
        app.line_bot_api.reply_message(
            reply_token, text_message)  # ส่งข้อความตอบกลับไป

    def test1():
        return 'ทดสอบสำเร็จ'

    def setjob(req):
        job = req["queryResult"]["outputContexts"][1]["parameters"]["job"]
        # jobsubject = jobsubject.upper()
        return job

    def setTime(req):
        time = req["queryResult"]["outputContexts"][0]["parameters"]["time"]
        if time == 'เช้า' or time == 'ช่วงเช้า':
            time = 'morning'
        elif time == 'บ่าย' or time == 'ช่วงบ่าย':
            time = 'afternoon'
        elif time == 'เย็น' or time == 'ช่วงเย็น':
            time = 'evening'
        return time

    def setDay(req):
        day = req["queryResult"]["outputContexts"][0]["parameters"]["day"]
        return day

    def setSubject(req):
        subject = req["queryResult"]["outputContexts"][0]["parameters"]["classroom"]
        return subject

    def setSection(req):
        section = req["queryResult"]["outputContexts"][0]["parameters"]["section"]
        if section == "Sec 1":
            section = '1'
        elif section == 'Sec 2':
            section = '2'
        elif section == 'วิชาเลือก':
            section = '1'
        return section

    # เข้า database by job
    def getgroups_ID(job_name):
        groupjob_id = db.getSubbyJOb(job_name)
        return groupjob_id

    # เข้า database by group_job
    def getdata_SubjectbyGroupjob(groupjob_id):
        ans = db.getSubbyGroupjob(groupjob_id)
        return ans

    # เข้า database by job and period
    def getdata_SubjectbyJob(groupjob_id, period):
        ans = db.getSubbyJobnPeriod(groupjob_id, period)
        return ans

    # เข้า database by job and period and time
    def getdata_SubjectbyTimeJob(groupjob_id, period, day):
        ans = db.getSubbyTime(groupjob_id, period, day)
        return ans

    # เข้า database by time only
    def getdata_SubjectbyTime(period, day):
        ans = db.getSubbyTimeNG(period, day)
        return ans

    # เข้า database เมื่อมันไม่มีวันที่กำหนด โดยมันเก็บค่าวิชาทั้งหมดในเทอมนั้นออกจาก database
    def getdata_SubAll():
        ans = db.getAllSub()
        return ans

    # scene 1.1 job only by groupjob when not day or show all by job
    def answerbyJobOnly(job, groupjob_id):
        resualt = Logic.getdata_SubjectbyGroupjob(groupjob_id)
        subject = ''
        temp = []
        ans = dict()
        if len(resualt) > 0:
            for key, val in resualt.items():
                if val not in temp:
                    temp.append(val)
                    ans[key] = val
                    subject += " วิชา : " + \
                        ans[str(key)]["subject_id"]+" " + \
                        ans[str(key)]["subject_name"]+"เวลา . " + \
                        ans[str(key)]["time"] + "\n"

            replyMgs = " วิชาเลือกที่เปิดในเทอมนี้ตามสายงานด้าน "+job + \
            " มีดังนี้ก๊าบ "+"\n"+subject+"\nน้องๆสามารถเลือกลงทะเบียนได้เลยนะก๊าบ"
        return replyMgs

    # scence 1.3 by job and period (group_job,period,day)

    def answerbyJobnPeriodnDay(job, groupjob_id, period, day):
        resualt = Logic.getdata_SubjectbyTimeJob(groupjob_id, period, day)
        print(resualt)
        subject = ''
        temp = []
        ans = dict()
        if len(resualt) > 0:
            for key, val in resualt.items():
                if val not in temp:
                    temp.append(val)
                    ans[key] = val
                    subject += " วิชา : " + \
                        ans[str(key)]["subject_id"]+" " + \
                        ans[str(key)]["subject_name"]+"เวลา . " + \
                        ans[str(key)]["time"] + "\n"
            if period == 'morning':
                period = "เช้า"
            if period == 'afternoon':
                period = "บ่าย"
            if period == 'evening':
                period = "เย็น"

            replyMgs = " วิชาเลือกที่เปิดในเทอมนี้ตามสายงานด้าน "+job+" ช่วง "+period+" ของวัน "+day+" มีดังนี้ " + \
            "\n"+subject+"น้องๆสามารถเลือกลงได้เลยนะก๊าบ"

        elif len(ans) <= 0:
            allsub = Logic.answerbyJobOnly(job, groupjob_id)
            replyMgs = " เทอมนี้ยังไม่มีวิชาที่เปิดสอนในช่วงเวลาที่น้องๆเลือกก๊าบ น้องๆสามารถเลือกเพิ่มเติมได้จาก " + allsub
        return replyMgs

    # scene 2.1 only time
    def answerbyTimeOnly(period, day):
        result = Logic.getdata_SubjectbyTime(period, day)
        subject = ''
        temp = []
        ans = dict()
        if len(result) > 0:
            for key, val in result.items():
                if val not in temp:
                    temp.append(val)
                    ans[key] = val
                    subject += "เวลา . " + \
                        ans[str(key)]["time"] + " วิชา : " + \
                        ans[str(key)]["subject_id"]+" " + \
                        ans[str(key)]["subject_name"]+"\n"
            if period == 'morning':
                period = "เช้า"
            if period == 'afternoon':
                period = "บ่าย"
            if period == 'evening':
                period = "เย็น"

            replyMgs = "สำหรับวิชาเลือกที่เปิดให้ลงทะเบียนในเทอมนี้ช่วง"+period+"ของวัน" + \
                day+"มีดังนี้"+"\n"+subject+"น้องๆสามารถเลือกลงทะเบียนได้เลยนะก๊าบ"

        elif len(result) <= 0:
            replyMgs = Logic.answerAllSub()
        return replyMgs

    # scene 2.2 all of semester not job not period not day
    def answerAllSub():
        resualt = Logic.getdata_SubAll()
        subject = ''
        temp = []
        ans = dict()
        if len(resualt) > 0:
            for key, val in resualt.items():
                if val not in temp:
                    temp.append(val)
                    ans[key] = val
                    subject += " วิชา : " + \
                        ans[str(key)]["subject_id"]+" " + \
                        ans[str(key)]["subject_name"]+"เวลา . " + \
                        ans[str(key)]["time"] + "\n"

            replyMgs = "ไม่มีวิชาเลือกในวันที่น้องๆเลือกในเทอมนี้ก๊าบ "+"\n"+"โดยวิชาเลือกที่เปิดสอนทั้งหมดในเทอมนี้ มีดังนี้ก๊าบ " + \
                "\n"+"ซึ่งวันพฤหัสบดีและวันศุกร์นั้นจะมีวันเวลาเรียนในช่วงเดียวกันก๊าบ" + \
                "\n"+subject+"น้องๆสามารถเลือกลงทะเบียนได้เลยนะก๊าบ"
        return replyMgs

    # classroom
    # เข้า Data base subject section day
    def getData_classroom(subject, section, day):
        classroom = db.getClassroom(subject, section, day)
        return classroom

    # scene ask classroom
    def ansClassroom(subject, section, day):
        result = Logic.getData_classroom(subject, section, day)
        msg = ''
        temp = []
        classroom = dict()
        if len(result) > 0:
            for key, val in result.items():
                if val not in temp:
                    temp.append(val)
                    classroom[key] = val
                    msg += " เซค "+classroom[str(key)]["section"]+"\n" +\
                        "เรียนที่ "+classroom[str(key)]["classroom"]+"\n" +\
                        "เวลา " + classroom[str(key)]["time"]+"\n"

            replyMsg = "วิชา "+subject+" วัน"+day+msg

        elif len(result) <= 0:
            replyMsg = "น้องใส่ข้อมูลผิดหรือเปล่าก๊าบ"
        return replyMsg
