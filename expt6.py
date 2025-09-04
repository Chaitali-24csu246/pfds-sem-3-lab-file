# STRING OPERATIONS AND BUILT-IN FUNCTIONS IN PYTHON
#EXPT 6
print("====== STRING CREATION ======")
str1 = "Hello"
str2 = 'World'
str3 = """Multi-line
string"""
print("str1:", str1)
print("str2:", str2)
print("str3:", str3)

print("\n====== INDEXING AND SLICING ======")
sample = "PythonProgramming"
print("Original:", sample)
print("First character:", sample[0])
print("Last character:", sample[-1])
print("Slice [0:6]:", sample[0:6])
print("Slice [6:]:", sample[6:])
print("Reversed:", sample[::-1])

print("\n====== CONCATENATION AND REPETITION ======")
print("Concatenation:", str1 + " " + str2)
print("Repetition:", str1 * 3)

print("\n====== MEMBERSHIP TESTING ======")
print("'Python' in sample?", "Python" in sample)
print("'Java' not in sample?", "Java" not in sample)

print("\n====== BUILT-IN STRING METHODS ======")
text = "  hello, PYTHON world!  "
print("Original text:", repr(text))
print("strip():", text.strip())
print("lower():", text.lower())
print("upper():", text.upper())
print("title():", text.title())
print("capitalize():", text.capitalize())
print("swapcase():", text.swapcase())
print("replace('PYTHON', 'Java'):", text.replace("PYTHON", "Java"))
print("count('o'):", text.count('o'))
print("find('world'):", text.find('world'))
print("rfind('o'):", text.rfind('o'))
print("startswith('  he'):", text.startswith("  he"))
print("endswith('!  '):", text.endswith("!  "))

print("\n====== STRING TESTING METHODS ======")
alphanum = "Python123"
space_str = "   "
print("isalnum():", alphanum.isalnum())
print("isalpha():", str1.isalpha())
print("isdigit():", "12345".isdigit())
print("islower():", str1.islower())
print("isupper():", str2.isupper())
print("isspace():", space_str.isspace())

print("\n====== STRING FORMATTING ======")
name = "Alice"
age = 30
print("Using format(): Hello, {}. You are {} years old.".format(name, age))
print(f"Using f-string: Hello, {name}. You are {age} years old.")

print("\n====== ESCAPE CHARACTERS ======")
print("Newline:\\n -> Hello\nWorld")
print("Tab:\\t -> Hello\tWorld")
print("Backslash:\\\\ -> A\\B\\C")
print("Quote: \"Hello\"")

print("\n====== RAW STRINGS ======")
print(r"This is a raw string: C:\new_folder\test")

print("\n====== SPLIT AND JOIN ======")
csv = "apple,banana,cherry"
print("split(','):", csv.split(","))
words = ['Join', 'these', 'words']
print("join with space:", " ".join(words))

print("\n====== STRING LENGTH ======")
print("len('Python'):", len("Python"))

print("\n====== STRING COMPARISON ======")
print("'apple' == 'apple':", 'apple' == 'apple')
print("'Apple' < 'apple':", 'Apple' < 'apple')  # Case-sensitive

print("\n====== STRING ITERATION ======")
for char in "Hi!":
    print(char)
