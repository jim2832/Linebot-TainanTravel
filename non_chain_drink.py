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
drink1 = "雙生綠豆沙牛奶"
drink2 = "藥師的私房紅茶"
drink3 = "波哥茶飲"
drink4 = "東洲黑糖奶舖"
drink5 = "布萊恩紅茶"
drink6 = "老丘茶舖"
drink7 = "鮮果診所"
drink8 = "雙全紅茶"
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#非連鎖飲料主頁1
def non_drink_imagemap1():
    output_message = ImagemapSendMessage(
        base_url = "https://i.imgur.com/9KWOrQJ.jpg",
        alt_text = "此裝置不支援樣板。", #無法支援格式所顯示的文字
        base_size = BaseSize(height = 1600, width = 1600),
        actions =[
            #1
            MessageImagemapAction(
                text = f"{drink1}介紹",
                area = ImagemapArea(x = 0, y= 0, width = 800, height = 800)
            ),
            #2
            MessageImagemapAction(
                text = f"{drink2}介紹",
                area = ImagemapArea(x = 800, y= 0, width = 800, height = 800)
            ),
            #3
            MessageImagemapAction(
                text = f"{drink3}介紹",
                area = ImagemapArea(x = 0, y= 800, width = 800, height = 800)
            ),
            #4
            MessageImagemapAction(
                text = f"{drink4}介紹",
                area = ImagemapArea(x = 800, y= 800, width = 800, height = 800)
            )
        ]
    )
    return output_message

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#非連鎖飲料主頁2
def non_drink_imagemap2():
    output_message = ImagemapSendMessage(
        base_url = "https://i.imgur.com/BGPJaHA.jpg",
        alt_text = "此裝置不支援樣板。", #無法支援格式所顯示的文字
        base_size = BaseSize(height = 1600, width = 1600),
        actions =[
            #5
            MessageImagemapAction(
                text = f"{drink5}介紹",
                area = ImagemapArea(x = 0, y= 0, width = 800, height = 800)
            ),
            #6
            MessageImagemapAction(
                text = f"{drink6}介紹",
                area = ImagemapArea(x = 800, y= 0, width = 800, height = 800)
            ),
            #7
            MessageImagemapAction(
                text = f"{drink7}介紹",
                area = ImagemapArea(x = 0, y= 800, width = 800, height = 800)
            ),
            #8
            MessageImagemapAction(
                text = f"{drink8}介紹",
                area = ImagemapArea(x = 800, y= 800, width = 800, height = 800)
            )
        ]
    )
    return output_message

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#非連鎖飲料介紹

#1
def drink1_func():
    reply_arr = []

    output_message1 = f"{drink1}菜單"
    output_message2 = ImageSendMassage(
        original_content_url = "https://pic.pimg.tw/haruhii/1620129653-1114303957-g.jpg",
        preview_image_url = "https://pic.pimg.tw/haruhii/1620129653-1114303957-g.jpg"
    )
    # output_message3 = text_reply.text_reply_message(f"{drink1}營業時間\n\n星期一：休息\n星期二：休息星期三：11:00–18:00\n星期四：11:00–18:00\n星期五：11:00–18:00\n星期六：11:00–18:00\n星期日：11:00–18:00")
    # output_message4 = f"{drink1}地圖位置"
    # output_message5 = LocationSendMessage(
    #     title = f"{drink1}",
    #     address = "台南市中西區民族路二段281號",
    #     latitude = "22.99641400517901",
    #     longitude = "120.2034199312454"
    # )

    reply_arr.extend([output_message1,output_message2])

    return reply_arr

#-----------------------------------------------------------------------------------------------------------

#2
def drink2_func():
    reply_arr = []

    output_message1 = f"{drink2}菜單"
    output_message2 = ImageSendMassage(
        original_content_url = "https://img.pboss.tw/uploads/20200218224754_97.jpg",
        preview_image_url = "https://img.pboss.tw/uploads/20200218224754_97.jpg"
    )
    output_message3 = text_reply.text_reply_message(f"{drink2}營業時間\n\n星期一：休息\n星期二：休息\n星期三：11:00–22:00\n星期四：11:00–22:00\n星期五：11:00–22:00\n星期六：11:00–22:00\n星期日：11:00–22:00")
    output_message4 = f"{drink2}地圖位置"
    output_message5 = LocationSendMessage(
        title = f"{drink2}",
        address = "台南市中西區府前路一段373號",
        latitude = "22.990081571756036",
        longitude = "120.1989005568693"
    )

    reply_arr.extend([output_message1,output_message2,output_message3,output_message4,output_message5])

    return reply_arr

