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

# instruction of pushing code to heroku
# git add .
# git commit -am'ok'
# git push heroku master

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
        output_message = StickerSendMessage(package_id='2',sticker_id='1')
        #output_message = StickerSendMessage(package_id='2',sticker_id=str(random.randint(140,180)))
        line_bot_api.reply_message(event.reply_token, output_message)

    elif msg_type == "text":
        user_message = event.message.text

        if user_message == "可樂": 
            output_message = text_reply.text_reply_message("可樂好喝")
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == "宏宏的愛人":
            output_message = text_reply.text_reply_message("嵐嵐<3")
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == "可i宏宏":
            output_message = AudioSendMessage(
                originalContentUrl = "https://mega.nz/file/kMwwjKiD#S3T5z8v1YpD-vK8SHE6oZBiGxuRkKVTMW4XLyK7IgZk",
                duration = "60000"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == "肥宅快樂水":
            output_message = ImageSendMessage(
                original_content_url = "https://f.share.photo.xuite.net/chungming01/1fe45d1/10789161/501035944_m.jpg",
                preview_image_url = "https://f.share.photo.xuite.net/chungming01/1fe45d1/10789161/501035944_m.jpg"
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

        elif user_message == "台南美食":
            output_message = TemplateSendMessage(
                alt_text = "",
                template = ButtonsTemplate(
                    thumbnail_image_url = "https://nurseilife.cc/wp-content/uploads/20170526115242_44.jpg",
                    title = "台南美食",
                    text = "帶你發掘你曾未發現過的美食",
                    actions = [
                        MessageTemplateAction(
                            label = "好吃的",
                            text = "好吃的"
                        ),
                        MessageTemplateAction(
                            label = "好喝的",
                            text = "好喝的"
                        ),
                        MessageTemplateAction(
                            label = "咖啡廳",
                            text = "咖啡廳"
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == "飲料":
            output_message = TemplateSendMessage(
            alt_text = "要顯示的字",
                template = ImageCarouselTemplate(
                    colunms = [
                        ImageCarouselColumn(
                            image_url = "",
                            action = URITemplateAction(
                                label = "標題",
                                uri = "網址"
                            )
                        ),
                        ImageCarouselColumn(
                            image_url = "",
                            action = URITemplateAction(
                                label = "標題",
                                uri = "網址"
                            )
                        ),
                        ImageCarouselColumn(
                            image_url = "",
                            action = URITemplateAction(
                                label = "標題",
                                uri = "網址"
                            )
                        ),
                        ImageCarouselColumn(
                            image_url = "",
                            action = URITemplateAction(
                                label = "標題",
                                uri = "網址"
                            )
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, output_message)
            
        else:
            output_message = text_reply.text_reply_message("請輸入有效指令！")
            line_bot_api.reply_message(event.reply_token, output_message)

# instruction of pushing code to heroku
# git add .
# git commit -am'ok'
# git push heroku master

#組圖訊息
def imagemap_message():
    output_message = ImagemapSendMessage(
        base_url = "https://www.gomaji.com/blog/wp-content/uploads/2020/04/IMG_0164-696x462.jpg",
        alt_text = "",
        base_size = BaseSize(height = 2000, width = 2000),
        actions =[
            #1
            URIImagemapAction(
                link_uri = "https://mega.nz/file/kQpm2bBa#trwG57vTJSv62v_eMqJ4z7sEEXOVAIYMquoJPg_p_jM",
                area = ImagemapArea(x = 0, y= 0, width = 1000, height = 1000)
            ),
            #2
            URIImagemapAction(
                link_uri = "https://mega.nz/file/QB4w1RpC#HM8hyzce2PkzztD1ZnSQF6sWrUcyYvyjz795S9erjSQ",
                area = ImagemapArea(x = 1000, y= 0, width = 1000, height = 1000)
            ),
            #3
            URIImagemapAction(
                link_uri = "https://mega.nz/file/8IwyRBbZ#T1DudpbwW7sVkk2dtgQLvi2mhqvIriwK_iql2LQR3oQ",
                area = ImagemapArea(x = 0, y= 1000, width = 1000, height = 1000)
            ),
            #4
            URIImagemapAction(
                link_uri = "https://mega.nz/file/MAhkjD7R#37wuu9Za0SYvEEE240IBJHed9IwFVQVWf16h16crD6Q",
                area = ImagemapArea(x = 1000, y= 1000, width = 1000, height = 1000)
            )
        ]
    )
    return output_message


#按鈕介面訊息
def button_message():
    output_message = TemplateSendMessage(
        alt_text = "好消息來了",
        template = ButtonsTemplate(
            thumbnail_image_url = "https://lurl.cc/pgUcaP",
            title = "",
            text = "",
            actions = [
                DatetimePickerTemplateAction(
                    label = "請選擇生日",
                    data = "input birthday",
                    mode = "data",
                    initial = "1999-01-01",
                    max = "2021-07-07",
                    min = "1930-01-01"
                ),
                MessageTemplateAction(
                    label = "看抽獎品項",
                    text = "有哪些抽獎品項呢？"
                ),
                URITemplateAction(
                    label = "免費註冊享回饋",
                    uri =""
                )
            ]
        )
    )
    return output_message


#確認介面訊息
def Confirm_Template():
    output_message = TemplateMessage(
        alt_text = "是否註冊成為會員？",
        template = Confirm_Template(
            text = "是否註冊成會員？",
            actions = [
                PostbackTemplateAction(
                    label = "馬上註冊",
                    text = "註冊會員",
                    data = "會員註冊"
                ),
                MessageTemplateAction(
                    label = "查詢其他功能",
                    text = "查詢其他功能"
                )
            ]
        )
    )
    return output_message

#多頁訊息(旋轉木馬)
def Carousel_Template(): #最多十組
    output_message = TemplateSendMessage(
        columns = [
            CarouselColumn( #1
                thumbnail_image_url = "",
                title = "第一塊模板",
                text = "註解",
                actions = [
                    PostbackTemplateAction(
                        label = "",
                        data = ""
                    ),
                    MessageTemplateAction(
                        label = "",
                        text = ""
                    ),
                    URITemplateAction(
                        label = "",
                        uri =""
                    )
                ]
            ),
            CarouselColumn( #2
                thumbnail_image_url = "",
                title = "第二塊模板",
                text = "註解",
                actions = [
                    PostbackTemplateAction(
                        label = "",
                        data = ""
                    ),
                    MessageTemplateAction(
                        label = "",
                        text = ""
                    ),
                    URITemplateAction(
                        label = "",
                        uri =""
                    )
                ]
            ),
            CarouselColumn( #3
                thumbnail_image_url = "",
                title = "第三塊模板",
                text = "註解",
                actions = [
                    PostbackTemplateAction(
                        label = "",
                        data = ""
                    ),
                    MessageTemplateAction(
                        label = "",
                        text = ""
                    ),
                    URITemplateAction(
                        label = "",
                        uri =""
                    )
                ]
            ),
            CarouselColumn( #4
                thumbnail_image_url = "",
                title = "第四塊模板",
                text = "註解",
                actions = [
                    PostbackTemplateAction(
                        label = "",
                        data = ""
                    ),
                    MessageTemplateAction(
                        label = "",
                        text = ""
                    ),
                    URITemplateAction(
                        label = "",
                        uri =""
                    )
                ]
            )
        ]
    )

#多頁圖片(旋轉木馬圖片)
def image_carousel_message():
    output_message = TemplateSendMessage(
        alt_text = "要顯示的字",
        template = ImageCarouselTemplate(
            colunms = [
                ImageCarouselColumn(
                    image_url = "",
                    action = URITemplateAction(
                        label = "標題",
                        uri = "網址"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "",
                    action = URITemplateAction(
                        label = "標題",
                        uri = "網址"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "",
                    action = URITemplateAction(
                        label = "標題",
                        uri = "網址"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "",
                    action = URITemplateAction(
                        label = "標題",
                        uri = "網址"
                    )
                )
            ]
        )
    )
    

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)