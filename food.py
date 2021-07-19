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

#-------------------------------------------------------

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

food1 = "邱家小捲米粉"
food2 = "矮仔成蝦仁飯"
food3 = "阿松割包"
food4 = "文章牛肉湯"
food5 = "醇涎坊鍋燒意麵"
food6 = "勝利早點"
food7 = "無名米糕"
food8 = "王氏魚皮"
food9 = "阿江鱔魚意麵"
food10 = "周氏蝦捲"
food11 = "小杜意麵"
food12 = "富盛號碗粿"
food13 = "福記肉圓"
food14 = "鼎富發豬油拌飯"
food15 = "國華街肉燥飯"
food16 = "丹丹漢堡(成功店)"
food17 = "炸雞洋行"
food18 = "阿明豬心冬粉"
food19 = "赤崁棺材板"
food20 = "阿堂鹹粥"

@handler.add(MessageEvent)
def handle_message(event):
    print(event)
    message_send_time = float(event.timestamp)/1000
    message_get_time = float(time.time())
    msg_type = event.message.type

    if msg_type == "text":
        user_message = event.message.text

        #美食主界面
        if user_message == "吃的":
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

#美食part1
def food_carousel_template1():
    output_message = TemplateSendMessage(
        alt_text = "此裝置不支援樣板。", #無法支援格式所顯示的文字
        template = CarouselTemplate(
            columns = [
                CarouselColumn( #1
                    thumbnail_image_url = "",
                    title = f"{food1}",
                    text = "",
                    actions = [
                        MessageTemplateAction(
                            label = "點我看菜單",
                            text = f"{food1}菜單"
                        ),
                        MessageTemplateAction(
                            label = "點我看營業時間",
                            text = f"{food1}營業時間"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{food1}的google地圖位置"
                        )
                    ]
                )
            ]
        )
    )
    return output_message

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#美食part2
def food_carousel_template2():
    output_message = TemplateSendMessage(
        alt_text = "此裝置不支援樣板。", #無法支援格式所顯示的文字
        template = CarouselTemplate(
            columns = [
                CarouselColumn( #1
                    thumbnail_image_url = "",
                    title = f"{food1}",
                    text = "",
                    actions = [
                        MessageTemplateAction(
                            label = "點我看菜單",
                            text = f"{food1}菜單"
                        ),
                        MessageTemplateAction(
                            label = "點我看營業時間",
                            text = f"{food1}營業時間"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{food1}的google地圖位置"
                        )
                    ]
                )
            ]
        )
    )
    return output_message

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#點心
def dessert_carousel_template():
    output_message = TemplateSendMessage(
        alt_text = "此裝置不支援樣板。", #無法支援格式所顯示的文字
        template = CarouselTemplate(
            columns = [
                CarouselColumn( #1
                    thumbnail_image_url = "",
                    title = f"{food1}",
                    text = "",
                    actions = [
                        MessageTemplateAction(
                            label = "點我看菜單",
                            text = f"{food1}菜單"
                        ),
                        MessageTemplateAction(
                            label = "點我看營業時間",
                            text = f"{food1}營業時間"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{food1}的google地圖位置"
                        )
                    ]
                )
            ]
        )
    )
    return output_message

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)