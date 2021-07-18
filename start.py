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

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# instruction of pushing code to heroku
# git add .
# git commit -am'ok'
# git push heroku master

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Messgae Types
# 1. Text Message
# 2. Sticker Message
# 3. Image Message
# 4. Video Message
# 5. Audio Message
# 6. Location Message
# 7. Imgaemap Message
# 8. Template Message
# 9. Flex Message

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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
        output_message = StickerSendMessage(package_id='1',sticker_id='1')
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

        elif user_message == "宏宏的家在哪裡":
            output_message = LocationSendMessage(
                title = "宏宏的家",
                address = "台中市北屯區陳平一街76巷2號5樓-2",
                latitude = "24.186120316114284",
                longitude = "120.66672397075935"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == "肥宅快樂水":
            output_message = ImageSendMessage(
                original_content_url = "https://f.share.photo.xuite.net/chungming01/1fe45d1/10789161/501035944_m.jpg",
                preview_image_url = "https://f.share.photo.xuite.net/chungming01/1fe45d1/10789161/501035944_m.jpg"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        #首頁
        elif user_message == "台南旅遊":
            output_message = TemplateSendMessage(
                alt_text = "此裝置不支援樣板。", #無法支援格式所顯示的文字
                template = ButtonsTemplate(
                    thumbnail_image_url = "https://nurseilife.cc/wp-content/uploads/20170526115242_44.jpg",
                    title = "台南旅遊",
                    text = "帶你玩遍美食之都台南",
                    actions = [
                        MessageTemplateAction(
                            label = "景點",
                            text = "景點"
                        ),
                        MessageTemplateAction(
                            label = "吃的",
                            text = "吃的"
                        ),
                        MessageTemplateAction(
                            label = "喝的",
                            text = "喝的"
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, output_message)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        #景點區域
        elif user_message == "景點":
            output_message = TemplateSendMessage(
                alt_text = "此裝置不支援樣板。", #無法支援格式所顯示的文字
                template = CarouselTemplate(
                    columns = [
                        CarouselColumn( #1
                            thumbnail_image_url = "https://pic.pimg.tw/whuy123/1523332170-611241936.jpg",
                            title = "赤崁樓",
                            text = "歷史悠久的荷治時期行政中心",
                            actions = [
                                URITemplateAction(
                                    label = "點我看介紹",
                                    uri = "https://www.taiwan.net.tw/m1.aspx?sNo=0001016&id=10889"
                                ),
                                MessageTemplateAction(
                                    label = "點我看景點圖片",
                                    text = "赤崁樓圖片"
                                ),
                                MessageTemplateAction(
                                    label = "點我看地圖位置",
                                    text = "可由此打開赤崁樓的google地圖位置"
                                )
                            ]
                        ),
                        CarouselColumn( #2
                            thumbnail_image_url = "https://image.cdn-eztravel.com.tw/BIvf9xU550uLpO3D1NYvXGNT4nyO_NgoOh-5hPd4IEQ/g:ce/aHR0cHM6Ly92YWNhdGlvbi5jZG4tZXp0cmF2ZWwuY29tLnR3L2ltZy9WRFIvVE5OXzEyMDAzMzQyMTAuanBn.jpg",
                            title = "安平古堡",
                            text = "由荷蘭人建造的台灣史上第一座城堡",
                            actions = [
                                URITemplateAction(
                                    label = "點我看介紹",
                                    uri = "https://www.taiwan.net.tw/m1.aspx?sNo=0001016&id=147"
                                ),
                                MessageTemplateAction(
                                    label = "點我看景點圖片",
                                    text = "安平古堡圖片"
                                ),
                                MessageTemplateAction(
                                    label = "點我看地圖位置",
                                    text = "可由此打開安平古堡的google地圖位置"
                                )
                            ]
                        ),
                        CarouselColumn( #3
                            thumbnail_image_url = "https://www.chimeimuseum.org/uploads/sliders/60da70ae81eaa.jpg",
                            title = "奇美博物館",
                            text = "擁有西洋藝術、樂器、兵器等的知名博物館",
                            actions = [
                                URITemplateAction(
                                    label = "點我看介紹",
                                    uri = "https://www.taiwan.net.tw/m1.aspx?sNo=0001016&id=2574"
                                ),
                                MessageTemplateAction(
                                    label = "點我看景點圖片",
                                    text = "奇美博物館圖片"
                                ),
                                MessageTemplateAction(
                                    label = "點我看地圖位置",
                                    text = "可由此打開奇美博物館的google地圖位置"
                                )
                            ]
                        ),
                        CarouselColumn( #4
                            thumbnail_image_url = "https://cc.tvbs.com.tw/img/program/upload/2020/02/05/20200205163001-ba4cb2f0.jpg",
                            title = "神農街",
                            text = "以街底主祀神農氏之藥王廟為名的創新老街",
                            actions = [
                                URITemplateAction(
                                    label = "點我看介紹",
                                    uri = "https://www.travelking.com.tw/tourguide/scenery105017.html"
                                ),
                                MessageTemplateAction(
                                    label = "點我看景點圖片",
                                    text = "神農街圖片"
                                ),
                                MessageTemplateAction(
                                    label = "點我看地圖位置",
                                    text = "可由此打開神農街的google地圖位置"
                                )
                            ]
                        ),
                        CarouselColumn( #5
                            thumbnail_image_url = "https://img.natgeomedia.com/userfiles/PhotoContest/925/sm1920/2019090977389193.jpg",
                            title = "漁光島",
                            text = "接近傍晚的夕陽總是引人入勝",
                            actions = [
                                URITemplateAction(
                                    label = "點我看介紹",
                                    uri = "https://www.twtainan.net/zh-tw/attractions/detail/5520"
                                ),
                                MessageTemplateAction(
                                    label = "點我看景點圖片",
                                    text = "漁光島圖片"
                                ),
                                MessageTemplateAction(
                                    label = "點我看地圖位置",
                                    text = "可由此打開漁光島的google地圖位置"
                                )
                            ]
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, output_message)

 #----------------------------------------------------------------------------

        #景點位置區域
        elif user_message == "可由此打開赤崁樓的google地圖位置":
            output_message = LocationSendMessage(
                title = "赤崁樓",
                address = "台南市中西區民族路二段212號",
                latitude = "22.99762337852117",
                longitude = "120.2024704919533"
            )

            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == "可由此打開安平古堡的google地圖位置":
            output_message = LocationSendMessage(
                title = "安平古堡",
                address = "台南市安平區國勝路82號",
                latitude = "23.001593229535548",
                longitude = "120.1606351263452"
            )

            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == "可由此打開奇美博物館的google地圖位置":
            output_message = LocationSendMessage(
                title = "奇美博物館",
                address = "台南市仁德區文華路二段66號",
                latitude = "22.93480286259137",
                longitude = "120.2260482551798"
            )

            line_bot_api.reply_message(event.reply_token, output_message)
        
        elif user_message == "可由此打開神農街的google地圖位置":
            output_message = LocationSendMessage(
                title = "神農街",
                address = "台南市中西區民族路二段212號",
                latitude = "22.99753585895218",
                longitude = "120.19648398291852"
            )

            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == "可由此打開漁光島的google地圖位置":
            output_message = LocationSendMessage(
                title = "漁光島",
                address = "台南市安平區漁光路114號",
                latitude = "22.98054329215947",
                longitude = "120.15580504320876"
            )            

            line_bot_api.reply_message(event.reply_token, output_message)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        elif user_message == "吃的":
            output_message = text_reply.text_reply_message("想找好吃的嗎")
            line_bot_api.reply_message(event.reply_token, output_message)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        elif user_message == "喝的":
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

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            
        else:
            output_message = text_reply.text_reply_message("請輸入有效指令！")
            line_bot_api.reply_message(event.reply_token, output_message)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# instruction of pushing code to heroku
# git add .
# git commit -am'ok'
# git push heroku master

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)