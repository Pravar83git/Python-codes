a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
if (a>b) & (a>c):
    print(f"{a} is: greatest")
elif (b>a) & (b>c):
    print(f"{b} is: greatest")
else:
    print(f"{c} is: greatest")
print("Program by Pravar")