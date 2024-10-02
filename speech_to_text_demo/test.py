import time
import threading

times = time.time()

print(times)

print("Start : %s" % time.ctime())
time.sleep (3)
print("End : %s" % time.ctime())