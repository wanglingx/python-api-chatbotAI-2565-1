import app
class Logic:
    def reply(intent, text, reply_token, id, disname, req):  # function reply
        if intent == 'testdodo':  # จับว่าเป็น intent ไหน
            test1(reply_token)
        elif intent == 'Test':
            test2(reply_token, req)
            # if intent == 'test2':

def test1(reply_token):
    text_message = app.TextSendMessage(text='ทดสอบสำเร็จ')
    app.line_bot_api.reply_message(
        reply_token, text_message)  # ส่งข้อความตอบกลับไป


def test2(reply_token, req):
    weight = req["queryResult"]["parameters"]["weight"]
    text = 'มึงน้ำหนัก'+str(weight)
    text_message = app.TextSendMessage(text)
    app.line_bot_api.reply_message(reply_token, text_message)
