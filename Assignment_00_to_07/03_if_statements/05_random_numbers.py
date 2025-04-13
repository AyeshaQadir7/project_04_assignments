import random

N_NUMBERS = 10
MIN__RANGE = 1
MAX_VALUE = 100


def main():
    for _ in range(N_NUMBERS):
        value = random.randint(MIN__RANGE, MAX_VALUE)
        print(value)


if __name__ == "__main__":
    main()
