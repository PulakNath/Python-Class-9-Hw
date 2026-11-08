num = int(input("Enter a number: "))
digits = 0
while num // 10 > 0:
    digits += 1
    num //= 10
print("The number of digits is:", digits + 1)