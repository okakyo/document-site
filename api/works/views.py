from linebot import WebhookHandler,LineBotApi
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,)
from django.shortcuts import render, HttpResponse,redirect
from django.views.decorators.csrf import csrf_exempt
import json 
import os
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
        handler.handle(body, signature)
        return HttpResponse('OK', status=200)
    else: 
        return redirect('/')
