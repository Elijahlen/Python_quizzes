# Defines two classes, Point() and Triangle().
# An object for the second class is created by passing named arguments,
# point_1, point_2 and point_3, to its constructor.
# Such an object can be modified by changing one point, two or three points
# thanks to the function change_point_or_points().
# At any stage, the object maintains correct values
# for perimeter and area.
#
# Written by Eric Martin for COMP9021


from math import sqrt


class PointError(Exception):
    def __init__(self, message):
        self.message = message


class Point():
    def __init__(self, x = None, y = None):
        if x is None and y is None:
            self.x = 0
            self.y = 0
        elif x is None or y is None:
            raise PointError('Need two coordinates, point not created.')
        else:
            self.x = x
            self.y = y

    def collinear(self, p2, p3):
        if (p2.y - self.y) * (p3.x - p2.x) == (p3.y - p2.y) * (p2.x - self.x):
            return True
        return False



class TriangleError(Exception):
    def __init__(self, message):
        self.message = message


class Triangle:
    def __init__(self, *, point_1, point_2, point_3):
        if point_1.collinear(point_2, point_3):
            self.deal_with_error('Initialisation')
        else:
            self._initialise(point_1, point_2, point_3)

    def deal_with_error(self, phase):
        if phase == 'Initialisation':
            raise TriangleError('Incorrect input, triangle not created.')
        else:
            print('Incorrect input, triangle not modified.')
       
    def change_point_or_points(self, *, point_1 = None, point_2 = None, point_3 = None):
        if not point_1:
            point_1 = self.point_1
        if not point_2:
            point_2 = self.point_2
        if not point_3:
            point_3 = self.point_3
        if point_1.collinear(point_2, point_3):
            self.deal_with_error('Update')
        else:           
            self._initialise(point_1, point_2, point_3)

    def _initialise(self, point_1, point_2, point_3):
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3
        length_12 = self._side_length(point_1, point_2)
        length_13 = self._side_length(point_1, point_3)
        length_23 = self._side_length(point_2, point_3)
        self.perimeter = length_12 + length_13 + length_23
        half_perimeter = self.perimeter / 2
        self.area = sqrt(half_perimeter * (half_perimeter - length_12) *
                            (half_perimeter - length_13) * (half_perimeter - length_23)
                        )

    def _side_length(self, p, q):
        return sqrt((q.x - p.x) ** 2 + (q.y - p.y) ** 2)
        
        

            
            
