#!/usr/bin/python3

import requests
import pickle
import json
import time
import platform
import os

f=open("./config.json")
conf=f.read()
f.close()
cfg=json.loads(conf)
_hash=[]
now_env=platform.platform()

def Receive():
    roomid=cfg['Roomid']
    url_api='https://api.live.bilibili.com/xlive/web-room/v1/dM/gethistory?roomid={}'.format(roomid)
    r=requests.get(url_api)
    dat=json.loads(r.text)
    for i in range(10):
        barrage=dat['data']['room'][i]
        barrage_hash=pickle.dumps(barrage)
        if barrage_hash in _hash:
            continue
        print(barrage['nickname']+': '+barrage['text'])
        _hash.append(barrage_hash)

def Clear_Screen():
    if "Windows" in now_env:
        os.system("cls")
    else:
        os.system("clear")

Clear_Screen()
while 1:
    Receive()
    time.sleep(3)