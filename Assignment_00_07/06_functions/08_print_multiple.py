def print_multiple(message: str, repeats: int):
    for i in range(repeats):
        print(repeats)


def main():
    message = input("Please type a message: ")
    repeats = int(input("How many times do you want to repeat it? "))
    print_multiple(message, repeats)


if __name__ == "__main__":
    main()
