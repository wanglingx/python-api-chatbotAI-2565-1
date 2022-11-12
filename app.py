from flask import Flask, jsonify, request
from linebot import *
from linebot.models import *

app = Flask(__name__)
import service.endpoint 

line_bot_api = LineBotApi(
    'eYbpJmbmoA7dOeNDxt5hwmGIrVqQit277XtbUGgMluBE8etfKEuD6uuiJkofvBMCFtu13Iel6nQcxq2Wl8tCiXCAnw2CyaRfjSg/JPv0xGVG270Gp38/ZsNry8tOJXmkMX5wYsaW+342ucW+hcSmxwdB04t89/1O/w1cDnyilFU=')
# ใส่ channel access token
handler = WebhookHandler(
    '73f8aaa61ae1c830c7c7074b595d8ab7')  # ใส่ Channel secret

if __name__ == "__main__":
    app.run()
