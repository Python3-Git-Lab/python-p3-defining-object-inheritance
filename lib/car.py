from vehicle import Vehicle

#-----sub-class
class Car(Vehicle):
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"

car1= Car("toyota",30 , 35)
car1.fill_up_tank()