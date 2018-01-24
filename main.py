from machine import Pin
#from machine import Timer

print('hello world')

led = Pin("G16", mode=Pin.OUT)

led(0)

#pycom.heartbeat(False)
#pycom.rgbled(0x003300)

#Timer.sleep_us(5000000)

import mylora

#pycom.rgbled(0x0)
led(1)
