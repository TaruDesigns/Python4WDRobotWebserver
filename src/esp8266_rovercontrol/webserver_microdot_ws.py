from microdot import Microdot, send_file
from microdot_websocket import with_websocket
import gc
from time import sleep
from json import loads

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
    while True:
        try:
            # Catch exception since sometimes the connection is reset
            data = ws.receive() 
            print(data)
            dataObj = loads(data)
            if dataObj["type"] == "webrepl":
                stopserver(request)
            elif dataObj["type"] == "motors":
                motors.motors_analog(dataObj["speed"], dataObj["direction"])
            gc.collect()
        except:
            pass
        sleep(0.016)
  
@mainserver.route('/webrepl', methods=['GET', 'POST'])
def stopserver(request):
    #TODO Fix this
    print("Got Webrepl, stopping server") 
    request.app.shutdown()
    return 'The server is shutting down...'         

if __name__ == "__main__":
    mainserver.run(port=80)
