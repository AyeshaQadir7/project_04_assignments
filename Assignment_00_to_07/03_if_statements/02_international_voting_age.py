PETURKSBOUIPO_AGE: int = 16
STANLAU_AGE: int = 25
MAYENGUA_AGE: int = 48


def main():
    user_age = int(input("Enter your age: "))

    if user_age >= PETURKSBOUIPO_AGE:
        print(
            "You can vote in Peturksbouipo where the voting age is "
            + str(PETURKSBOUIPO_AGE)
            + "."
        )

    else:
        print(
            "You can not vote in Peturksbouipo where the voting age is "
            + str(PETURKSBOUIPO_AGE)
            + "."
        )

    # Check if the user can vote in Stanlau
    if user_age >= STANLAU_AGE:
        print(
            "You can vote in Stanlau where the voting age is " + str(STANLAU_AGE) + "."
        )
    else:
        print(
            "You can not vote in Stanlau where the voting age is "
            + str(STANLAU_AGE)
            + "."
        )

    # Check if user can vote in Mayengua
    if user_age >= MAYENGUA_AGE:
        print(
            "You can vote in Mayengua where the voting age is "
            + str(MAYENGUA_AGE)
            + "."
        )
    else:
        print(
            "You can not vote in Mayengua where the voting age is "
            + str(MAYENGUA_AGE)
            + "."
        )


if __name__ == "__main__":
    main()
