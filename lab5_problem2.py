# ==================================================
# IT 2750 - Scripting Fundamentals for Cybersecurity
# Cuyahoga Community College
# Lab 5 – Problem 2
# ==================================================
# Student Name: YOUR_NAME_HERE
# Student Email: YOUR_EMAIL_HERE
# ==================================================

alphabet = "abcdefghijklmnopqrstuvwxyz"
key = "zjrekydnqoluaxmicvpgtfbhws"

# Encrypt a message using a key and output ciphertext
def encrypt_message(plaintext, key):
    # Create a placeholder variable to store the ciphertext
    ciphertext = ""

    # Iterate through each character in the plaintext message
    for char in plaintext:

        # If the character is in the alphabet, replace the
        # character in the alphabet with the corresponding
        # character in the key and add it to the ciphertext.
        # If it is not (find returns -1), add the character
        # as-is (space, uppercase letter, symbol, etc.)
        if alphabet.find(char) > -1:
            ciphertext += key[alphabet.find(char)]
        else:
            ciphertext += char

    # Return the encrypted text
    return ciphertext

# PART A
# ======
# Create a function, decrypt_message, that decrypts ciphertext created using
# the encrypt_message function. The decrypt_message function should have two
# parameters: ciphertext and key, where ciphertext is the ciphertext generated
# by the encrypt_message function and the key is the symmetric key used
# to encrypt the original method. The function should output the decrypted
# plaintext.
#
# Hint: the plaintext sent to encrypted_text as an argument for the plaintext
# parameter should match the output of decrypt_message function

## YOUR CODE HERE ##

def main():  # DO NOT EDIT THIS LINE

    print("Welcome to the Encryption System!")

    # PART B
    # ======
    # Ask the user for text to encrypt, "What text would you like to encrypt?",
    # using an input call and saving into a variable called input_text

    ## YOUR CODE HERE ##
    input_text = input("What text would you like to encrypt? ")

    # PART C
    # ======
    # Create a new variable called encrypted_text and set its value to be the output
    # from a function call to encrypt_message, passing along the input_text and
    # the key

    ## YOUR CODE HERE ##

    # PART D
    # ======
    # Create a new variable called decrypted_text and set its value to be the output
    # from a function call to decrypt_message, passing along the encrypted_text and
    # the key

    ## YOUR CODE HERE ##

    # PART E
    # ======
    # Display the input_text, encrypted_text, and decrypted_text on three lines in
    # the following format:
    #
    #     Original message: input_text
    #     Encrypted message: encrypted_text
    #     Decrypted message: decrypted_text
    #
    # You should replace input_text, encrypted_text, and decrypted_text with the values
    # of those variables. Do not add any additional content and make sure each print
    # statement displays on a separate line

    ## YOUR CODE HERE ##

    return  # DO NOT EDIT THIS LINE

if __name__ == "__main__":  # DO NOT EDIT THIS LINE
    main()                  # DO NOT EDIT THIS LINE