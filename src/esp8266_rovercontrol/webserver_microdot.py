from microdot import Microdot, send_file

mainserver = Microdot()

@mainserver.route('/motors', methods=['POST'])
def motors(request):
    print("Got motors")
    print(request.json)
    return "OK", 202

@mainserver.route('/servos', methods=['POST'])
def servos(request):
    print("Got servos:")
    print(request.json) 
    return "OK", 203

@mainserver.route('/webrepl/', methods=['GET', 'POST'])
def webrepl(request):
    print("Got Webrepl, stopping server") 
    request.app.shutdown()
    return 'The server is shutting down...'    

@mainserver.route('/static/<path:path>')
def static(request, path):
    if '..' in path:
        # directory traversal is not allowed
        return 'Not found', 404
    return send_file('static/' + path)    

@mainserver.route('/')
def index(request):
    print("got index")
    return send_file('static/htmljoysticksrest.html')



