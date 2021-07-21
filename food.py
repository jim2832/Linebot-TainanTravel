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
                    thumbnail_image_url = "https://pic.pimg.tw/whuy123/1523332170-611241936.jpg",
                    title = f"{food1}",
                    text = "歷史悠久的荷治時期行政中心",
                    actions = [
                        MessageTemplateAction(
                            label = f"{food1}",
                            text = "https://www.twtainan.net/zh-tw/attractions/detail/674"
                        ),
                        MessageTemplateAction(
                            label = "點我看景點圖片",
                            text = f"{food1}圖片"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{food1}的google地圖位置"
                        )
                    ]
                ),
                CarouselColumn( #2
                    thumbnail_image_url = "https://image.cdn-eztravel.com.tw/BIvf9xU550uLpO3D1NYvXGNT4nyO_NgoOh-5hPd4IEQ/g:ce/aHR0cHM6Ly92YWNhdGlvbi5jZG4tZXp0cmF2ZWwuY29tLnR3L2ltZy9WRFIvVE5OXzEyMDAzMzQyMTAuanBn.jpg",
                    title = f"{food2}",
                    text = "由荷蘭人建造的台灣史上第一座城堡",
                    actions = [
                        MessageTemplateAction(
                            label = f"{food2}",
                            text = "https://www.twtainan.net/zh-tw/attractions/detail/671"
                        ),
                        MessageTemplateAction(
                            label = "點我看景點圖片",
                            text = f"{food2}圖片"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{food2}的google地圖位置"
                        )
                    ]
                ),
                CarouselColumn( #3
                    thumbnail_image_url = "https://www.chimeimuseum.org/uploads/sliders/60da70ae81eaa.jpg",
                    title = f"{food3}",
                    text = "擁有西洋藝術、樂器、兵器等的知名博物館",
                    actions = [
                        MessageTemplateAction(
                            label = f"{food3}",
                            text = "https://www.twtainan.net/zh-tw/attractions/detail/572"
                        ),
                        MessageTemplateAction(
                            label = "點我看景點圖片",
                            text = f"{food3}圖片"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{food3}的google地圖位置"
                        )
                    ]
                ),
                CarouselColumn( #4
                    thumbnail_image_url = "https://cc.tvbs.com.tw/img/program/upload/2020/02/05/20200205163001-ba4cb2f0.jpg",
                    title = f"{food4}",
                    text = "以街底主祀神農氏之藥王廟為名的創新老街",
                    actions = [
                        MessageTemplateAction(
                            label = f"{food4}",
                            text = "https://www.twtainan.net/zh-tw/attractions/detail/1351"
                        ),
                        MessageTemplateAction(
                            label = "點我看景點圖片",
                            text = f"{food4}圖片"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{food4}的google地圖位置"
                        )
                    ]
                ),
                CarouselColumn( #5
                    thumbnail_image_url = "https://img.natgeomedia.com/userfiles/PhotoContest/925/sm1920/2019090977389193.jpg",
                    title = f"{food5}",
                    text = "接近傍晚的夕陽總是引人入勝\n是個讓外地遊客流連忘返的美麗沙灘",
                    actions = [
                        MessageTemplateAction(
                            label = f"{food5}",
                            text = "https://www.twtainan.net/zh-tw/attractions/detail/5520"
                        ),
                        MessageTemplateAction(
                            label = "點我看景點圖片",
                            text = f"{food5}圖片"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{food5}的google地圖位置"
                        )
                    ]
                ),
                CarouselColumn( #6
                    thumbnail_image_url = "https://tainan.funcard.com.tw/imageCache/tainan/JnLv_600x400.jpg",
                    title = f"{food6}",
                    text = "清領時期繁盛一時的重要商業據點",
                    actions = [
                        MessageTemplateAction(
                            label = f"{food6}",
                            text = "https://www.twtainan.net/zh-tw/attractions/detail/687"
                        ),
                        MessageTemplateAction(
                            label = "點我看景點圖片",
                            text = f"{food6}圖片"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{food6}的google地圖位置"
                        )
                    ]
                ),
                CarouselColumn( #7
                    thumbnail_image_url = "https://4.bp.blogspot.com/-0kz6Q2pW1wk/Xiq0YZ-cKlI/AAAAAAAAJ6U/5rTRQS-99gk2LmMV9VJia79EjcalGfIPQCKgBGAsYHg/s1600/IMG_8444.jpg",
                    title = f"{food7}",
                    text = "台灣最知名和最熱鬧的夜市之一",
                    actions = [
                        MessageTemplateAction(
                            label = f"{food7}",
                            text = "https://www.twtainan.net/zh-tw/attractions/detail/5572"
                        ),
                        MessageTemplateAction(
                            label = "點我看景點圖片",
                            text = f"{food7}圖片"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{food7}的google地圖位置"
                        )
                    ]
                ),
                CarouselColumn( #8
                    thumbnail_image_url = "https://pic.pimg.tw/anrine910070/1601175205-2788673474-g.jpg",
                    title = f"{food8}",
                    text = "擁有專屬生日採鹽的原日式試鹽工廠",
                    actions = [
                        MessageTemplateAction(
                            label = f"{food8}",
                            text = "https://www.twtainan.net/zh-tw/attractions/detail/1323"
                        ),
                        MessageTemplateAction(
                            label = "點我看景點圖片",
                            text = f"{food8}圖片"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{food8}的google地圖位置"
                        )
                    ]
                ),
                CarouselColumn( #9
                    thumbnail_image_url = "https://photo.travelking.com.tw/scenery/98E3B96F-21E9-41AD-8193-31840E021733_e.jpg",
                    title = f"{food9}",
                    text = "具有三百多年歷史的文化古都核心",
                    actions = [
                        MessageTemplateAction(
                            label = f"{food9}",
                            text = "https://www.twtainan.net/zh-tw/attractions/detail/800"
                        ),
                        MessageTemplateAction(
                            label = "點我看景點圖片",
                            text = f"{food9}圖片"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{food9}的google地圖位置"
                        )
                    ]
                ),
                CarouselColumn( #10
                    thumbnail_image_url = "https://www.twtainan.net/image/13910/1024x768",
                    title = f"{food10}",
                    text = "以鹽為最大特色的高聳壯觀鹽山",
                    actions = [
                        MessageTemplateAction(
                            label = f"{food10}",
                            text = "https://www.twtainan.net/zh-tw/attractions/detail/471"
                        ),
                        MessageTemplateAction(
                            label = "點我看景點圖片",
                            text = f"{food10}圖片"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{food10}的google地圖位置"
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
                #11
                #小杜意麵
                CarouselColumn(
                    thumbnail_image_url = "", #圖片連結
                    title = f"{food11}", #標題
                    text = "", #推薦料理
                    actions = [
                        MessageTemplateAction(
                            label = "點我看菜單",
                            text = f"{food11}菜單"
                        ),
                        MessageTemplateAction(
                            label = "點我看營業時間",
                            text = f"{food11}營業時間"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{food11}的google地圖位置"
                        )
                    ]
                ),
                #12
                #富盛號碗粿
                CarouselColumn(
                    thumbnail_image_url = "", #圖片連結
                    title = f"{food12}", #標題
                    text = "", #推薦料理
                    actions = [
                        MessageTemplateAction(
                            label = "點我看菜單",
                            text = f"{food12}菜單"
                        ),
                        MessageTemplateAction(
                            label = "點我看營業時間",
                            text = f"{food12}營業時間"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{food12}的google地圖位置"
                        )
                    ]
                ),
                #13
                #福記肉圓
                CarouselColumn(
                    thumbnail_image_url = "", #圖片連結
                    title = f"{food13}", #標題
                    text = "", #推薦料理
                    actions = [
                        MessageTemplateAction(
                            label = "點我看菜單",
                            text = f"{food13}菜單"
                        ),
                        MessageTemplateAction(
                            label = "點我看營業時間",
                            text = f"{food13}營業時間"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{food13}的google地圖位置"
                        )
                    ]
                ),
                #14
                #鼎富發豬油拌飯
                CarouselColumn(
                    thumbnail_image_url = "", #圖片連結
                    title = f"{food14}", #標題
                    text = "", #推薦料理
                    actions = [
                        MessageTemplateAction(
                            label = "點我看菜單",
                            text = f"{food14}菜單"
                        ),
                        MessageTemplateAction(
                            label = "點我看營業時間",
                            text = f"{food14}營業時間"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{food14}的google地圖位置"
                        )
                    ]
                ),
                #15
                #國華街肉燥飯
                CarouselColumn(
                    thumbnail_image_url = "", #圖片連結
                    title = f"{food15}", #標題
                    text = "", #推薦料理
                    actions = [
                        MessageTemplateAction(
                            label = "點我看菜單",
                            text = f"{food15}菜單"
                        ),
                        MessageTemplateAction(
                            label = "點我看營業時間",
                            text = f"{food15}營業時間"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{food15}的google地圖位置"
                        )
                    ]
                ),
                #16
                #丹丹漢堡(成功店)
                CarouselColumn(
                    thumbnail_image_url = "", #圖片連結
                    title = f"{food16}", #標題
                    text = "", #推薦料理
                    actions = [
                        MessageTemplateAction(
                            label = "點我看菜單",
                            text = f"{food16}菜單"
                        ),
                        MessageTemplateAction(
                            label = "點我看營業時間",
                            text = f"{food16}營業時間"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{food16}的google地圖位置"
                        )
                    ]
                ),
                #17
                #炸雞洋行
                CarouselColumn(
                    thumbnail_image_url = "", #圖片連結
                    title = f"{food17}", #標題
                    text = "", #推薦料理
                    actions = [
                        MessageTemplateAction(
                            label = "點我看菜單",
                            text = f"{food17}菜單"
                        ),
                        MessageTemplateAction(
                            label = "點我看營業時間",
                            text = f"{food17}營業時間"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{food17}的google地圖位置"
                        )
                    ]
                ),
                #18
                #阿明豬心冬粉
                CarouselColumn(
                    thumbnail_image_url = "", #圖片連結
                    title = f"{food18}", #標題
                    text = "", #推薦料理
                    actions = [
                        MessageTemplateAction(
                            label = "點我看菜單",
                            text = f"{food18}菜單"
                        ),
                        MessageTemplateAction(
                            label = "點我看營業時間",
                            text = f"{food18}營業時間"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{food18}的google地圖位置"
                        )
                    ]
                ),
                #19
                #赤崁棺材板
                CarouselColumn(
                    thumbnail_image_url = "", #圖片連結
                    title = f"{food19}", #標題
                    text = "", #推薦料理
                    actions = [
                        MessageTemplateAction(
                            label = "點我看菜單",
                            text = f"{food19}菜單"
                        ),
                        MessageTemplateAction(
                            label = "點我看營業時間",
                            text = f"{food19}營業時間"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{food19}的google地圖位置"
                        )
                    ]
                ),
                #20
                #阿堂鹹粥
                CarouselColumn(
                    thumbnail_image_url = "", #圖片連結
                    title = f"{food20}", #標題
                    text = "", #推薦料理
                    actions = [
                        MessageTemplateAction(
                            label = "點我看菜單",
                            text = f"{food20}菜單"
                        ),
                        MessageTemplateAction(
                            label = "點我看營業時間",
                            text = f"{food20}營業時間"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{food20}的google地圖位置"
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