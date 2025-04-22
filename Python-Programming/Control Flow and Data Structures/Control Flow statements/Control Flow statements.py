#---------------------------------break---------------------------------
# Iterate over a list/tuple and print the values. break the loop if a negative number is encounterd

lst = [1, 2, 75, 42, 50, -5, 7, 0, 100, 101, 102]

for number in lst:

    if number < 0:
        print("Negative number encounterd:", number)
        continue
    elif number == 0:
        pass
    else:
        print(5 / number)
print('\n')

#---------------------------------continue---------------------------------
# program to square numbers less than 10 while iterating a list/tuple

lst = [1, -2, -5, 10, 5, 9, 12]

for number in lst:
    if number >=10:
        print("Skiping the loop at number:", number)
        break
        print("asdfasdfasdf")

    print("square of:", {number}, " ", {number**2})

print('asdfasdfasdf')
print('\n')

#---------------------------------pass---------------------------------
#kono loop er porer sobgulo (not to be current indentation) code skip korar jonno pass use kora hoy

for i in range(10):
    if i >5:
        print(i)
    else:
        pass

lis=[1,-2,-5,10,9,11]
for number in lis:
    if number >= 10:
        print("Skip",number)
        pass
    print(f"square of {number}:{number**2}")
print('\n')

#---------------------------------Example---------------------------------
operator = ''

while operator != 'Q':
    print("""
    Select the operation that you want to perform
    +: Addition
    -: Subtraction
    *: Multiplication
    /: Division
    Q: Quit
    """)
    operator = input("Select +, -, *, / or Q: ")
    if operator == '+':
        operand_1 = float(input("Enter the 1st operand: "))
        operand_2 = float(input("Enter the 2nd operand: "))
        print(f"Addition of {operand_1} and {operand_2} = {operand_1 + operand_2}")
    elif operator == '-':
        operand_1 = float(input("Enter the 1st operand: "))
        operand_2 = float(input("Enter the 2nd operand: "))
        print(f"Subtraction of {operand_1} and {operand_2} = {operand_1 - operand_2}")
    elif operator == '*':
        operand_1 = float(input("Enter the 1st operand: "))
        operand_2 = float(input("Enter the 2nd operand: "))
        print(f"Multiplication of {operand_1} and {operand_2} = {operand_1 * operand_2}")
    elif operator == '/':
        operand_1 = float(input("Enter the 1st operand: "))
        operand_2 = float(input("Enter the 2nd operand: "))
        print(f"Division of {operand_1} and {operand_2} = {operand_1 / operand_2}")
    elif operator == 'Q':
        print("Exiting the calculator program")
        break
    else:
        print("\n\nPlease enter a valid choice")