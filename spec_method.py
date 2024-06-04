class House:
    def __init__(self, numberOfFloors):
        self.numberOfFFloors = numberOfFloors
        self.numberOfFFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFFloors = floors
        print(self.numberOfFFloors)


number = int(input('Введите кол-во этажей: '))

h = House(0)

print(h.setNewNumberOfFloors(number))
