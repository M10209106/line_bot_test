#-*- coding: UTF-8 -*-

from flask import Flask, request
import os
import line_bot_controller

app = Flask(__name__)
line_token = os.environ.get('Line_Token', None)
channel_secret = os.environ.get('Channel_Secret', None)
line_bot_controller = line_bot_controller.LineController(line_token, channel_secret)


@app.route('/', methods=['GET'])
def index():
    return "<p>Hello World!</p>"


@app.route('/send_message', methods=['POST'])
def send_message():
    data_in = request.get_json(force=True)
    print data_in
    article = {}
    article['title'] = data_in['title']
    article['content'] = data_in['content']

    data = line_bot_controller.sendText(article)
    return data


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # print("body:",body)
    
    try:
        line_bot_controller.handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

if __name__ == '__main__':
    app.run()
