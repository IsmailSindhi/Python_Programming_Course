# pyhton program to cheak prime number:

# This user input
num = int(input("Enter a number"))
for i in range(2,num):
    if num % i == 0: # condtion for prime numbers
        print(f"{num} is not prime")
        break
else:
    print(f"{num} prime")

