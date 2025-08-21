#EXPERIMENT 4
#Check if number is prime or armstrong without function
#do with function later when covered
num=int(input("Enter a number : "))
# Prime number check
if num>1 :
    for i in range(2, num):
        if num % i == 0:
            print(num, "is NOT a prime number")
            break
    else:
        print(num, "is a PRIME number")#not necessary to indent ar same place as if in this case
else:
    print(num, "is NOT a prime number")
#Armstrong number
l=len(str(num))#getting length of number
sum=0 #initalizing sum for armstrong number
for i in str(num):#iterating throught string
    i=int(i)#converting back for calculation
    sum+=i**l #calculating armstrong number
#armstrong number condition and then output
if(sum==num):
    print("Is Armstrong number")
else:
    print("Isn't Armstrong number")
    
