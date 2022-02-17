# python program to cheak number is positive or negative

num = int(input("Enter a number: "))
if num > 0:
    print(f"{num} is positve")
elif num == 0:
    print(f"{num} is neutral")
else:
    print(f"{num} is negative")