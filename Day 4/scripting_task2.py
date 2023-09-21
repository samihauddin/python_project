import os

#path = './os_scripting'

#os.mkdir(path)


# user creating own directory

dir_name = input("What would you like the directory to be called?")

os.mkdir(dir_name)
print(f"Directory '{dir_name} has been created")