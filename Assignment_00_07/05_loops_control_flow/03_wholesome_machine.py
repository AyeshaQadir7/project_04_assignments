AFFRIMATION: str = "I am capable of doing anything I set my mind to."


def main():
    print("Please type the following affrimation: " + AFFRIMATION)

    user_feedback = input()
    while user_feedback != AFFRIMATION:
        print("Please try again.")
        user_feedback = input()
        print("Please type the folowing affirmation: " + AFFRIMATION)
        user_feedback = input()

    print("That's right! :)")


if __name__ == "__main__":
    main()
