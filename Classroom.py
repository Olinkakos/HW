class Classroom:
    def __init__(self, number,  capacity, equipment):
        self.number = number
        self.capacity = capacity
        self.equipment = equipment
    def is_larger(self, a):
        return self.capacity > a.capacity

    def equipment_differences(self, a):
        b = []
        for i in self.equipment:
            if i not in a.equipment:
                b.append(i)
        return b
    def __str__(self):
        do = ', '.join(self.equipment)
        return ('Classroom ' + str(self.number) + ' has a capacity of ' + str(self.capacity) +' persons and has the following equipment: ' + do + '.')

    def __repr__(self):
        return 'Classroom({}, {}, {})'.format(self.number, self.capacity, self.equipment)


class Building:
    def __init__(self, address, classrooms):
        self.address = address      
        self.classrooms = classrooms

class AcademicBuilding(Building):
    def total_equipment(self):
        we = []
        for i in self.classrooms:
            we.append(i)
            return list(set([(i, we.count(i)) for i in we]))

    def __str__(self):
        return "{} \n".format(self.address) + '\n'.join([i.__str__() for i in self.classrooms])





classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
classroom_007 = Classroom('007', 12, ['TV'])
classroom_008 = Classroom('008', 25, ['PC', 'projector'])
classrooms = [classroom_016, classroom_007, classroom_008]
building = AcademicBuilding('Kozelnytska st. 2a', classrooms)

print(classroom_016.equipment_differences(classroom_008))
print(classroom_016.__str__())
