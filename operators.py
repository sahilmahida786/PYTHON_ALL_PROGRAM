print("HELLO ALL OPERATORS")

#FIRST OPERATORS = ( ARITHMETIC OPERATOR )
a = 56
b = 39
print ( a + b )  #(ADDITION)
print ( a - b )  #(SUBTRACTION)
print ( a * b )  #(MULTIPLICATION)
print ( a / b )  #(DIVISION)
print ( a % b )  #(MODULUS)
print ( a ** b )  #(EXPONENTIATION)
print ( a // b )  #(FLOOR DIVISION)

#SECOND OPERATORS = (ASSIGNMENT OPERATOR)

x = 45
x += 30
print ( x ) #(ADDITION)

x = 45
x -= 30
print ( x ) #(SUBTRACTION)

x = 45
x *= 30
print ( x ) #(MULTIPLICATION)

x = 45
x /= 30
print ( x )  #(DIVISION)

x = 45
x %= 30
print ( x )  #(MODULUS)

#THIRD OPERATORS = (COMPARISON OPERATOR)

a = 55
b = 35

print ( a == b )  # (EQUAL TO)
print ( a != b)   # (NOT EQUAL TO)
print ( a < b )   # (GREATER THAN)
print ( a > b )   # (LESS THAN)
print ( a <= b )  # (GREATER THAN EQUAL TO)
print ( a >= b )  # (LESS THAN EQUAL TO)


#(FOURTH OPERATORD) = (LOGICAL OPERATOR)

x = 5

print(x > 3 and x < 10) #AND   (BOTH STATEMENT ARE RIGHT THAN TRUE)
print(x > 3 or x < 4)   #OR    (ONE STATEMENT ARE RIGHT THAN TRUE)
print(not(x > 3 and x < 10)) #NOT REVERSE OF AND(BOTH ARE WORNG THAN TRUE)


# Math library
import math
print(math.e)               #math.e value(2.71) (we are use in non-linear increase or decrease growth population)
print(math.ceil(21.9))      #math.ceil (0.9 = 1) 
print(math.pi)              #math.pi(3.14)
print(math.fsum([2,56,90])) #math.fsum(one by one plus a value)
print(math.floor(69.8))     #math.floor(value are convet in to integer)
print(math.factorial(3))    #math.factorial 1*2*3