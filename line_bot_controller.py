#-*- coding: UTF-8 -*-

from flask import request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

import json

class LineController:
    def __init__(self, token):
        self.line_bot_api = LineBotApi(token)
        pass

    def notification(self, title, content):
        print title, content
        with open('data/notify_list.json', 'r') as file:
            notify_list = json.load(file)
        if len(notify_list) == 0:
            return False
        
        content = "{}\n{}".format(title, content)
        self.line_bot_api.multicast(notify_list, TextSendMessage(text=content))
        return True

    def sendText(self, article):
        send_notify = self.notification(article['title'], article['content'])
        return 'OK'