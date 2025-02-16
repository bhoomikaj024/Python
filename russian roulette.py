import random
names = input("Enter the names separated by a space. \n")
list_names = names.split( )
list_len = len(list_names)
index = random.randint(0,list_len)
print(f"{list_names[index]} should pay the Bill.")

