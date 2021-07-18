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

# instruction of pushing code to heroku
# git add .
# git commit -am'ok'
# git push heroku master

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#圖片
def image_carousel_message1():
    output_message = TemplateSendMessage(
        alt_text = "此裝置不支援樣板。", #無法支援格式所顯示的文字
        template = ImageCarouselTemplate(
            columns = [
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/yRxl6rd.jpg",
                    action = MessageTemplateAction(
                        label = "",
                        text = "1"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/398srGx.jpg",
                    action = MessageTemplateAction(
                        label = "",
                        text = "2"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/PUze65H.jpg",
                    action = MessageTemplateAction(
                        label = "",
                        text = "3"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/RvwCe1M.jpg",
                    action = MessageTemplateAction(
                        label = "",
                        text = "4"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/bH9uIPR.jpg",
                    action = MessageTemplateAction(
                        label = "",
                        text = "5"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/37uUjGk.jpg",
                    action = MessageTemplateAction(
                        label = "",
                        text = "6"
                    )
                )
            ]
        )
    )
    return output_message