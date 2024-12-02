'''
class Person:
    name = "Bouraghda"
    Birthday = 1976
    
    def my_age(self):
        age = 2024 - self.Birthday
        print('Your age is :', age)
        
    
obj = Person()
# print(obj.name)
obj.my_age()
'''
'''
class Human:
    def __init__(self, Name, Birth):
        self.Name      = Name
        self.__Birth   = Birth
        self.__Max_Age = 100
    
    # getter method
    def get_Birth(self):
        return self.__Birth
    
    # setter method
    def set_Birth(self, value):
        if 1920 < value < 2021:
            self.__Birth = value
            print("New value assigned .")
        else:
            print("Enter a valid birth year")
    
hum = Human('Mohamed',1976)
print(hum.Name, hum.get_Birth())
hum.set_Birth(1933)
print(hum.Name, hum.get_Birth())
'''
'''
class Human:
    def __init__(self, Name,Birth):
        self.Name = Name
        self.__Birth = Birth
        self.__Max_Age = 100
    
    # getter method
    @property
    def Birth(self):
        return self.__Birth
    
    # setter method
    @Birth.setter
    def Birth(self, value):
        if 1920 < value < 2021:
            self.__Birth = value
            print("New value assigned .")
        else:
            print("Enter a valid birth year")
    
hum = Human('Mohamed',1976)
print(hum.Name, hum.Birth)
hum.Birth = 1900
print(hum.Name, hum.Birth)
'''
class Human:
    def __init__(self,Name) -> None:
        self.Name = Name
        self.Independant = True
        
    def Talk(self):
        print(f"Hi {self.Name} I'm an abstract human being !")

    def Greet(self):
        print("Hello world")
    
class Woman(Human):
    def Talk(self):
        super().Talk() # = Human.Talk(self)
        print(f"I'm class from Humain  ")
        

moh = Woman("Rahma")
moh.Talk()

