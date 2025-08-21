#EXPERIMENT 5
#Program to illustrate use of existing  math functions in Python (log, sin, cos,  abs etc.)
# Program to illustrate essential math functions in Python
import math
print("Math Functions Demo\n")
# numbers to use
num1 = -25
num2 = 16
angle = math.pi / 6   # 30 degrees in radians pi/6=30 deg
# absolute value
print("abs(", num1, ") =", abs(num1))

# square root
print("sqrt(", num2, ") =", math.sqrt(num2))

# powers and exponentials
print("pow(2, 5) =", math.pow(2, 5))
print("exp(2) =", math.exp(2))

# logarithms
print("log(", num2, ") =", math.log(num2))      # natural log
print("log10(", num2, ") =", math.log10(num2))  # base 10 log

# trigonometric functions
print("sin(30°) =", math.sin(angle))
print("cos(30°) =", math.cos(angle))
print("tan(30°) =", math.tan(angle))

# inverse trig functions
print("asin(0.5) =", math.degrees(math.asin(0.5)), "degrees")
print("acos(0.5) =", math.degrees(math.acos(0.5)), "degrees")
print("atan(1) =", math.degrees(math.atan(1)), "degrees")

# conversions
print("degrees(pi/6) =", math.degrees(angle))
print("radians(180) =", math.radians(180))

# constants
print("Value of pi =", math.pi)
print("Value of e  =", math.e)

# rounding functions
print("ceil(4.3) =", math.ceil(4.3))
print("floor(4.7) =", math.floor(4.7))

# factorial, lcm, and gcd(hcf)
print("factorial(5) =", math.factorial(5))
print("gcd(24, 36) =", math.gcd(24, 36))
print("lcm(22,4,6,8) =",math.lcm(22,4,6,8))
