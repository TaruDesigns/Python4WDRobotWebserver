@REM ampy put .\settings.json
@REM ampy put static

@REM del boot.mpy
@REM ampy rm boot.mpy
@REM timeout 1
@REM python -m mpy_cross boot.py
@REM timeout 3
@REM ampy put boot.mpy

del main.mpy
ampy rm main.mpy
timeout 1
python -m mpy_cross main.py
timeout 3
ampy put .\main.mpy
ampy put main.py


@REM del helpers.mpy
@REM ampy rm helpers.mpy
@REM timeout 1
@REM python -m mpy_cross helpers.py
@REM timeout 3
@REM ampy put .\helpers.mpy

del motorcontrol.mpy
ampy rm motorcontrol.mpy
timeout 1
python -m mpy_cross motorcontrol.py
timeout 3
ampy put .\motorcontrol.mpy

del servocontrol.mpy
ampy rm servocontrol.mpy
timeout 1
python -m mpy_cross servocontrol.py
timeout 3
ampy put .\servocontrol.mpy

@REM del wlansettings.mpy
@REM ampy rm wlansettings.mpy
@REM timeout 1
@REM python -m mpy_cross wlansettings.py
@REM timeout 3
@REM ampy put .\wlansettings.mpy 
::ampy put microdot.mpy
::ampy put microdot_websocket.mpy