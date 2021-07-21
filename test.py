def food_carousel_template1():
    output_message = TemplateSendMessage(
        alt_text = "此裝置不支援樣板。", #無法支援格式所顯示的文字
        template = CarouselTemplate(
            columns = [
                #1
                #邱家小捲米粉
                CarouselColumn(
                    thumbnail_image_url = "https://candicecity.com/wp-content/uploads/2019/07/P4144607.jpg",
                    title = f"{food1}",
                    text = "國華街上遠近馳名的小捲米粉\n推薦料理：小捲米粉、小捲湯",
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
                    text = "讓人吃完齒頰生香的蝦仁飯\n推薦料理：蝦仁飯、香煎鴨蛋",
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
                    thumbnail_image_url = "http://1.bp.blogspot.com/-fogSQPqjjuU/UAYtovVLaxI/AAAAAAAADNA/cuNwHI4XIjc/s1600/IMG_5215.JPG",
                    title = f"{food3}",
                    text = "麵皮、滷肉、酸菜和花生粉的絕妙組合\n推薦料理：普通包、瘦肉包",
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
                    text = "全台灣人都聽過的知名牛肉湯\n推薦菜色：招牌牛肉湯、牛肉燥飯",
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
                    text = "戶限為穿的古早味美食\n推薦料理：鍋燒意麵、鍋燒冬粉",
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
                    text = "成大學生和附近居民最愛的早餐店\n推薦料理：沙拉蛋餅、豬排吐司夾蛋",
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
                    text = "紅遍大街小巷的八珍玉食\n推薦料理：米糕、魚肚麵線",
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
                    text = "令人大快朵頤的海味專賣店\n推薦料理：魚皮湯、魯魚肚",
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
                    text = "乾炒焦香又爽脆可口的佳餚\n推薦料理：冠軍乾炒鱔魚意麵、鱔魚米粉湯",
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
                    thumbnail_image_url = "http://2.bp.blogspot.com/_UA6xx1hhCsQ/SYaaanQbucI/AAAAAAAABas/boIKMS6X0AI/s280/zhous+shrimp+roll.jpg",
                    title = f"{food10}",
                    text = "台南必吃經典名產\n推薦料理：炸蝦捲、蝦丸湯",
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