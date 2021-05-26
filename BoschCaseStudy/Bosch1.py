from datetime import datetime, timedelta

if __name__ == '__main__':
    time = str(datetime.time(datetime.now().replace(microsecond=0)))
    print("Current Time :", end=" ")
    print(time)
    hh, mm, ss = map(int, time.split(':'))
    cr_time = timedelta(hours=hh, minutes=mm, seconds=ss)
    full_day = timedelta(hours=24, minutes=0, seconds=0)
    print("Percentage of the day :", end=" ")
    print(cr_time/full_day*100)
