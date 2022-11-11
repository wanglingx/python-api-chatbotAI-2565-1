from __main__ import app
from flask import Flask, jsonify, request
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
        groupjob_id = 'GJ001'
        period = 'afternoon'
        day = 'พฤหัสบดี'
        # sent to database
        ans = db.getSubbyTimeNG(period,day)
        return jsonify({'message': ans })
