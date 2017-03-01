#-*- coding: UTF-8 -*-

from flask import Flask, request
import os
import line_bot_controller

app = Flask(__name__)
line_token = os.environ.get('Line_Token', None)
line_bot_controller = line_bot_controller.LineController(line_token)

@app.route('/', methods=['GET'])
def index():
    return "<p>Hello World!</p>"

@app.route('/callback', methods=['POST'])
def callback():
    data_in = request.get_json(force=True)
    print data_in
    article = {}
    article['title'] = data_in['title']
    article['content'] = data_in['content']

    data = line_bot_controller.sendText(article)
    return data

if __name__ == '__main__':
    app.run()
