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
def carousel_template():
    output_message = TemplateSendMessage(
        alt_text = "此裝置不支援樣板。", #無法支援格式所顯示的文字
        template = CarouselTemplate(
            columns = [
                CarouselColumn( #1
                    thumbnail_image_url = "https://pic.pimg.tw/whuy123/1523332170-611241936.jpg",
                    title = "赤崁樓",
                    text = "歷史悠久的荷治時期行政中心",
                    actions = [
                        URITemplateAction(
                            label = "點我看介紹",
                            uri = "https://www.twtainan.net/zh-tw/attractions/detail/674"
                        ),
                        MessageTemplateAction(
                            label = "點我看景點圖片",
                            text = "赤崁樓圖片"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = "可由此打開赤崁樓的google地圖位置"
                        )
                    ]
                ),
                CarouselColumn( #2
                    thumbnail_image_url = "https://image.cdn-eztravel.com.tw/BIvf9xU550uLpO3D1NYvXGNT4nyO_NgoOh-5hPd4IEQ/g:ce/aHR0cHM6Ly92YWNhdGlvbi5jZG4tZXp0cmF2ZWwuY29tLnR3L2ltZy9WRFIvVE5OXzEyMDAzMzQyMTAuanBn.jpg",
                    title = "安平古堡",
                    text = "由荷蘭人建造的台灣史上第一座城堡",
                    actions = [
                        URITemplateAction(
                            label = "點我看介紹",
                            uri = "https://www.twtainan.net/zh-tw/attractions/detail/671"
                        ),
                        MessageTemplateAction(
                            label = "點我看景點圖片",
                            text = "安平古堡圖片"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = "可由此打開安平古堡的google地圖位置"
                        )
                    ]
                ),
                CarouselColumn( #3
                    thumbnail_image_url = "https://www.chimeimuseum.org/uploads/sliders/60da70ae81eaa.jpg",
                    title = "奇美博物館",
                    text = "擁有西洋藝術、樂器、兵器等的知名博物館",
                    actions = [
                        URITemplateAction(
                            label = "點我看介紹",
                            uri = "https://www.twtainan.net/zh-tw/attractions/detail/572"
                        ),
                        MessageTemplateAction(
                            label = "點我看景點圖片",
                            text = "奇美博物館圖片"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = "可由此打開奇美博物館的google地圖位置"
                        )
                    ]
                ),
                CarouselColumn( #4
                    thumbnail_image_url = "https://cc.tvbs.com.tw/img/program/upload/2020/02/05/20200205163001-ba4cb2f0.jpg",
                    title = "神農街",
                    text = "以街底主祀神農氏之藥王廟為名的創新老街",
                    actions = [
                        URITemplateAction(
                            label = "點我看介紹",
                            uri = "https://www.twtainan.net/zh-tw/attractions/detail/1351"
                        ),
                        MessageTemplateAction(
                            label = "點我看景點圖片",
                            text = "神農街圖片"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = "可由此打開神農街的google地圖位置"
                        )
                    ]
                ),
                CarouselColumn( #5
                    thumbnail_image_url = "https://img.natgeomedia.com/userfiles/PhotoContest/925/sm1920/2019090977389193.jpg",
                    title = "漁光島",
                    text = "接近傍晚的夕陽總是引人入勝\n是個讓外地遊客流連忘返的美麗沙灘",
                    actions = [
                        URITemplateAction(
                            label = "點我看介紹",
                            uri = "https://www.twtainan.net/zh-tw/attractions/detail/5520"
                        ),
                        MessageTemplateAction(
                            label = "點我看景點圖片",
                            text = "漁光島圖片"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = "可由此打開漁光島的google地圖位置"
                        )
                    ]
                ),
                CarouselColumn( #6
                    thumbnail_image_url = "https://tainan.funcard.com.tw/imageCache/tainan/JnLv_600x400.jpg",
                    title = "德記洋行",
                    text = "清領時期繁盛一時的重要商業據點",
                    actions = [
                        URITemplateAction(
                            label = "點我看介紹",
                            uri = "https://www.twtainan.net/zh-tw/attractions/detail/687"
                        ),
                        MessageTemplateAction(
                            label = "點我看景點圖片",
                            text = "德記洋行圖片"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = "可由此打開德記洋行的google地圖位置"
                        )
                    ]
                ),
                CarouselColumn( #7
                    thumbnail_image_url = "https://4.bp.blogspot.com/-0kz6Q2pW1wk/Xiq0YZ-cKlI/AAAAAAAAJ6U/5rTRQS-99gk2LmMV9VJia79EjcalGfIPQCKgBGAsYHg/s1600/IMG_8444.jpg",
                    title = "花園夜市",
                    text = "台灣最知名和最熱鬧的夜市之一",
                    actions = [
                        URITemplateAction(
                            label = "點我看介紹",
                            uri = "https://www.twtainan.net/zh-tw/attractions/detail/5572"
                        ),
                        MessageTemplateAction(
                            label = "點我看景點圖片",
                            text = "花園夜市圖片"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = "可由此打開花園夜市的google地圖位置"
                        )
                    ]
                ),
                CarouselColumn( #8
                    thumbnail_image_url = "https://pic.pimg.tw/anrine910070/1601175205-2788673474-g.jpg",
                    title = "夕遊出張所",
                    text = "擁有專屬生日採鹽的原日式試鹽工廠",
                    actions = [
                        URITemplateAction(
                            label = "點我看介紹",
                            uri = "https://www.twtainan.net/zh-tw/attractions/detail/1323"
                        ),
                        MessageTemplateAction(
                            label = "點我看景點圖片",
                            text = "夕遊出張所圖片"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = "可由此打開夕遊出張所的google地圖位置"
                        )
                    ]
                ),
                CarouselColumn( #9
                    thumbnail_image_url = "https://photo.travelking.com.tw/scenery/98E3B96F-21E9-41AD-8193-31840E021733_e.jpg",
                    title = "台南孔廟",
                    text = "具有三百多年歷史的文化古都核心",
                    actions = [
                        URITemplateAction(
                            label = "點我看介紹",
                            uri = "https://www.twtainan.net/zh-tw/attractions/detail/800"
                        ),
                        MessageTemplateAction(
                            label = "點我看景點圖片",
                            text = "台南孔廟圖片"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = "可由此打開台南孔廟的google地圖位置"
                        )
                    ]
                ),
                CarouselColumn( #10
                    thumbnail_image_url = "https://www.twtainan.net/image/13910/1024x768",
                    title = "七股鹽山",
                    text = "以鹽為最大特色的高聳壯觀鹽山",
                    actions = [
                        URITemplateAction(
                            label = "點我看介紹",
                            uri = "https://www.twtainan.net/zh-tw/attractions/detail/471"
                        ),
                        MessageTemplateAction(
                            label = "點我看景點圖片",
                            text = "七股鹽山圖片"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = "可由此打開七股鹽山的google地圖位置"
                        )
                    ]
                )
            ]
        )
    )
    return output_message

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#圖片
def image_carousel_message1():
    output_message = TemplateSendMessage(
        alt_text = "此裝置不支援樣板。", #無法支援格式所顯示的文字
        template = ImageCarouselTemplate(
            columns = [
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/yRxl6rd.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/yRxl6rd.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/398srGx.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/398srGx.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/PUze65H.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/PUze65H.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/RvwCe1M.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/RvwCe1M.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/bH9uIPR.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/bH9uIPR.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/37uUjGk.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/37uUjGk.jpg"
                    )
                )
            ]
        )
    )
    return output_message

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#2
def image_carousel_message2():
    output_message = TemplateSendMessage(
        alt_text = "此裝置不支援樣板。", #無法支援格式所顯示的文字
        template = ImageCarouselTemplate(
            columns = [
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/EbZ8lZ5.jpg",
                    action = URITemplateAction(
                        label = "安平古堡",
                        uri = "https://i.imgur.com/EbZ8lZ5.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/nWRr8oX.jpg",
                    action = URITemplateAction(
                        label = "安平古堡",
                        uri = "https://i.imgur.com/nWRr8oX.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/NxELnR1.jpg",
                    action = URITemplateAction(
                        label = "安平古堡",
                        uri = "https://i.imgur.com/NxELnR1.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/yp8H3SH.jpg",
                    action = URITemplateAction(
                        label = "安平古堡",
                        uri = "https://i.imgur.com/yp8H3SH.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/zxqj0w1.jpg",
                    action = URITemplateAction(
                        label = "安平古堡",
                        uri = "https://i.imgur.com/zxqj0w1.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/PhOxzSl.jpg",
                    action = URITemplateAction(
                        label = "安平古堡",
                        uri = "https://i.imgur.com/PhOxzSl.jpg"
                    )
                )
            ]
        )
    )
    return output_message

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#3
def image_carousel_message3():
    output_message = TemplateSendMessage(
        alt_text = "此裝置不支援樣板。", #無法支援格式所顯示的文字
        template = ImageCarouselTemplate(
            columns = [
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/XvCgXge.jpg",
                    action = URITemplateAction(
                        label = "奇美博物館",
                        uri = "https://i.imgur.com/XvCgXge.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/DiH2m7b.jpg",
                    action = URITemplateAction(
                        label = "奇美博物館",
                        uri = "https://i.imgur.com/DiH2m7b.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/SuvZZHn.jpg",
                    action = URITemplateAction(
                        label = "奇美博物館",
                        uri = "https://i.imgur.com/SuvZZHn.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/qw1Oii8.jpg",
                    action = URITemplateAction(
                        label = "奇美博物館",
                        uri = "https://i.imgur.com/qw1Oii8.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/7u5Mpki.jpg",
                    action = URITemplateAction(
                        label = "奇美博物館",
                        uri = "https://i.imgur.com/7u5Mpki.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/8uKcck1.jpg",
                    action = URITemplateAction(
                        label = "奇美博物館",
                        uri = "https://i.imgur.com/8uKcck1.jpg"
                    )
                )
            ]
        )
    )
    return output_message

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#4
def image_carousel_message4():
    output_message = TemplateSendMessage(
        alt_text = "此裝置不支援樣板。", #無法支援格式所顯示的文字
        template = ImageCarouselTemplate(
            columns = [
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/dpR0jX9.jpg",
                    action = URITemplateAction(
                        label = "神農街",
                        uri = "https://i.imgur.com/dpR0jX9.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/U93wtTD.jpg",
                    action = URITemplateAction(
                        label = "神農街",
                        uri = "https://i.imgur.com/U93wtTD.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/Xrahdlb.jpg",
                    action = URITemplateAction(
                        label = "神農街",
                        uri = "https://i.imgur.com/Xrahdlb.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/8RemImd.jpg",
                    action = URITemplateAction(
                        label = "神農街",
                        uri = "https://i.imgur.com/8RemImd.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/gNIpdzB.jpg",
                    action = URITemplateAction(
                        label = "神農街",
                        uri = "https://i.imgur.com/gNIpdzB.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/H7N1IdC.jpg",
                    action = URITemplateAction(
                        label = "神農街",
                        uri = "https://i.imgur.com/H7N1IdC.jpg"
                    )
                )
            ]
        )
    )
    return output_message

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#5
def image_carousel_message5():
    output_message = TemplateSendMessage(
        alt_text = "此裝置不支援樣板。", #無法支援格式所顯示的文字
        template = ImageCarouselTemplate(
            columns = [
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/yRxl6rd.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/yRxl6rd.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/398srGx.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/398srGx.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/PUze65H.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/PUze65H.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/RvwCe1M.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/RvwCe1M.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/bH9uIPR.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/bH9uIPR.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/37uUjGk.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/37uUjGk.jpg"
                    )
                )
            ]
        )
    )
    return output_message

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#6
def image_carousel_message6():
    output_message = TemplateSendMessage(
        alt_text = "此裝置不支援樣板。", #無法支援格式所顯示的文字
        template = ImageCarouselTemplate(
            columns = [
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/yRxl6rd.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/yRxl6rd.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/398srGx.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/398srGx.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/PUze65H.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/PUze65H.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/RvwCe1M.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/RvwCe1M.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/bH9uIPR.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/bH9uIPR.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/37uUjGk.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/37uUjGk.jpg"
                    )
                )
            ]
        )
    )
    return output_message

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#7
def image_carousel_messag7():
    output_message = TemplateSendMessage(
        alt_text = "此裝置不支援樣板。", #無法支援格式所顯示的文字
        template = ImageCarouselTemplate(
            columns = [
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/yRxl6rd.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/yRxl6rd.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/398srGx.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/398srGx.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/PUze65H.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/PUze65H.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/RvwCe1M.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/RvwCe1M.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/bH9uIPR.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/bH9uIPR.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/37uUjGk.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/37uUjGk.jpg"
                    )
                )
            ]
        )
    )
    return output_message

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#8
def image_carousel_message8():
    output_message = TemplateSendMessage(
        alt_text = "此裝置不支援樣板。", #無法支援格式所顯示的文字
        template = ImageCarouselTemplate(
            columns = [
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/yRxl6rd.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/yRxl6rd.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/398srGx.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/398srGx.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/PUze65H.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/PUze65H.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/RvwCe1M.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/RvwCe1M.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/bH9uIPR.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/bH9uIPR.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/37uUjGk.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/37uUjGk.jpg"
                    )
                )
            ]
        )
    )
    return output_message

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#9
def image_carousel_message9():
    output_message = TemplateSendMessage(
        alt_text = "此裝置不支援樣板。", #無法支援格式所顯示的文字
        template = ImageCarouselTemplate(
            columns = [
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/yRxl6rd.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/yRxl6rd.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/398srGx.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/398srGx.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/PUze65H.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/PUze65H.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/RvwCe1M.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/RvwCe1M.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/bH9uIPR.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/bH9uIPR.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/37uUjGk.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/37uUjGk.jpg"
                    )
                )
            ]
        )
    )
    return output_message

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#10
def image_carousel_message10():
    output_message = TemplateSendMessage(
        alt_text = "此裝置不支援樣板。", #無法支援格式所顯示的文字
        template = ImageCarouselTemplate(
            columns = [
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/yRxl6rd.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/yRxl6rd.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/398srGx.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/398srGx.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/PUze65H.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/PUze65H.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/RvwCe1M.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/RvwCe1M.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/bH9uIPR.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/bH9uIPR.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/37uUjGk.jpg",
                    action = URITemplateAction(
                        label = "赤崁樓",
                        uri = "https://i.imgur.com/37uUjGk.jpg"
                    )
                )
            ]
        )
    )
    return output_message

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# instruction of pushing code to heroku
# git add .
# git commit -am'ok'
# git push heroku master

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------