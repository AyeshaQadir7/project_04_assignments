def main():
    fruit: str = input("Enter a fruit: ")
    stock = num_in_stock(fruit)
    if stock == 0:
        print("This fruit is not in stock!")

    else:
        print("This fruit is in stock! Here is how many left:", stock)


def num_in_stock(fruit):
    if fruit == "apple":
        return 10
    elif fruit == "banana":
        return 24
    elif fruit == "orange":
        return 18

    else:
        return 0


if __name__ == "__main__":
    main()
