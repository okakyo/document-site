from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json 
import os
# Create your views here.

token=os.environ.get('YOUR_CHANNEL_ACCESS_TOKEN')
secret_key= os.environ.get('YOUR_CHANNEL_SECRET')

lineBot=line.LineBot(token,secret_key)
handler = WebhookHandler(secret_key)


@csrf_exempt
def index(request):
    if(request.method=="POST"):
        requestBody= json.loads(request.body.decode('utf-8'))
        events=requestBody['events']
        for event in events:
            
    return HttpResponse()