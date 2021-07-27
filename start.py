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
        # elif user_message == "台南旅遊" or "台南" or "旅遊":
        #     output_message = TemplateSendMessage(
        #         alt_text = "此裝置不支援樣板。", #無法支援格式所顯示的文字
        #         template = ButtonsTemplate(
        #             thumbnail_image_url = "https://nurseilife.cc/wp-content/uploads/20170526115242_44.jpg",
        #             title = "台南旅遊",
        #             text = "帶你玩遍美食之都台南",
        #             actions = [
        #                 MessageTemplateAction(
        #                     label = "景點",
        #                     text = "景點"
        #                 ),
        #                 MessageTemplateAction(
        #                     label = "吃的",
        #                     text = "吃的"
        #                 ),
        #                 MessageTemplateAction(
        #                     label = "喝的",
        #                     text = "喝的"
        #                 )
        #             ]
        #         )
        #     )
        #     line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == "台南旅遊":
            reply_arr = []
            output_message1 = text_reply.text_reply_message("您好，請問想查詢什麼呢？")
            
            output_message2 = ImagemapSendMessage(
                base_url = "https://i.imgur.com/0tztQt1.jpg",
                alt_text = "此裝置不支援樣板。", #無法支援格式所顯示的文字
                base_size = BaseSize(height = 2000, width = 2000),
                actions =[
                    #1
                    MessageImagemapAction(
                        text = "台南景點",
                        area = ImagemapArea(x = 0, y= 0, width = 1000, height = 1000)
                    ),
                    #2
                    MessageImagemapAction(
                        text = "台南美食",
                        area = ImagemapArea(x = 1000, y= 0, width = 1000, height = 1000)
                    ),
                    #3
                    MessageImagemapAction(
                        text = "台南飲料",
                        area = ImagemapArea(x = 0, y= 1000, width = 1000, height = 1000)
                    ),
                    #4
                    MessageImagemapAction(
                        text = "台南咖啡廳",
                        area = ImagemapArea(x = 1000, y= 1000, width = 1000, height = 1000)
                    )
                ]
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)
            line_bot_api.reply_message(event.reply_token, reply_arr)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        #景點
        elif user_message == "台南景點":
            output_message = tourist_carousel_template()
            line_bot_api.reply_message(event.reply_token, output_message)


        #景點位置區域

        #1
        elif user_message ==f"{place1}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{place1}的google地圖位置") 
            output_message2 = LocationSendMessage(
                title = f"{place1}",
                address = "台南市中西區民族路二段212號",
                latitude = "22.99762337852117",
                longitude = "120.2024704919533"
 
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #2
        elif user_message == f"{place2}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{place2}的google地圖位置") 
            output_message2 = LocationSendMessage(
                title = f"{place2}",
                address = "台南市安平區國勝路82號",
                latitude = "23.001593229535548",
                longitude = "120.1606351263452"
 
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #3
        elif user_message == f"{place3}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{place3}的google地圖位置") 
            output_message2 = LocationSendMessage(
                title = f"{place3}",
                address = "台南市仁德區文華路二段66號",
                latitude = "22.93480286259137",
                longitude = "120.2260482551798"
 
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)
            line_bot_api.reply_message(event.reply_token, reply_arr)
        
        #4
        elif user_message == f"{place4}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{place4}的google地圖位置") 
            output_message2 = LocationSendMessage(
                title = f"{place4}",
                address = "台南市中西區民族路二段212號",
                latitude = "22.99753585895218",
                longitude = "120.19648398291852"
 
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #5
        elif user_message == f"{place5}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{place5}的google地圖位置") 
            output_message2 = LocationSendMessage(
                title = f"{place5}",
                address = "台南市安平區漁光路114號",
                latitude = "22.98054329215947",
                longitude = "120.15580504320876"
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)            
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #6
        elif user_message == f"{place6}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{place6}的google地圖位置") 
            output_message2 = LocationSendMessage(
                title = f"{place6}",
                address = "台南市安平區古堡街108號",
                latitude = "23.003306864536732",
                longitude = "120.15982008130227"
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)            
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #7
        elif user_message == f"{place7}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{place7}的google地圖位置") 
            output_message2 = LocationSendMessage(
                title = f"{place7}",
                address = "台南市北區海安路三段533號",
                latitude = "23.01159041194204",
                longitude = "120.20039541306427"
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)            
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #8
        elif user_message == f"{place8}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{place8}的google地圖位置") 
            output_message2 = LocationSendMessage(
                title = f"{place8}",
                address = "台南市安平區古堡街196號",
                latitude = "23.002783289337064",
                longitude = "120.15633702634503"
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)            
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #9
        elif user_message == f"{place9}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{place9}的google地圖位置") 
            output_message2 = LocationSendMessage(
                title = f"{place9}",
                address = "台南市中西區南門路2號",
                latitude = "22.990712678956807",
                longitude = "120.20431901470467"
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)            
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #10
        elif user_message == f"{place10}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{place10}的google地圖位置") 
            output_message2 = LocationSendMessage(
                title = f"{place10}",
                address = "台南市七股區鹽埕里66號",
                latitude = "23.154298515853103",
                longitude = "120.09994515333189"
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)            
            line_bot_api.reply_message(event.reply_token, reply_arr)


