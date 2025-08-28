"""Give the commands to print each fruit
in a fruit list, add a fruit to the list and  remove a fruit from the list."""
fruit=list()#Creating list
#Creating menu
while True:
    choice=input("Do you want to: \n A) Add a fruit\n B) Remove a fruit\n C)View all fruits : ") 
  #choice input
  #error handling
    if choice not in ['a','b','c','A','B','C']:
        print("Wrong input")
      #adding fruit
    elif choice in ['a','A']:
        a=input("Enter new fuit name")
        fruit.append(a)
        print("New fruit added")
      #removing
    elif choice in ['b','B']:
        a=input("Enter fruit name to be removed")
        if a in fruit:
            fruit.remove(a)
            print("Removed first occurrence of ", a," from list")
        else:
            print("Fruit not in list")
          #display
    else:
        for i in fruit:
            print(i)
    choice2=input("Click 'y' to exit")
    if choice2=='y' or choice2=='Y':
        break


