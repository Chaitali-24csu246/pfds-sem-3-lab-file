#factorial using recursive function
def factorial(n):
    if n<0:
        return "No factorial exists"
    if n==1 or n==0:
        return 1;
    else:
        return n*factorial(n-1)
a=int(input("Enter a number: "))
print("After evaluation for factorial, result is : \n", factorial(a))
