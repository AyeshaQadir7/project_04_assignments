import random

NUM_SIDE: int = 6


def main():
    die1: int = random.randint(1, NUM_SIDE)
    die2: int = random.randint(1, NUM_SIDE)

    total: int = die1 + die2

    print("Dice have ", NUM_SIDE, " sides.")
    print("First die: ", die1)
    print("Second die: ", die2)
    print("Total: ", total)


if __name__ == "__main__":
    main()
