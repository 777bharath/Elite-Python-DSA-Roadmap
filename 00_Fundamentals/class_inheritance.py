'''class Engine:
    def start(self):
        return "Car started !"
    
class Electronics:
    def power_on(self):
        return "System Online."        



class tesla(Engine,Electronics):
    pass

model_s=tesla()
print(model_s.start())'''


class Product:
    def __init__(self,brand,name):
        self.brand=brand
        self.name=name

    def show_details(self):
        return f"Brand:{self.brand}\nName:{self.name}"
    
class SmartPhone(Product):
    def __init__(self, brand, name,ram):
        super().__init__(brand, name)
        self.ram=ram

     



s1=SmartPhone("Apple","Iphone 17","ram")

print(s1.show_details())
        