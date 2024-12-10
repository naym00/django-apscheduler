from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from help.generic import Generic as G

def start():
	scheduler = BackgroundScheduler()
	scheduler.add_job(G().dateTimeNow, 'date', run_date=datetime(2024, 12, 10, 13, 13, 0))
	scheduler.start()