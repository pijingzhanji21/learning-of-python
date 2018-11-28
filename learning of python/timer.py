'''定时器触发多线程'''
import schedule
import time
import threading
def job():
    print('this is job')
    time.sleep(2)
    print('the job is done')
def job1():
    print('this is job1')
    time.sleep(1)
    print('the job1 is done')

def run_threading(func):
    t=threading.Thread(target=func,)
    t.start()
schedule.every(1).second.do(run_threading,job)
schedule.every(1).second.do(run_threading,job1)
while 1:
    schedule.run_pending()