#-----------------------------------------------------------------------------------------------------------

#3
def drink3_func():
    reply_arr = []

    output_message1 = f"{drink3}菜單"
    output_message2 = ImageSendMassage(
        original_content_url = "https://img.rainieis.tw/uploads/20200331171352_42.jpg",
        preview_image_url = "https://img.rainieis.tw/uploads/20200331171352_42.jpg"
    )
    output_message3 = text_reply.text_reply_message(f"{drink3}營業時間\n\n星期一：07:30–22:20\n星期二：07:30–22:20\n星期三：07:30–22:20\n星期四：07:30–22:20\n星期五：07:30–22:20\n星期六：07:30–22:20\n星期日：07:30–22:20")
    output_message4 = f"{drink3}地圖位置"
    output_message5 = LocationSendMessage(
        title = f"{drink3}",
        address = "台南市東區勝利路58號",
        latitude = "22.991807323612214",
        longitude = "120.21786800286743"
    )

    reply_arr.extend([output_message1,output_message2,output_message3,output_message4,output_message5])

    return reply_arr

#-----------------------------------------------------------------------------------------------------------

#4
def drink4_func():
    reply_arr = []

    output_message1 = f"{drink4}菜單"
    output_message2 = ImageSendMassage(
        original_content_url = "https://cdn.walkerland.com.tw/images/upload/poi/p72729/m61256/10c17eee9f5b34a0c062724b76fb6531ab9ea26f.jpg",
        preview_image_url = "https://cdn.walkerland.com.tw/images/upload/poi/p72729/m61256/10c17eee9f5b34a0c062724b76fb6531ab9ea26f.jpg"
    )
    output_message3 = text_reply.text_reply_message(f"{drink4}營業時間\n\n星期一：07:00–23:00\n星期二：07:00–23:00\n星期三：07:00–23:00\n星期四：07:00–23:00\n星期五：07:00–23:00\n星期六：07:00–23:00\n星期日：07:00–23:00")
    output_message4 = f"{drink4}地圖位置"
    output_message5 = LocationSendMessage(
        title = f"{drink4}",
        address = "台南市東區東寧路122號",
        latitude = "22.991686179273763",
        longitude = "120.22187476012003"
    )

    reply_arr.extend([output_message1,output_message2,output_message3,output_message4,output_message5])

    return reply_arr

#-----------------------------------------------------------------------------------------------------------

#5
def drink5_func():
    reply_arr = []

    output_message1 = f"{drink5}菜單"
    output_message2 = ImageSendMassage(
        original_content_url = "https://scontent.ftpe10-1.fna.fbcdn.net/v/t1.6435-9/160095769_3747199388661202_1238568005909003349_n.jpg?_nc_cat=106&ccb=1-3&_nc_sid=c4c01c&_nc_ohc=6fSpesEXwRkAX9BovE7&_nc_ht=scontent.ftpe10-1.fna&oh=12d6f1e782dfb2cd7edec381c7eb4716&oe=6123B398",
        preview_image_url = "https://scontent.ftpe10-1.fna.fbcdn.net/v/t1.6435-9/160095769_3747199388661202_1238568005909003349_n.jpg?_nc_cat=106&ccb=1-3&_nc_sid=c4c01c&_nc_ohc=6fSpesEXwRkAX9BovE7&_nc_ht=scontent.ftpe10-1.fna&oh=12d6f1e782dfb2cd7edec381c7eb4716&oe=6123B398"
    )
    output_message3 = text_reply.text_reply_message(f"{drink5}營業時間\n\n星期一：07:00–19:00\n星期二：07:00–19:00\n星期三：07:00–19:00\n星期四：07:00–19:00\n星期五：09:00–21:00\n星期六：09:00–21:00\n星期日：09:00–21:00")
    output_message4 = f"{drink5}地圖位置"
    output_message5 = LocationSendMessage(
        title = f"{drink5}",
        address = "台南市中西區正興街62之2號",
        latitude = "22.99425824478952",
        longitude = "120.19757166469964"
    )

    reply_arr.extend([output_message1,output_message2,output_message3,output_message4,output_message5])

    return reply_arr

