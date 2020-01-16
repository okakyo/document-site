import os,json 

from linebot import WebhookHandler,LineBotApi
from linebot.models import (MessageEvent, TextMessage, TextSendMessage)
from linebot.exceptions import (InvalidSignatureError)

from django.shortcuts import render, HttpResponse,redirect
from django.http import HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


token=os.environ['YOUR_CHANNEL_ACCESS_TOKEN']
secret_key= os.environ['YOUR_CHANNEL_SECRET']

lineBot=LineBotApi(token)
handler = WebhookHandler(secret_key)


# キャッチアップ用のHTML
def index(request):
    return render(request,'index.html')

# 以下、ボットのシステムを構築 
@csrf_exempt
def callback(request):
    if(request.method=="POST"):
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            HttpResponseForbidden()
        return HttpResponse('OK', status=200)
    else: 
        return redirect('/')

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    lineBot.reply_message(event.reply_token,TextSendMessage(text=event.message.text))