from hmc5883l import HMC5883L

class CompassControl(object):
    """Class to implement heading control. Currently using HMC5883L, might expand to include different ICs."""
    def __init__(self, config:dict):
        super(CompassControl, self).__init__()
        print("Starting Compass...")
        self.config = config
        self.sensor = HMC5883L(self.config['GPIO_SCL'], self.config['GPIO_SDA'])
        print("Compass Started!")
    
    def get_heading(self):
        self.x, self.y, self.z = self.sensor.read()
        return self.sensor.format_result(self.x, self.y, self.z)

    