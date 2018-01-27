from machine import Pin
import sys
import json
import os

print('hello world')

# Below asssumes you have an expansion board (tested with a Rev v2.1A)
led = Pin("G16", mode=Pin.OUT)

led(0)

import mylora

led(1)
