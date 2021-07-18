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

#圖片
def image_carousel_message1():
    output_message = TemplateSendMessage(
        template = ImageCarouselTemplate(
            colunms = [
                ImageCarouselColumn(image_url = "https://i.imgur.com/yRxl6rd.jpg",),
                ImageCarouselColumn(image_url = "https://i.imgur.com/398srGx.jpg",),
                ImageCarouselColumn(image_url = "https://i.imgur.com/PUze65H.jpg",),
                ImageCarouselColumn(image_url = "https://i.imgur.com/RvwCe1M.jpg",),
                ImageCarouselColumn(image_url = "https://i.imgur.com/bH9uIPR.jpg",),
                ImageCarouselColumn(image_url = "https://i.imgur.com/37uUjGk.jpg",)
            ]
        )
    )
    return output_message