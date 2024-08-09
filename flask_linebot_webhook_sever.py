from flask import (
    Flask,
    request,
    abort,
    render_template,
)
from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage                     # 傳輸回官方後台的資料格式
)
from linebot.v3.webhooks import (
    MessageEvent,                   # 傳輸過來的方法
    TextMessageContent              # 使用者傳輸過來的資料格式
)
from handle_key import get_secret_and_token

app = Flask(__name__)
keys = get_secret_and_token()
handler = WebhookHandler(keys['LINEBOT_SECRET_KEY'])
configuration = Configuration(access_token=keys['LINEBOT_ACCESS_TOKEN'])

@app.route("/") 
def say_hello_world(username=""):
    # 測試用，確定Webhook Server有連通
    return render_template("hello.html", name=username)

@app.route("/callback", methods=['POST'])
def callback():
    # 設計一個callback的路由器，提供給Line官方後台去呼叫
    # 也就是所謂的呼叫Webhook Sever
    # 因為官方會把使用者傳輸的訊息轉傳給Webhook Sever
    # 所以會使RESTful API的PORT方法
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    # 根據不同的使用者事件（event），用不同的方式回應
    # eg. MessageEvent 代表使用者單純傳訊息的事件
    # TextMessageContent 代表使用者傳輸的訊息內容是文字
    # 符合兩個條件的事件，會被handle_message 所處理
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[
                    TextMessage(text=event.message.text)
                ]
            )
        )

if __name__ == "__main__":
    app.run(debug=True) 