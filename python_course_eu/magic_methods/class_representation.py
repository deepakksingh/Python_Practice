
class Car():
    def __init__(self,name,color,engine_status = False):
        self.name = name
        self.color = color
        self.engine_status = engine_status

    def showCar(self):
        print("The car name is {} and its {} in color.".format(self.name,self.color))

    def __str__(self):
        print("calling magic method __str__()")
        return "The car name is {} and its {} in color.".format(self.name,self.color)
        
    def __hash__(self):
        return 1
    
c1 = Car("AUDI","dark-blue")
c2 = Car("BMW", "electric-blue")
c1.showCar()
print(str(c1))
hash(c1)
hash(c2)
