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

#組圖訊息
def imagemap_message():
    output_message = ImagemapSendMessage(
        base_url = "https://www.gomaji.com/blog/wp-content/uploads/2020/04/IMG_0164-696x462.jpg",
        alt_text = "", #無法支援格式所顯示的文字
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

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Tempalte format：
# 1. Confirm_Template
# 2. Button_Template
# 3. Carousel_Template
# 4. Image_Carousel_Template


# Template Action：
# 1. Message -> MessageTemplateAction
# 2. Uri -> URITemplateAction
# 3. Postback -> PostbackTemplateAction
# 4. Datetimepicker -> DatetimePickerTemplateAction

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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