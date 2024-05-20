# def funI(*args,**):
#    print(args)
   

# funI(10,20,30,340,name='ram', Address='itahari')
# a={'name':'Ram'}
# # print(a['name'])
# print(a.get('nami'))

# a=int(input("the number:"))
# b=int(input("the total number of multiples:"))
# for i in range(1,b+1):
    
#     c=a*i
#     print(a,"*",i,"=",c)
# try:
#     a=20
#     print(b)
    
# except:
#     print("error")



# class ClassName:
#     def __init__(self):
#         print("hello")
    
        
# obj=ClassName()

# class student:
#     def __init__(self,name):
#         self.name=name
# obj1=student('ram')
# obj2=student('Hari')
  
# class Atm:
#     #   
#     def __init__ (self, name):
#         self.name = name
    
#     def show(self, age):
#         print(f"my name is {self.name} and age is {age}")
#     def __str__ (self):
#         return f"{self.name}"
    
    
    
# obj = Atm("hari")
# print(obj)  





# ab= [10,20,30]#list((10, 20, 30))
# print(ab)

# class Calc:
     
#     def add():
#         try:
#             m = int(input("enter the number:"))
#             n = int(input("enter the second number:"))
#             result = m+n
#             return result7
        
#         except ValueError:
#             print("input should be a number")
#             return None

class Atm:
    
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    def display(self):
            print(f"Name is {self.name} and addrsss is {self.address}")
            
    def show_detail(self):
            print(f"{self.name} and {self.address}")
            
obj1 = Atm('Ram', 'address')
obj1.display()
obj1.show_detail()
print(obj1.name)
obj1.name = "Hari"
obj1.display()
        
            
    
