import hashlib


def generate_md5(word):
    """Generate MD5 hash of the given word."""
    return hashlib.md5(word.encode()).hexdigest()


def caesar_encrypt(word, shift=3):
    """Encrypt word using Caesar Cipher with a given shift."""
    encrypted = ""
    for char in word:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted


def caesar_decrypt(word, shift=3):
    """Decrypt word by reversing the Caesar Cipher shift."""
    return caesar_encrypt(word, -shift)


def main():
    print("=" * 45)
    print("      MD5 Hash & Caesar Cipher Program")
    print("=" * 45)

    word = input("\nEnter a word: ")

    md5_hash = generate_md5(word)
    encrypted = caesar_encrypt(word)
    decrypted = caesar_decrypt(encrypted)

    print(f"\nMD5 Hash:       {md5_hash}")
    print(f"Encrypted Word: {encrypted}")
    print(f"Decrypted Word: {decrypted}")
    print("\n" + "=" * 45)


if __name__ == "__main__":
    main()