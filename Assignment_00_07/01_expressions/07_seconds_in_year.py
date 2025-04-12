DAY_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MINUTES_PER_HOUR: int = 60
SECCONDS_PER_MINUTE: int = 60


def main():

    seconds_in_year: int = (
        DAY_PER_YEAR * HOURS_PER_DAY * MINUTES_PER_HOUR * SECCONDS_PER_MINUTE
    )

    print(f"There are {seconds_in_year} seconds in a year")


if __name__ == "__main__":
    main()
