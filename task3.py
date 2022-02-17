# Python program to print sum of natural till user input

num = int(input("Enter a number: "))
sum_of_all = 0
while num > 0:
    sum_of_all = sum_of_all + num
    num = num - 1
print(f"Sum of numbers is {sum_of_all}")