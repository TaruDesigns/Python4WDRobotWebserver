ampy put .\settings.json
ampy put static
@REM python -m mpy_cross boot.py
@REM ampy rm boot.mpy
@REM ampy put boot.mpy
del main.mpy
ampy rm main.mpy
python -m mpy_cross main.py
ampy put .\main.mpy
del motorcontrol.mpy
python -m mpy_cross motorcontrol.py
ampy rm motorcontrol.mpy
ampy put .\motorcontrol.mpy
@REM python -m mpy_cross servocontrol.py
@REM ampy rm servocontrol.mpy
@REM ampy put .\servocontrol.mpy
@REM python -m mpy_cross wlansettings.py
@REM ampy put .\wlansettings.mpy 
::ampy put microdot.mpy
::ampy put microdot_websocket.mpy