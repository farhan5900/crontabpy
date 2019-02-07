import time
from crontab import CronTab
import sys

uname = sys.argv[1]

users_cron = CronTab(user=uname)
job = users_cron[1]

while True:
  job.run_pending()
  time.sleep(1)
