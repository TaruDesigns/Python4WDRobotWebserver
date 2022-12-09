# Initially based on GPIO Webserver from https://RandomNerdTutorials.com
import network
from wlansettings import *
print('Starting ESP....')

import esp
esp.osdebug(None)

import gc
gc.collect()

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())