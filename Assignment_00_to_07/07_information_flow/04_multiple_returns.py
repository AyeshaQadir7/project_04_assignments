def get_user_info():
    first_name: str = input("Enter your first name: ")
    last_name: str = input("Enter your last name: ")
    email: str = input("Enter you email address: ")

    return first_name, last_name, email


def main():
    user_data = get_user_info()
    print("Received user data:", user_data)


if __name__ == "__main__":
    main()