#-----------------------------------------------------------------------------------------------------------

#6
def drink6_func():
    reply_arr = []

    output_message1 = f"{drink6}菜單"
    output_message2 = ImageSendMassage(
        original_content_url = "https://img.pboss.tw/uploads/20181022154530_28.jpg",
        preview_image_url = "https://img.pboss.tw/uploads/20181022154530_28.jpg"
    )
    output_message3 = text_reply.text_reply_message(f"{drink6}營業時間\n\n星期一：10:30–21:00\n星期二：10:30–21:00\n星期三：10:30–21:00\n星期四：10:30–21:00\n星期五：10:30–21:00\n星期六：10:30–21:00\n星期日：10:30–21:00")
    output_message4 = f"{drink6}地圖位置"
    output_message5 = LocationSendMessage(
        title = f"{drink6}",
        address = "台南市中西區南門路105號",
        latitude = "22.98772785779906",
        longitude = "120.20461382615942"
    )

    reply_arr.extend([output_message1,output_message2,output_message3,output_message4,output_message5])

    return reply_arr

#-----------------------------------------------------------------------------------------------------------

#7
def drink7_func():
    reply_arr = []

    output_message1 = f"{drink7}菜單"
    output_message2 = ImageSendMassage(
        original_content_url = "https://scontent.ftpe10-1.fna.fbcdn.net/v/t31.18172-8/13723949_537923076399586_3264104757293871409_o.png?_nc_cat=108&ccb=1-3&_nc_sid=730e14&_nc_ohc=j2KPwAZUh7UAX9HMDDg&tn=DbO66jLhb-cjliWk&_nc_ht=scontent.ftpe10-1.fna&oh=ce31009fc3c636d95dc0b92f608c172b&oe=61236939",
        preview_image_url = "https://scontent.ftpe10-1.fna.fbcdn.net/v/t31.18172-8/13723949_537923076399586_3264104757293871409_o.png?_nc_cat=108&ccb=1-3&_nc_sid=730e14&_nc_ohc=j2KPwAZUh7UAX9HMDDg&tn=DbO66jLhb-cjliWk&_nc_ht=scontent.ftpe10-1.fna&oh=ce31009fc3c636d95dc0b92f608c172b&oe=61236939"
    )
    output_message3 = text_reply.text_reply_message(f"{drink7}營業時間\n\n星期一：11:00–20:00\n星期二：11:00–20:00\n星期三：11:00–20:00\n星期四：11:00–20:00\n星期五：11:00–20:00\n星期六：11:00–20:00\n星期日：12:00–20:00")
    output_message4 = f"{drink7}地圖位置"
    output_message5 = LocationSendMessage(
        title = f"{drink7}",
        address = "台南市北區長榮路四段68號",
        latitude = "23.004569499766045",
        longitude = "120.22272710800463"
    )

    reply_arr.extend([output_message1,output_message2,output_message3,output_message4,output_message5])

    return reply_arr

#-----------------------------------------------------------------------------------------------------------

#8
def drink8_func():
    reply_arr = []

    output_message1 = f"{drink8}菜單"
    output_message2 = ImageSendMassage(
        original_content_url = "https://www.foodytw.com/upload/review/image/2020/03/ab10e1a09046989ed045d78de99a6d91.jpg",
        preview_image_url = "https://www.foodytw.com/upload/review/image/2020/03/ab10e1a09046989ed045d78de99a6d91.jpg"
    )
    output_message3 = text_reply.text_reply_message(f"{drink8}營業時間\n\n星期一：11:00–18:00\n星期二：11:00–18:00\n星期三：11:00–18:00\n星期四：11:00–18:00\n星期五：11:00–18:00\n星期六：11:00–18:00\n星期日：休息")
    output_message4 = f"{drink8}地圖位置"
    output_message5 = LocationSendMessage(
        title = f"{drink8}",
        address = "台南市中西區中正路131巷2號",
        latitude = "22.99229565673917",
        longitude = "120.19970712239932"
    )

    reply_arr.extend([output_message1,output_message2,output_message3,output_message4,output_message5])

    return reply_arr