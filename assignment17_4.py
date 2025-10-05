import time
import schedule

def display():
    print("namaskar")

def main():
    schedule.every().day.at("09:00").do(display) 
    print("program is at waiting state...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()           

