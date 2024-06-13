class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


p1 = Building(22, 'ЖК ОКт')
p2 = Building(10, 'ЖК Том')

print(p1, p2, sep='\n')