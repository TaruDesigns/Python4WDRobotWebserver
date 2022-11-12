# Complete project details at https://RandomNerdTutorials.com
import json, gc
import webrepl
from time import sleep_ms

# Load settings
try:
  with open("settings.json") as f:
    config = json.load(f)
except:
  print("Cannot load JSON Config! Entering WebREPL")
  webrepl.start()
  raise("Cannot load JSON Config! Entering WebREPL")

# Initialize Peripherals
if config["ENABLE_MOTORS"]:
  from motorcontrol import MotorControl
  motors = MotorControl(config)
if config["ENABLE_SERVOS"]:
  from servocontrol import ServoControl
  servos = ServoControl(config)
if config["ENABLE_COMPASS"]: 
  from compasscontrol import CompassControl
  compass = CompassControl(config)

if config["ENABLE_WS"]:
  from webserver_microdot_ws import mainserver
else:
  from webserver_microdot import mainserver

print("Starting Webserver")
gc.collect()
mainserver.run(port=80)
print("This is after AppRun")

# If loop ends, start webrepl

webrepl.start()