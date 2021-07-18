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