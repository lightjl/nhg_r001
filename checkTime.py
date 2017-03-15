from datetime import *
from datetime import datetime,timedelta
import time

#print(datetime.now().hour)
def checkTime(hourBegin, hourEnd):
    if datetime.now().hour >= hourBegin and datetime.now().hour <= hourEnd:
        return True
    else:
        return False

#day = datetime.now() - timedelta(1)
#print(.weekday())
#print(datetime.now())
