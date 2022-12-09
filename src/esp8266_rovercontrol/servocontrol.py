
from machine import Pin, PWM
from helpers import map

class ServoControl:
  """docstring for ServoControl."""
  def __init__(self, config:dict):
    print("Starting Servos...")
    self.servos = {}
    self.config = config
    self._init_servos()
    self._init_pwm_freqs()
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
    self.servos['NOD'] = PWM(Pin(self.config['GPIO_SERVO_NOD']))
    self.servos['ROLL'] = PWM(Pin(self.config['GPIO_SERVO_ROLL']))

  def _init_pwm_freqs(self):
    for s in self.servos:
      self.servos[s].freq(self.config["PWM_SERVO_FREQ"])  

  def servo_handler(self, x: int, y: int):
    """Moves the servos to the correct position.
    'X' will map to 'Roll', 'Y' will map to 'Nod'
    Args:
        params (dict): Dict with x and y parameters.
    """
    #TODO Implement "Speed"-> Run to desired location in multiple steps to avoid jerking motions
    print("Mapping Servos...")
    rollscaled = map(x, -100, 100, self.config["SERVO_ROLL_DUTYCYCLE_MIN"], self.config["SERVO_ROLL_DUTYCYCLE_MAX"])
    nodscaled = map(y, -100, 100, self.config["SERVO_NOD_DUTYCYCLE_MIN"], self.config["SERVO_NOD_DUTYCYCLE_MAX"])
    print("Roll: " + str(rollscaled) + " Nod: " + str(nodscaled))
    self.servos['NOD'].duty(nodscaled)
    self.servos['ROLL'].duty(rollscaled)
    print("Servos moved")