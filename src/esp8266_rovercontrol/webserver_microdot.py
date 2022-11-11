try:
  import usocket as socket
except:
  import socket


from microdot import Microdot

mainserver = Microdot()

@mainserver.route('/motors/', methods=['POST'])
def motors(request):
    print("Got motors")
    print(request.form)
    return "OK", 202

@mainserver.route('/servos/<joint>/<value>', methods=['POST'])
def servos(request, joint, value):
    print("Got servos: " + joint + value) 
    return "OK", 203

@mainserver.route('/webrepl/', methods=['GET', 'POST'])
def index_servos(request):
    #TODO Fix this
    print("Got Webrepl, stopping server") 
    request.app.shutdown()
    return 'The server is shutting down...'    

@mainserver.route('/')
def index(request):
    print("got index")
    with open('htmlbasic.html') as f: 
      htmlbase = f.read()
      html = htmlbase    
    return html, 202, {'Content-Type': 'text/html'}     



