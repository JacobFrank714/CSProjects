
# ALGORITHM :
#       1. display the main menu and ask user what task they want performed
#       2. check what their answer is
#       3. depending on what the answer is, ask the user what the want encoded/decoded or quit the program
#       4. ask how many numbers they want to shift the message by
#       5. perform the encode/decode function
#       6. present the encoded/decoded message
#       7. start from the main menu until user wants to quit


# import statements

# functions
def encode(msg, shift):
    msg = msg.upper()
    en_msg = []
    for i in msg:
        if i == ' ':
            en_msg.append(i)
            continue
        if (ord(i)+shift) > ord('Z'):
            i = chr(ord(i)-26)
        en_msg.append(chr(ord(i)+shift))
    en_msg = ''.join(en_msg[:])
    return en_msg


def decode(msg, shift):
    msg = msg.upper()
    de_msg = []
    for i in msg:
        if i == ' ':
            de_msg.append(i)
            continue
        if (ord(i) - shift) < ord('A'):
            i = chr(ord(i) + 26)
        de_msg.append(chr(ord(i) - shift))
    de_msg = ''.join(de_msg[:])
    return de_msg


if __name__ == "__main__":
    # main program
    while True:
        choice = input('MAIN MENU\n'
                       '1) Encoding a string\n'
                       '2) Decode a string\n'
                       'Q) Quit\n'
                       'Enter your selection ==> ')
        print()
        if choice == '1':
            message = input('Enter (brief) text to encrypt: ')
            shift_number = int(input('Enter the number to shift letters by: '))
            print('Encrypted: {}\n'.format(encode(message, shift_number)))
            continue
        elif choice == '2':
            message = input('Enter (brief) text to decrypt: ')
            shift_number = int(input('Enter the number to shift letters by: '))
            print('Decrypted: {}\n'.format(decode(message, shift_number)))
            continue
        elif choice == 'Q' or choice == 'q':
            break
        else:
            continue
