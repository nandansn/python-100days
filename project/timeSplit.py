

def time_splitter():
    start_time = float(input("Enter Start Time: "))
    end_time = float(input("End End Time: "))
    interval = float(input("Time Interval: "))
    total = 0
    while True:
        
        
        if start_time == end_time:
            
            break    
        print("{} to {} : {}".format(start_time, start_time + interval, int(interval)))
        start_time = start_time + interval
        total +=1
    print("total hours: {}".format(total))

time_splitter()