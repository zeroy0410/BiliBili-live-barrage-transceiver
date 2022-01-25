#!/usr/bin/python3

import requests
import pickle
import json

f=open("./config.json")
conf=f.read()
f.close()
cfg=json.loads(conf)
_hash=[]
lis=[]
def Receive():
    roomid=cfg['Roomid']
    url_api='https://api.live.bilibili.com/xlive/web-room/v1/dM/gethistory?roomid={}'.format(roomid)
    r=requests.get(url_api)
    dat=json.loads(r.text)
    for barrage in dat['data']['room']:
        barrage_hash=pickle.dumps(barrage)
        if barrage_hash in _hash:
            continue
        _hash.append(barrage_hash)
        lis.append(barrage['nickname']+': '+barrage['text'])
    return lis
