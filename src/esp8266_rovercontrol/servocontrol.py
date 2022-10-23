
from machine import Pin, PWM

class ServoControl:
  """docstring for ServoControl."""
  def __init__(self, config:dict):
    print("Starting Servos...")
    self.servos = {}
    self.config = config
    self._init_servos()
    self._init_pwm_freqs()
    self.__duty_nod = 0
    self.__duty_roll = 0
    print("ServosStarted!")

  def reload_config(self, config:dict):
    """Reloads Config parameters and reassigns pins
    This will force all the motors to stop for a moment

    Args:
        config (dict): _description_
    """
    self.config = config
    self._init_servos()

  def _init_servos(self):
    self.servos['nod'] = PWM(Pin(self.config['GPIO_SERVO_NOD']))
    self.servos['roll'] = PWM(Pin(self.config['GPIO_SERVO_ROLL']))

  def _init_pwm_freqs(self):
    for s in self.servos:
      self.servos[s].freq(self.config["PWM_SERVO_FREQ"])  

  def servo_handler(self, params: dict):
    #TODO Angle-dutycycle conversion
    #TODO make this look better
    #TODO Implement "Speed"-> Run to desired location in multiple steps
    if 'nodSlider' in params:
      servo = self.servos['nod']
      angle = int(params["nodSlider"])
    elif 'rollSlider' in params:
      servo = self.servos['roll']
      angle = int(params["rollSlider"])
    print(servo)
    servo.duty(int(angle))