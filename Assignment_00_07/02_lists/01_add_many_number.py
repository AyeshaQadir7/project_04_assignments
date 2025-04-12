def add_many_nums(numbers) -> int:
    total: int = 0
    for number in numbers:
        total += number
    return total


def main():
    numbers: list[int] = [1, 2, 3, 4, 5]
    sum_of_nums: int = add_many_nums(numbers)
    print(sum_of_nums)


if __name__ == "__main__":
    main()
