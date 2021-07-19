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
from tourist_spots import *
from food import *
from drink import *

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
        output_message = StickerSendMessage(package_Id='1',sticker_Id='1')
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

        #景點
        elif user_message == "景點":
            output_message = tourist_carousel_template()
            line_bot_api.reply_message(event.reply_token, output_message)


        #景點位置區域

        #1
        elif user_message ==f"可由此打開{place1}的google地圖位置":
            output_message = LocationSendMessage(
                title = f"{place1}",
                address = "台南市中西區民族路二段212號",
                latitude = "22.99762337852117",
                longitude = "120.2024704919533"
            )

            line_bot_api.reply_message(event.reply_token, output_message)

        #2
        elif user_message == f"可由此打開{place2}的google地圖位置":
            output_message = LocationSendMessage(
                title = f"{place2}",
                address = "台南市安平區國勝路82號",
                latitude = "23.001593229535548",
                longitude = "120.1606351263452"
            )

            line_bot_api.reply_message(event.reply_token, output_message)

        #3
        elif user_message == f"可由此打開{place3}的google地圖位置":
            output_message = LocationSendMessage(
                title = f"{place3}",
                address = "台南市仁德區文華路二段66號",
                latitude = "22.93480286259137",
                longitude = "120.2260482551798"
            )

            line_bot_api.reply_message(event.reply_token, output_message)
        
        #4
        elif user_message == f"可由此打開{place4}的google地圖位置":
            output_message = LocationSendMessage(
                title = f"{place4}",
                address = "台南市中西區民族路二段212號",
                latitude = "22.99753585895218",
                longitude = "120.19648398291852"
            )

            line_bot_api.reply_message(event.reply_token, output_message)

        #5
        elif user_message == f"可由此打開{place5}的google地圖位置":
            output_message = LocationSendMessage(
                title = f"{place5}",
                address = "台南市安平區漁光路114號",
                latitude = "22.98054329215947",
                longitude = "120.15580504320876"
            )            

            line_bot_api.reply_message(event.reply_token, output_message)

        #6
        elif user_message == f"可由此打開{place6}的google地圖位置":
            output_message = LocationSendMessage(
                title = f"{place6}",
                address = "台南市安平區古堡街108號",
                latitude = "23.003306864536732",
                longitude = "120.15982008130227"
            )            

            line_bot_api.reply_message(event.reply_token, output_message)

        #7
        elif user_message == f"可由此打開{place7}的google地圖位置":
            output_message = LocationSendMessage(
                title = f"{place7}",
                address = "台南市北區海安路三段533號",
                latitude = "23.01159041194204",
                longitude = "120.20039541306427"
            )            

            line_bot_api.reply_message(event.reply_token, output_message)

        #8
        elif user_message == f"可由此打開{place8}的google地圖位置":
            output_message = LocationSendMessage(
                title = f"{place8}",
                address = "台南市安平區古堡街196號",
                latitude = "23.002783289337064",
                longitude = "120.15633702634503"
            )            

            line_bot_api.reply_message(event.reply_token, output_message)

        #9
        elif user_message == f"可由此打開{place9}的google地圖位置":
            output_message = LocationSendMessage(
                title = f"{place9}",
                address = "台南市中西區南門路2號",
                latitude = "22.990712678956807",
                longitude = "120.20431901470467"
            )            

            line_bot_api.reply_message(event.reply_token, output_message)

        #10
        elif user_message == f"可由此打開{place10}的google地圖位置":
            output_message = LocationSendMessage(
                title = f"{place10}",
                address = "台南市七股區鹽埕里66號",
                latitude = "23.154298515853103",
                longitude = "120.09994515333189"
            )            

            line_bot_api.reply_message(event.reply_token, output_message)


        #景點照片區域

        #1
        elif user_message == f"{place1}圖片":
            output_message = image_carousel_message1()
            line_bot_api.reply_message(event.reply_token, output_message)

        #2
        elif user_message == f"{place2}圖片":
            output_message = image_carousel_message2()
            line_bot_api.reply_message(event.reply_token, output_message)
        
        #3
        elif user_message == f"{place3}圖片":
            output_message = image_carousel_message3()
            line_bot_api.reply_message(event.reply_token, output_message)

        #4
        elif user_message == f"{place4}圖片":
            output_message = image_carousel_message4()
            line_bot_api.reply_message(event.reply_token, output_message)

        #5
        elif user_message == f"{place5}圖片":
            output_message = image_carousel_message5()
            line_bot_api.reply_message(event.reply_token, output_message)

        #6
        elif user_message == f"{place6}圖片":
            output_message = image_carousel_message6()
            line_bot_api.reply_message(event.reply_token, output_message)
        
        #7
        elif user_message == f"{place7}圖片":
            output_message = image_carousel_message7()
            line_bot_api.reply_message(event.reply_token, output_message)

        #8
        elif user_message == f"{place8}圖片":
            output_message = image_carousel_message8()
            line_bot_api.reply_message(event.reply_token, output_message)
        
        #9
        elif user_message == f"{place9}圖片":
            output_message = image_carousel_message9()
            line_bot_api.reply_message(event.reply_token, output_message)
        
        #10
        elif user_message == f"{place10}圖片":
            output_message = image_carousel_message10()
            line_bot_api.reply_message(event.reply_token, output_message)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        #美食主界面
        elif user_message == "吃的":
            output_message = TemplateSendMessage(
                alt_text = "此裝置不支援樣板。", #無法支援格式所顯示的文字
                template = ButtonsTemplate(
                    thumbnail_image_url = "https://nurseilife.cc/wp-content/uploads/20170526115242_44.jpg",
                    title = "台南美食",
                    text = "所有的台南佳餚都在這",
                    actions = [
                        MessageTemplateAction(
                            label = "台南美食part1",
                            text = "台南美食part1"
                        ),
                        MessageTemplateAction(
                            label = "台南美食part2",
                            text = "台南美食part2"
                        ),
                        MessageTemplateAction(
                            label = "台南點心",
                            text = "台南點心"
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        #美食part1
        elif user_message == "台南美食part1":
            output_message = food_carousel_template1()
            line_bot_api.reply_message(event.reply_token, output_message)

        #美食part2
        elif user_message == "台南美食part2":
            output_message = food_carousel_template2()
            line_bot_api.reply_message(event.reply_token, output_message)
        
        #點心
        elif user_message == "台南點心":
            output_message = dessert_carousel_template()
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