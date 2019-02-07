import time
from crontab import CronTab
import sys
import os

def main():
  cron_tabs = []

  # check whether username is provided or not as an argument
  # if not current user is considered
  if len(sys.argv) < 2:
    cron_tabs = CronTab(user=True)
  else:
    cron_tabs = CronTab(sys.argv[1])

  # check if any crontab is defined, if it is considered only
  # last one
  if len(cron_tabs) > 1:
    job = cron_tabs[-1]
  else:
    sys.exit(1) # no cron job is defined for the given user

  while True:
    job.run_pending()
    time.sleep(1)

if __name__ == '__main__':
  main()
