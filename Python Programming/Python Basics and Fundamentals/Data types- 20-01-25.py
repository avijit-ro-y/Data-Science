#---------------------------------Operators---------------------------------
a = 5
b = 3

addition = a + b # Addition of numbers
subtraction = a - b # Subtraction of numbers
multiplication = a * b # Multiplication of numbers
division = a / b # divison of a by b
floor_division = a // b # floor division of a by b
modulo = a % b # Modulo of a by b
exponent = a ** b # # Power

print("Operands are:", a, "and", b)
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Floor division:", floor_division)
print("Mudulo:", modulo)
print("Exponent:", exponent,'\n')

#---------------------------------Comparison Operators---------------------------------
a = 5
b = 3

print("a:", a, "b:", b)
print("a greater than b:", a > b)

print("a less than b:", a < b)

print("a equals to b:", a == b)

print("a not equal to b:", a != b)

print("a greater than equal to b", a >= b)

print("a less than equal to b", a <= b,'\n')

#---------------------------------Logical Operators---------------------------------
a = True
b = False

print(f"{a} and {b}: {a and b}")
print(f"{a} or {b}: {a or b}")
print(f"not {a}: {not a}",'\n')

#---------------------------------Bitwise Operators---------------------------------
a = 50 # 110010
b = 5 #  000101

print("Here, '0b' at the start of binary number in the \nbelow two statements is how python stores binary numbers")
print(f"Binary Represention of {a}: {bin(a)}")
print(f"Binary Represention of {b}: {bin(b)}")

# Print bitwise AND operation
print(f"\nBitwise AND on {a}, {b}: {a & b}")
print(f"\nBitwise OR on {a}, {b}: {a | b}")
print(f"\nBitwise NOT on {a}: {~a}")
print(f"\nBitwise XOR on {a}, {b}: {a ^ b}")
print(f"\nBitwise RIGHT SHIFT on {a}: {a >> 2}")
print(f"\nBitwise LEFT SHIFT on {a}: {a << 2}",'\n')

#---------------------------------Assignment Operators---------------------------------
a = 10
b = 5

# perform += opertor b+=a => b = b+a
b += a
print(b)

# Subtract and assign value b-=a => b = b-a
b -= a
print(b)

# multiply and assign b*=a => b = b * a
b *= a
print(b)

# bitwise AND operator b&=a => b = b & a
b &= a
print(b,'\n')

#---------------------------------Identity Operators---------------------------------
a = 20
b = 15
c = 20
print(a is c)

#---------------------------------Membership Operators---------------------------------
x = 2
y = 8

lst = [1, 2, 3, 4, 5]

print(f"{x} in {lst}: {x in lst}")
print(f"{y} not in {lst}: {y not in lst}",'\n')

#---------------------------------Ternary Operators---------------------------------
a = 10
b = 5
c = 15

min_value = a if a < b else b
print(min_value)

min_value = c if c > b  else b
print(min_value,'\n')
