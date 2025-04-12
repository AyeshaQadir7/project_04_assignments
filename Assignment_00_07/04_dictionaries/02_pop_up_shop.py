def main():
    fruits = {"apple": 15, "banana": 10, "orange": 25, "kiwi": 35, "grape": 18}

    total_cost = 0
    for fruit_name in fruits:
        price = fruits[fruit_name]
        amount_bought = int(
            input("\033[1;3mHow many " + fruit_name + " you want?: \033[0m")
        )
        total_cost += price * amount_bought

    print("Total cost is " + str(total_cost))


if __name__ == "__main__":
    main()
