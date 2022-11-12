from microdot import Microdot, send_file
from microdot_websocket import with_websocket
import gc
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
    while True:
        try:
            data = ws.receive() 
            print(data)
            gc.collect()
        except:
            pass
        sleep(0.016)
     
@mainserver.route('/webrepl/', methods=['GET', 'POST'])
def stopserver(request):
    #TODO Fix this
    print("Got Webrepl, stopping server") 
    request.app.shutdown()
    return 'The server is shutting down...'         

if __name__ == "__main__":
    mainserver.run(port=80)
