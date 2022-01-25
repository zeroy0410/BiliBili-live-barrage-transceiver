#!/usr/bin/python3

import requests
import json
import platform
import os

f=open("./config.json")
conf=f.read()
f.close()
cfg=json.loads(conf)
now_env=platform.platform()

def Send(s):
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
        return "Sent successfully"
    else:
    	return r.text