import requests


BASE_API_URL="" # ベースURL 

class LineBot(object):
    def __init__(self,token,secret_key):
        self.lineToken=token
        self.secret_key=secret_key
        self.header= {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
    def __call__(self,message):

        pass
    def __baseApi(): # 基本的な送信データ
        pass

    # 以下、Bot のシステム
    def sendMessage(): # Clasify  message, Image, Movie message etc ...  
        pass
    def replyMessage():# Send the baseMent API 
        pass