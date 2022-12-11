ampy put .\settings.json
@REM ampy put static

@REM del boot.mpy
@REM ampy rm boot.mpy
@REM timeout 1
@REM python -m mpy_cross boot.py
@REM timeout 2
@REM ampy put boot.mpy

del main.mpy
ampy rm main.mpy
timeout 1
python -m mpy_cross main.py
timeout 2
ampy put .\main.mpy
ampy put main.py


@REM del helpers.mpy
@REM ampy rm helpers.mpy
@REM timeout 1
@REM python -m mpy_cross helpers.py
@REM timeout 2
@REM ampy put .\helpers.mpy

@REM del motorcontrol.mpy
@REM ampy rm motorcontrol.mpy
@REM timeout 1
@REM python -m mpy_cross motorcontrol.py
@REM timeout 2
@REM ampy put .\motorcontrol.mpy

@REM del servocontrol.mpy
@REM ampy rm servocontrol.mpy
@REM timeout 1
@REM python -m mpy_cross servocontrol.py
@REM timeout 2
@REM ampy put .\servocontrol.mpy

del hmc5883l.mpy
ampy rm hmc5883l.mpy
timeout 1
python -m mpy_cross hmc5883l.py
timeout 2
ampy put .\hmc5883l.mpy

del compasscontrol.mpy
ampy rm compasscontrol.mpy
timeout 1
python -m mpy_cross compasscontrol.py
timeout 2
ampy put .\compasscontrol.mpy




@REM del wlansettings.mpy
@REM ampy rm wlansettings.mpy
@REM timeout 1
@REM python -m mpy_cross wlansettings.py
@REM timeout 2
@REM ampy put .\wlansettings.mpy 
::ampy put microdot.mpy
::ampy put microdot_websocket.mpy