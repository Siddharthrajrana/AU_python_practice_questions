#Question : To show Count down of time 
import time
 
sec = 60

print("Count Down Starts ")
while(sec!=0):
    print(sec)
    time.sleep(1)# Sleep for 1 seconds
    sec=sec-1


print("Exam is over !")