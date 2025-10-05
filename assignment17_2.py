import time
import schedule
import datetime

def display():
    print("current time:",datetime.datetime.now())

def main():
    schedule.every(1).minute.do(display) 
    print("program is at waiting state...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()           

