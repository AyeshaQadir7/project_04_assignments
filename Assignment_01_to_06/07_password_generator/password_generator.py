import random

print("Welcome To Password Generator")


chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*().,?0123456789"

number = input("Amount of passwords to generate: ")
number = int(number)

length = input("Input your password lenght: ")
length = int(length)

print("\nHere are your password: ")

for pwd in range(number):
    passwords = ""
    for c in range(length):
        passwords += random.choice(chars)

    print(passwords)
