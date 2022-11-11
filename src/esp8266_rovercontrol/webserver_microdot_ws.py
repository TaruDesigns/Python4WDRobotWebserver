from microdot_asyncio import Microdot, send_file
from microdot_asyncio_websocket import with_websocket

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
async def wsmotors(request, ws):
    # while True:
        print("Got Websocket Data")
        data = await ws.receive()
        print(data)
        await ws.send(data)
     
@mainserver.route('/webrepl/', methods=['GET', 'POST'])
def stopserver(request):
    #TODO Fix this
    print("Got Webrepl, stopping server") 
    request.app.shutdown()
    return 'The server is shutting down...'         

print("Starting Server")
mainserver.run(port=80)