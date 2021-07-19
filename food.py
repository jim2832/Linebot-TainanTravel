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