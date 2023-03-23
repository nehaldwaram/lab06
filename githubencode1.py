def print_menu():
    # initializes and prints main menu
    print(f'Menu')
    print(f'-------------')
    print(f'1. Encode\n2. Decode\n3. Quit')
    print()


def encode(password):
    # takes in password to be encoded from user
    encoded = ''
    for element in password:
        # adds 3 to each element in password
        if int(element) < 7:
            element = str(int(element) + 3)
        elif int(element) == 7:
            element = '0'
        elif int(element) == 8:
            element = '1'
        elif int(element) == 9:
            element = '2'
        # adds new element to encoded string
        encoded += str(element)
    return encoded                      # returns encoded string

def decode(password):
    #takes in encoded password and returns decoded password
    decoded = ''
    password = str(password)
    for a in password:
        a = int(a)
        if a == 0:
            a = 7
        elif a == 1:
            a = 8
        elif a == 2:
            a = 9
        else:
            a = a - 3
        decoded += str(a)
    return decoded
print(decode(45678888))
if __name__ == "__main__":
    running = True
    while True:
        print_menu()
        # prompt user to choose an option
        option = int(input(f"Please enter an option: "))
        if option == 1:
            # prompt user to enter password
            user_input = input("Please enter your passcode to encode: ")
            # encode and store password into a new variable 
            encode_password = encode(user_input)
            print(f"Your password has been encoded and stored! ")
            print()
        elif option == 2:
            # print the encoded and decoded passwords
            decoded_password = decode(encode_password)
            print(f"The encoded password is {encode_password}, and the original password is {decoded_password} ")
            print()
        elif option == 3:
            # exit program
            break
