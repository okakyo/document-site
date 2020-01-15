from django.shortcuts import render,HttpResponse,


# キャッチアップ用のHTML
def index(request):
    return render(request,'index.html')

# 以下、ボットのシステムをc構築 
def sayHello(request):
    return json()

def sendCode(request):
    return HttpResponse(request.body)

