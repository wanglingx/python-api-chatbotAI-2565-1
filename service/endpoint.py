from __main__ import app
from flask import request
import app as api
from service.logic import Logic as lg
import service.plugin as db

class Endpoint:
    @app.route("/callback", methods=['POST'])
    def callback():
        body = request.get_data(as_text=True)
        print(body)
        req = request.get_json(silent=True, force=True)
        # ชื่อ intent ใน Dialog flow
        intent = req["queryResult"]["intent"]["displayName"]
        # ข้อความที่ส่งมา
        text = req['originalDetectIntentRequest']['payload']['data']['message']['text']
        # reply token
        reply_token = req['originalDetectIntentRequest']['payload']['data']['replyToken']
        # id ของผู้ใช้
        id = req['originalDetectIntentRequest']['payload']['data']['source']['userId']
        disname = api.line_bot_api.get_profile(id).display_name  
        
        # ชื่อของผู้ใช้
        # print(req)
        print('id = ' + id)
        print('name = ' + disname)
        print('text = ' + text)
        print('intent = ' + intent)
        print('reply_token = ' + reply_token)

        lg.reply(intent, text, reply_token, id, disname, req)
        return 'OK'

    #Test get data
    @app.route('/getTime', methods=['GET'])
    def getsub1():
        groupjob_id = 'GJ007'
        job = 'data science'
        period = 'afternoon'
        day = 'พฤหัสบดี'
        # sent to database
        result = db.getAllSub()
        subject = ''
        count = 1
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

        replyMgs = "วิชาเลือกที่เปิดในเทอมนี้ทั้งหมดมีดังนี้ก๊าบ" + \
            "\n"+"ซึ่งวันพฤหัสบดีและวันศุกร์นั้นจะมีวันเวลาเรียนในช่วงเดียวกันก๊าบ"+"\n"+subject+"น้องๆสามารถเลือกลงทะเบียนได้เลยนะก๊าบ"
        return replyMgs

    @app.route('/getTime2', methods=['GET'])
    def getsub2():
        return lg.answerbyTimeOnly(period='afternoon', day='จันทร์')
    
