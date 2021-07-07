from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

#---------------- self define module ----------------
import text_push as text_push


#---------------- end of define module ----------------

def text_reply_message(user_message):
    if(user_message == "test"):
        output_message = "This is a test."
    elif(user_message == "push"):
        text_push.text_push_message("This is a Push test.")
        output_message = "This is Push test reply."
    else:  
        output_message = user_message  

    return TextSendMessage(text=output_message)

def image_reply_message(user_message):
    if(user_message == "可樂"):
        output_message = ImageSendMessage(
            original_content_url = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fblog.xuite.net%2Fchungming01%2Ftwblog%2F106578814&psig=AOvVaw0JV7TR5GNy4349MN-bKgF0&ust=1625729867993000&source=images&cd=vfe&ved=0CAoQjRxqFwoTCIDOjtK80PECFQAAAAAdAAAAABAD"
            preview_image_url = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fblog.xuite.net%2Fchungming01%2Ftwblog%2F106578814&psig=AOvVaw0JV7TR5GNy4349MN-bKgF0&ust=1625729867993000&source=images&cd=vfe&ved=0CAoQjRxqFwoTCIDOjtK80PECFQAAAAAdAAAAABAD"
        )