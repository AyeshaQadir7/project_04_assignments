def in_range(n, low, high):
    return low <= n <= high  # Pythonic way to check if n is in the range


def main():
    n = int(input("Enter a number to check: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))

    if in_range(n, low, high):
        print(f"{n} is in the range!")
    else:
        print(f"{n} is NOT in the range.")


if __name__ == "__main__":
    main()
