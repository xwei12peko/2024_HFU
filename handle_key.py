import os, sys

def get_secret_and_token():
    # https://github.com/line/line-bot-sdk-python/blob/master/examples/flask-echo/app_with_handler.py   #從此地拉的code
    # 1.先到LINE Developer Console，把Channel Secret & Channel Accsss Token複製起來
    # 2.把這兩個密文，存到環境變數內；工具列搜尋<環境變數>，新增兩個環境變數，並把值貼上去
    # 3.按下確定儲存，要記得變數名稱，這些資訊只會存在你當前使用的電腦裡
    # 4.透過以下程式碼，取得環境變數儲存的對應數值
    channel_secret = os.getenv('LINEBOT_SECRET_KEY', None)
    channel_access_token = os.getenv('LINEBOT_ACCESS_TOKEN', None)
    if channel_secret is None:
        print('Specify LINEBOT_SECRET_KEY as environment variable.')
        sys.exit(1)
    if channel_access_token is None:
        print('Specify LINEBOT_ACCESS_TOKEN as environment variable.')
        sys.exit(1)

    return {
        'LINEBOT_SECRET_KEY': channel_secret,
        'LINEBOT_ACCESS_TOKEN': channel_access_token
    } 