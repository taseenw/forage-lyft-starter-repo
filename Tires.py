from Serviceable import Serviceable

class Tires(Serviceable):
    pass

class CarriganTires(Tires):
    def __init__(self,sensors:list):
        self.sensors = sensors
    
    def needs_service(self):
        for sensor in self.sensors:
            if sensor >= 0.9:
                return True
        return False

class OctoprimeTires(Tires):
    def __init__(self,sensors:list):
        self.sensors = sensors
    
    def needs_service(self):
        sum=0
        for sensor in self.sensors:
            sum=sum+sensor
            if sum <= 3:
                return True
        return False
