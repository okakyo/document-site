from django.shortcuts import render,HttpResponse,redirect
from linebot import WebhookHandler

# キャッチアップ用のHTML
def index(request):
    return render(request,'index.html')

# 以下、ボットのシステムを構築 

def callback(request):
    if(method=="POST"):
        signature =  request.headers['X-Line-Signature']

    else:
        redirect('/')
        

def sayHello(request):
    if(request.method== "POST"):
        pass
    return json()

def sendCode(request):
    return HttpResponse(request.body)

