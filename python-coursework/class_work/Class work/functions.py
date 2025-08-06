'''
def function_name()
    #some code
function_name()
'''
#ATM CODE
data = {"current_balance": 5000, "history": []}

def Menu():
    print("[C]heck Balance")
    print("[D]eposit")
    print("[W]ithdraw")
    print("[V]iew Transaction History")
    print("[E]xit\n")

def Welcome():
    print("Welcome to ATM".center(40, "*"))

def Check_Balance():
    print(f"Current Balance: ${data['current_balance']}")

def Withdraw():
    amount = int(input("Enter the amount to withdraw: "))
    if amount <= data["current_balance"]:
        data["current_balance"] -= amount
        data["history"].append(f"Withdraw: ${amount}")
        print(f"${amount} is successfully withdrawn!")
    else:
        print("Insufficient Balance")

def Deposit():
    amount = int(input("Enter the amount to deposit: "))
    data["current_balance"] += amount
    data["history"].append(f"Deposited: ${amount}")
    print(f"${amount} is successfully deposited!")

def View_History():
    if data["history"]:
        print("Transaction History".center(40, "-"))
        for i in data["history"]:
            print(i)
        print("End of history".center(40, "-"))
    else:
        print("No Transactions")

def Flow_Check(ch):
    if ch == "C":
        Check_Balance()
    elif ch == "D":
        Deposit()
    elif ch == "W":
        Withdraw()
    elif ch == "V":
        View_History()

Welcome()
while True:
    Menu()
    ch = input("Enter the char [C/D/W/V/E]: ").upper()
    
    if ch == "E":
        print(" Thank You ".center(40, "."))
        break
    elif ch in ["C", "D", "W", "V"]:
        Flow_Check(ch)
    else:
        print("Invalid Choice")

#output:
'''
*************Welcome to ATM*************
[C]heck Balance
[D]eposit
[W]ithdraw
[V]iew Transaction History
[E]xit

Enter the char [C/D/W/V/E]: c
Current Balance: $5000
[C]heck Balance
[D]eposit
[W]ithdraw
[V]iew Transaction History
[E]xit

Enter the char [C/D/W/V/E]: d
Enter the amount to deposit: 3500
$3500 is successfully deposited!
[C]heck Balance
[D]eposit
[W]ithdraw
[V]iew Transaction History
[E]xit

Enter the char [C/D/W/V/E]: d
Enter the amount to deposit: 4000
$4000 is successfully deposited!
[C]heck Balance
[D]eposit
[W]ithdraw
[V]iew Transaction History
[E]xit

Enter the char [C/D/W/V/E]: 3124
Invalid Choice
[C]heck Balance
[D]eposit
[W]ithdraw
[V]iew Transaction History
[E]xit

Enter the char [C/D/W/V/E]: c
Current Balance: $12500
[C]heck Balance
[D]eposit
[W]ithdraw
[V]iew Transaction History
[E]xit

Enter the char [C/D/W/V/E]: w
Enter the amount to withdraw: 1300
$1300 is successfully withdrawn!
[C]heck Balance
[D]eposit
[W]ithdraw
[V]iew Transaction History
[E]xit

Enter the char [C/D/W/V/E]: w
Enter the amount to withdraw: 100
$100 is successfully withdrawn!
[C]heck Balance
[D]eposit
[W]ithdraw
[V]iew Transaction History
[E]xit

Enter the char [C/D/W/V/E]: v
----------Transaction History-----------
Deposited: $3500
Deposited: $4000
Withdraw: $1300
Withdraw: $100
-------------End of history-------------
[C]heck Balance
[D]eposit
[W]ithdraw
[V]iew Transaction History
[E]xit

Enter the char [C/D/W/V/E]: e
.............. Thank You ...............

=== Code Execution Successful ===
''' 

#FUNCTION TYPES 
# 1. POSITIONAL ARGUMENT --> These are the most common. You must pass values in the same order as the function parameters.
def greet(name, age):
    print(f"Hello {name} , you are {age} years old.")
    
greet("Alice",25) 

#OUTPUT -> Hello Alice , you are 25 years old.

#1.Positional Agr

'''
1.Positional Agr

def function_name(agr1,agr2,agr3):
    #block of code


function_name(val1,val2,val3)
function_name(val3,val1,val2)
function_name(agr1,agr2,agr3)
'''

def student_details(name, rollno, marks, grade, course):
    print("Name:", name)
    print("Rollno:", rollno)
    print("Marks:", marks)
    print("Grade:", grade)
    print("Course:", course)

name = input("Name: ")  
rollno = int(input("Roll no: "))
marks = int(input("Marks: "))
grade = input("Grade: ")
student_course = input("Course: ")

student_details(name, rollno, marks, grade, student_course)  
student_details("Alice", 101, 92, "A", "Python")
student_details("Bob", 102, 78, "C", "C++")
student_details("Leorah", 103, 88, "B+", "AI & ML")

