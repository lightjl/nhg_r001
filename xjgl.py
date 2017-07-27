from sys import path
path.append(r'D:\zzz\joinquant\sendEmail')
path.append(r'D:\zzz\joinquant\WorkInTime')
import json
import requests
from datetime import *
import time
import sendMail
import WorkInTime

class Xjgl(object):
    __highIn = 0

    def __init__(self, highIn):
        self.__highIn = highIn
        self.__initHigh = highIn

    def reset(self):
        self.__highIn = self.__initHigh

    def WatchXjgl(self):
        sendString = ''
        try:
            check_seesion = requests.Session()
            url = 'https://www.jisilu.cn/data/repo/sz_repo_list/?___t=1489544161142'
            xjglInfo = check_seesion.get(url)
            #print(xjglInfo.content.decode())
            jsonXjgl = json.loads(xjglInfo.content.decode())
        except:
            return
        i = 0
        #for row in jsonXjgl['rows']:
        row = jsonXjgl['rows'][0]
        #print(row)
        rowHigh = float(row['cell']['daily_profit2'])
        if rowHigh > self.__highIn:    #新高超过前基准
            sub = '逆回购: ' + row['id'] + ' 破 ' + str(self.__highIn) + ', 现日年化: ' + row['cell']['daily_profit2']
            self.__highIn = max(self.__highIn * 1.3, rowHigh)
            print(sub)
            #sendMail.sendMail(sub, "")

xjglWatch = Xjgl(4)
now = datetime.now()
nowDay = now.day

print("现金管理正在运行")
timeTrade = [['9:29', '11:30'], ['13:00', '15:00']]
workTime = WorkInTime.WorkInTime(timeTrade)
while True:
    if now.weekday() < 5:
        if workTime.isNewDay():
            xjglWatch.reset()
        #print(datetime.now())
        xjglWatch.WatchXjgl()
        workTime.relax()

