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

  def _motors_stop(self):
    self.motors['LEFT_FW'].duty(self.config["DUTYCYCLE_STOP"])
    self.motors['LEFT_BW'].duty(self.config["DUTYCYCLE_STOP"])
    self.motors['RIGHT_FW'].duty(self.config["DUTYCYCLE_STOP"])
    self.motors['RIGHT_BW'].duty(self.config["DUTYCYCLE_STOP"])

  def update_speeds(self, left_fw, left_bw, right_fw, right_bw):
    self.__duty_left_fw = left_fw
    self.__duty_left_bw = left_bw
    self.__duty_right_fw = right_fw
    self.__duty_right_bw = right_bw

    print("LEFT FW " + str(left_fw))
    print("LEFT BW " + str(left_bw))
    print("RIGHT FW " + str(right_fw))    
    print("RIGHT BW " + str(right_bw))

    self.motors['LEFT_FW'].duty(self.__duty_left_fw)
    self.motors['LEFT_BW'].duty(self.__duty_left_bw)
    self.motors['RIGHT_FW'].duty(self.__duty_right_fw)
    self.motors['RIGHT_BW'].duty(self.__duty_right_bw)    


  def motors_analog(self, speed:int, direction:str):
    #Get scaled value
    speedscaled = self._map(speed, 0, 100, self.config["MOTOR_DUTYCYCLE_MIN"], self.config["MOTOR_DUTYCYCLE_MAX"])
    if direction == "C":
        #Deadzone
        self.update_speeds(self.config["MOTOR_DUTYCYCLE_MIN"], self.config["MOTOR_DUTYCYCLE_MIN"], self.config["MOTOR_DUTYCYCLE_MIN"], self.config["MOTOR_DUTYCYCLE_MIN"])
        pass
    elif direction == "N":
        #LEFT FW and RIGHT FW proportional to speed
        self.update_speeds(speedscaled, self.config["MOTOR_DUTYCYCLE_MIN"], speedscaled, self.config["MOTOR_DUTYCYCLE_MIN"])
    elif direction == "NE":
        # LEFT FW scaled speed, RIGHT FW scaledspeed/2
        self.update_speeds(speedscaled, self.config["MOTOR_DUTYCYCLE_MIN"], speedscaled//2, self.config["MOTOR_DUTYCYCLE_MIN"])
        pass
    elif direction == "NW":
        # LEFT FW scaled speed/2, RIGHT FW scaledspeed
        self.update_speeds(speedscaled//2, self.config["MOTOR_DUTYCYCLE_MIN"], speedscaled, self.config["MOTOR_DUTYCYCLE_MIN"])
        pass
    elif direction == "S":
        # LEFT BW and RIGHT BW scaled speed
        self.update_speeds(self.config["MOTOR_DUTYCYCLE_MIN"],speedscaled, self.config["MOTOR_DUTYCYCLE_MIN"], speedscaled)        
        pass
    elif direction == "SE":
        # LEFT BW scaledspeed and RIGHT BW scaled speed/2
        self.update_speeds(self.config["MOTOR_DUTYCYCLE_MIN"],speedscaled, self.config["MOTOR_DUTYCYCLE_MIN"], speedscaled//2)    
        pass
    elif direction == "SW":
        # LEFT BW scaledspeed/2 and RIGHT BW scaled speed
        self.update_speeds(self.config["MOTOR_DUTYCYCLE_MIN"],speedscaled//2, self.config["MOTOR_DUTYCYCLE_MIN"], speedscaled)          
        pass
    elif direction == "E":
        # LEFT BW and RIGHT FW scaled speed
        self.update_speeds(speedscaled, self.config["MOTOR_DUTYCYCLE_MIN"], self.config["MOTOR_DUTYCYCLE_MIN"], speedscaled)   
        pass
    elif direction == "W":
        # LEFT FW and RIGHT BW scaled speed
        self.update_speeds(self.config["MOTOR_DUTYCYCLE_MIN"], speedscaled, speedscaled, self.config["MOTOR_DUTYCYCLE_MIN"],)
        pass
                                                     
  def _map(self, x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


#Testing from CPython - Removed so it won't use memory on ESP8266
"""
if __name__ == "__main__":
    #Some quick testing
    import json
    with open("settings.json") as f:
        config = json.load(f)
    motors = MotorControl(config)
    speed, direction = 100, "N"
    print("N; speed: " + str(speed))
    motors.motors_analog(speed, direction)
    print("---------")
    speed, direction = 100, "S"
    print("S; speed: " + str(speed))
    motors.motors_analog(speed, direction)
    print("---------")
    speed, direction= 100, "E"
    print("E; speed: " + str(speed))
    motors.motors_analog(speed, direction)
    print("---------")  
    speed, direction = 100,  "W"
    print("W; speed: " + str(speed))
    motors.motors_analog(speed, direction)    
    print("---------")
    speed, direction = 100, "NE"
    print("NE; speed: " + str(speed))
    motors.motors_analog(speed, direction)  
    print("---------")
    speed, direction = 100, "SE"
    print("SE; speed: " + str(speed))
    motors.motors_analog(speed, direction)  
    print("---------")
    speed, direction = 100, "NW"
    print("NW; speed: " + str(speed))
    motors.motors_analog(speed, direction)  
    print("---------")
    speed, direction = 100, "SW"
    print("SW; speed: " + str(speed))
    motors.motors_analog(speed, direction)                         
    print("---------")
    speed, direction = 50, "SW"
    print("SW 50%; speed: " + str(speed))
    motors.motors_analog(speed, direction)    
    print("---------")
    speed, direction = 50, "SE"
    print("SE 50%; speed: " + str(speed))
    motors.motors_analog(speed, direction)            
    print("---------")
    speed, direction = 50, "NE"
    print("NE 50%; speed: " + str(speed))
    motors.motors_analog(speed, direction)  
    print("---------")          
    speed, direction = 50, "NW"
    print("NW 50%; speed: " + str(speed))
    motors.motors_analog(speed, direction)           
    print("---------")          
    speed, direction = 50, "N"
    print("N 50%; speed: " + str(speed))
    motors.motors_analog(speed, direction)     
"""              