from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

from PIL import Image
from io import StringIO

import requests
import random
import json
import math
import time
import datetime

#---------------- self define module ----------------
import text_push as text_push
import text_reply as text_reply

#---------------- self define variables ----------------
from mykey import *

#---------------- line settings ----------------
# Channel Access Token
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
# Channel Secret
handler = WebhookHandler(LINE_CHANNEL_SECRET)

#---------------------------------------------------

app = Flask(__name__)

# 監聽所有來自 /callback 的 Post Request
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
@handler.add(MessageEvent)
def handle_message(event):
    print(event)
    message_send_time = float(event.timestamp)/1000
    message_get_time = float(time.time())
    msg_type = event.message.type

    if event.message.text == "info":
        output_message = TextSendMessage(text=str(event))  
        line_bot_api.reply_message(event.reply_token, output_message)

    if event.message.text.lower() == "speed" :
        output_message = ("【收到訊息時間】\n{} 秒\n【處理訊息時間】\n{} 秒".format(message_get_time-message_send_time,float(time.time())-message_get_time))
        output_message = text_reply.text_reply_message(user_message)
        line_bot_api.reply_message(event.reply_token, output_message)

    if msg_type == "sticker":
        output_message = StickerSendMessage(package_id='2',sticker_id=str(random.randint(140,180)))
        line_bot_api.reply_message(event.reply_token, output_message) 

    elif msg_type == "text":
        user_message = event.message.text

        if user_message == "可樂": 
            output_message = text_reply.text_reply_message("可樂好喝")
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == "肥宅快樂水":
            output_message = ImageSendMessage(
                preview_image_url = "https://f.share.photo.xuite.net/chungming01/1fe45d1/10789161/501035944_m.jpg"
                original_content_url = "https://f.share.photo.xuite.net/chungming01/1fe45d1/10789161/501035944_m.jpg",
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == "宏宏的家在哪裡":
            output_message = LocationSendMessage(
                title = "宏宏的家",
                address = "台中市北屯區陳平一街76巷2號5樓-2",
                latitude = "24.186120316114284",
                longitude = "120.66672397075935"
            )
            line_bot_api.reply_message(event.reply_token, output_message)
            
        # else:
        #     output_message = text_reply.text_reply_message("你說的是不是："+ user_message)
        #     line_bot_api.reply_message(event.reply_token, output_message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)