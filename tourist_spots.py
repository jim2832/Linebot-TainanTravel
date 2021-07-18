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
        alt_text = "此裝置不支援樣板格式。",
        template = ImageCarouselTemplate(
            colunms = [
                ImageCarouselColumn(image_url = "https://view.boch.gov.tw/NationalHistorical/Images/Items/middle/DA09602000349.jpg"),
                ImageCarouselColumn(image_url = "https://photo.travelking.com.tw/scenery/64F103E3-0BB2-4E08-988A-29E9A5434C3C_e.jpg"),
                ImageCarouselColumn(image_url = "https://pic.easytravel.com.tw/Attachments/m/A77936.jpg"),
                ImageCarouselColumn(image_url = "https://3.bp.blogspot.com/-dQ41OiHWsDk/WPxkPnLyrxI/AAAAAAAARkM/rT-QDpNjCoEavfKFs8lW5cZu0q9eMzjdwCEw/s1600/3V8A9583.JPG"),
                ImageCarouselColumn(image_url = "https://sya.tw/wp-content/uploads/2014/02/33.jpg")
            ]
        )
    )
    return output_message