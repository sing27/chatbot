import time
import threading


X = 5
time_started = time.time()
running = True


def never_stop():
    global time_started, running
    time_check = 0
    while running:
        if time.time() > time_started + X:
            print("time up")
            time_started = time.time()
            continue  # or raise TimeoutException()
        print (time_check) # do whatever you need to do
        time.sleep(1)
        time_check += 1

t1 = threading.Thread(target=never_stop)
#t1.start()

def handle_conversation():
    global time_started, running

    t1.start()
    while True:
        user_input = input("User: ")        
        time_started = time.time()
        print("reset time")

if __name__ =="__main__":
    handle_conversation()


