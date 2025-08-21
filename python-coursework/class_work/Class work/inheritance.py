class A:
    def printa(self):
        print("This is the parent class")
        
a = A()        
a.printa()

# This is the parent class

# Single inheritance
class A:
    def printa(self):
        print("This is the parent class")
        
class B(A):
    def printb(self):
        print("This is child class-B->A")

b = B()
b.printa()
b.printb()

'''
This is the parent class
This is child class-B->A

'''

# Multilevel inheritance
class A:
    def printa(self):
        print("This is the parent class: A")
        
class B(A):
    def printb(self):
        print("This is child class-B->A")
        
class C(B):
    def printc(self):
        print("This is grand-child class: C->B->A")

c = C()
c.printa()
c.printb()
c.printc()

'''
This is the parent class: A
This is child class-B->A
This is grand-child class: C->B->A
'''

# Multiple inheritance
class A:
    def printa(self):
        print("This is the parent class: A")
        
class B:
    def printb(self):
        print("This is the parent class: B")
        
class C:
    def printc(self):
        print("This is the parent class: C")
        
class D(A,B,C):
    def printd(self):
        print('''
             This is child class
                  A B C 
                  \ | /
                    D
                    ''')
        
d = D()
d.printa()
d.printb()
d.printc()
d.printd()

'''
<main.py>:19: SyntaxWarning: invalid escape sequence '\ '
This is the parent class: A
This is the parent class: B
This is the parent class: C

             This is child class
                  A B C 
                  \ | /
                    D
                    

=== Code Execution Successful ===
'''

# Hirearchial inheritance
class A:
    def printa(self):
        print('''This is the parent class A-> (B,C,D)''')
        
class B(A):
    def printb(self):
        print("This is the child class: B->A")
        
class C(A):
    def printc(self):
        print("This is the child class: C->A")
        
class D(A):
    def printd(self):
        print("This is the child class: D->A")
        
d = D()
d.printa()
d.printd()

c = C()
c.printa()
c.printc()

b = B()
b.printa()
b.printb()

'''
This is the parent class A-> (B,C,D)
This is the child class: D->A
This is the parent class A-> (B,C,D)
This is the child class: C->A
This is the parent class A-> (B,C,D)
This is the child class: B->A

=== Code Execution Successful ===
'''
# Uber example
class Person:
    def login(self,name,phonenumber,gender):
        self.name = name 
        self.phonenumber = phonenumber 
        self.gender = gender
        
class Driver(Person):
    def driverdetails(self,vehno,photo,vehtype):
        self.vehno = vehno
        self.photo = photo 
        self.vehtype = vehtype
        print(f"\nHello {self.name}\nYour driver account is successfully created.")
        
class Wheels_2:
    def Price2W(self):
        self.fare = 30
        return self.fare
        
class Wheels_3:
    def Price3W(self):
        self.fare = 60 
        return self.fare
        
class Wheels_4:
    def Price4W(self):
        self.fare = 120 
        return self.fare
        
''' class FareCal(2_Wheels,3_Wheels,4_Wheels,Driver):
    def farecal(self,distance):
        if self.vehtype == 2: '''
            
        
    
        
class DriverRides(Driver):
    def driver_rides(self,exp,totalride):
        self.exp = exp
        self.totalride = totalride
        print(f"Helloo {self.name} .\n Your ride deatils are updated!")
        
        
class User(Person):
    def ridedetails(self,droppoint,pickup):
        self.droppoint = droppoint
        self.pickup = pickup 
        print(f"\nHello {self.name}\nYou booked the ride successfuly.\nHave fun!!!.")
        
leorah = User()        
leorah.login('leorah',8373689307,'F')
leorah.ridedetails("Ammerpet","Uppal")

ricky = Driver()        
ricky.login('ricky',8373689307,'M')
ricky.driverdetails(233,'nat.png','car')



        
        
        
    