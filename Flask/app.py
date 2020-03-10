from flask import Flask, request, abort


from linebot import LineBotApi,WebhookHandler
from linebot.models import TextSendMessage, MessageEvent,TextMessage, ImageSendMessage
from linebot.exceptions import LineBotApiError, InvalidSignatureError


app = Flask(__name__)
line_bot_api = LineBotApi("0fbixQI2IB1UYAukAR6hcHmaxhbrOVs5NyjYebYQdMo0LCqqRu3e6N1eqNv19X9Kbulxv7B9C0A13GSSTAoz+HXMAR4LgVd1roJlXJ7mPJ2c4vMyhaGXGcoGw+gVM3FLAH5bDXUpEuhrKm9GaGQUjQdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("3848424dc45ce3a927dcbec148135094")

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event)
    print(event.source.user_id)
    text=event.message.text

    if (text=="Hi"):
        reply_text = "Hello"
        #Your user ID

    elif(text=="你好"):
        reply_text = "哈囉"
    elif(text=="機器人"):
        reply_text = "叫我嗎"
    else:
        reply_text = text
#如果非以上的選項，就會學你說話

    message = TextSendMessage(reply_text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    #port = int(os.environ.get('PORT', 5000))
    #app.run(host='0.0.0.0', port=port)
    app.run()