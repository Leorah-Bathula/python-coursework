hr,mins = list(map(int,input("Enter the HH:MM  :").split(":")))

if hr >= 0 and hr <= 24 and mins > 0 and mins <= 60 :
    if hr >= 0 and hr < 4:
        print("It's high time. Time to sleep")
    elif hr >= 4 and hr < 12:
        print("Good morning! Have a nice day ")
    elif hr >= 12 and hr < 16:
        print("Good afternoon! Yum Lunch time")
    elif hr >= 16 and hr < 20:
        print("Good evening! Play time")
        
    elif hr >= 20 and hr < 24:
        print("Good night!Time to sleep")

else:
    print("Enter the proper input , invalid input !")

    
#2 To check the number of seats availble using if else:
seats = {
    'L1': True,
    'L2': False,
    'L3': True,
    'L4': True,
    'L5': False,
    'U1': True,
    'U2': False,
    'U3': True,
    'U4': True,
    'U5': False,
    
}

seat_no = input("Enter the seat number to check its availabilty: ").upper()

if seat_no in seats:
    if seats[seat_no]:
        print("Already Booked. Try with other number")
        
    else:
        print("Seat is available. Hurry up")
else:
    print("Enter the correct seat number")
        

# Check the product availablity using if-else:
data = {
    'watch' :  {'discount':10, 'brands':['titan','fastrack']},
    'jeans' :  {'discount':60, 'brands':['denim','roadster']},
}

print(data.keys())
product = input("Enter the category: ")

if product in data:
    print(f"{data[product]["discount"]} % discount is going on for this brands {data[product]["brands"]}")
        
else:
    print(f"Product is not available. Check other products: {data}")            


# movie selection 
movies = {
    'Salar' :  {'kids' : True},
    'Starr' :  {'kids' : True},
    'Arjunreddy' : {'kids' : False},
    'Teddy' :  {'kids' : False}
    
}

print("Welcome to hotstar".center(30,"="))
movie = input("ENter the movie name: ").title()

if movie in movies:
    if movies[movie]["kids"]:
        print(f"Good selection you can watch with your family\n{movie}...")
    else:
        print(f"Adult movie kids are not allowed\n{movie}...")
        
else:
    print(f"{movie} is not availble")
    
        