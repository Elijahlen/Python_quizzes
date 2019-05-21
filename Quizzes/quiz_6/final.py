# Defines two classes, Point() and Triangle().
# An object for the second class is created by passing named arguments,
# point_1, point_2 and point_3, to its constructor.
# Such an object can be modified by changing one point, two or three points
# thanks to the method change_point_or_points().
# At any stage, the object maintains correct values
# for perimeter and area.
#
# Written by *** and Eric Martin for COMP9021


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
            
    # Possibly define other methods


class TriangleError(Exception):
    def __init__(self, message):
        self.message = message

def line(x1,y1,x2,y2,x3,y3):
    if x1==x2==x3:
        return 0
    elif x1==x2 :
        if y1 == y2:
            return 0
        else:
            return 1
    elif x2==x3 :
        if y2 == y3:
            return 0
        else:
            return 1
    elif x1==x3 :
        if y1 == y3:
            return 0
        else:
            return 1        
    else:
        if not((y2-y1)/(x2-x1) == (y3-y2)/(x3-x2)):
            return 1
        else:
            return 0

class Triangle:
    def __init__(self, *, point_1, point_2, point_3):
        if line(point_1.x,point_1.y,point_2.x,point_2.y,point_3.x,point_3.y):
            self.point_1 = point_1
            self.point_2 = point_2
            self.point_3 = point_3
            Triangle.perimeter(self)
            Triangle.area(self)
        else:
            raise TriangleError('Incorrect input, triangle not created.')
    

    def perimeter(self) :
        
        self.L_1 = sqrt((self.point_1.x-self.point_2.x)**2+\
                   (self.point_1.y-self.point_2.y)**2)
        self.L_2 = sqrt((self.point_1.x-self.point_3.x)**2+\
                   (self.point_1.y-self.point_3.y)**2)
        self.L_3 = sqrt((self.point_2.x-self.point_3.x)**2+\
                   (self.point_2.y-self.point_3.y)**2)
        self.perimeter = self.L_1+self.L_2+self.L_3
        
    def area(self) :
        s = (self.L_1+self.L_2+self.L_3)/2
        S = sqrt(s*(s-self.L_1)*(s-self.L_2)*(s-self.L_3))
        self.area = S
                   
    def change_point_or_points(self, *, point_1 = None,point_2 = None, point_3 = None):
        inter_1 = self.point_1
        inter_2 = self.point_2
        inter_3 = self.point_3
        if not(point_1 is None):
            inter_1 = point_1
        if not(point_2 is None):
            inter_2 = point_2
        if not(point_3 is None):
            inter_3 = point_3
        
        if not(line(inter_1.x,inter_1.y,inter_2.x,inter_2.y,inter_3.x,inter_3.y)):
            print('Incorrect input, triangle not modified.')
        elif line(inter_1.x,inter_1.y,inter_2.x,inter_2.y,inter_3.x,inter_3.y):
            self.point_1=inter_1
            self.point_2=inter_2
            self.point_3=inter_3
            Triangle.perimeter(self)
            Triangle.area(self)
            
