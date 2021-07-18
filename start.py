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
                                    uri = "https://www.twtainan.net/zh-tw/attractions/detail/674"
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
                                    uri = "https://www.twtainan.net/zh-tw/attractions/detail/671"
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
                                    uri = "https://www.twtainan.net/zh-tw/attractions/detail/572"
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
                                    uri = "https://www.twtainan.net/zh-tw/attractions/detail/1351"
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
                            text = "接近傍晚的夕陽總是引人入勝\n是個讓外地遊客流連忘返的美麗沙灘",
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
                        ),
                        CarouselColumn( #6
                            thumbnail_image_url = "https://tainan.funcard.com.tw/imageCache/tainan/JnLv_600x400.jpg",
                            title = "德記洋行",
                            text = "清領時期繁盛一時的重要商業據點",
                            actions = [
                                URITemplateAction(
                                    label = "點我看介紹",
                                    uri = "https://www.twtainan.net/zh-tw/attractions/detail/687"
                                ),
                                MessageTemplateAction(
                                    label = "點我看景點圖片",
                                    text = "德記洋行圖片"
                                ),
                                MessageTemplateAction(
                                    label = "點我看地圖位置",
                                    text = "可由此打開德記洋行的google地圖位置"
                                )
                            ]
                        ),
                        CarouselColumn( #7
                            thumbnail_image_url = "https://4.bp.blogspot.com/-0kz6Q2pW1wk/Xiq0YZ-cKlI/AAAAAAAAJ6U/5rTRQS-99gk2LmMV9VJia79EjcalGfIPQCKgBGAsYHg/s1600/IMG_8444.jpg",
                            title = "花園夜市",
                            text = "台灣最知名和最熱鬧的夜市之一",
                            actions = [
                                URITemplateAction(
                                    label = "點我看介紹",
                                    uri = "https://www.twtainan.net/zh-tw/attractions/detail/5572"
                                ),
                                MessageTemplateAction(
                                    label = "點我看景點圖片",
                                    text = "花園夜市圖片"
                                ),
                                MessageTemplateAction(
                                    label = "點我看地圖位置",
                                    text = "可由此打開花園夜市的google地圖位置"
                                )
                            ]
                        ),
                        CarouselColumn( #8
                            thumbnail_image_url = "https://pic.pimg.tw/anrine910070/1601175205-2788673474-g.jpg",
                            title = "夕遊出張所",
                            text = "擁有專屬生日採鹽的原日式試鹽工廠",
                            actions = [
                                URITemplateAction(
                                    label = "點我看介紹",
                                    uri = "https://www.twtainan.net/zh-tw/attractions/detail/1323"
                                ),
                                MessageTemplateAction(
                                    label = "點我看景點圖片",
                                    text = "夕遊出張所圖片"
                                ),
                                MessageTemplateAction(
                                    label = "點我看地圖位置",
                                    text = "可由此打開夕遊出張所的google地圖位置"
                                )
                            ]
                        ),
                        CarouselColumn( #9
                            thumbnail_image_url = "https://photo.travelking.com.tw/scenery/98E3B96F-21E9-41AD-8193-31840E021733_e.jpg",
                            title = "台南孔廟",
                            text = "具有三百多年歷史的文化古都核心",
                            actions = [
                                URITemplateAction(
                                    label = "點我看介紹",
                                    uri = "https://www.twtainan.net/zh-tw/attractions/detail/800"
                                ),
                                MessageTemplateAction(
                                    label = "點我看景點圖片",
                                    text = "台南孔廟圖片"
                                ),
                                MessageTemplateAction(
                                    label = "點我看地圖位置",
                                    text = "可由此打開台南孔廟的google地圖位置"
                                )
                            ]
                        ),
                        CarouselColumn( #10
                            thumbnail_image_url = "https://www.twtainan.net/image/13910/1024x768",
                            title = "七股鹽山",
                            text = "以鹽為最大特色的高聳壯觀鹽山",
                            actions = [
                                URITemplateAction(
                                    label = "點我看介紹",
                                    uri = "https://www.twtainan.net/zh-tw/attractions/detail/471"
                                ),
                                MessageTemplateAction(
                                    label = "點我看景點圖片",
                                    text = "七股鹽山圖片"
                                ),
                                MessageTemplateAction(
                                    label = "點我看地圖位置",
                                    text = "可由此打開七股鹽山的google地圖位置"
                                )
                            ]
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, output_message)

 #----------------------------------------------------------------------------

        #景點位置區域
        #1
        elif user_message == "可由此打開赤崁樓的google地圖位置":
            output_message = LocationSendMessage(
                title = "赤崁樓",
                address = "台南市中西區民族路二段212號",
                latitude = "22.99762337852117",
                longitude = "120.2024704919533"
            )

            line_bot_api.reply_message(event.reply_token, output_message)

        #2
        elif user_message == "可由此打開安平古堡的google地圖位置":
            output_message = LocationSendMessage(
                title = "安平古堡",
                address = "台南市安平區國勝路82號",
                latitude = "23.001593229535548",
                longitude = "120.1606351263452"
            )

            line_bot_api.reply_message(event.reply_token, output_message)

        #3
        elif user_message == "可由此打開奇美博物館的google地圖位置":
            output_message = LocationSendMessage(
                title = "奇美博物館",
                address = "台南市仁德區文華路二段66號",
                latitude = "22.93480286259137",
                longitude = "120.2260482551798"
            )

            line_bot_api.reply_message(event.reply_token, output_message)
        
        #4
        elif user_message == "可由此打開神農街的google地圖位置":
            output_message = LocationSendMessage(
                title = "神農街",
                address = "台南市中西區民族路二段212號",
                latitude = "22.99753585895218",
                longitude = "120.19648398291852"
            )

            line_bot_api.reply_message(event.reply_token, output_message)

        #5
        elif user_message == "可由此打開漁光島的google地圖位置":
            output_message = LocationSendMessage(
                title = "漁光島",
                address = "台南市安平區漁光路114號",
                latitude = "22.98054329215947",
                longitude = "120.15580504320876"
            )            

            line_bot_api.reply_message(event.reply_token, output_message)

        #6
        elif user_message == "可由此打開德記洋行的google地圖位置":
            output_message = LocationSendMessage(
                title = "德記洋行",
                address = "台南市安平區古堡街108號",
                latitude = "23.013119029447406",
                longitude = "120.16109490409369"
            )            

            line_bot_api.reply_message(event.reply_token, output_message)

        #7
        elif user_message == "可由此打開花園夜市的google地圖位置":
            output_message = LocationSendMessage(
                title = "花園夜市",
                address = "台南市北區海安路三段533號",
                latitude = "23.01159041194204",
                longitude = "120.20039541306427"
            )            

            line_bot_api.reply_message(event.reply_token, output_message)

        #8
        elif user_message == "可由此打開夕遊出張所的google地圖位置":
            output_message = LocationSendMessage(
                title = "夕遊出張所",
                address = "台南市安平區古堡街196號",
                latitude = "23.002783289337064",
                longitude = "120.15633702634503"
            )            

            line_bot_api.reply_message(event.reply_token, output_message)

        #9
        elif user_message == "可由此打開台南孔廟的google地圖位置":
            output_message = LocationSendMessage(
                title = "台南孔廟",
                address = "台南市中西區南門路2號",
                latitude = "22.990712678956807",
                longitude = "120.20431901470467"
            )            

            line_bot_api.reply_message(event.reply_token, output_message)

        #10
        elif user_message == "可由此打開七股鹽山的google地圖位置":
            output_message = LocationSendMessage(
                title = "七股鹽山",
                address = "台南市七股區鹽埕里66號",
                latitude = "23.154298515853103",
                longitude = "120.09994515333189"
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