import schedule
import time
def job():
    now = time.localtime()
    print("current time = ", str(now))

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)