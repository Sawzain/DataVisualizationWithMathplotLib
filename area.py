# import math 
# class Circle:
#     def __init__(self,r):
#         self.__r = r
#     def area(self,r):
#         area = float(math.pi*self.__r*self.__r)
#         print(f"the area is {area}")
    
# a=float(input("enter the radius"))        
# obj1=Circle(a)    
# obj1.area(a)
import math
class Circle:
    # try:
            def __init__(self,r):
                self.__r = r
            def area(self):
                area = float(math.pi*self.__r*self.__r)
                print(f"the area is {area}")
            def get_radius(self):
                return self.__r

try:   
    a=float(input("enter the radius"))        
    obj1=Circle(a)    
    obj1.area()
    print(obj1.get_radius())
    
except ValueError:
        print("error")
        
        
    
        