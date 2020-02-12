import time
input("----Press Enter--- to start time ")

start_time=time.time()
input("----Press Enter--- to stop time ")
stop_time=time.time()
elapsed=stop_time-start_time
mins=elapsed//60
secs=elapsed%60
hours=mins//60
mins=mins%60
print("Time of Elapsed is {}:{}:{}".format(int(hours),int(mins),secs))
