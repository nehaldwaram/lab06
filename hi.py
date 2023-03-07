def print_menu():
    print(f'Menu')
    print(f'-------------')
    print(f'1. Encode\n2. Decode\n3. Quit')
    print()


def encode(password):
    encoded = ''
    for element in password:
        if int(element) < 7:
            element = str(int(element) + 3)
        elif int(element) == 7:
            element == '0'
        elif int(element) == 8:
            element == '1'
        elif int(element) == 9:
            element == '2'
        encoded += str(element)
    return encoded


if __name__ == "__main__":
    user_input = input()
    print(encode(user_input))

