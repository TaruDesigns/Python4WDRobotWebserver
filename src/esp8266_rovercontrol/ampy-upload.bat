@REM python -m mpy_cross boot.py
@REM ampy put boot.mpy
@REM python -m mpy_cross main.py
@REM ampy put .\main.mpy
@REM ampy put .\settings.json
python -m mpy_cross webserver_microdot_ws.py
ampy put .\webserver_microdot_ws.mpy
@REM ampy put .\htmljoysticks.html
@REM python -m mpy_cross motorcontrol.py
@REM ampy put .\motorcontrol.mpy
@REM python -m mpy_cross servocontrol.py
@REM ampy put .\servocontrol.mpy
@REM python -m mpy_cross wlansettings.py
@REM ampy put .\wlansettings.mpy 
::ampy put joy.js
::ampy put microdot.mpy
::ampy put microdot_websocket.mpy