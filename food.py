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

food1 = "邱家小卷米粉"
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

dessert1 = "裕成水果店"
dessert2 = "南泉冰果室"
dessert3 = "正宗古早味冰粉圓"
dessert4 = "林加白糖粿"
dessert5 = "江水號"
dessert6 = "蜷尾家"
dessert7 = "冰鄉"
dessert8 = "宇作茶屋"
dessert9 = "同記安平豆花"

#美食part1
def food_carousel_template1():
    output_message = TemplateSendMessage(
        alt_text = "此裝置不支援樣板。", #無法支援格式所顯示的文字
        template = CarouselTemplate(
            columns = [
                #1
                #邱家小卷米粉
                CarouselColumn(
                    thumbnail_image_url = "https://candicecity.com/wp-content/uploads/2019/07/P4144607.jpg",
                    title = f"{food1}",
                    text = "國華街上遠近馳名的小卷米粉\n✏️推薦料理：小卷米粉、小卷湯",
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
                ),
                #2
                #矮仔成蝦仁飯
                CarouselColumn(
                    thumbnail_image_url = "https://www.yummyday.com.tw/upload/v6/0l6/36474de699494ed297b85dcfeb29a737.jpg",
                    title = f"{food2}",
                    text = "讓人吃完齒頰生香的蝦仁飯\n✏️推薦料理：蝦仁飯、香煎鴨蛋",
                    actions = [
                        MessageTemplateAction(
                            label = "點我看菜單",
                            text = f"{food2}菜單"
                        ),
                        MessageTemplateAction(
                            label = "點我看營業時間",
                            text = f"{food2}營業時間"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{food2}的google地圖位置"
                        )
                    ]
                ),
                #3
                #阿松割包
                CarouselColumn(
                    thumbnail_image_url = "https://s3-us-west-1.amazonaws.com/pic.2bite.com/event/5e98461c5b4d047cdc229217/cover/b02ce95107414327b274c32208dc4735.jpg",
                    title = f"{food3}",
                    text = "麵皮、滷肉和酸菜的絕妙組合\n✏️推薦料理：普通包、瘦肉包",
                    actions = [
                        MessageTemplateAction(
                            label = "點我看菜單",
                            text = f"{food3}菜單"
                        ),
                        MessageTemplateAction(
                            label = "點我看營業時間",
                            text = f"{food3}營業時間"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{food3}的google地圖位置"
                        )
                    ]
                ),
                #4
                #文章牛肉湯
                CarouselColumn(
                    thumbnail_image_url = "https://img.rainieis.tw/uploads/20200330233358_12.jpg",
                    title = f"{food4}",
                    text = "全台灣人都聽過的知名牛肉湯\n✏️推薦菜色：招牌牛肉湯、牛肉燥飯",
                    actions = [
                        MessageTemplateAction(
                            label = "點我看菜單",
                            text = f"{food4}菜單"
                        ),
                        MessageTemplateAction(
                            label = "點我看營業時間",
                            text = f"{food4}營業時間"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{food4}的google地圖位置"
                        )
                    ]
                ),
                #5
                #醇涎坊鍋燒意麵
                CarouselColumn(
                    thumbnail_image_url = "https://4.bp.blogspot.com/-fXC5rl_Dtx4/XilfkEbLc3I/AAAAAAAAJzQ/3GMFUUz9oFMmkn1U7ArJb5DlzaPzM8UYwCKgBGAsYHg/s1600/IMG_0997.jpg",
                    title = f"{food5}",
                    text = "戶限為穿的古早味美食\n✏️推薦料理：鍋燒意麵、鍋燒冬粉",
                    actions = [
                        MessageTemplateAction(
                            label = "點我看菜單",
                            text = f"{food5}菜單"
                        ),
                        MessageTemplateAction(
                            label = "點我看營業時間",
                            text = f"{food5}營業時間"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{food5}的google地圖位置"
                        )
                    ]
                ),
                #6
                #勝利早點
                CarouselColumn(
                    thumbnail_image_url = "https://img.ltn.com.tw/Upload/playing/page/2020/03/05/200305-19193-1-5OuGz.jpg",
                    title = f"{food6}",
                    text = "成大學生和附近居民最愛的早餐店\n✏️推薦料理：沙拉蛋餅、豬排吐司夾蛋",
                    actions = [
                        MessageTemplateAction(
                            label = "點我看菜單",
                            text = f"{food6}菜單"
                        ),
                        MessageTemplateAction(
                            label = "點我看營業時間",
                            text = f"{food6}營業時間"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{food6}的google地圖位置"
                        )
                    ]
                ),
                #7
                #無名米糕
                CarouselColumn(
                    thumbnail_image_url = "https://pic.pimg.tw/imsean/1469108135-953791719.jpg",
                    title = f"{food7}",
                    text = "紅遍大街小巷的八珍玉食\n✏️推薦料理：米糕、魚肚麵線",
                    actions = [
                        MessageTemplateAction(
                            label = "點我看菜單",
                            text = f"{food7}菜單"
                        ),
                        MessageTemplateAction(
                            label = "點我看營業時間",
                            text = f"{food7}營業時間"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{food7}的google地圖位置"
                        )
                    ]
                ),
                #8
                #王氏魚皮
                CarouselColumn(
                    thumbnail_image_url = "https://cdn.walkerland.com.tw/images/upload/poi/p952/m46619/51c5125714ad81f6c457f4214d0906270c98d83b.jpg",
                    title = f"{food8}",
                    text = "令人大快朵頤的海味專賣店\n✏️推薦料理：魚皮湯、魯魚肚",
                    actions = [
                        MessageTemplateAction(
                            label = "點我看菜單",
                            text = f"{food8}菜單"
                        ),
                        MessageTemplateAction(
                            label = "點我看營業時間",
                            text = f"{food8}營業時間"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{food8}的google地圖位置"
                        )
                    ]
                ),
                #9
                #阿江鱔魚意麵
                CarouselColumn(
                    thumbnail_image_url = "https://img.rainieis.tw/uploads/20180816160442_76.jpg",
                    title = f"{food9}",
                    text = "乾炒焦香又爽脆可口的佳餚\n✏️推薦料理：鱔魚意麵、鱔魚米粉",
                    actions = [
                        MessageTemplateAction(
                            label = "點我看菜單",
                            text = f"{food9}菜單"
                        ),
                        MessageTemplateAction(
                            label = "點我看營業時間",
                            text = f"{food9}營業時間"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{food9}的google地圖位置"
                        )
                    ]
                ),
                #10
                #周氏蝦捲
                CarouselColumn(
                    thumbnail_image_url = "https://live.staticflickr.com/4100/4904166650_608292d939_b.jpg",
                    title = f"{food10}",
                    text = "台南必吃經典名產\n✏️推薦料理：炸蝦捲、蝦丸湯",
                    actions = [
                        MessageTemplateAction(
                            label = "點我看菜單",
                            text = f"{food10}菜單"
                        ),
                        MessageTemplateAction(
                            label = "點我看營業時間",
                            text = f"{food10}營業時間"
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
                    thumbnail_image_url = "https://4.bp.blogspot.com/-q3wk9qvQ424/WdIt3-qpwmI/AAAAAAAAGYs/X0hfJS5db7M_gRdhZ0Vf3kT0ZiP1MPoEQCKgBGAs/w1200-h630-p-k-no-nu/07.jpg", #圖片連結
                    title = f"{food11}", #標題
                    text = "在地人從小吃到大的懷舊味道\n✏️推薦料理：乾意麵、骨肉湯", #推薦料理
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
                    thumbnail_image_url = "https://static.wixstatic.com/media/060fcb_d29cc3e603954682a703e3d0be08aa46.jpg/v1/fill/w_498,h_332,al_c,q_85,usm_0.66_1.00_0.01/060fcb_d29cc3e603954682a703e3d0be08aa46.jpg", #圖片連結
                    title = f"{food12}", #標題
                    text = "令人食指大動的傳統中式美食\n✏️推薦料理：碗粿、魚焿", #推薦料理
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
                    thumbnail_image_url = "https://media-cdn.tripadvisor.com/media/photo-s/0d/f6/b4/d7/caption.jpg", #圖片連結
                    title = f"{food13}", #標題
                    text = "特製醬料加上Q彈肉圓總是供不應求\n✏️推薦料理：肉圓(以二粒為單位)", #推薦料理
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
                    thumbnail_image_url = "https://4.bp.blogspot.com/-pBTuW6nyGlI/Wz3y7BZgm3I/AAAAAAAAa4g/7JdT0LZdCs4xF_RaALwKNDh8CxivJHoXQCKgBGAs/s1600/06.jpg", #圖片連結
                    title = f"{food14}", #標題
                    text = "讓人愛不釋手的生蛋黃和豬油拌飯\n✏️推薦料理：豬油拌飯(含生蛋黃)", #推薦料理
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
                    thumbnail_image_url = "https://3.bp.blogspot.com/-RgfFRmKSunA/W-RrUSrIGYI/AAAAAAAAgqI/1McdpIrvyGYjVg8WxjCkbsF2QdMIRorrgCKgBGAs/s1600/IMG_7830.jpg", #圖片連結
                    title = f"{food15}", #標題
                    text = "香飄十里且家喻戶曉的國華街經典\n✏️推薦料理：肉燥飯、魚鬆飯", #推薦料理
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
                    thumbnail_image_url = "https://hululu.tw/wp-content/uploads/20200510000540_51.jpg", #圖片連結
                    title = f"{food16}", #標題
                    text = "紅遍全台灣的南部僅有可口早/午餐\n✏️推薦料理：4號餐、9號餐", #推薦料理
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
                    thumbnail_image_url = "https://i.imgur.com/Fxx3cGX.jpg", #圖片連結
                    title = f"{food17}", #標題
                    text = "外酥內軟的炸雞總讓人吃的津津有味\n✏️推薦料理：八兩雞、黃金魚條", #推薦料理
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
                    thumbnail_image_url = "https://i.imgur.com/2yxHQ8p.jpg", #圖片連結
                    title = f"{food18}", #標題
                    text = "台南保安路的超人氣排隊美食\n✏️推薦料理：豬心冬粉、麻油豬心", #推薦料理
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
                    thumbnail_image_url = "https://img.rainieis.tw/uploads/20180212120804_61.jpg", #圖片連結
                    title = f"{food19}", #標題
                    text = "巷弄間的70年台南名產兼美食\n✏️推薦料理：正老牌棺材板", #推薦料理
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
                    thumbnail_image_url = "https://media-cdn.tripadvisor.com/media/photo-s/0f/72/57/10/congee.jpg", #圖片連結
                    title = f"{food20}", #標題
                    text = "讓人吃完超滿足的極澎湃鹹粥\n✏️推薦料理：土魠鹹粥、虱目鹹粥", #推薦料理
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

#甜點
def dessert_carousel_template():
    output_message = TemplateSendMessage(
        alt_text = "此裝置不支援樣板。", #無法支援格式所顯示的文字
        template = CarouselTemplate(
            columns = [
                #1
                #裕成水果店
                CarouselColumn(
                    thumbnail_image_url = "https://travelimg.yamedia.tw/20180811/20180809235833512.jpg",
                    title = f"{dessert1}",
                    text = "每一口都吃得到老闆用心的浮誇水果冰\n✏️推薦料理：草莓、芒果牛奶冰",
                    actions = [
                        MessageTemplateAction(
                            label = "點我看菜單",
                            text = f"{dessert1}菜單"
                        ),
                        MessageTemplateAction(
                            label = "點我看營業時間",
                            text = f"{dessert1}營業時間"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{dessert1}的google地圖位置"
                        )
                    ]
                ),
                #2
                #南泉冰果室
                CarouselColumn(
                    thumbnail_image_url = "https://hululu.tw/wp-content/uploads/20191122085927_45.jpg",
                    title = f"{dessert2}",
                    text = "來台南必吃的浮誇澎湃系水果冰店\n✏️推薦料理：番茄蜜餞冰",
                    actions = [
                        MessageTemplateAction(
                            label = "點我看菜單",
                            text = f"{dessert2}菜單"
                        ),
                        MessageTemplateAction(
                            label = "點我看營業時間",
                            text = f"{dessert2}營業時間"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{dessert2}的google地圖位置"
                        )
                    ]
                ),
                #3
                #正宗古早味冰粉圓
                CarouselColumn(
                    thumbnail_image_url = "https://scontent.ftpe10-1.fna.fbcdn.net/v/t1.18169-9/548441_432767113405121_1782768189_n.jpg?_nc_cat=110&ccb=1-3&_nc_sid=09cbfe&_nc_ohc=HQ_PNX4wmTIAX9PMuYq&_nc_ht=scontent.ftpe10-1.fna&oh=af63df3f1207e1b7b98189faa54c67c1&oe=61211028",
                    title = f"{dessert3}",
                    text = "清涼解渴的夏日古早好滋味\n✏️推薦料理：大杯冰粉圓",
                    actions = [
                        MessageTemplateAction(
                            label = "點我看菜單",
                            text = f"{dessert3}菜單"
                        ),
                        MessageTemplateAction(
                            label = "點我看營業時間",
                            text = f"{dessert3}營業時間"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{dessert3}的google地圖位置"
                        )
                    ]
                ),
                #4
                #林家白糖粿
                CarouselColumn(
                    thumbnail_image_url = "https://flyblog.cc/wp-content/uploads/2020/12/DSCF6408.jpg",
                    title = f"{dessert4}",
                    text = "當地人最愛的甘甜點心\n✏️推薦料理：白糖糕、蕃薯椪",
                    actions = [
                        MessageTemplateAction(
                            label = "點我看菜單",
                            text = f"{dessert4}菜單"
                        ),
                        MessageTemplateAction(
                            label = "點我看營業時間",
                            text = f"{dessert4}營業時間"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{dessert4}的google地圖位置"
                        )
                    ]
                ),
                #5
                #江水號
                CarouselColumn(
                    thumbnail_image_url = "https://4.bp.blogspot.com/-6YiIlfeSMF0/Xmn-RFrmw4I/AAAAAAAANEY/I4II1eSrx3sdgIUFSo-tCPrtcXzpnbG3QCKgBGAsYHg/s1600/IMG_0746.jpg",
                    title = f"{dessert5}",
                    text = "配料滿到爆炸的超好吃芋泥冰\n✏️推薦料理：芋頭冰、八寶冰",
                    actions = [
                        MessageTemplateAction(
                            label = "點我看菜單",
                            text = f"{dessert5}菜單"
                        ),
                        MessageTemplateAction(
                            label = "點我看營業時間",
                            text = f"{dessert5}營業時間"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{dessert5}的google地圖位置"
                        )
                    ]
                ),
                #6
                #蜷尾家
                CarouselColumn(
                    thumbnail_image_url = "https://img.dingeat.com/uploads/20200614234025_85.jpg",
                    title = f"{dessert6}",
                    text = "在夏日解熱的最佳甜點\n✏️推薦料理：蜜香紅茶霜淇淋",
                    actions = [
                        MessageTemplateAction(
                            label = "點我看菜單",
                            text = f"{dessert6}菜單"
                        ),
                        MessageTemplateAction(
                            label = "點我看營業時間",
                            text = f"{dessert6}營業時間"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{dessert6}的google地圖位置"
                        )
                    ]
                ),
                #7
                #冰鄉
                CarouselColumn(
                    thumbnail_image_url = "https://hululu.tw/wp-content/uploads/flickr/39478016202_e133871f03_c.jpg",
                    title = f"{dessert7}",
                    text = "便宜又大碗的夏日必吃冰店\n✏️推薦料理：芒果牛乳冰、草莓醬乳冰",
                    actions = [
                        MessageTemplateAction(
                            label = "點我看菜單",
                            text = f"{dessert7}菜單"
                        ),
                        MessageTemplateAction(
                            label = "點我看營業時間",
                            text = f"{dessert7}營業時間"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{dessert7}的google地圖位置"
                        )
                    ]
                ),
                #8
                #宇作茶屋
                CarouselColumn(
                    thumbnail_image_url = "https://d1ralsognjng37.cloudfront.net/493ffb52-96a0-49eb-8dc9-388914780be6.jpeg",
                    title = f"{dessert8}",
                    text = "濃厚日式風情的精緻茶屋\n✏️推薦料理：抹茶奶酪、抹茶善哉",
                    actions = [
                        MessageTemplateAction(
                            label = "點我看菜單",
                            text = f"{dessert8}菜單"
                        ),
                        MessageTemplateAction(
                            label = "點我看營業時間",
                            text = f"{dessert8}營業時間"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{dessert8}的google地圖位置"
                        )
                    ]
                ),
                #9
                #同記安平豆花
                CarouselColumn(
                    thumbnail_image_url = "https://www.saydigi.com/wp-content/uploads/2020/11/4bd191fe99ef8f862e28c8b49a89672c.jpg",
                    title = f"{dessert9}",
                    text = "台南必吃的甜而不膩豆花\n✏️推薦料理：傳統白豆花、鮮奶豆花",
                    actions = [
                        MessageTemplateAction(
                            label = "點我看菜單",
                            text = f"{dessert9}菜單"
                        ),
                        MessageTemplateAction(
                            label = "點我看營業時間",
                            text = f"{dessert9}營業時間"
                        ),
                        MessageTemplateAction(
                            label = "點我看地圖位置",
                            text = f"可由此打開{dessert9}的google地圖位置"
                        )
                    ]
                )
            ]
        )
    )
    return output_message