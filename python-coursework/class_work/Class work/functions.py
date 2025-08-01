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



