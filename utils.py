import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, URITemplateAction, TextMessage, TextSendMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction, PostbackTemplateAction, CarouselTemplate, CarouselColumn


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


def send_image_message(reply_token, url):
    line_bot_api = LineBotApi(channel_access_token)
    message = ImageSendMessage(
        type='image',
        original_content_url=url,
        preview_image_url=url
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"


def send_restaurant_info(reply_token, image_url, info_url, map_url, rec_url):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='餐廳資訊',
            text='點擊看介紹、地圖、更多推薦!',
            thumbnail_image_url=image_url,
            actions=[
                URITemplateAction(
                    label='介紹',
                    uri=info_url
                ), URITemplateAction(
                    label='地圖',
                    uri=map_url
                ), URITemplateAction(
                    label='更多推薦',
                    uri=rec_url
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_japanese_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='餐點類型',
            text='點擊你有興趣的料理',
            thumbnail_image_url='https://scontent-yyz1-1.cdninstagram.com/v/t51.2885-15/e35/120130316_1209935556036101_2012112683504480388_n.jpg?_nc_ht=scontent-yyz1-1.cdninstagram.com&_nc_cat=105&_nc_ohc=iz3HWy45vesAX-i8hq_&se=7&tp=1&oh=14e4147c6355f24ca8ddc5d25c04a199&oe=6012021A&ig_cache_key=MjQwNzI0OTg1ODM3NjA5MTM4Nw%3D%3D.2',
            actions=[
                MessageTemplateAction(
                    label='飯類',
                    text='rice'
                ),
                MessageTemplateAction(
                    label='壽司、生魚片',
                    text='sushi'
                ),
                MessageTemplateAction(
                    label='拉麵',
                    text='ramen'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_thai_restaurant_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='泰式餐廳',
            text='點擊餐廳看介紹',
            thumbnail_image_url='https://lh3.googleusercontent.com/N224Q4Rx1_TvTx9JtUkGzC2GsDEFfPMciR6Sd2k20m_cu00XQRbB0Jr2kw1ktpL35p7BhIjz1jY_hc55oIV1nIBjGMwiGnCZbghnnqvHAzNnSI9gDj8sQypKC7f5oanews9XQSzHXcA4zZKgLBWVKSjoEm-S1K90IhT6gdHOKfGQRfrAUqMyTM3qnf2huCc4xwzrpRbnQUHvGxFeOmYsLyq3Jm2PvZCqMxGThX5bZSUyDnuKFrB1kJvrWwIPM7NL4wUpqdTtYiCUs3SKNcb7506AnZbvVVGbSJGvDs75ZIrWoFDMFtL3sAUP5SbuFslLdpw5TCMoU5lQXAZY0P-doMVKu1uG2i5XCqfPS_HqrmIoUGOtkSlB9CHanaB69XkKKKnd2-ZA2jtR12neB74sVF7_4cVqpXqLW3T4YC5Sv5snqdYTa7fdu9CDzZZZc3dVA4Z8JiQE-Zbx4YI7EmLtvmO1w7ReOYSw77OjKqbBzUJtfbUl9qVALafGGiwVb4guHa7pRgobJ-bVZkFSFpj8lwooNG1seHilUDwmbFaw8086Fy4F3UERU1t7JFGy_IGYlaxlccSkGIRj2hq6TTDAcIr9WQohLNe-qHFAycpagOqLA5shEpNeVvZPKVTvrbp4wdOk98-ocl1xBu8E8mocMa9QPap7z7WwJpP8xuRjLqTPZW9AIB2Nxcd1RUb6jg=w678-h903-no?authuser=0',
            actions=[
                MessageTemplateAction(
                    label='山豬林',
                    text='thai1'
                ),
                MessageTemplateAction(
                    label='BITCH小姐',
                    text='thai2'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_korean_restaurant_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='韓式餐廳',
            text='點擊餐廳看介紹',
            thumbnail_image_url='https://decing.tw/wp-content/uploads/20190825180017_16.jpg',
            actions=[
                MessageTemplateAction(
                    label='豬對有',
                    text='korean1'
                ),
                MessageTemplateAction(
                    label='韓朝',
                    text='korean2'
                ),
                MessageTemplateAction(
                    label='老韓家韓式廚房',
                    text='korean3'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_tainan_restaurant_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='排隊美食',
            text='點擊餐廳看介紹',
            thumbnail_image_url='https://cdn2.ettoday.net/images/4330/4330047.jpg',
            actions=[
                MessageTemplateAction(
                    label='小赤佬',
                    text='tainan1'
                ),
                MessageTemplateAction(
                    label='文章牛肉湯',
                    text='tainan2'
                ),
                MessageTemplateAction(
                    label='富盛號',
                    text='tainan3'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_hotpot_restaurant_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='火鍋',
            text='點擊餐廳看介紹',
            thumbnail_image_url='https://i2.achangpro.com/img.pingu.blog/uploads/20190316115806_1.jpg',
            actions=[
                MessageTemplateAction(
                    label='築間',
                    text='hotpot1'
                ),
                MessageTemplateAction(
                    label='五鮮極',
                    text='hotpot2'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_diner_restaurant_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='美式餐廳',
            text='點擊餐廳看介紹',
            thumbnail_image_url='https://i2.wp.com/hululu.tw/wp-content/uploads/flickr/41150339274_00c0e7d4e1_c.jpg',
            actions=[
                MessageTemplateAction(
                    label='sk尚恩廚房',
                    text='diner1'
                ),
                MessageTemplateAction(
                    label='可可貝里',
                    text='diner2'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_japanese_rice_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='飯類',
            text='想吃什麼',
            thumbnail_image_url='https://cdn3.tw.orstatic.com/userphoto/photo/B/93R/01SQS60779F8D4EB2B4E44px.jpg',
            actions=[
                MessageTemplateAction(
                    label='丼飯',
                    text='donburi'
                ),
                MessageTemplateAction(
                    label='豬排',
                    text='tonkatsu'
                ),
                MessageTemplateAction(
                    label='日式定食',
                    text='teishoku'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_japanese_rice_restaurant_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='丼飯',
            text='點擊餐廳看介紹',
            thumbnail_image_url='https://cdn3.tw.orstatic.com/userphoto/photo/B/93R/01SQS60779F8D4EB2B4E44px.jpg',
            actions=[
                MessageTemplateAction(
                    label='肉肉控',
                    text='donburi1'
                ),
                MessageTemplateAction(
                    label='職人雙響丼',
                    text='donburi2'
                ),
                MessageTemplateAction(
                    label='炙丼家',
                    text='donburi3'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_japanese_teishoku_restaurant_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='日式定食',
            text='點擊餐廳看介紹',
            thumbnail_image_url='https://lh3.googleusercontent.com/RMKJCvhAgSPC_JwPrWkn5U9vPRplY1m-hLG892Dr9IPxsIJLBWwuhkPz4MUreayhZt0HOBVDAQEL4R5hS6IpQq9ZNpJkRhIYUiqrMxqOTl9nY223F4LA9GwVSh3AyJfIowgGS15buP00u3q6XMiYHfDtXiG0lOe1B78yoWOd5TO0Uzm8mDe_9ClaTo7B-Sd_YtpqaSHHY-wkVrjrBdWXK3Ri48Wq8MclkEPB3_fRbztSzUNkPqQXUBcrDthMTw0rcBPng9DboMRySdZc8im6N3vtSv5dGEIYh4_IO18wXGT_HB_DU-s31Nn9miwLwO1UMkkQQm-r6icFb9PnP6TKdF-Sev1TEexAUlMeVeTp2iwpufNNILBaAnQkb7EoulIZl2K5a9kbA63zwWBU0LWJG8v8RCAefI7QDPfEGHiVppVo6Hjg_meZlF2K9jMvtPIoWR5QdV-lkO--Gq18ApCDDfL0dI1qRhCrgVsjsDwqHhALu1x1u6EXiBO67XCIx2-ZQZcsZMnYD1KbHLeob4T409BPBw2FuVjKvbtts85T5d3MNeCC0GLmytF7MrQkmY_2YE95HSECk5lqj_aticvceo7KbBwcru03vSO-QIvMH4bDzo9a1IN-QINoyAQJn95e3di3_9NqfHVN7FbnUqgGxE7IGk6BWJKTkcOg6zGoPk0pE6OozN1GQfYpiw3QNg=w1204-h903-no?authuser=0',
            actions=[
                MessageTemplateAction(
                    label='漁人食堂',
                    text='teishoku1'
                ),
                MessageTemplateAction(
                    label='櫻之庭',
                    text='teishoku2'
                ),
                MessageTemplateAction(
                    label='石火山碳燒蓋飯',
                    text='teishoku3'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_japanese_sushi_restaurant_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='壽司、生魚片',
            text='點擊餐廳看介紹',
            thumbnail_image_url='https://pic.pimg.tw/shu333/1506931184-944375930.jpg',
            actions=[
                MessageTemplateAction(
                    label='毛丼',
                    text='sushi1'
                ),
                MessageTemplateAction(
                    label='鮨次郎',
                    text='sushi2'
                ),
                MessageTemplateAction(
                    label='日暮壽司',
                    text='sushi3'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_japanese_ramen_restaurant_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='拉麵',
            text='點擊餐廳看介紹',
            thumbnail_image_url='https://decing.tw/wp-content/uploads/20201020222151_4.jpg',
            actions=[
                MessageTemplateAction(
                    label='覺丸',
                    text='ramen1'
                ),
                MessageTemplateAction(
                    label='八峰亭',
                    text='ramen2'
                ),
                MessageTemplateAction(
                    label='寶來軒',
                    text='ramen3'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_japanese_tonkatsu_restaurant_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='豬排',
            text='點擊餐廳看介紹',
            thumbnail_image_url='https://scontent-yyz1-1.cdninstagram.com/v/t51.2885-15/e35/120130316_1209935556036101_2012112683504480388_n.jpg?_nc_ht=scontent-yyz1-1.cdninstagram.com&_nc_cat=105&_nc_ohc=iz3HWy45vesAX-i8hq_&se=7&tp=1&oh=14e4147c6355f24ca8ddc5d25c04a199&oe=6012021A&ig_cache_key=MjQwNzI0OTg1ODM3NjA5MTM4Nw%3D%3D.2',
            actions=[
                MessageTemplateAction(
                    label='元味屋',
                    text='tonkatsu1'
                ),
                MessageTemplateAction(
                    label='豚讚',
                    text='tonkatsu2'
                ),
                MessageTemplateAction(
                    label='森井',
                    text='tonkatsu3'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_button_carousel(id):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://lh3.googleusercontent.com/N224Q4Rx1_TvTx9JtUkGzC2GsDEFfPMciR6Sd2k20m_cu00XQRbB0Jr2kw1ktpL35p7BhIjz1jY_hc55oIV1nIBjGMwiGnCZbghnnqvHAzNnSI9gDj8sQypKC7f5oanews9XQSzHXcA4zZKgLBWVKSjoEm-S1K90IhT6gdHOKfGQRfrAUqMyTM3qnf2huCc4xwzrpRbnQUHvGxFeOmYsLyq3Jm2PvZCqMxGThX5bZSUyDnuKFrB1kJvrWwIPM7NL4wUpqdTtYiCUs3SKNcb7506AnZbvVVGbSJGvDs75ZIrWoFDMFtL3sAUP5SbuFslLdpw5TCMoU5lQXAZY0P-doMVKu1uG2i5XCqfPS_HqrmIoUGOtkSlB9CHanaB69XkKKKnd2-ZA2jtR12neB74sVF7_4cVqpXqLW3T4YC5Sv5snqdYTa7fdu9CDzZZZc3dVA4Z8JiQE-Zbx4YI7EmLtvmO1w7ReOYSw77OjKqbBzUJtfbUl9qVALafGGiwVb4guHa7pRgobJ-bVZkFSFpj8lwooNG1seHilUDwmbFaw8086Fy4F3UERU1t7JFGy_IGYlaxlccSkGIRj2hq6TTDAcIr9WQohLNe-qHFAycpagOqLA5shEpNeVvZPKVTvrbp4wdOk98-ocl1xBu8E8mocMa9QPap7z7WwJpP8xuRjLqTPZW9AIB2Nxcd1RUb6jg=w678-h903-no?authuser=0',
                    title='餐廳推薦',
                    text='想吃什麼種類?',
                    actions=[
                        MessageTemplateAction(
                            label='美式',
                            text='diner'
                        ),
                        MessageTemplateAction(
                            label='泰式',
                            text='thai cuisine'
                        ),
                        MessageTemplateAction(
                            label='韓式',
                            text='korean cuisine'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://lh3.googleusercontent.com/RMKJCvhAgSPC_JwPrWkn5U9vPRplY1m-hLG892Dr9IPxsIJLBWwuhkPz4MUreayhZt0HOBVDAQEL4R5hS6IpQq9ZNpJkRhIYUiqrMxqOTl9nY223F4LA9GwVSh3AyJfIowgGS15buP00u3q6XMiYHfDtXiG0lOe1B78yoWOd5TO0Uzm8mDe_9ClaTo7B-Sd_YtpqaSHHY-wkVrjrBdWXK3Ri48Wq8MclkEPB3_fRbztSzUNkPqQXUBcrDthMTw0rcBPng9DboMRySdZc8im6N3vtSv5dGEIYh4_IO18wXGT_HB_DU-s31Nn9miwLwO1UMkkQQm-r6icFb9PnP6TKdF-Sev1TEexAUlMeVeTp2iwpufNNILBaAnQkb7EoulIZl2K5a9kbA63zwWBU0LWJG8v8RCAefI7QDPfEGHiVppVo6Hjg_meZlF2K9jMvtPIoWR5QdV-lkO--Gq18ApCDDfL0dI1qRhCrgVsjsDwqHhALu1x1u6EXiBO67XCIx2-ZQZcsZMnYD1KbHLeob4T409BPBw2FuVjKvbtts85T5d3MNeCC0GLmytF7MrQkmY_2YE95HSECk5lqj_aticvceo7KbBwcru03vSO-QIvMH4bDzo9a1IN-QINoyAQJn95e3di3_9NqfHVN7FbnUqgGxE7IGk6BWJKTkcOg6zGoPk0pE6OozN1GQfYpiw3QNg=w1204-h903-no?authuser=0',
                    title='餐廳推薦',
                    text='想吃什麼種類?',
                    actions=[
                        MessageTemplateAction(
                            label='日式',
                            text='japanese cuisine'
                        ),
                        MessageTemplateAction(
                            label='火鍋',
                            text='hotpot'
                        ),
                        MessageTemplateAction(
                            label='排隊美食',
                            text='tainan'
                        ),
                    ]
                )
            ]
        )
    )
    line_bot_api.push_message(id, message)

    return "OK"


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
