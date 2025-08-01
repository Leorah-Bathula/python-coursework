#1.
''' 250*10/100
250*0.1 = 25
5/100 = 0.05 
250001<=salary<=500000'''


salary = float(input())

if salary <= 250000:
    print("No Tax")
elif 250001<=salary<=500000:
    print(salary*0.05)
elif 500001<=salary<=100000:
    print(salary*0.2)
elif salary>100000:
    print(salary * 0.3)
    

#2.
people = int(input())
ticket_collection = 0 

for i in range(people):
    age = int(input())
    if age < 5:
        ticket_collection += 0
    elif 5 <= age <= 18:
        ticket_collection += 100
    elif 19 <= age <= 60:
        ticket_collection += 150
    elif age>60:
        ticket_collection += 120
        
print(ticket_collection)        
    

#3.
units = int(input())
bill = 0
if units <= 100:
    bill = units * 1.5
elif 101 <= units < 200:
    bill = 100 * 1.5 + (units-100)*2.5
elif 201 <= units < 500:
    bill = 100*1.5 + 100*2.5 + (units-200)*4
elif units > 500:
    bill = 100 * 1.5 + 100 * 2.5 + 300*4 + (units-500) * 6
    
print(bill)    

#4.
hours = int(input())
if hours<2:
    print(30)
elif hours == 24:
    print(200)
elif 2<hours<24:
    print(30+(hours-2)*10)
    
#5.
product = input()
qua = int(input())

if qua == 0:
    print(f"{product}: Out of stock")
    
elif 1 <= qua <= 10:
    print(f"{product}: low stock")
    
elif 11 <= qua <= 50:
    print(f"{product}: in stock")    
    
elif qua > 50:
    print(f"{product}: over stock")    
    

#6.
n = int(input())
for i in range(n):
    for j in range(n):
        print((i+j)%2,end = " ")
    print()  

#7.
ch = int(input())
people = int(input())

if ch == 1:
    print(people * 500)
elif ch == 2:
    print(people*1300)
elif ch == 3:
    print(people*500)
else:
    print("Invalid Choice")

#8.
    