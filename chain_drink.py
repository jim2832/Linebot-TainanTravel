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

chain_drink1 = "五十嵐"
chain_drink2 = "清心福全"
chain_drink3 = "迷客夏"
chain_drink4 = "CoCo都可"
chain_drink5 = "大苑子"
chain_drink6 = "茶之魔手"
chain_drink7 = "幸福堂"
chain_drink8 = "茶湯會"
chain_drink9 = "鮮茶道"

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#確認樣板
def drink_confirm_template():
    output_message = TemplateSendMessage(
        alt_text = "此裝置不支援樣板。", #無法支援格式所顯示的文字
        template = ConfirmTemplate(
            text = "要查詢連鎖還是非連鎖飲料呢？",
            actions = [
                MessageTemplateAction(
                    label = "連鎖",
                    text = "台南連鎖飲料"
                ),
                MessageTemplateAction(
                    label = "非連鎖",
                    text = "台南非連鎖飲料"
                )
            ]
        )
    )
    return output_message

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#連鎖飲料多頁圖片
def drink_image_carousel_message():
    output_message = TemplateSendMessage(
        alt_text = "此裝置不支援樣板。", #無法支援格式所顯示的文字
        template = ImageCarouselTemplate(
            columns = [
                #1
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/KCpqjjk.jpg",
                    action = MessageTemplateAction(
                        label = f"{chain_drink1}",
                        text = f"{chain_drink1}菜單"
                    )
                ),
                #2
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/bLDgh3K.jpg",
                    action = MessageTemplateAction(
                        label = f"{chain_drink2}",
                        text = f"{chain_drink2}菜單"
                    )
                ),
                #3
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/SOB6LRO.jpg",
                    action = MessageTemplateAction(
                        label = f"{chain_drink3}",
                        text = f"{chain_drink3}菜單"
                    )
                ),
                #4
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/n6rxD4N.jpg",
                    action = MessageTemplateAction(
                        label = f"{chain_drink4}",
                        text = f"{chain_drink4}菜單"
                    )
                ),
                #5
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/JdNTAmo.jpg",
                    action = MessageTemplateAction(
                        label = f"{chain_drink5}",
                        text = f"{chain_drink5}菜單"
                    )
                ),
                #6
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/xuoW3x9.jpg",
                    action = MessageTemplateAction(
                        label = f"{chain_drink6}",
                        text = f"{chain_drink6}菜單"
                    )
                ),
                #7
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/oii5MZ1.jpg",
                    action = MessageTemplateAction(
                        label = f"{chain_drink7}",
                        text = f"{chain_drink7}菜單"
                    )
                ),
                #8
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/qldvEZo.jpg",
                    action = MessageTemplateAction(
                        label = f"{chain_drink8}",
                        text = f"{chain_drink8}菜單"
                    )
                ),
                #9
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/n5TUeUY.jpg",
                    action = MessageTemplateAction(
                        label = f"{chain_drink9}",
                        text = f"{chain_drink9}菜單"
                    )
                )
            ]
        )
    )
    return output_message

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

