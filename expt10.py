"""Give the commands to create a tuple of  computer parts, print the tuple.
Create  another tuple and join with the existing  one."""
newtuple=("CPU","MONITOR","KEYBOARD","MOUSE")#create tuple 1
newtuple2=("WEBCAM","MICROPHONE","SPEAKERS") #create tuple 2
#print tuple 1
print("tuple 1")
for i in newtuple:
    print(i)
finaltuple=newtuple+newtuple2 #joining tuples
#print tuple 2
print("tuple 2")
for i in newtuple2:
    print(i)
print("Joined 2 tuples")
for i in finaltuple:
    print(i)

