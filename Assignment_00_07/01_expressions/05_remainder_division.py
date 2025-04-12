def main():
    dividend: int = int(input("Enter the interger to be divided: "))
    divisor: int = int(input("Enter the interger to divide by: "))

    quotient: int = dividend // divisor
    remainder: int = dividend % divisor

    print(
        "The result of this division is "
        + str(quotient)
        + " with a remainder of "
        + str(remainder)
    )


if __name__ == "__main__":
    main()
