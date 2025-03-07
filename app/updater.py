from apscheduler.schedulers.background import BackgroundScheduler
from app.parser import update_currency_rates

scheduler = BackgroundScheduler()
scheduler.add_job(update_currency_rates, "interval", hours=1)
scheduler.start()
