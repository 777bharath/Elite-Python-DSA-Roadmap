"""class Car:
    def __init__(self,make,model,hp,engine):
        self.make   = make
        self.model  = model
        self.hp     = hp
        self.engine = engine
    
    def display(self):
        print(f"specs...\nmake   : {self.make}\nmodel  : {self.model}\nengine : {self.engine}\nstock  : {self.hp}hp\n...... ")

    def is_supercar(self):
        if self.hp>500:
            print(f"{self.make} {self.model} is a Supercar....")
        else:
            print(f"{self.make} {self.model} is not a Supercar....")


c1 = Car("Nissan",'R34 GTR',330,'2.6 INLINE6')
c2 = Car('Toyota','Supra MK4',320,'3.0 INLINE6')
c3 = Car('Lamborghini','Aventador',700,'6.5 V12')
c4 = Car('Buggati','Chiron',1500,'8.0 W16')

cars=[c1,c2,c3,c4]

for car in cars:
    car.is_supercar()
    print()
"""

#QUESTION 1 LEVEL EASY
"""
class Students():
    def __init__(self,name:str,marks:int):
        self.name=name
        self.marks=marks

    def display(self):
        print(f"Student info\nName  = {self.name}\nMarks = {self.marks}\n")

    def is_pass(self):
        return self.marks>=40
        
s1 =Students("Bharath",65)
s2 =Students("Abhinav",35)

student = [s1,s2]

for entry in student:
    entry.display()
    if entry.is_pass():
        print(f"{entry.name} passed...")
    else:
        print(f"{entry.name} failed...")"""
    
    

#QUESTION 2 LEVEL MEDIUM

'''class BankAccount():
    def __init__(self,name:str,balance:float):
        self.name=name
        self.balance=balance
    
    def deposit(self,amount:float):
       self.balance+=amount       

    def withdraw(self,amount:float):
        if amount>self.balance:
           print("Insufficient balance")
        else:
            self.balance-=amount

    def display_balance(self):
        print(f"Available Balance is {self.balance}.....\n")

        
b1= BankAccount("Achu",10000)
b2= BankAccount("Au",100)

b1.deposit(10000)
b1.withdraw(20001)
b1.display_balance()'''

# QUESTION 3 HARD

'''class Car:
    def __init__(self,make,model,hp,engine):
        self.make   = make
        self.model  = model
        self.hp     = hp
        self.engine = engine
    
    def display(self):
        print(f"specs...\nmake   : {self.make}\nmodel  : {self.model}\nengine : {self.engine}\nstock  : {self.hp}hp\n...... ")

    def is_supercar(self):
        if self.hp>500:
            print(f"{self.make} {self.model} is a Supercar....")
        else:
            print(f"{self.make} {self.model} is not a Supercar....")


c1 = Car("Nissan",'R34 GTR',330,'2.6 INLINE6')
c2 = Car('Toyota','Supra MK4',320,'3.0 INLINE6')
c3 = Car('Lamborghini','Aventador',700,'6.5 V12')
c4 = Car('Buggati','Chiron',1500,'8.0 W16')

cars=[c1,c2,c3,c4]

max=cars[0]

for car in cars:
    if car.hp>max.hp:
        max=car
print(max.model)'''
    


'''class Book():
    def __init__(self,title,author,pages:int):
        self.title=title
        self.author=author
        self.pages=pages

    def display(self):
        print(f"Book Details...\nTitle  :{self.title}\nAuthor :{self.author}\nPages  :{self.pages}\n")

    def is_long_book(self):
        return self.pages>=300

b1=Book("Rdr","Rockstar",400)
b2=Book("Hzd","guerila games",600)
b3=Book("Cp2077","cd projekt red",50)
b4=Book("gow","santa monica",500)

books=[b1,b2,b3,b4]
max_book=books[0]
long_book_count=0
for entry in books:
    if entry.is_long_book():
        long_book_count+=1
        print(f"{entry.title} is a long book")
    
    if entry.pages>max_book.pages:
        max_book=entry       
print(f"{max_book.title} is the book with max pages....\n")        
print(f"Number of long books : {long_book_count}") '''      
    

#MULTI CLASSES
#MULTI CLASSES
#MULTI CLASSES
#MULTI CLASSES


