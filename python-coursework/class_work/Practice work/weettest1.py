#1.
date, month, year = input().split('-')
print(f"{year}/{month}/{date}")

#3.
n = input()
print(n.translate(str.maketrans("aeiouAEIOU","**********")))

n = input()
vol = "aeiouAEIOU"
for i in n:
    if i in vol:
        print("*",end = " ")
    else:
        print(i,end=" ")

#4.
n = list(map(float,input().split()))
print(sum(n))
print(max(n))

#5.
credentials = ("admin", "python123")
username = input()
password = input()
if username == credentials[0] and password == credentials[1]:
    print("Login Succesful")
else:
    print("acces denied")

#6.
names = set(input().split(','))
print(sorted(names))

#7.
n = int(input())
d = { }
max_val = 0
max_name = None
for i in range(n):
    name, marks = input().split()
    marks = int(marks)
    if marks >= max_val:
        max_value = marks
        max_name = name
        
    d[name] = marks
    
print(max_name)    

#8.
n = input().split()
for i in n:
    print(i[::-1],end = " ")

#9.
l = list(map(int,input().split()))

while 0 in l:
    l.remove(0)
print(l)    

#10.
n = input()
d = {}
for i in n:
    if i != " " or i not in d:
        d[i] = n.count(i)
print(d)   



