#Your Code for making a basic stopwatch using 2 Push Button
from machine import Pin
import time
import random

pb = Pin(32, Pin.IN,Pin.PULL_UP)
pb1 = Pin(18, Pin.IN, Pin.PULL_UP)
led = Pin(25, Pin.OUT)

x = None
x1 = None

while True:
    pb_val = pb.value()
    pb1_val = pb1.value()

    
    led.on()
    time.sleep(0.1)
    led.off()
    time.sleep(0.1)
    
    if pb_val ==0:
        led.on()
        time.sleep(2)
        led.off()
        
            
        r = random.randint(1,5)
        time.sleep(r)
        led.on()
        x = time.ticks_ms()

        while pb.value()==1:
            pass
            x1 = time.ticks_ms()
            time.sleep(0.1)
            
            
        elapsedtime = time.ticks_diff(x1,x)
        print("Reaction Time!:", elapsedtime)
        led.off()
        time.sleep(0.1)
        
            
        time.sleep(5)
            
        
        
      
                
        
    
    
    
    
