import time
import schedule

def display():
    print("lunch time !!")

def display2():
    print("wrap up work")

def main():
    schedule.every().day.at("13:00").do(display) 
    schedule.every().day.at("18:00").do(display2) 
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()           

