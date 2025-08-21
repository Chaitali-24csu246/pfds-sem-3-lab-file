#EXPERIMENT 2
#Write a Program to display a number if  it is positive or negative and check if  integer is odd or even. Apply it to n  numbers.
n=int(input("Enter number of numbers you want to enter : "))
for i in range (0,n):
    number=int(input("Enter a number"))
  #check odd or even
    if(number%2==0):
        print(number," is an even number")
    else: 
        print(number,"is an odd number")
    #check positive negative
    if(number<0):
        print(number,"is a negative integer")
    else:
        print(number,"is a positive integer")
