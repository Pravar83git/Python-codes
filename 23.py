def perf_num(n):
    if n<2:
        return False
    divisors_sum = 1
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            divisors_sum+=1
            if i!=n//i:
                divisors_sum+=n//i
    return divisors_sum
number= int(input("Enter a number: "))
if perf_num(number):
    print(f"{number} is a Perfect number")
else:
    print("Not a perfect number")
print("Program by Pravar")