import random


def main():

    secret_number = random.randint(1, 99)

    print("I am thinking of aa number between 1 and 99...")

    guess = int(input("Enter a guess: "))

    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is low ")
        else:
            print("Your guess is high")

        print()
        guess = int(input("Enter a new guess: "))

    print("Congratulations! You guessed my number " + str(secret_number) + "!")


if __name__ == "__main__":
    main()
