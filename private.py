class Atm:
    def __init__ (self, name, address):
        self.__name = name
        self.__address = address
    
    def display(self):
        print(f"{self.__name} and {self.__address}")
        
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
obj1 = Atm("ram", "kalanki")
obj1.display()
print('name is', obj1.get_name())
print('address is', obj1.get_address())
# obj1._Atm__name = 'hari'
obj1.set_name('hari')
obj1.display()  


