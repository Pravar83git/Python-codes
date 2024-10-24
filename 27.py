#WAP to swap two numbers
a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))

print("using 3 variables")
temp=a
a=b
b=temp
print(f'Numbers after swapping: {a}, {b}')

print("using 2 variables")

a=a+b
b=a-b
a=a-b
print(f'Numbers after swapping: {a}, {b}')

print("Program by Pravar")