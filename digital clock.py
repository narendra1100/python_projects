hours=2
minuts=0
seconds=0
import time
from turtle import *
setup()
t=Turtle()
while True:
    t.clear()
    t.write(str(hours).zfill(2)+":"+str(minuts).zfill(2)+":"+str(seconds).zfill(2), font=("arial",30,"normal"))
    seconds=seconds+1
    time.sleep(1)
    if seconds==60:
        seconds=0
        minuts=minuts+1
    if minuts==60:
        minuts=0        
        hours=hours+1
    if hours==24:
        hour=0
        