'''
OUTPUT:
Name: Jessi
Roll no: 32
Marks: 97
Grade: A
Course: Python
Name: Jessi
Rollno: 32
Marks: 97
Grade: A
Course: Python
Name: Alice
Rollno: 101
Marks: 92
Grade: A
Course: Python
Name: Bob
Rollno: 102
Marks: 78
Grade: C
Course: C++
Name: Leorah
Rollno: 103
Marks: 88
Grade: B+
Course: AI & ML

=== Code Execution Successful ===
'''
#var = lambda parameters/arguments : Expression


s = lambda s: s[0]
print(s("python"))

add = lambda a,b : a + b
print(add(10,20))

greater = lambda a,b : a  if a > b else b
print(greater(10,20))

evenorodd = lambda n : "Even" if n % 2 == 0 else "Odd"
print(evenorodd(15))
print(evenorodd(90))

sumof3num = lambda a,b,c : a + b + c
print(sumof3num(30,20,10))

# Mapping 

# Sequence dealing : map,filter,reduce

s = "python programming"
changestr = list(map(lambda i : i.upper(),s))
print(changestr)

#Displaying Ascii charcaters 
asci = list(map(lambda i : ord(i),s))
print(asci)

vowels = "aeiouAEIOU"
frmt = list(map(lambda i: "*" if i in vowels else "0",s))
print(frmt)

l = [1,2,3,4,5,6,7,8,9,10]
listupdate = list(map(lambda i: i+1,l))
print(listupdate)

# Removing the last number
t = (20,50,30,60,70,89,56,12)
tupleupdate = tuple(map(lambda i: i //10 , t))
print(tupleupdate)

s = {"python","html","css","java","mysql"}
setupdate = set(map(lambda i : i.upper(),s))
print(setupdate)

d = {1: "leorah", 2:"jessi", 3:"keerthana", 4:"nihitha", 5: "ricky"}
dictupdate = dict(map(lambda i: (i, d[i].title()), d))
print(dictupdate)

'''
['P', 'Y', 'T', 'H', 'O', 'N', ' ', 'P', 'R', 'O', 'G', 'R', 'A', 'M', 'M', 'I', 'N', 'G']
[112, 121, 116, 104, 111, 110, 32, 112, 114, 111, 103, 114, 97, 109, 109, 105, 110, 103]
['0', '0', '0', '0', '*', '0', '0', '0', '0', '*', '0', '0', '*', '0', '0', '*', '0', '0']
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
(2, 5, 3, 6, 7, 8, 5, 1)
{'CSS', 'PYTHON', 'HTML', 'JAVA', 'MYSQL'}
{1: 'Leorah', 2: 'Jessi', 3: 'Keerthana', 4: 'Nihitha', 5: 'Ricky'}

=== Code Execution Successful ===
'''

# Filter
vowels = "aeiouAEIOU"
s = "python programming"
fmrt = list(filter(lambda i:  i in vowels, s))
print("Filter: ",fmrt)

fmrt = list(filter(lambda i:  i not in vowels, s))
print("Filter: ",fmrt)

'''
Filter:  ['o', 'o', 'a', 'i']
Filter:  ['p', 'y', 't', 'h', 'n', ' ', 'p', 'r', 'g', 'r', 'm', 'm', 'n', 'g']

=== Code Execution Successful ===
'''
vowels = "aeiouAEIOU"
s = "python programming"
fmrt = list(filter(lambda i:  i in vowels, s))
print("Filter: ",fmrt)

fmrt = list(filter(lambda i:  i not in vowels, s))
print("Filter: ",fmrt)

l = [10,20,31,45,40,60,24,77]
evenlist = list(filter(lambda i : i % 2 == 0 , l))
print(evenlist)

oddlist = list(filter(lambda i : i % 2 != 0 , l))
print(oddlist)

t = (90,34,50,60,34,32,33)
divtup = list(filter(lambda i : i % 10 == 0, t))
print("using filter",divtup)

s = {"python","html","css","java","mysql"}
stset = set(filter(lambda i : i.startswith("p"),s))
print(stset)

products = {"mouse": 10,"keyboard":0,"laptops": 30,"phone": 0, "charger": 13}
prodisplay = list(filter(lambda i: products[i] > 0,products))
print(prodisplay)

'''
Filter:  ['o', 'o', 'a', 'i']
Filter:  ['p', 'y', 't', 'h', 'n', ' ', 'p', 'r', 'g', 'r', 'm', 'm', 'n', 'g']
[10, 20, 40, 60, 24]
[31, 45, 77]
using filter [90, 50, 60]
{'python'}

=== Code Execution Successful ===

['mouse', 'laptops', 'charger']

=== Code Execution Successful ===
'''

# Reduce

from functools import reduce
l = [1,2,3,4]
suml = reduce(lambda s,a : s + a, l)
print("Reduce: ",suml)

s = {"python","html","css","java","mysql"}
names = reduce(lambda n , name: n+" "+name,s)
print(names)

t = (1,2,3,4,5)
product = reduce(lambda pro,item : pro * item,t)
print(product)

from functools import reduce

d = {'mysql':10,'python':40,"html":90,"java":30}
sumup = reduce(lambda s, i: s + d[i], d, 0)  # Start from 0
print(sumup)

'''
Reduce:  10
css mysql java python html
120
170

=== Code Execution Successful ===
'''