'''class Book():
    def __init__(self,title,author,pages:int):
        self.title=title
        self.author=author
        self.pages=pages

    def display(self):
        print(f"Book Details...\nTitle  :{self.title}\nAuthor :{self.author}\nPages  :{self.pages}\n")

    def is_long_book(self):
        return self.pages>=300
        
class Library():
    def __init__(self):
        self.books=[]
    
    def add_book(self,book):
        self.books.append(book)        

    def show_all_books(self):
        for book in self.books:
            book.display()
    
    def show_long_books(self):
        print("****LONG BOOKS****\n")
        for book in self.books:
            if book.is_long_book():
                book.display()

    def max_page_book(self):
        maxbook=self.books[0]
        for book in self.books:
            if book.pages>maxbook.pages:
                maxbook=book
        print (f"max paged book is {maxbook.title}")
    

b1=Book("Rdr","Rockstar",400)
b2=Book("Hzd","guerila games",600)
b3=Book("Cp2077","cd projekt red",50)
b4=Book("gow","santa monica",500)

library=Library()

library.add_book(b1)
library.add_book(b2)
library.add_book(b3)
library.add_book(b4)

library.show_all_books()
library.show_long_books()
library.max_page_book()'''



'''class Student():
    def __init__(self,name,marks:int):
        self.name=name
        self.marks=marks

    def display(self):
        print(f"Student Details***\nName  = {self.name}\nMarks = {self.marks}\n")
    
    def is_pass(self):
        return self.marks>=40
    
class Classroom():
    def __init__(self):
        self.room=[]

    def add_student(self,student):
        self.room.append(student)

    def show_all_students(self):
        for stud in self.room:
            stud.display()

    def show_passed_students(self):
        print("Passed list***")
        for stud in self.room:
            if stud.is_pass():
                print(f"{stud.name} has passed")

    def find_topper(self):
        print("\nTopper****")
        max_mark=self.room[0]
        for stud in self.room:
            if stud.marks>max_mark.marks:
                max_mark=stud
        print(f"{max_mark.name} has the max marks\n")        

    def averge_marks(self):
        avgcount=0
        for stud in self.room:
            avgcount+=stud.marks
        print(f"Average marks = {avgcount/len(self.room)}")



s1=Student("bharath",65)
s2=Student("achu",25)
s3=Student("abhinav",55)
s4=Student("bh",15)        

classroom=Classroom()

classroom.add_student(s1)
classroom.add_student(s2)
classroom.add_student(s3)
classroom.add_student(s4)

classroom.show_all_students()
classroom.show_passed_students()
classroom.find_topper()
classroom.averge_marks()'''



'''class product():
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def display(self):
        print(f"PRODUCT DETAILS.....\nProduct name     = {self.name}\nProduct price  = {self.price}")
    def is_expensive(self):
        return self.price>5000

class Cart():
    def __init__(self):
        self.items=[]
    def add_product(self,product):
        self.items.append(product)
    def show_cart(self):
        for item in self.items:
            item.display()    
    def total_price(self):
        total=0
        for item in self.items:
            total+=item.price
        return total   
    def show_expensive_products(self):
        print("EXPENSIVE ITEMS***")
        for item in self.items:
            if item.is_expensive():
                print(f"{item.name}")
    def most_expensive_product(self):
        exp=self.items[0]
        for item in self.items:
            if item.price>exp.price:
                exp=item
        return exp              

p1=product("RTX 3050",18000)
p2=product("RAM",3000)
p3=product("SSD",4500)
p4=product("I5 12thGen",10000)

c=Cart()
c.add_product(p1)
c.add_product(p2)
c.add_product(p3)
c.add_product(p4)

c.show_cart()
print(f"Total price is {c.total_price()}")
c.show_expensive_products()
expensive=c.most_expensive_product()
print(f"Most Expensive product is {expensive.name}")'''


'''class Ship:
    # Class Attribute (Every ship is in the same sea)
    location = "Atlantic Ocean"

    def __init__(self, name):
        # Instance Attribute (Every ship has its own name)
        self.name = name

# Creating (instantiating) two separate objects
ship_a = Ship("Discovery")
ship_b = Ship("Endeavour")

ship_a.location = "pacific"

print(ship_a.name) # Output: Discovery
print(ship_a.location) # Output: Atlantic Ocean
print(ship_b.location)
print(Ship.location)
'''





def apply_tax(price):
    return price * 1.10

class Gadget:
    catalog = []  

    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
       
        self.catalog.append(name) 

    def get_total_price(self):
       
        self.cost = apply_tax(self.cost)
        return self.cost


phone = Gadget("Smartphone", 500)
laptop = Gadget("lap", 500)
print(phone.catalog)
            