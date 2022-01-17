#!/usr/bin/python3

import requests
import pickle
import json
import time
import platform
import os
from inputimeout import inputimeout, TimeoutOccurred

f=open("./config.json")
conf=f.read()
f.close()
cfg=json.loads(conf)
_hash=[]
now_env=platform.platform()
scr=[]
op='c'

def Send():
    url = "https://api.live.bilibili.com/msg/send"
    headers={
        "Host": "api.live.bilibili.com",
        "Cookie": cfg['Cookie'],
        "Content-Length": "976",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
        "Sec-Ch-Ua-Platform": "Linux",
        #"Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryBOBZrWcfQvq74DSN",
        #"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept": "*/*",
        "Origin": "https://live.bilibili.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://live.bilibili.com/24005500?visit_id=7bbizwdw3e80",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    s=input("Please input the barrage you want to send: ")
    data={
        "bubble":"0",
        "msg":s,
        "color":"16777215",
        "mode":"1",
        "fontsize":"25",
        "rnd":"1642322875",
        "roomid":"24005500",
        "csrf":cfg['csrf'],
        "csrf_token":cfg['csrf_token']
    }
    r=requests.post(url,headers=headers,data=data)
    sta=json.loads(r.text)
    if sta['code']==0:
        print("Sent successfully")
    else:
    	print(r.text)

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
        scr.append(barrage['nickname']+': '+barrage['text'])
        _hash.append(barrage_hash)
    for i in scr:
        print(i)

def Clear_Screen():
    if "Windows" in now_env:
        os.system("cls")
    else:
        os.system("clear")

while 1:
    Clear_Screen()
    Receive()
    op='c'
    try:
        op=inputimeout(prompt='>>',timeout=5)
    except TimeoutOccurred:
            pass
    if op=='i':
        Send()
        time.sleep(2)
    elif op=='c':
        continue
    else:
        break