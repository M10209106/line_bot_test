#-*- coding: UTF-8 -*-
from flask import request, abort
from linebot import LineBotApi
from linebot.models import *
import json


class LineController:
    def __init__(self, token):
        self.line_bot_api = LineBotApi(token)
        pass

    def notification(self, title, content):
        with open('data/notify_list.json', 'r') as file:
            notify_list = json.load(file)
        if len(notify_list) == 0:
            return False
        
        content = title + "\n" + content
        self.line_bot_api.multicast(notify_list, TextSendMessage(text=content))
        return True

    def sendText(self, article):
        send_notify = self.notification(article['title'], article['content'])
        return 'OK'    

    def replyText(self, event):
        content = event.source.user_id + "\n" + event.message.text
        self.line_bot_api.reply_message(event.reply_token, TextSendMessage(text=str(content)))
        return 'OK'