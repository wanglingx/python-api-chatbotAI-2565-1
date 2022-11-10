from flask import Flask, jsonify, request
from linebot import *
from linebot.models import *

app = Flask(__name__)
import service.endpoint

line_bot_api = LineBotApi(
    'K5pHyly4QvSH2xtvNwX8GoN3nbaQc9Lzwzeko+QbpkU9tK+tE4SihRtrrq8cSRBZFtu13Iel6nQcxq2Wl8tCiXCAnw2CyaRfjSg/JPv0xGWbQ98bbr6iRRqyuO/VSsw0ehTtXSkcs03/DX5M3Waq1gdB04t89/1O/w1cDnyilFU=')
# ใส่ channel access token
handler = WebhookHandler(
    '73f8aaa61ae1c830c7c7074b595d8ab7')  # ใส่ Channel secret

if __name__ == "__main__":
    app.run()
