from math import *

class Triangle:
    def __init__(self, point1, point2, point3):
        self.points = [point1, point2, point3]

    def get_line_length(self, point1, point2):
        return sqrt((point1.get_xposition() - point2.get_xposition()) ** 2 +
                    (point1.get_yposition() - point2.get_yposition()) ** 2)

    def get_sides(self):
        side1 = self.get_line_length(self.points[0], self.points[1])
        side2 = self.get_line_length(self.points[1], self.points[2])
        side3 = self.get_line_length(self.points[2], self.points[0])
        return side1, side2, side3

    def is_triangle(self):
        side1, side2, side3 = self.get_sides()
        if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
            return True
        return False

    def get_perimeter(self):
        return sum(self.get_sides())

    def get_area(self):
        side1, side2, side3 = self.get_sides()
        half = (side1 + side2 + side3) / 2
        return sqrt(half * (half - side1) * (half - side2) * (half - side3))