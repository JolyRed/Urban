class House:
    def __init__(self, numberOfFloors, floors):
        self.numberOfFloors = numberOfFloors
        self.floors = floors

    def __del__(self):
        self.numberOfFloors = self.floors
        print(self.numberOfFloors)


h = House(0, 15)
print(h)




