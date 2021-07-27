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
cafe1 = "秘氏咖啡"
cafe2 = "Error22 鼴鼠"
cafe3 = "kokoni café"
cafe4 = "StableNice BLDG."
cafe5 = "離島咖啡"
cafe6 = "ALFEE Coffee"
cafe7 = "果核抵家"
cafe8 = "everything cafe 任事咖啡"
cafe9 = "二子咖啡"
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#多頁圖片
def cafe_image_carousel():
    output_message = TemplateSendMessage(
        alt_text = "此裝置不支援樣板。", #無法支援格式所顯示的文字
        template = ImageCarouselTemplate(
            columns = [
                #1
                ImageCarouselColumn(
                    image_url = "",
                    action = MessageTemplateAction(
                        label = f"{cafe1}",
                        text = ""
                    )
                ),
                #2
                ImageCarouselColumn(
                    image_url = "",
                    action = MessageTemplateAction(
                        label = f"{cafe2}",
                        text = ""
                    )
                ),
                #3
                ImageCarouselColumn(
                    image_url = "",
                    action = MessageTemplateAction(
                        label = f"{cafe3}",
                        text = ""
                    )
                ),
                #4
                ImageCarouselColumn(
                    image_url = "",
                    action = MessageTemplateAction(
                        label = f"{cafe4}",
                        text = ""
                    )
                ),
                #5
                ImageCarouselColumn(
                    image_url = "",
                    action = MessageTemplateAction(
                        label = f"{cafe5}",
                        text = ""
                    )
                ),
                #6
                ImageCarouselColumn(
                    image_url = "",
                    action = MessageTemplateAction(
                        label = f"{cafe6}",
                        text = ""
                    )
                ),
                #7
                ImageCarouselColumn(
                    image_url = "",
                    action = MessageTemplateAction(
                        label = f"{cafe7}",
                        text = ""
                    )
                ),
                #8
                ImageCarouselColumn(
                    image_url = "",
                    action = MessageTemplateAction(
                        label = f"{cafe8}",
                        text = ""
                    )
                )
            ]
        )
    )
    return output_message