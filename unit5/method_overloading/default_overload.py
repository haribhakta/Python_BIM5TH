# Program to show method_overloading in python to find area of
# rectangle, square

class Area:
    def findarea(self,l=None,b=None):
        if l is not None and b is None:
            # find area of square
            a = l * l
            print ("Area of square = ",a)
        elif l is not None and b is not None:
            # find area of rectangle
            a = l * b
            print ("Area of Rectangle = ",a)

objarea = Area()
objarea.findarea(5)
objarea.findarea(7,2)
