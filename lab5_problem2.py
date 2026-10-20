# ==================================================
# IT 2750 - Scripting Fundamentals for Cybersecurity
# Cuyahoga Community College
# Lab 5 – Problem 2
# ==================================================
# Student Name: Kyle Quiros
# Student Email: S01026892@acad.tri-c.edu
# ==================================================

alphabet = "abcdefghijklmnopqrstuvwxyz"
key = "zjrekydnqoluaxmicvpgtfbhws"


# Encrypt a message using a key and output ciphertext
def encrypt_message(plaintext, key):
    ciphertext = ""

    for char in plaintext:
        if alphabet.find(char) > -1:
            ciphertext += key[alphabet.find(char)]
        else:
            ciphertext += char

    return ciphertext


# PART A
# ======
def decrypt_message(ciphertext, key):
    plaintext = ""

    for char in ciphertext:
        if key.find(char) > -1:
            plaintext += alphabet[key.find(char)]
        else:
            plaintext += char

    return plaintext


def main():  # DO NOT EDIT THIS LINE

    print("Welcome to the Encryption System!")

    # PART B
    # ======
    input_text = input("What text would you like to encrypt? ")

    # PART C
    # ======
    encrypted_text = encrypt_message(input_text, key)

    # PART D
    # ======
    decrypted_text = decrypt_message(encrypted_text, key)

    # PART E
    # ======
    print(f"Original message: {input_text}")
    print(f"Encrypted message: {encrypted_text}")
    print(f"Decrypted message: {decrypted_text}")

    return  # DO NOT EDIT THIS LINE


if __name__ == "__main__":  # DO NOT EDIT THIS LINE
    main()                  # DO NOT EDIT THIS LINE
