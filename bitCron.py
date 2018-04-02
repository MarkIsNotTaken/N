from crontab import CronTab


my_cron = CronTab(user = "Mark")
file_cron = CronTab(tabfile="bitcoinScrape.tab")
job = my_cron.new(command='python C:\Users\Student\Documents\GitHub\Network_Survival_Tools\webscrape.py')
job.hour.every(24)

my_cron.write()
