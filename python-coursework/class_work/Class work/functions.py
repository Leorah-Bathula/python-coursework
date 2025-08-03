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


