import time
import threading



def infinite_loop_func(): 

   print('Thread-t1:開始循環') 
   while 1: 

       if my_event.is_set(): 
           break 

       print('Thread-t1:從串列讀取') 

       time.sleep(1 ) 
   print(f'Thread-t1: my_event.is_set() = {my_event.is_set()}') 

t1 = threading.Thread(target =Infinity_loop_func) # 建立 t1 執行緒
t1.start()   
time.sleep(5) # wait 5秒
my_event.set() #設定5秒後的事件