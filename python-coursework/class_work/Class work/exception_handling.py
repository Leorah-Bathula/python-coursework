try:
    a = 12/6
    b = int(input("Enter the int: "))
    c = 3 + 6
    d = {1:2,2:4,5:7}
    i = d[2]
    l = [0,1,2,3,4]
    m = l[1]
    c = a + e 


except ZeroDivisionError:
    print("Can't divide with zero")   

except ValueError:
    print("Please enter the proper datatype")   

except TypeError:
    print("We can't add 2 diff types")      

except KeyError:
    print("We dont have that key")    

except IndexError:
    print("we dont have that index")    

except NameError:
    print("please define the var")    

try:
    a = 12/6
    b = int(input("Enter the int: "))
    c = 3 + 6
    d = {1:2,2:4,5:7}
    i = d[2]
    l = [0,1,2,3,4]
    m = l[1]
    c = a + e 


except ZeroDivisionError:
    print("Can't divide with zero")   

except ValueError:
    print("Please enter the proper datatype")   

except TypeError:
    print("We can't add 2 diff types")      

except KeyError:
    print("We dont have that key")    

except IndexError:
    print("we dont have that index")    

except NameError:
    print("please define the var")    


try:
    a = 12/6
    b = int(input("Enter the int: "))
    c = 3 + 6
    d = {1:2,2:4,5:7}
    i = d[2]
    l = [0,1,2,3,4]
    m = l[1]
    c = a + e 


except ZeroDivisionError:
    print("Can't divide with zero")   

except ValueError:
    print("Please enter the proper datatype")   

except TypeError:
    print("We can't add 2 diff types")      

except KeyError:
    print("We dont have that key")    

except IndexError:
    print("we dont have that index")    

except NameError:
    print("please define the var")    

'''
try:
    a = 12/6
    b = int(input("Enter the int: "))
    c = 3 + 6
    d = {1:2,2:4,5:7}
    i = d[2]
    l = [0,1,2,3,4]
    m = l[1]
    c = a + e 


except (ZeroDivisionError,ValueError,TypeError,KeyError,IndexError,NameError):
    print("Error occured")

    
'''  
'''
try:
    a = 12 / 6
    print("a =", a)

    b = int(input("Enter the int: "))
    print("b =", b)

    c = 3 + 6
    print("c =", c)

    d = {1: 2, 2: 4, 5: 7}
    i = d[2]
    print("i =", i)

    l = [0, 1, 2, 3, 4]
    m = l[1]
    print("m =", m)

    # ❌ This will cause an error on purpose
    c = a + e   # 'e' not defined

except (ZeroDivisionError, ValueError, TypeError, KeyError, IndexError, NameError) as err:
    print(f"Error occurred: {err}")

'''

'''
try:
    print("a =", 12/6)
    print("b =", int(input("Enter an int: ")))
    print("c =", 3+6)
    print("i =", {1:2,2:4,5:7}[2])
    print("m =", [0,1,2,3,4][1])
    print("test =", 12/6 + e)   # ❌ error on purpose
except Exception as e:
    print("Error occurred:", e)

    
try:
except Exception as e:
else:
finally:
    
'''

