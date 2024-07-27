import sys

letters = 'abcdefghijklmnopqrstuvwxyz'

def main():
    print('*** CAESAR CIPHER PROGRAM ***')
    message = str(input("Enter the message: "))
    key = int(input("Enter the shift value: "))
    check(message, key)

def check(message, key):
    choice = input("Press 'e' to encrypt, 'd' to decrypt and 'q' to quit: ")
    if choice.lower() == 'e':
        print(encrypt(message, key))
    elif choice.lower() == 'd':
        print(decrypt(message, key))
    elif choice.lower() == 'q':
        sys.exit()
    else:
        print('Invalid Choice, Try Again')
        check(message, key)

def encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        letter = letter.lower()
        if letter != ' ':
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = (index + key) % 26
                ciphertext += letters[new_index]
        else:
            ciphertext += ' '
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    for letter in ciphertext:
        letter = letter.lower()
        if letter != ' ':
            index = letters.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = (index - key) % 26
                plaintext += letters[new_index]
        else:
            plaintext += ' '
    return plaintext

if __name__ == "__main__":
    main()    