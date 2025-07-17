''' Type Conversion (Type Casting)
Type conversion in Python refers to converting the value of one data type to another using
built-in functions such as int(), float(), str(), bool(), list(), tuple(), set(),
and dict().'''

# 1. Converting from int
int_a = 3
print(float(int_a))
print(str(int_a))
print(bool(int_a))

''' print(list(int_a))
print(set(int_a))
print(tuple(int_a))
print(dict(int_a)) int is not iterable for list, tuple, set, dict these raise an error'''

#2. Converting from float
float_n = 3.2 
print(int(float_n)) #Truncates decimal part
print(str(float_n))
print(bool(float_n))

''' print(list(float_n))
print(set(float_n))
print(dict(float_n))
print(tuple(float_n)) float is not iterable for list, tuple, set, dict these raise an error'''

#3. Converting from str
str_c = "Kitty"
print(int('10')) # output : 10 only numeric strings

''' print(int('10.9')) #  Error , use float() instead
print(int(str_c)) # error , invalid literal ''' 

print(float('10.8')) # Valid float string 
# print(float(str_c)) error 

print(bool(str_c))
print(list(str_c)) # ['K', 'i', 't', 't', 'y'] Converts to list of characters
print(tuple(str_c)) # ('K', 'i', 't', 't', 'y') Valid
print(set(str_c)) # {'t', 'y', 'K', 'i'} removes duplicates
# print(dict(str_c)) needs list of key-value pairs


# 4. Converting from list
list_d = [1,2,4,5,6,7]
#print(int(list_d)) errror
#print(float(list_d)) error

print(str(list_d))
print(bool(list_d))
print(tuple(list_d))
print(set(list_d))

# print(dict(list_d)) needs list of key-value pairs

# 5. Converting from tuple
tuple_f = (1,2,3,4)
# print(int(tuple_f)) error 
# print(float(tuple_f)) error 

print(str(tuple_f))
print(bool(tuple_f))
print(list(tuple_f))
print(set(tuple_f))
#print(dict(tuple_f)) must be key-value pairs 

# 6. Converting from set
set_e = {9,3,4,5}
''' print(int(set_e))
print(float(set_e)) Error '''

print(str(set_e))
print(bool(set_e))
print(list(set_e))
print(tuple(set_e))

# print(dict(set_e)) error must be key-value pairs 

# 7. Converting from dict
dict_g = {"color":"blue","num":21,"jars": 98}
''' print(int(dict_g))
print(float(dict_g)) error '''

print(str(dict_g))
print(bool(dict_g))
print(list(dict_g)) # Keys only
print(tuple(dict_g)) # Keys only
print(set(dict_g)) # Keys only

# 8. Converting from bool
boolean = False
print(int(False))
print(int(True))
print(float(False))
print(float(True))
print(str(True))
print(str(False))

''' print(list(False))
print(tuple(False))
print(set(False))
print(dict(False))   error not iterable '''

#9. Dictionary Conversion
# To convert a list to a dictionary, it must be a list of key-value tuples.
d = [('name','jes'),('batch',22)]
print(dict(d))






