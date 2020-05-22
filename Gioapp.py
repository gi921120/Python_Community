from Funtions import * 
age=int()
BirthYear=input('Birth Year: ')
age = BornYear(int(BirthYear))
print(age)

class PointClient:
    def __init__(self,x,y):
        self.x=x
        self.y=y 
    def move(self):
        print("move")
    
    def draw(self):
        print("draw")


point1=PointClient(20,10) # Object definition 
point1.draw() # access the method in the object 
print(point1.x)

class Person():
    def __init__(self,name):
        self.name =name

    def talk(self):
        print(f"Hi, I am {self.name}")

wayne=Person("Wayne")
#print(wayne.name)
wayne.talk()


from eco import ship

ship.calcShip()