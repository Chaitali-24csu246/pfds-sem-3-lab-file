"""Give the commands to find length of  the list and check if a fruit exists
in the  list, create copy of the list."""
fruit=["Apple", "Mango", "Banana", "Grapes", "Guava", "Peach", "Plum"]#Creating list
print("Length of list fruit is : ", len(fruit))#length
checkfruit=input("Enter fruit yu want to find in list: ")#checking if fruit in list
if checkfruit in fruit:
    print("Fruit in list")
else:
    print("Not in list")
fruitcopy=fruit.copy()#making a copy
print("Copy created")
