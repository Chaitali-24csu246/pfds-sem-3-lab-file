#EXPERIMENT 3
#Write a program to print each letter of a  word. Repeat this process for at least  five words.

print("You will enter 5 words")
l=list()#creating list for words
#taking input 5 times
for i in range(5):
    print("Enter word ",i+1)
    word=input()
    #adding word to list
    l.append(word)
print("Displaying letters:")
for i in l:
    #nesting loops to iterate through string
    for n in i:
        print(n)
    print("\n")
