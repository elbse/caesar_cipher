"""
Caesar Cipher Program
=====================
A simple implementation of the Caesar cipher — a substitution cipher
that shifts each letter in a message by a fixed number of positions
in the alphabet.

How it works:
  - Encryption: each letter is replaced by the letter 'shift' positions
    ahead in the alphabet. For example, with shift=3, 'A' becomes 'D'.
  - Decryption: the shift is reversed (negated), mapping each letter back
    to its original position.
  - Non-alphabetic characters (digits, spaces, punctuation) are left unchanged.
  - Letter case is preserved: uppercase stays uppercase, lowercase stays lowercase.

The translation table is built with str.maketrans(), which maps every character
in the original alphabet to its shifted counterpart. Applying it with
str.translate() processes the entire message in a single pass.
"""


# ---------------------------------------------------------------------------
# Core cipher logic
# ---------------------------------------------------------------------------

def caesar(text, shift, encrypt=True):
    """
    Apply the Caesar cipher to a string.

    Parameters
    ----------
    text    : str  — the message to encrypt or decrypt
    shift   : int  — number of positions to shift (1–25)
    encrypt : bool — True to encrypt, False to decrypt (default True)

    Returns
    -------
    str — the transformed message, or an error string for invalid input
    """

    # Validate that shift is an integer (guards against accidental float input)
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    # Only shifts 1–25 make sense; a shift of 0 or 26 would be a no-op
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    # The 26-letter alphabet — used as both the source and the basis for the
    # shifted version
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Decryption is just encryption with the opposite shift direction
    if not encrypt:
        shift = -shift

    # Build the shifted alphabet by slicing and rejoining:
    #   alphabet[shift:]  — letters from the shift point to 'z'
    #   alphabet[:shift]  — letters from 'a' up to (but not including) the shift point
    # Example: shift=3 → 'defghijklmnopqrstuvwxyzabc'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    # Create a character-to-character translation table for both cases.
    # str.maketrans maps each character in the first string to the character
    # at the same position in the second string.
    translation_table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted_alphabet + shifted_alphabet.upper()
    )

    # Apply the translation in a single pass; characters not in the table
    # (digits, spaces, punctuation) are passed through unchanged
    encrypted_text = text.translate(translation_table)
    return encrypted_text


def encrypt(text, shift):
    """
    Encrypt plaintext using the Caesar cipher.

    Parameters
    ----------
    text  : str — plaintext message
    shift : int — number of positions to shift right (1–25)

    Returns
    -------
    str — the encrypted (ciphertext) message
    """
    return caesar(text, shift)


def decrypt(text, shift):
    """
    Decrypt a Caesar-cipher message back to plaintext.

    Parameters
    ----------
    text  : str — ciphertext message
    shift : int — the shift value that was used to encrypt (1–25)

    Returns
    -------
    str — the original plaintext message
    """
    return caesar(text, shift, encrypt=False)


# ---------------------------------------------------------------------------
# Test cases
# ---------------------------------------------------------------------------

