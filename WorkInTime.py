from datetime import *
from datetime import datetime,timedelta
import time
#timeBucket=[[时间起，时间止]，[时间点]*2]
#从小到大排序，不支持跨日
class WorkInTime():
    def __init__(self, timeBucket, addTime=46):    #工作时间段和冗余时间
        self.__time = timeBucket
        now = datetime.now()
        self.__timeType = [[time.mktime(time.strptime(str(now.year) + '-' + str(now.month) + '-' + str(now.day) +\
                            ' ' + i + ':00', '%Y-%m-%d %H:%M:%S')) for i in timeB] for timeB in self.__time[:]
                         ]

        self.__timeType233 = [[i for i in timeB] for timeB in self.__time[:]
                         ]
        self.addTime = addTime      #冗余时间
    def relax(self):
        timeNow = time.time()
        timeBucket = self.__timeType
        if (timeNow > timeBucket[-1][1]):      #大于一天终止时间
            sleepTime = round(timeBucket[-1][0] - timeNow + 24 * 60 * 60, 0)
            time.sleep(sleepTime+self.addTime)
        elif timeNow < timeBucket[0][0]:      #小于一天开始时间
                sleepTime = round(timeBucket[0][0] - timeNow)
                time.sleep(sleepTime + self.addTime)
        else:
            for i in range(len(timeBucket)-1)[::-1]:
                if (timeNow > timeBucket[i][1] and timeNow <= timeBucket[i+1][0]):
                    sleepTime = round(timeBucket[i+1][0]-timeNow)
                    time.sleep(sleepTime+self.addTime)


