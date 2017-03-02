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

    def replyText(self, event):
        content = "{}\n{}".format(type(event.source), event.message.text)
        self.line_bot_api.reply_message(event.reply_token, TextSendMessage(text=str(content)))
        return 'OK'