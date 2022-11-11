python -m mpy_cross boot.py
ampy put boot.mpy
python -m mpy_cross main.py
ampy put .\main.mpy
ampy put .\settings.json
python -m mpy_cross webserver_microdot_ws.py
ampy put .\webserver_microdot_ws.mpy
ampy put .\htmljoysticks.html
python -m mpy_cross motorcontrol.py
ampy put .\motorcontrol.mpy
python -m mpy_cross servocontrol.py
ampy put .\servocontrol.mpy
python -m mpy_cross wlansettings.py
ampy put .\wlansettings.mpy 
::ampy put joy.js
::ampy put microdot.mpy
::ampy put microdot_websocket.mpy