#-*- coding: UTF-8 -*-
from flask import request
import json

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

class LineController:
    def __init__(self, token, channel_secret):
        self.line_bot_api = LineBotApi(token)
        self.handler = WebhookHandler(channel_secret)
        pass

    def notification(self, title, content):
        # print title, content
        # with open('data/notify_list.json', 'r') as file:
        #     notify_list = json.load(file)
        # if len(notify_list) == 0:
        #     return False
        notify_list = ["Ue43669a8557190c6d91cf84c44a5902b"]
        
        content = "{}\n{}".format(title, content)
        self.line_bot_api.multicast(notify_list, TextSendMessage(text=content))
        return True

    def sendText(self, article):
        send_notify = self.notification(article['title'], article['content'])
        return 'OK'    

    def getMessage(self, article):
        @self.handler.add(MessageEvent, message=TextMessage)
        def handle_message(self, event):
            print("event.reply_token:", event.reply_token)
            print("event.message.text:", event.message.text)
            content = '[REPLY]' + event.message.text
            self.line_bot_api.reply_message(event.reply_token, TextSendMessage(text=content))
            return 0