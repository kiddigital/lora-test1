# lora-test1
First test project on LoRaWAN using a LoPy from Pycom

Add a file called 'myconfig.py' into a 'lib' subdirectory which should contain
the following:

```python
import binascii

cfg = {}
cfg['app_eui'] = binascii.unhexlify('<hexvalueofthe_app_eui>')
cfg['app_key'] = binascii.unhexlify('<hexvalueofthe_app_key>')
```

Fill in the info of your application and you should be good to go.
