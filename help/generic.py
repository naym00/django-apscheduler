from datetime import datetime, date, timedelta

class Generic:
    def getDateTimeNow(self):
        now = datetime.now()
        print(now)
        return now