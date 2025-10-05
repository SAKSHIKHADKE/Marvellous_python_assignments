import time
import schedule
import datetime

def display():
        ret=open("marvellous.txt","a")

        ret.write(str(datetime.datetime.now()))

def main():
    schedule.every(5).minutes.do(display) 
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()           

