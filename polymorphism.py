

'''Different classes with the same method:'''
'''   
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
    def move(self):
        print("Car can be driven ")
        
class Boat:
    def __init__(self,brand,model):
        self.model=model
        self.brand=brand
    
    def move(self):
        print("Boat can be sail")

class Plane:
    def __init__(self,model,brand):
        self.brand=brand
        self.model=model
    def move(self):
        print("Plane can crash")

car=Car("Ford","Mustang")
boat=Boat("Titanic","XYZ")
plane=Plane("Boeing","747")

for x in (car,boat,plane):
    x.move() 
 '''
    
"""Create a class called Vehicle and make Car, Boat, Plane child classes of Vehicle: """

class Vehicle:
    def __init__ (self,model,brand):
        self.brand=brand
        self.model=model
    
    def move(self):
        pass

class Car(Vehicle):
    pass
    
        
class Boat(Vehicle):
    pass
    def move(self):
        print("Boat can be sail")

class Plane(Vehicle):
    pass
    def move(self):
        print("Plane can crash")
car=Car("Ford","Mustang")
boat=Boat("Titanic","XYZ")
plane=Plane("Boeing","747")

for x in (car,boat,plane):
    print(x.brand)
    print(x.model)