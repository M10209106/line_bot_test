#-*- coding: UTF-8 -*-
import requests
import re
import os
import random
from bs4 import BeautifulSoup
from collections import defaultdict
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)
line_token = os.environ.get('Line_Token', None)
channel_secret = os.environ.get('Channel_Secret', None)
signature_test = ''

line_bot_api = LineBotApi(line_token)
handler = WebhookHandler(channel_secret)

@app.route('/', methods=['GET'])
def index():
    return "<p>Hello World!</p>"
    

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    signature_test = signature
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    content = type(signature_test).__name__
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=content))
    return 0


if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0', port=5566, debug=True)