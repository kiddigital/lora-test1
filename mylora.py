import binascii
import pycom
import socket
import time
from network import LoRa

import myconfig

# Colors
off = 0x000000
red = 0x330000
green = 0x003300
blue = 0x000033

# Turn off hearbeat LED
pycom.heartbeat(False)

# Initialize LoRaWAN radio
lora = LoRa(mode=LoRa.LORAWAN)

# Print Dev EUI of your device (handy to register your device :)
print(binascii.hexlify(lora.mac()).upper().decode('utf-8'))

# Set network keys
app_eui = myconfig.cfg['app_eui']
app_key = myconfig.cfg['app_key']

# Join the network
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0, dr=0)
pycom.rgbled(red)

print(lora.compliance_test())

# Loop until joined
while not lora.has_joined():
    print('Not joined yet...')
    pycom.rgbled(off)
    time.sleep(2.5)
    pycom.rgbled(red)
    time.sleep(2.5)

print('Joined')
pycom.rgbled(blue)

print(lora.compliance_test())

s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
s.setblocking(True)

i = 0
while i < 10:
    data = 'Hello World %s' % i

    pycom.rgbled(blue)
    count = s.send(data.encode('UTF-8'))
    print('Sent %s bytes' % count)

    pycom.rgbled(green)
    #time.sleep(3.0)
    s.settimeout(3.0) # configure a timeout value of 3 seconds
    try:
        answer = s.recv(64)   # get the packet received (if any)
        print(answer)
    except socket.timeout:
        print('No packet received')

    pycom.rgbled(blue)
    print(lora.stats())
    time.sleep(3)
    i += 1

print('Done')

pycom.rgbled(off)
