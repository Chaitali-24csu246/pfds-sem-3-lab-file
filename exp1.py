#Experiment 1
#Variable assignment and math operations program

# integers
a = 10
b = 3

# float
x = 4.5
y = 2.0

# string (just for fun, won't be used in math)
name = "Math Demo"

print("----", name, "----")

# basic operations
sum_int = a + b
diff_int = a - b
prod_int = a * b
div_int = a / b   # division gives float

print("Integer operations:")
print(a, "+", b, "=", sum_int)
print(a, "-", b, "=", diff_int)
print(a, "*", b, "=", prod_int)
print(a, "/", b, "=", div_int)

print()

# float operations
sum_float = x + y
pow_float = x ** y
mod_float = x % y

print("Float operations:")
print(x, "+", y, "=", sum_float)
print(x, "**", y, "=", pow_float)
print(x, "%", y, "=", mod_float)

print()

# mixing int and float
mix = a * y + x
print("Mixing int and float gives:", mix)
