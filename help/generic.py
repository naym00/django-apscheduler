from datetime import datetime, date, timedelta

class Generic:
    def getDateTimeNow(self):
        now = datetime.now()
        print('Run on a specific time interval ', now)
        return now
    
    def dateTimeNow(self):
        now = datetime.now()
        print('Run on a specific datetime ', now)
        return now