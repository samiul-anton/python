from django.shortcuts import render
from django.http import HttpResponse
import psutil
import time
from time import localtime, strftime
import json
import asyncio
import websockets
import server


def home(request):
    start_server = websockets.serve(server.hello)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
    return render(request, 'server/dashboard.html')
