@REM python -m mpy_cross boot.py
@REM ampy rm boot.mpy
del main.mpy
python -m mpy_cross main.py
ampy rm main.mpy
del webserver_microdot_ws.mpy
python -m mpy_cross webserver_microdot_ws.py
ampy rm webserver_microdot_ws.mpy
del .\motorcontrol.mpy
python -m mpy_cross motorcontrol.py
ampy rm motorcontrol.mpy
@REM python -m mpy_cross servocontrol.py
@REM ampy rm servocontrol.mpy
@REM python -m mpy_cross wlansettings.py