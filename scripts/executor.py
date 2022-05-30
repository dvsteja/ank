from setuptools import Command
import crontab
from crontab import CronTab

cron = CronTab(user='root')

job = cron.new(command='python3 connvzn.py')
job.minute.every(1)
cron.write()

# if this fails execute it manually by adding below line to crontab -e [1]
# */1 * * * * /usr/bin/python3 /var/www/html/scripts/executor.py