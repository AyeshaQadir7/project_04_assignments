import math


def main():
    ab: float = float(input("Enter the lenght of AB: "))
    ac: float = float(input("Enter the lenght of AC: "))

    bc: float = math.sqrt(ab**2 + ac**2)

    print(f"The length of BC is ( the hypotenuse) is: " + str(bc))


if __name__ == "__main__":
    main()
