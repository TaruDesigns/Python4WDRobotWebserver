

from machine import Pin, PWM

class MotorControl:
  """docstring for MotorControl."""
  def __init__(self, config:dict):
    print("Starting motors...")
    self.motors = {}
    self.config = config
    self._init_motors()
    self._init_pwm_freqs()
    self._speed = ''
    self._direction = ''
    self.__duty_left_fw = 0
    self.__duty_left_bw = 0
    self.__duty_right_fw = 0
    self.__duty_right_bw = 0
    print("Motors Started!")

  def reload_config(self, config:dict):
    """Reloads Config parameters and reassigns pins
    This will force all the motors to stop for a moment

    Args:
        config (dict): _description_
    """
    self._motors_stop()
    self.config = config
    self._init_motors()

  def _init_motors(self):
    """Initialize Motors (PWM Objects)

    Args:
        config (dict): dict with all the GPIO pins

    Returns:
        motors: dict with all the motor objects
    """
    self.motors['LEFT_FW'] = PWM(Pin(self.config['GPIO_LEFT_FW']))
    self.motors['LEFT_BW'] = PWM(Pin(self.config['GPIO_LEFT_BW'])) 
    self.motors['RIGHT_FW'] = PWM(Pin(self.config['GPIO_RIGHT_FW'])) 
    self.motors['RIGHT_BW'] = PWM(Pin(self.config['GPIO_RIGHT_BW'])) 

  def _init_pwm_freqs(self):
    for m in self.motors:
      self.motors[m].freq(self.config["PWM_MOTOR_FREQ"]) 

  def motor_handler(self, params: dict):
    #TODO Switch to generic input using X-Y (Joystick style) input
    if params["direction"] == "stopall" or params["speed"] == "stopall":
      self._motors_stop()
    elif params["direction"] == "fw":
      self._motors_fw(params["speed"])
    elif params["direction"] == "bw":
      self._motors_bw(params["speed"])
    elif params["direction"] == "lt":
      self._motors_lt(params["speed"])
    elif params["direction"] == "rt":
      self._motors_rt(params["speed"])    

  def _motors_stop(self):
    self.motors['LEFT_FW'].duty(self.config["DUTYCYCLE_STOP"])
    self.motors['LEFT_BW'].duty(self.config["DUTYCYCLE_STOP"])
    self.motors['RIGHT_FW'].duty(self.config["DUTYCYCLE_STOP"])
    self.motors['RIGHT_BW'].duty(self.config["DUTYCYCLE_STOP"])

  def _motors_fw(self, speed:str):
    # Both sides going forwards
    if speed == "high":
      dutycycle = self.config["DUTYCYCLE_HIGH"]
    else:
      dutycycle = self.config["DUTYCYCLE_LOW"]
    self.motors['LEFT_FW'].duty(self.config["DUTYCYCLE_STOP"])
    self.motors['LEFT_BW'].duty(dutycycle)
    self.motors['RIGHT_FW'].duty(self.config["DUTYCYCLE_STOP"])
    self.motors['RIGHT_BW'].duty(dutycycle)

  def _motors_bw(self, speed:str):
    # Both sides going backwards
    if speed == "high":
      dutycycle = self.config["DUTYCYCLE_HIGH"]
    else:
      dutycycle = self.config["DUTYCYCLE_LOW"]   
    self.motors['LEFT_FW'].duty(dutycycle)
    self.motors['LEFT_BW'].duty(self.config["DUTYCYCLE_STOP"])
    self.motors['RIGHT_FW'].duty(dutycycle)
    self.motors['RIGHT_BW'].duty(self.config["DUTYCYCLE_STOP"])    

  def _motors_lt(self, speed:str):
    #Going left = Left side going backwards, right side going forwards
    if speed == "high":
      dutycycle = self.config["DUTYCYCLE_HIGH"]
    else:
      dutycycle = self.config["DUTYCYCLE_LOW"]  
    self.motors['LEFT_FW'].duty(dutycycle)
    self.motors['LEFT_BW'].duty(self.config["DUTYCYCLE_STOP"])
    self.motors['RIGHT_FW'].duty(self.config["DUTYCYCLE_STOP"])
    self.motors['RIGHT_BW'].duty(dutycycle)     

  def _motors_rt(self, speed:str):
    #Going right = right side going backwards, left side going forwards
    if speed == "high":
      dutycycle = self.config["DUTYCYCLE_HIGH"]
    else:
      dutycycle = self.config["DUTYCYCLE_LOW"]  
    self.motors['LEFT_FW'].duty(self.config["DUTYCYCLE_STOP"])
    self.motors['LEFT_BW'].duty(dutycycle)
    self.motors['RIGHT_FW'].duty(dutycycle)
    self.motors['RIGHT_BW'].duty(self.config["DUTYCYCLE_STOP"]) 