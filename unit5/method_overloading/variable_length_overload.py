# program to show variable length argument overloading
class Area:
    def findarea(self,*args):
        if len(args)==0:
            # find area of square
            a = 1
            print ("You donot have any arguments")
        elif len(args)==1:
            # find area of rectangle
            a = args[0] * args[0]
            print ("Area of Square = ",a)
        elif len(args) == 2:
            a = args[0] * args[1]
            print("Area of Rectangle = ",a)
        elif len(args) == 3:
            v = args[0] * args[1] * args[2]
            print("Volume of object = ",v)



objarea = Area()
objarea.findarea()
objarea.findarea(5)
objarea.findarea(2,7)
objarea.findarea(2,7,3)
