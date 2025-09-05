# 1. Types of Methods(Instance,Class,Static)

class Student:
    total_students = 0 # class variable 

    def __init__(self,name,age):
        self.name = name 
        self.age = age 
        Student.total_students += 1

    # Instance Method 
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")  

    # Class method
    @classmethod
    def get_total_students(cls):
        print(f"Total Students: {cls.total_students}")  

    # Static method
    @staticmethod
    def is_eligible(age):
        return 18 <= age <= 30 

s1 = Student("Arun",20)   
s2 = Student("Meena",17)   
s1.display()    
Student.get_total_students()
print(Student.is_eligible(25))

# 2. Consturctor Usage (Book Class)

class Book:
    def __init__(self,title,author,price):
        self.title = title 
        self.author = author
        self.price = price 

    def display_info(self):
        print(f"Title: {self.title}")  
        print(f"Author: {self.author}")  
        print(f"Price: {self.price}")

b = Book("The Alchemist","Paul Coelho",399)     
b.display_info() 

# 3. Encapsulation - Public,Protected,Private

class Account:
    def __init__(self,account_holder,pin):
        self.account_holder = account_holder # public
        self._balance = 3850 # Protected(default balance)
        self.__pin = pin 

    def deposit(self,amount):
        self._balance += amount 
        print(f"Deposited ${amount}") 

    def withdraw(self,pin,amount):
        if pin == self.__pin:
            if amount <= self._balance:
                self._balance -= amount 
                print(f"Withdrawn ${amount}") 

            else:
                print("Insufficient Balance")     
        else:
            print("Invalid Pin")

    def show_balance(self):
        print(f"Available Balance {self._balance}")    

acc = Account("Ravi",1234)     
acc.deposit(5000)   
acc.withdraw(1234,1500)
acc.show_balance()

# 4. Multilevel Inheritance - Ride Booking system 
class User:
    def login(self):
        print("User logged in")

class Rider(User):
    def book_ride(self):
        print("Ride booked successfully") 

class Payment(Rider):
    def make_payment(self):
        print("Payment completed")  

p = Payment()  
p.login()   
p.book_ride()   
p.make_payment()

# 5. Multiple Inheritance - Food Delivery app 

class LocationService:
    def track_location(self):
        print("Current location tracked")

class OrderService:
    def place_order(self):
        print("Order placed successfully")    

class DeliveryApp(LocationService,OrderService):
    def confirm_delivery(self):
        print("Delivery confirmed to your address")     

app = DeliveryApp()   
app.track_location()   
app.place_order()    
app.confirm_delivery()    

# 8. Method Overriding - Shape Areas

import math

class Shape:
    def area(self):
        print("Area not defined")

class Square(Shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        print(f"Square Area: {self.side * self.side}")       

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius 

    def area(self):
        print(f"Circle Area: {round(math.pi * self.radius * self.radius,2)}")  

s = Square(4)  
c = Circle(3)  

s.area()
c.area()

# 9. Operator Overloading 
class Point:
    def __init__(self,x,y):
        self.x = x 
        self.y = y

    def __add__(self,other):
        return Point(self.x + other.x , self.y + other.y)  
    
    def display(self):
        print(f"Sum: ({self.x}, {self.y})")

p1 = Point(1,2)  
p2 = Point(3,4)  
p3 = p1 + p2
p3.display()    

# 10. Abstraction - notification system 

from abc import ABC, abstractmethod
   
class Notification(ABC):  
    @abstractmethod
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        print("Email sent to user@example.com")

class SMSNotification(Notification):
    def send(self):
        print("SMS sent to registered number")   

e = EmailNotification()
s = SMSNotification()

e.send()
s.send()