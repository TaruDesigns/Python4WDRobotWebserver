# Complete project details at https://RandomNerdTutorials.com
import json
import webrepl
from time import sleep_ms

# Load settings
try:
  with open("settings.json") as f:
    config = json.load(f)
except:
  print("Cannot load JSON Config! Entering WebREPL")
  webrepl.start()

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

# Initialize Webserver
from webserver import WebServer
server = WebServer(config, "Test")


while True:
  try:
    # Handle request
    endpoint, params = server.handle_connection()
    try:
      # TODO Add better error handling
      if "webrepl" in endpoint:
        # Break Loop to enter WebREPL
        break
      elif config["ENABLE_MOTORS"] and "motors" in endpoint:
        motors.motor_handler(params)
      elif config["ENABLE_SERVOS"] and "servos" in endpoint:
        servos.servo_handler(params)
    except Exception as e:
      #TODO Add better error handling
      print(e)
    #Serve webpage to client
    # TODO add the compass heading on screen
    # TODO Add CAM on the HTML
    server.serve_webpage()
  except Exception as e:
    print("Error main!")
    print(e)
    raise e

# If loop ends, start webrepl

webrepl.start()