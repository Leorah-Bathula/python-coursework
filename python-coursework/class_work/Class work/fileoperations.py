


'''try:
    with open("demo2.txt",'r+') as file:
        print(f"Read entire content: \n{file.read()}\n") 
        file.seek(0)   
        print(f"Read only first line: \n{file.readline()}\n") 
        file.seek(0)   
        print(f"Return all the lines in a list: \n{file.readlines()}\n") 
        file.write("\nmike\napple\nbanana")
        file.seek(0)
        print(file.read())
        file.close()

        
        
except FileNotFoundError:
    print("File is not there") 


  try:
    file = open("demo2.txt", "r+")   # allows both reading and writing

except FileNotFoundError:
    print("File is not there")    

else:
    print(f"Read entire content: \n{file.read()}\n") 
    file.seek(0)   
    print(f"Read only first line: \n{file.readline()}\n") 
    file.seek(0)   
    print(f"Return all the lines in a list: \n{file.readlines()}\n") 
    
    # write new content at the end
    file.write("\nmike\napple\nbanana")

    file.seek(0)   # go back to start
    print("After writing:")
    print(file.read())
    file.close() 


try:
    with open("demo.txt","a+") as file:
        
        file.write("End of the file")
        file.seek(0)
        print(file.read())
        file.close()

except FileNotFoundError:
    print("File is not there")


try:
    with open("demos.txt","w+") as file:
        
        file.write("End of the file")
        file.seek(0)
        print(file.read())
        file.close()

except Exception as e:
    print("Error Occured: ",e) '''    


#import os
#os.mkdir("Batch-31")

'''import os 

if not os.path.exists("Batch-31"):
    os.mkdir("Batch-31") # make an empty folder

os.rmdir("Batch-31")   # works for empty folder (remove an empty folder)

import os

os.makedirs("Batch-31\subchild") # make a folder inside folder

import os 
import shutil  # Removing the files which has content in it

shutil.rmtree("Batch-31")


import os
print(os.getcwd())

import os 
print(os.getcwd())
os.chdir('..')

import os 
print(os.getcwd())
print(os.listdir('.'))

import os 
filepath = os.path.join("1415","demo.txt")
with open(filepath,"w+") as f:
    f.write("Hello World")
    f.seek(0)
    print(f.read())


import os
filepath = os.path.join("1415","demo.txt")
os.remove(filepath)    '''











