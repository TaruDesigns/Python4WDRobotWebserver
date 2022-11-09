try:
  import usocket as socket
except:
  import socket


from microdot import Microdot

mainserver = Microdot()

@mainserver.route('/motors/', methods=['POST'])
def index_motors(request):
    print("Got motors")
    print(request.form)

@mainserver.route('/servos/nod/', methods=['POST'])
def servos_nod(request):
    print("Got servos Nod") 
    print(request.form)

@mainserver.route('/servos/roll/', methods=['POST'])
def servos_roll(request):
    print("Got servos Roll") 
    print(request.form)    

@mainserver.route('/webrepl/', methods=['GET', 'POST'])
def index_servos(request):
    #TODO Fix this
    print("Got Webrepl") 
    import webrepl
    webrepl.start()

@mainserver.route('/')
def index(request):
    print("got index")
    with open('htmlbase.html') as f: 
      htmlbase = f.read()
      html = htmlbase    
    return html, 202, {'Content-Type': 'text/html'}     