#-----------------------------------------------------------------------------
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

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        #美食主界面
        elif user_message == "台南美食":
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
                            label = "台南甜點",
                            text = "台南甜點"
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, output_message)

    #---------------------------------------------------------------------

        #美食part1
        elif user_message == "台南美食part1":
            output_message = food_carousel_template1()
            line_bot_api.reply_message(event.reply_token, output_message)

    #----------------------------------------------------------------------

        #美食part2
        elif user_message == "台南美食part2":
            output_message = food_carousel_template2()
            line_bot_api.reply_message(event.reply_token, output_message)

    #----------------------------------------------------------------------



            #-------------------------------------------------------------

            #美食菜單
        elif user_message == f"{food1}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://i.imgur.com/4pw7i8S.jpg",
                preview_image_url = "https://i.imgur.com/4pw7i8S.jpg"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food2}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://img.rainieis.tw/uploads/20180211203240_42.jpg",
                preview_image_url = "https://img.rainieis.tw/uploads/20180211203240_42.jpg"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food3}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://pic.pimg.tw/tainanlohas/1415102681-4123707573.jpg",
                preview_image_url = "https://pic.pimg.tw/tainanlohas/1415102681-4123707573.jpg"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food4}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://fengtaiwanway.com/wp-content/uploads/pixnet/1464808199-26107633.jpg",
                preview_image_url = "https://fengtaiwanway.com/wp-content/uploads/pixnet/1464808199-26107633.jpg"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food5}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://pic.pimg.tw/nikitarh/1606665478-1026621535-g_n.jpg",
                preview_image_url = "https://pic.pimg.tw/nikitarh/1606665478-1026621535-g_n.jpg"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food6}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://pic.pimg.tw/matsurica/4bf3f7ec949f7.jpg",
                preview_image_url = "https://pic.pimg.tw/matsurica/4bf3f7ec949f7.jpg"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food7}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://img.bopomo.tw/20190305233812_61.jpg",
                preview_image_url = "https://img.bopomo.tw/20190305233812_61.jpg"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food8}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://images.zi.org.tw/bigfang/2020/09/15165908/1600160347-bf78e344a5b5b63be889d19218eb6be2.jpg",
                preview_image_url = "https://images.zi.org.tw/bigfang/2020/09/15165908/1600160347-bf78e344a5b5b63be889d19218eb6be2.jpg"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food9}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://i.imgur.com/I1y3CAm.jpg",
                preview_image_url = "https://i.imgur.com/I1y3CAm.jpg"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food10}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://scontent.ftpe10-1.fna.fbcdn.net/v/t1.6435-9/131766081_1751405925021066_2159747408668762709_n.jpg?_nc_cat=106&ccb=1-3&_nc_sid=730e14&_nc_ohc=a5PNNlgVa_0AX8AawrR&tn=DbO66jLhb-cjliWk&_nc_ht=scontent.ftpe10-1.fna&oh=a06711c4688174efe464754ecb19d0e0&oe=60FC98FF",
                preview_image_url = "https://scontent.ftpe10-1.fna.fbcdn.net/v/t1.6435-9/131766081_1751405925021066_2159747408668762709_n.jpg?_nc_cat=106&ccb=1-3&_nc_sid=730e14&_nc_ohc=a5PNNlgVa_0AX8AawrR&tn=DbO66jLhb-cjliWk&_nc_ht=scontent.ftpe10-1.fna&oh=a06711c4688174efe464754ecb19d0e0&oe=60FC98FF"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food11}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://4.bp.blogspot.com/-yOzQNhbI4aQ/XoBuboSpDsI/AAAAAAAAOqs/mi6VjloP1akm49P5Feez3ixOgM02ygXjwCKgBGAsYHg/s1600/IMG_2672.jpg",
                preview_image_url = "https://4.bp.blogspot.com/-yOzQNhbI4aQ/XoBuboSpDsI/AAAAAAAAOqs/mi6VjloP1akm49P5Feez3ixOgM02ygXjwCKgBGAsYHg/s1600/IMG_2672.jpg"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food12}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://img.rainieis.tw/uploads/20180212114310_48.jpg",
                preview_image_url = "https://img.rainieis.tw/uploads/20180212114310_48.jpg"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food13}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://img.13shaniu.tw/uploads/20190721233842_54.jpeg",
                preview_image_url = "https://img.13shaniu.tw/uploads/20190721233842_54.jpeg"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food14}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://sillybaby.tw/wp-content/uploads/20180510115225_38.jpg",
                preview_image_url = "https://sillybaby.tw/wp-content/uploads/20180510115225_38.jpg"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food15}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://3.bp.blogspot.com/-lRJyFRbEn2c/W-RrUQ0QUII/AAAAAAAAgqI/bONSCYpIaksmZD6NRrzfRk_NgA0JPn59gCKgBGAs/s1600/IMG_7797.jpg",
                preview_image_url = "https://3.bp.blogspot.com/-lRJyFRbEn2c/W-RrUQ0QUII/AAAAAAAAgqI/bONSCYpIaksmZD6NRrzfRk_NgA0JPn59gCKgBGAs/s1600/IMG_7797.jpg"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food16}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://scontent.ftpe10-1.fna.fbcdn.net/v/t1.6435-9/133250809_3597804996939301_1854083568135046080_n.jpg?_nc_cat=102&ccb=1-3&_nc_sid=c4c01c&_nc_ohc=-pQMW5XjPLUAX_MPySk&_nc_ht=scontent.ftpe10-1.fna&oh=62be5f40928f5d3a2fa5a21890236084&oe=60FC7D44",
                preview_image_url = "https://scontent.ftpe10-1.fna.fbcdn.net/v/t1.6435-9/133250809_3597804996939301_1854083568135046080_n.jpg?_nc_cat=102&ccb=1-3&_nc_sid=c4c01c&_nc_ohc=-pQMW5XjPLUAX_MPySk&_nc_ht=scontent.ftpe10-1.fna&oh=62be5f40928f5d3a2fa5a21890236084&oe=60FC7D44"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food17}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://scontent.ftpe10-1.fna.fbcdn.net/v/t1.6435-9/186528711_6049655938385449_4302705472193818662_n.jpg?_nc_cat=100&ccb=1-3&_nc_sid=8bfeb9&_nc_ohc=0gbsHfVco7UAX8DE_mJ&_nc_ht=scontent.ftpe10-1.fna&oh=b45fa57fa1f10cd5200d51a4a94559f3&oe=60FD6060",
                preview_image_url = "https://scontent.ftpe10-1.fna.fbcdn.net/v/t1.6435-9/186528711_6049655938385449_4302705472193818662_n.jpg?_nc_cat=100&ccb=1-3&_nc_sid=8bfeb9&_nc_ohc=0gbsHfVco7UAX8DE_mJ&_nc_ht=scontent.ftpe10-1.fna&oh=b45fa57fa1f10cd5200d51a4a94559f3&oe=60FD6060"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food18}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://lh3.googleusercontent.com/zebMrQBQ5Rp4Fp_jM9eZJ_ZbC011ePVodvu40cp5xEjc7jxzbSrREwYJMEj0330Fq1ITg2Pz-OqtOIlL0CiEDUEOfRCwu3g=s600",
                preview_image_url = "https://lh3.googleusercontent.com/zebMrQBQ5Rp4Fp_jM9eZJ_ZbC011ePVodvu40cp5xEjc7jxzbSrREwYJMEj0330Fq1ITg2Pz-OqtOIlL0CiEDUEOfRCwu3g=s600"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food19}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://img.rainieis.tw/uploads/20180212120801_68.jpg",
                preview_image_url = "https://img.rainieis.tw/uploads/20180212120801_68.jpg"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food20}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://img.rainieis.tw/uploads/20200330234808_8.jpg",
                preview_image_url = "https://img.rainieis.tw/uploads/20200330234808_8.jpg"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

            #-------------------------------------------------------------

            #美食營業時間
        elif user_message == f"{food1}營業時間":
            output_message = text_reply.text_reply_message(f"{food1}營業時間\n\n星期一：休息\n星期二：休息\n星期三：11:00–17:00\n星期四：11:00–17:00\n星期五：11:00–17:00\n星期六：11:00–17:00\n星期日：11:00–17:00")
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food2}營業時間":
            output_message = text_reply.text_reply_message(f"{food2}營業時間\n\n星期一：08:30–19:30\n星期二：休息\n星期三：08:30–19:30\n星期四：08:30–19:30\n星期五：08:30–19:30\n星期六：08:30–19:30\n星期日：08:30–19:30")
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food3}營業時間":
            output_message = text_reply.text_reply_message(f"{food3}營業時間\n\n星期一：08:00–18:00\n星期二：08:00–18:00\n星期三：08:00–18:00\n星期四：休息\n星期五：08:00–18:00\n星期六：08:00–18:00\n星期日：08:00–18:00")
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food4}營業時間":
            output_message = text_reply.text_reply_message(f"{food4}營業時間\n\n星期一：休息\n星期二：10:00–02:00\n星期三：10:00–02:00\n星期四：10:00–02:00\n星期五：10:00–02:00\n星期六：10:00–02:00\n星期日：10:00–00:00")
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food5}營業時間":
            output_message = text_reply.text_reply_message(f"{food5}營業時間\n\n星期一：06:00–21:00\n星期二：06:00–21:00\n星期三：06:00–21:00\n星期四：06:00–21:00\n星期五：06:00–21:00\n星期六：06:00–21:00\n星期日：06:00–21:00")
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food6}營業時間":
            output_message = text_reply.text_reply_message(f"{food6}營業時間\n\n星期一：18:00–04:00\n星期二：18:00–04:00\n星期三：18:00–04:00\n星期四：18:00–04:00\n星期五：18:00–04:00\n星期六：18:00–04:00\n星期日：18:00–04:00")
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food7}營業時間":
            output_message = text_reply.text_reply_message(f"{food7}營業時間\n\n星期一：\n09:30–15:00, 17:00–20:00\n星期二：\n09:30–15:00, 17:00–20:00\n星期三：\n09:30–15:00, 17:00–20:00\n星期四：\n09:30–15:00, 17:00–20:00\n星期五：\n09:30–15:00, 17:00–20:00\n星期六：\n09:30–15:00, 17:00–20:00\n星期日：休息")
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food8}營業時間":
            output_message = text_reply.text_reply_message(f"{food8}營業時間\n\n星期一：04:00–14:00\n星期二：04:00–14:00\n星期三：04:00–14:00\n星期四：04:00–14:00\n星期五：04:00–14:00\n星期六：04:00–15:00\n星期日：04:00–15:00")
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food9}營業時間":
            output_message = text_reply.text_reply_message(f"{food9}營業時間\n\n星期一：休息\n星期二：17:00–00:00\n星期三：17:00–00:00\n星期四：17:00–00:00\n星期五：17:00–00:00\n星期六：17:00–00:00\n星期日：17:00–00:00")
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food10}營業時間":
            output_message = text_reply.text_reply_message(f"{food10}營業時間\n\n星期一：10:00–21:30\n星期二：10:00–21:30\n星期三：10:00–21:30\n星期四：10:00–21:30\n星期五：10:00–21:30\n星期六：10:00–21:30\n星期日：10:00–21:30")
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food11}營業時間":
            output_message = text_reply.text_reply_message(f"{food11}營業時間\n\n星期一：16:30–01:00\n星期二：16:30–01:00\n星期三：16:30–01:00\n星期四：16:30–01:00\n星期五：16:30–01:30\n星期六：16:30–01:30\n星期日：16:30–01:30")
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food12}營業時間":
            output_message = text_reply.text_reply_message(f"{food12}營業時間\n\n星期一：07:00–17:30\n星期二：07:00–17:30\n星期三：07:00–17:30\n星期四：休息\n星期五：07:00–17:30\n星期六：07:00–17:30\n星期日：07:00–17:30")
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food13}營業時間":
            output_message = text_reply.text_reply_message(f"{food13}營業時間\n\n星期一：休息\n星期二：06:30–18:30\n星期三：06:30–18:30\n星期四：06:30–18:30\n星期五：06:30–18:30\n星期六：06:30–18:30\n星期日：06:30–18:30")
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food14}營業時間":
            output_message = text_reply.text_reply_message(f"{food14}營業時間\n\n星期一：10:30–19:30\n星期二：10:30–19:30\n星期三：10:30–19:30\n星期四：10:30–19:30\n星期五：10:30–19:30\n星期六：10:30–19:30\n星期日：10:30–19:30")
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food15}營業時間":
            output_message = text_reply.text_reply_message(f"{food15}營業時間\n\n星期一：07:00–14:30\n星期二：07:00–14:30\n星期三：07:00–14:30\n星期四：休息\n星期五：07:00–14:30\n星期六：07:00–14:30\n星期日：07:00–14:30")
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food16}營業時間":
            output_message = text_reply.text_reply_message(f"{food16}營業時間\n\n星期一：07:00–22:00\n星期二：07:00–22:00\n星期三：休息\n星期四：07:00–22:00\n星期五：07:00–22:00\n星期六：07:00–22:00\n星期日：07:00–22:00")
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food17}營業時間":
            output_message = text_reply.text_reply_message(f"{food17}營業時間\n\n星期一：休息\n星期二：休息\n星期三：12:00–18:00\n星期四：12:00–18:00\n星期五：12:00–18:00\n星期六：12:00–18:00\n星期日：12:00–18:00")
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food18}營業時間":
            output_message = text_reply.text_reply_message(f"{food18}營業時間\n\n星期一：17:00–00:00\n星期二：17:00–00:00\n星期三：17:00–00:00\n星期四：17:00–00:00\n星期五：17:00–00:00\n星期六：17:00–00:00\n星期日：17:00–00:00")
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food19}營業時間":
            output_message = text_reply.text_reply_message(f"{food19}營業時間\n\n星期一：11:00–21:00\n星期二：11:00–21:00\n星期三：11:00–21:00\n星期四：11:00–21:00\n星期五：11:00–21:00\n星期六：11:00–21:00\n星期日：11:00–21:00")
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{food20}營業時間":
            output_message = text_reply.text_reply_message(f"{food20}營業時間\n\n星期一：05:00–12:30\n星期二：休息\n星期三：05:00–12:30\n星期四：05:00–12:30\n星期五：05:00–12:30\n星期六：05:00–12:30\n星期日：05:00–12:30")
            line_bot_api.reply_message(event.reply_token, output_message)

            #-------------------------------------------------------------

            #美食地圖位置
        #1
        elif user_message ==f"{food1}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{food1}的google地圖位置") 
            output_message2 = LocationSendMessage(
                title = f"{food1}",
                address = "台南市中西區國華街三段5號",
                latitude = "22.99355830555154",
                longitude = "120.197479227042"
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #2
        elif user_message ==f"{food2}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{food2}的google地圖位置") 
            output_message2 = LocationSendMessage(
                title = f"{food2}",
                address = "台南市中西區海安路一段66號",
                latitude = "22.98897454659431",
                longitude = "120.19527211288802"
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #3
        elif user_message ==f"{food3}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{food3}的google地圖位置") 
            output_message2 = LocationSendMessage(
                title = f"{food3}",
                address = "台南市中西區國華街三段181號",
                latitude = "22.99756243319255",
                longitude = "120.19890510920264"
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #4
        elif user_message ==f"{food4}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{food4}的google地圖位置") 
            output_message2 = LocationSendMessage(
                title = f"{food4}",
                address = "708台南市安平區安平路590號",
                latitude = "22.998750218851384",
                longitude = "120.16973447085927"
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #5
        elif user_message ==f"{food5}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{food5}的google地圖位置") 
            output_message2 = LocationSendMessage(
                title = f"{food5}",
                address = "台南市中西區保安路53號",
                latitude = "22.99025382562354",
                longitude = "120.19640750231954"
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #6
        elif user_message ==f"{food6}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{food6}的google地圖位置") 
            output_message2 = LocationSendMessage(
                title = f"{food6}",
                address = "台南市東區勝利路119號",
                latitude = "22.99467882677812",
                longitude = "120.21792580970332"
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #7
        elif user_message ==f"{food7}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{food7}的google地圖位置") 
            output_message2 = LocationSendMessage(
                title = f"{food7}",
                address = "台南市中西區中山路8巷5號",
                latitude = "22.992811497425294",
                longitude = "120.20594536499986"
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #8
        elif user_message ==f"{food8}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{food8}的google地圖位置") 
            output_message2 = LocationSendMessage(
                title = f"{food8}",
                address = "台南市安平區安平路612號",
                latitude = "22.998934777722237",
                longitude = "120.16887777875954"
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #9
        elif user_message ==f"{food9}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{food9}的google地圖位置") 
            output_message2 = LocationSendMessage(
                title = f"{food9}",
                address = "台南市中西區民族路三段89號",
                latitude = "22.998364945021",
                longitude = "120.19696113865045"
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #10
        elif user_message ==f"{food10}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{food10}的google地圖位置") 
            output_message2 = LocationSendMessage(
                title = f"{food10}",
                address = "台南市安平區安平路408-1號",
                latitude = "22.998097253954455",
                longitude = "120.17459910476686"
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #11
        elif user_message ==f"{food11}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{food11}的google地圖位置") 
            output_message2 = LocationSendMessage(
                title = f"{food11}",
                address = "台南市中西區友愛街143號",
                latitude = "22.991519859859444",
                longitude = "120.1991163002723"
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #12
        elif user_message ==f"{food12}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{food12}的google地圖位置") 
            output_message2 = LocationSendMessage(
                title = f"{food12}",
                address = "台南市中西區民族路三段11號",
                latitude = "22.997607846744017",
                longitude = "120.19921193444611"
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #13
        elif user_message ==f"{food13}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{food13}的google地圖位置") 
            output_message2 = LocationSendMessage(
                title = f"{food13}",
                address = "台南市中西區府前路一段215號",
                latitude = "22.989144129134928",
                longitude = "120.2037448190117"
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #14
        elif user_message ==f"{food14}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{food14}的google地圖位置") 
            output_message2 = LocationSendMessage(
                title = f"{food14}",
                address = "台南市中西區大德街38號",
                latitude = "22.989456875210564",
                longitude = "120.19569979202385"
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #15
        elif user_message ==f"{food15}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{food15}的google地圖位置") 
            output_message2 = LocationSendMessage(
                title = f"{food15}",
                address = "台南市中西區民族路三段104號",
                latitude = "22.99888561400458",
                longitude = "120.19721339754601"
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #16
        elif user_message ==f"{food16}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{food16}的google地圖位置") 
            output_message2 = LocationSendMessage(
                title = f"{food16}",
                address = "台南市北區成功路380號",
                latitude = "23.000357785827312",
                longitude = "120.20017912913502"
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #17
        elif user_message ==f"{food17}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{food17}的google地圖位置") 
            output_message2 = LocationSendMessage(
                title = f"{food17}",
                address = "台南市中西區國華街三段22號",
                latitude = "22.99341779274471",
                longitude = "120.19754275895937"
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #18
        elif user_message ==f"{food18}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{food18}的google地圖位置") 
            output_message2 = LocationSendMessage(
                title = f"{food18}",
                address = "台南市中西區保安路72號",
                latitude = "22.990495165451254",
                longitude = "120.19612642519014"
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #19
        elif user_message ==f"{food19}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{food19}的google地圖位置") 
            output_message2 = LocationSendMessage(
                title = f"{food19}",
                address = "台南市中西區中正路康樂市場180號",
                latitude = "22.992374990454337",
                longitude = "120.19615810739693"
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #20
        elif user_message ==f"{food20}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{food20}的google地圖位置") 
            output_message2 = LocationSendMessage(
                title = f"{food20}",
                address = "台南市中西區西門路一段728號",
                latitude = "22.98996871769685",
                longitude = "120.19788844000415"
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #----------------------------------------------------------------------

        #甜點
        elif user_message == "台南甜點":
            output_message = dessert_carousel_template()
            line_bot_api.reply_message(event.reply_token, output_message)

            #-------------------------------------------------------------

            #甜點菜單
        elif user_message == f"{dessert1}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://cdn.walkerland.com.tw/images/upload/poi/p11650/m40005/e6b2643a352a4d0d2144e1d87ea52cddb72e2f99.jpg",
                preview_image_url = "https://cdn.walkerland.com.tw/images/upload/poi/p11650/m40005/e6b2643a352a4d0d2144e1d87ea52cddb72e2f99.jpg"
            )
            line_bot_api.reply_message(event.reply_token, output_message)
        
        elif user_message == f"{dessert2}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://pic.pimg.tw/tainanlohas/1504591024-203960289.jpg",
                preview_image_url = "https://pic.pimg.tw/tainanlohas/1504591024-203960289.jpg"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{dessert3}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://scontent.ftpe10-1.fna.fbcdn.net/v/t1.18169-9/12347875_1223221574359667_4192191577517058670_n.jpg?_nc_cat=109&ccb=1-3&_nc_sid=e3f864&_nc_ohc=vBkwkgKxMF8AX_Eneot&_nc_ht=scontent.ftpe10-1.fna&oh=15e7fb5c63d1ec7c46e44da4c2dc43d7&oe=611F4C96",
                preview_image_url = "https://scontent.ftpe10-1.fna.fbcdn.net/v/t1.18169-9/12347875_1223221574359667_4192191577517058670_n.jpg?_nc_cat=109&ccb=1-3&_nc_sid=e3f864&_nc_ohc=vBkwkgKxMF8AX_Eneot&_nc_ht=scontent.ftpe10-1.fna&oh=15e7fb5c63d1ec7c46e44da4c2dc43d7&oe=611F4C96"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{dessert4}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://i.imgur.com/QNWdJ4R.jpg",
                preview_image_url = "https://i.imgur.com/QNWdJ4R.jpg"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{dessert5}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://i1.wp.com/fishalee.com/wp-content/uploads/2019-05-20_1219-compressor-compressor.jpg?resize=720%2C270&ssl=1",
                preview_image_url = "https://i1.wp.com/fishalee.com/wp-content/uploads/2019-05-20_1219-compressor-compressor.jpg?resize=720%2C270&ssl=1"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{dessert6}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://i.imgur.com/OyyavM3.jpg",
                preview_image_url = "https://i.imgur.com/OyyavM3.jpg"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{dessert7}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://img.vivawei.tw/20181007065232_95.jpg",
                preview_image_url = "https://img.vivawei.tw/20181007065232_95.jpg"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{dessert8}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://pic.pimg.tw/jeremyckt2/1601721111-44603135-g.jpg",
                preview_image_url = "https://pic.pimg.tw/jeremyckt2/1601721111-44603135-g.jpg"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{dessert9}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://i.imgur.com/3bi33Fq.jpg",
                preview_image_url = "https://i.imgur.com/3bi33Fq.jpg"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

            #-------------------------------------------------------------

            #甜點營業時間
        elif user_message == f"{dessert1}營業時間":
            output_message = text_reply.text_reply_message(f"{dessert1}營業時間\n\n星期一：休息\n星期二：12:00–01:00\n星期三：12:00–01:00\n星期四：12:00–01:00\n星期五：12:00–01:00\n星期六：12:00–01:00\n星期日：12:00–01:00")
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{dessert2}營業時間":
            output_message = text_reply.text_reply_message(f"{dessert2}營業時間\n\n星期一：12:00–18:00\n星期二：12:00–18:00\n星期三：12:00–18:00\n星期四：12:00–18:00\n星期五：12:00–18:00\n星期六：12:00–21:00\n星期日：12:00–21:00")
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{dessert3}營業時間":
            output_message = text_reply.text_reply_message(f"{dessert3}營業時間\n\n星期一：休息\n星期二：07:45–13:00\n星期三：07:45–13:00\n星期四：07:45–13:00\n星期五：07:45–13:00\n星期六：07:45–13:00\n星期日：07:45–13:00")
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{dessert4}營業時間":
            output_message = text_reply.text_reply_message(f"{dessert4}營業時間\n\n星期一：11:30–20:00\n星期二：11:30–20:00\n星期三：11:30–20:00\n星期四：11:30–20:00\n星期五：11:30–20:00\n星期六：11:30–20:00\n星期日：11:30–20:00")
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{dessert5}營業時間":
            output_message = text_reply.text_reply_message(f"{dessert5}營業時間\n\n星期一：12:00–21:00\n星期二：12:00–21:00\n星期三：12:00–21:00\n星期四：12:00–21:00\n星期五：12:00–21:00\n星期六：12:00–21:00\n星期日：12:00–21:00")
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{dessert6}營業時間":
            output_message = text_reply.text_reply_message(f"{dessert6}營業時間\n\n星期一：11:00–21:00\n星期二：11:00–21:00\n星期三：11:00–21:00\n星期四：11:00–17:00\n星期五：11:00–21:00\n星期六：11:00–21:00\n星期日：11:00–21:00")
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{dessert7}營業時間":
            output_message = text_reply.text_reply_message(f"{dessert7}營業時間\n\n星期一：12:00–21:00\n星期二：12:00–21:00\n星期三：12:00–21:00\n星期四：12:00–21:00\n星期五：12:00–21:00\n星期六：12:00–21:00\n星期日：12:00–21:00")
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{dessert8}營業時間":
            output_message = text_reply.text_reply_message(f"{dessert8}營業時間\n\n星期一：11:00–19:00\n星期二：休息\n星期三：11:00–19:00\n星期四：11:00–19:00\n星期五：11:00–19:00\n星期六：10:30–19:00\n星期日：10:30–19:00")
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{dessert9}營業時間":
            output_message = text_reply.text_reply_message(f"{dessert9}營業時間\n\n星期一：09:00–23:00\n星期二：09:00–23:00\n星期三：09:00–23:00\n星期四：09:00–23:00\n星期五：09:00–23:00\n星期六：09:00–23:00\n星期日：09:00–23:00")
            line_bot_api.reply_message(event.reply_token, output_message)

           #-------------------------------------------------------------

            #甜點地圖位置
        #1
        elif user_message ==f"{dessert1}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{dessert1}的google地圖位置")
            output_message2 = LocationSendMessage(
                title = f"{dessert1}",
                address = "台南市中西區民生路一段122號",
                latitude = "22.994032350718996",
                longitude = "120.20100664416861"
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #2
        elif user_message ==f"{dessert2}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{dessert2}的google地圖位置")
            output_message2 = LocationSendMessage(
                title = f"{dessert2}",
                address = "台南市安平區安平路270號",
                latitude = "22.99851590645143",
                longitude = "120.17880424290001"
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #3
        elif user_message ==f"{dessert3}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{dessert3}的google地圖位置")
            output_message2 = LocationSendMessage(
                title = f"{dessert3}",
                address = "台南市中西區海安路二段290號",
                latitude = "22.998631537375974",
                longitude = "120.19816665512356"
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #4
        elif user_message ==f"{dessert4}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{dessert4}的google地圖位置")
            output_message2 = LocationSendMessage(
                title = f"{dessert4}",
                address = "台南市中西區友愛街213號之2號",
                latitude = "22.99192946660628",
                longitude = "120.1971526618522"
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #5
        elif user_message ==f"{dessert5}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{dessert5}的google地圖位置")
            output_message2 = LocationSendMessage(
                title = f"{dessert5}",
                address = "台南市中西區國華街三段16巷13號",
                latitude = "22.99331009676464",
                longitude = "120.19772273415386"
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #6
        elif user_message ==f"{dessert6}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{dessert6}的google地圖位置")
            output_message2 = LocationSendMessage(
                title = f"{dessert6}",
                address = "台南市中西區正興街92號",
                latitude = "22.994302620492856",
                longitude = "120.19712312218958"
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #7
        elif user_message ==f"{dessert7}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{dessert7}的google地圖位置")
            output_message2 = LocationSendMessage(
                title = f"{dessert7}",
                address = "台南市中西區民生路一段160號",
                latitude = "22.994229511108202",
                longitude = "120.20024588499835"
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #8
        elif user_message ==f"{dessert8}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{dessert8}的google地圖位置")
            output_message2 = LocationSendMessage(
                title = f"{dessert8}",
                address = "台南市中西區新美街72號",
                latitude = "22.99542959022524",
                longitude = "120.20048274085703"
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)
            line_bot_api.reply_message(event.reply_token, reply_arr)

        #9
        elif user_message ==f"{dessert9}在哪裡":
            reply_arr = []
            output_message1 = text_reply.text_reply_message(f"{dessert9}的google地圖位置")
            output_message2 = LocationSendMessage(
                title = f"{dessert9}",
                address = "台南市安平區安北路433號",
                latitude = "22.999906372453964",
                longitude = "120.15338501065318"
            )
            reply_arr.append(output_message1)
            reply_arr.append(output_message2)
            line_bot_api.reply_message(event.reply_token, reply_arr)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
        #飲料
        elif user_message == "台南飲料":
            output_message = drink_confirm_template()
            line_bot_api.reply_message(event.reply_token, output_message)

