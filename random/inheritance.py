class Fish:
    def __init__(self,fname,lname="Fish",
                skeleton="bone", eyelids=False):
        self.fname = fname
        self.lname = lname
        self.skeleton = skeleton
        self.eyelids = eyelids


    def swim(self):
        print("The fish is swimming.")

    def swim_backwards(self):
        print("The fish is swimming backwards.")

class Trout(Fish):
    def __init__(self,water="freshwater"):
        self.water = water
        super().__init__(self)

terry = Trout()
terry.fname = "Terry"
print(terry.fname + " " + terry.lname)
print(terry.eyelids)
print(terry.water)
terry.swim()


class ClownFish(Fish):

    def live_with_anemone(self):
        print("The clownfish is coexisting with sea anemone")


class Shark(Fish):
    def __init__(self,fname,lname="Shark",
                    skeleton="cartilage",eyelids=True):
        self.fname = fname
        self.lname = lname
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")

sammy = Shark("Sammy")
print(sammy.fname + " " + sammy.lname )
sammy.swim()
sammy.swim_backwards()
print(sammy.eyelids)
print(sammy.skeleton)

casey = ClownFish("Casey")
print(casey.fname + " " + casey.lname)
casey.swim()
casey.live_with_anemone()




