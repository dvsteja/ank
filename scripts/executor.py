from setuptools import Command
import crontab
from crontab import CronTab

cron = CronTab(user='root')

job = cron.new(command='python connvzn.py')
job.minute.every(1)
cron.write()
