num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    rem = num%10 # last digit
    reverse= (reverse * 10)+ rem
    num = num//10 # remaning number
print(reverse)