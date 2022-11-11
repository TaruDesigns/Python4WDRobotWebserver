from microdot import Microdot, send_file
from microdot_websocket import with_websocket

app = Microdot()


@app.route('/')
def index(request):
    return send_file('includes.html')


@app.route('/ws')
@with_websocket
def wsmotors(request, ws):
    while True:
        print("Got Websocket Data")
        data = ws.receive()
        print(data)
        ws.send(data)
     

print("Starting Server")
app.run(port=80)