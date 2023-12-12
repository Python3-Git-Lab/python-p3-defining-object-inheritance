#--------superclass

class Vehicle:

    def __init__(self,name,  wheel_size, wheel_number):
        self.name= name
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number

    def go(self):
        return "vrrrrrrrooom!"

    def fill_up_tank(self):
        print ("filling up!")

