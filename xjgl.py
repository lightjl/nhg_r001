import json
import requests
from datetime import *
import time
import sendMail
import checkTime

class Xjgl(object):
    __highIn = 0

    def __init__(self, highIn):
        self.__highIn = highIn
    pass

    def WatchXjgl(self):
        sendString = ''
        check_seesion = requests.Session()
        url = 'https://www.jisilu.cn/data/repo/sz_repo_list/?___t=1489544161142'
        xjglInfo = check_seesion.get(url)
        #print(xjglInfo.content.decode())
        jsonXjgl = json.loads(xjglInfo.content.decode())
        i = 0
        #for row in jsonXjgl['rows']:
        row = jsonXjgl['rows'][0]
        print(row)
        rowHigh = float(row['cell']['high'])
        if rowHigh > self.__highIn:    #新高超过前基准
            sub = '逆回购: ' + row['id'] + ' 破 ' + str(self.__highIn) + ', 现价: ' + row['cell']['price']
            self.__highIn = max(self.__highIn * 1.3, rowHigh)
            print(sub)
            sendMail.sendMail(sub, sub)

xjglWatch = Xjgl(6)
while True:
    outTime = ['9:30', '11:30', '13:00', '15:00']
    now = datetime.now()
    outTimeType = [time.mktime(time.strptime(str(now.year) + '-' + str(now.month) + '-' + str(now.day) + \
                   ' ' + i + ':00', '%Y-%m-%d %H:%M:%S')) for i in outTime]

    if datetime.now().weekday() < 5:
        print(datetime.now())
        timeNow = time.time()
        if timeNow > outTimeType[3]:    #停市后
            sleepTime = round(outTimeType[0]-timeNow+24*60*60,0)
            print(sleepTime)
            time.sleep(sleepTime)
        elif timeNow > outTimeType[1] and timeNow < outTimeType[2]:
            #休市期间
            sleepTime = round(outTimeType[2]-timeNow)
            print(sleepTime)
            time.sleep(sleepTime)

        if checkTime.checkTime(9,14):
            xjglWatch.WatchXjgl()
        time.sleep(60)

