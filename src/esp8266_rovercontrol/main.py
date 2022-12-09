# Complete project details at https://RandomNerdTutorials.com
import json, gc

# Load settings
try:
  with open("settings.json") as f:
    config = json.load(f)
except:
  print("Cannot load JSON Config! Entering WebREPL")
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

print("Starting Webserver")
gc.collect()
from microdot import Microdot, send_file
from microdot_websocket import with_websocket
from time import sleep

mainserver = Microdot()

@mainserver.route('/')
def index(request):
    return send_file('static/htmljoysticks.html')

@mainserver.route('/static/<path:path>')
def static(request, path):
    if '..' in path:
        # directory traversal is not allowed
        return 'Not found', 404
    return send_file('static/' + path)

@mainserver.route('/wscontrol')
@with_websocket
def wsmotors(request, ws):
    print("Preparing WS")
    while True:
      try:
        # Catch exception since sometimes the connection is reset
        data = ws.receive() 
        print(data)
        dataObj = json.loads(data)
        if dataObj["type"] == "stopserver":
            stopserver(request)
        elif dataObj["type"] == "motors":
            motors.motors_analog(dataObj["speed"], dataObj["direction"])
        elif dataObj["type"] == "servos":
            servos.servo_handler(int(dataObj["x"]), int(dataObj["y"]))            
        gc.collect()
      except:
        pass
      sleep(0.016) # Loop timer, 60Hz
  
@mainserver.route('/stopserver', methods=['GET', 'POST'])
def stopserver(request):
    #TODO Fix this
    print("Stopping server") 
    request.app.shutdown()
    return 'The server is shutting down...'         

mainserver.run(port=5000)
