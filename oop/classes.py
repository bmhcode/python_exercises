class Car:
    def __init__(self, type, power, color):
        self.type  = type
        self.power = power
        self.color = color
    
    def get_color(self):
        return self.color
        
car = Car('Golf', 5, 'black')
print(car.type)
print(car.get_color())

        