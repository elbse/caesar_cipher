# Caesar Cipher Activity

def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(
        alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text


def encrypt(text, shift):
    return caesar(text, shift)


def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)


def main():
    while True:
        print('\nCaesar Cipher Menu')
        print('1. Encryption')
        print('2. Decryption')
        print('3. Exit')

        choice = input('Choose an option (1/2/3): ').strip()

        if choice == '3':
            print('Goodbye!')
            break

        if choice not in {'1', '2'}:
            print('Invalid option, please choose 1, 2, or 3.')
            continue

        text = input('Enter text: ')
        if not text:
            print('Text cannot be empty. Please try again.')
            continue

        shift_input = input('Enter shift (1-25): ').strip()

        if not shift_input.isdigit():
            print('Shift must be an integer. Please try again.')
            continue

        shift = int(shift_input)

        if shift < 1 or shift > 25:
            print('Shift must be between 1 and 25. Please try again.')
            continue

        try:
            if choice == '1':
                result = encrypt(text, shift)
                print(f'Encrypted: {result}')
            else:
                result = decrypt(text, shift)
                print(f'Decrypted: {result}')
        except Exception as err:
            print(f'An error occurred: {err}. Please try again.')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nInterrupted by user. Exiting quietly.')