def run_tests():
    """
    Run three required test cases and print the results.

    Test 1 — Encryption  : verifies that a known plaintext encrypts correctly
    Test 2 — Decryption  : verifies that the ciphertext from Test 1 decrypts
                           back to the original plaintext
    Test 3 — Edge cases  : covers non-alphabetic characters, mixed case,
                           and the maximum shift value (25)
    """

    print('=' * 50)
    print('TEST CASES')
    print('=' * 50)

    # ------------------------------------------------------------------
    # Test 1: Encryption
    # Shift 'Hello, World!' by 3 → each letter moves 3 positions right.
    # 'H'→'K', 'e'→'h', 'l'→'o', 'o'→'r', 'W'→'Z', 'r'→'u', 'd'→'g'
    # Non-alphabetic characters (comma, space, exclamation) stay unchanged.
    # ------------------------------------------------------------------
    print('\nTest 1 — Encryption')
    plaintext = 'Hello, World!'
    shift_key = 3
    result = encrypt(plaintext, shift_key)
    expected = 'Khoor, Zruog!'
    status = 'PASS' if result == expected else 'FAIL'
    print(f'  Plaintext  : {plaintext}')
    print(f'  Shift      : {shift_key}')
    print(f'  Encrypted  : {result}')
    print(f'  Expected   : {expected}')
    print(f'  Result     : {status}')

    # ------------------------------------------------------------------
    # Test 2: Decryption
    # Feed the ciphertext from Test 1 back through decrypt() with the same
    # shift key; the output must match the original plaintext exactly.
    # ------------------------------------------------------------------
    print('\nTest 2 — Decryption')
    ciphertext = 'Khoor, Zruog!'
    result = decrypt(ciphertext, shift_key)
    expected = 'Hello, World!'
    status = 'PASS' if result == expected else 'FAIL'
    print(f'  Ciphertext : {ciphertext}')
    print(f'  Shift      : {shift_key}')
    print(f'  Decrypted  : {result}')
    print(f'  Expected   : {expected}')
    print(f'  Result     : {status}')

    # ------------------------------------------------------------------
    # Test 3: Edge cases
    #   (a) Maximum shift (25) — every letter shifts to just one step left
    #       in the alphabet. 'A'→'Z', 'B'→'A', etc.
    #   (b) Non-alphabetic characters — digits and punctuation must pass
    #       through unchanged.
    #   (c) Mixed case — uppercase and lowercase must be handled separately
    #       so case is preserved after the shift.
    # ------------------------------------------------------------------
    print('\nTest 3 — Edge cases')

    # (a) Maximum shift of 25
    edge_text = 'ABC xyz'
    edge_shift = 25
    result_a = encrypt(edge_text, edge_shift)
    expected_a = 'ZAB wxy'
    status_a = 'PASS' if result_a == expected_a else 'FAIL'
    print(f'\n  (a) Max shift (25)')
    print(f'      Input    : {edge_text}')
    print(f'      Encrypted: {result_a}')
    print(f'      Expected : {expected_a}')
    print(f'      Result   : {status_a}')

    # (b) Non-alphabetic characters unchanged
    edge_text_b = 'Test 123! #$%'
    result_b = encrypt(edge_text_b, 5)
    expected_b = 'Yjxy 123! #$%'
    status_b = 'PASS' if result_b == expected_b else 'FAIL'
    print(f'\n  (b) Non-alphabetic characters')
    print(f'      Input    : {edge_text_b}')
    print(f'      Encrypted: {result_b}')
    print(f'      Expected : {expected_b}')
    print(f'      Result   : {status_b}')

    # (c) Case preservation
    edge_text_c = 'PyThOn'
    result_c = encrypt(edge_text_c, 13)
    expected_c = 'ClGuBa'
    status_c = 'PASS' if result_c == expected_c else 'FAIL'
    print(f'\n  (c) Case preservation')
    print(f'      Input    : {edge_text_c}')
    print(f'      Encrypted: {result_c}')
    print(f'      Expected : {expected_c}')
    print(f'      Result   : {status_c}')

    print('\n' + '=' * 50)


# ---------------------------------------------------------------------------
# Interactive menu
# ---------------------------------------------------------------------------

def main():
    """
    Run the interactive Caesar Cipher menu.

    Presents a numbered menu allowing the user to encrypt a message,
    decrypt a message, or exit. Input is validated at each step before
    the cipher is applied.
    """

    while True:
        # Display the menu options on each loop iteration
        print('\nCaesar Cipher Menu')
        print('------------------')
        print('[1] Encryption')
        print('[2] Decryption')
        print('[3] Exit')
        print('------------------')

        choice = input('Choose an option [1][2][3]: ').strip()

        # Option 3: exit the program
        if choice == '3':
            print('Goodbye!')
            break

        # Reject anything that is not 1 or 2
        if choice not in {'1', '2'}:
            print('Invalid option, please choose 1, 2, or 3.')
            continue

        # --- Collect and validate the message ---
        text = input('Enter text: ')
        if not text:
            print('Text cannot be empty. Please try again.')
            continue

        # --- Collect and validate the shift key ---
        shift_input = input('Enter shift (1-25): ').strip()

        # isdigit() rejects floats, negative numbers written as '-3', and
        # any non-numeric string
        if not shift_input.isdigit():
            print('Shift must be an integer. Please try again.')
            continue

        shift = int(shift_input)

        # Enforce the valid range (isdigit() already blocks negatives)
        if shift < 1 or shift > 25:
            print('Shift must be between 1 and 25. Please try again.')
            continue

        # --- Apply the cipher and display the result ---
        try:
            if choice == '1':
                result = encrypt(text, shift)
                print('\nEncryption')
                print(f'Plaintext     : {text}')
                print(f'Shift key     : {shift}')
                print(f'Encrypted text: {result}')
            else:
                result = decrypt(text, shift)
                print('\nDecryption')
                print(f'Ciphertext    : {text}')
                print(f'Shift key     : {shift}')
                print(f'Decrypted text: {result}')

        except Exception as err:
            # Catch any unexpected runtime error so the program keeps running
            print(f'An error occurred: {err}. Please try again.')


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    # Run the test suite first so the output is visible before the menu starts
    run_tests()

    try:
        main()
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully without printing a traceback
        print('\nInterrupted by user. Exiting quietly.')