import time
import schedule

def display():
    print("checking email..")

def main():
    schedule.every(10).seconds.do(display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()           

