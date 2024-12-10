from apscheduler.schedulers.background import BackgroundScheduler
from help.generic import Generic as G

def start():
	scheduler = BackgroundScheduler()
	scheduler.add_job(G().getDateTimeNow, 'interval', seconds=5)
	scheduler.start()