#------------------------------------------------------------------------------------------------

        #連鎖
        elif user_message == "台南連鎖飲料":
            reply_arr = []
            
            output_message1 = text_reply.text_reply_message("點選圖片即可查看菜單！")
            output_message2 = drink_image_carousel_message()

            reply_arr.append(output_message1)
            reply_arr.append(output_message2)
            
            line_bot_api.reply_message(event.reply_token, reply_arr)


        #連鎖飲料菜單
        elif user_message == f"{chain_drink1}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://img.pboss.tw/pixnet/e279d34feae6dd59e63cedf2319b67f8.jpg",
                preview_image_url = "https://img.pboss.tw/pixnet/e279d34feae6dd59e63cedf2319b67f8.jpg"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{chain_drink2}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://www.chingshin.tw/upload/price/1907171531260000001.jpg",
                preview_image_url = "https://www.chingshin.tw/upload/price/1907171531260000001.jpg"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{chain_drink3}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://www.milkshoptea.com/upload/price/2104090830370000002.jpg",
                preview_image_url = "https://www.milkshoptea.com/upload/price/2104090830370000002.jpg"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{chain_drink4}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://dtvtjl5au16ai.cloudfront.net/wp-content/uploads/2021/04/CoCoMenu2021-4.jpg",
                preview_image_url = "https://dtvtjl5au16ai.cloudfront.net/wp-content/uploads/2021/04/CoCoMenu2021-4.jpg"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{chain_drink5}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://www.dayungs.com/wp-content/uploads/2021/07/%E5%AE%98%E7%B6%B2%E5%83%B9%E7%9B%AE%E8%A1%A8_0719-0815_%E5%8D%97.jpg",
                preview_image_url = "https://www.dayungs.com/wp-content/uploads/2021/07/%E5%AE%98%E7%B6%B2%E5%83%B9%E7%9B%AE%E8%A1%A8_0719-0815_%E5%8D%97.jpg"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{chain_drink6}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://i.imgur.com/9nSiF2g.jpg",
                preview_image_url = "https://i.imgur.com/9nSiF2g.jpg"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{chain_drink7}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://yinyih.tw/wp-content/uploads/20180911224137_47.jpg",
                preview_image_url = "https://yinyih.tw/wp-content/uploads/20180911224137_47.jpg"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{chain_drink8}菜單":
            output_message = ImageSendMessage(
                original_content_url = "https://tw.tp-tea.com/download/index.php?index_id=26",
                preview_image_url = "https://tw.tp-tea.com/download/index.php?index_id=26"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{chain_drink9}菜單":
            output_message = ImageSendMessage(
                original_content_url = "http://www.presotea.com.tw/webimages/1621218310781.jpg",
                preview_image_url = "http://www.presotea.com.tw/webimages/1621218310781.jpg"
            )
            line_bot_api.reply_message(event.reply_token, output_message)

#------------------------------------------------------------------------------------------------

        #非連鎖
        elif user_message == "台南非連鎖飲料":
            reply_arr = []
            output_message1 = text_reply.text_reply_message("點選圖片以取得資訊！\n(菜單、營業時間、位置)")
            output_message2 = non_drink_imagemap1()
            output_message3 = non_drink_imagemap2()

            reply_arr.extend([output_message1,output_message2,output_message3])
            line_bot_api.reply_message(event.reply_token, reply_arr)

#------------------------------------------------------------------------------------------------

        #資訊
        elif user_message == f"{drink1}資訊":
            output_message = drink1_func()
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{drink2}資訊":
            output_message = drink2_func()
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{drink3}資訊":
            output_message = drink3_func()
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{drink4}資訊":
            output_message = drink4_func()
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{drink5}資訊":
            output_message = drink5_func()
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{drink6}資訊":
            output_message = drink6_func()
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{drink7}資訊":
            output_message = drink7_func()
            line_bot_api.reply_message(event.reply_token, output_message)

        elif user_message == f"{drink8}資訊":
            output_message = drink8_func()
            line_bot_api.reply_message(event.reply_token, output_message)

#------------------------------------------------------------------------------

        #咖啡廳
        elif user_message == "台南咖啡廳":
            reply_arr = []

            output_message1 = text_reply.text_reply_message("點選圖片即可獲得資訊！")
            output_message2 = cafe_image_carousel()

            reply_arr.extend([output_message1,output_message2])
            line_bot_api.reply_message(event.reply_token, reply_arr)

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