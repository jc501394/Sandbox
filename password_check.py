

MINIMUM_LENGTH = 8


def main():
    password_request = get_password(MINIMUM_LENGTH)
    print_asterisks(password_request)


def get_password(length):
    password = input("Enter password of at least {} characters: ".format(length))
    while len(password) < length:
        print("Password too short")
        password = input("Enter password of at least {} characters: ".format(length))
    return password
def print_asterisks(sequence):
    print('*' * len(sequence))


main()