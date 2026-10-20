# IT 2750 - Scripting Fundamentals for Cybersecurity
## Lab 5 - String Manipulation and Encryption

### 🗒  Description
This repository contains the Python script for Lab 5 of the course IT 2750 - Scripting Fundamentals for Cybersecurity. There are two problems in this lab.

This lab encompasses two distinct yet crucial problems. The first problem, dubbed the "String Tester," engages students in sophisticated string manipulation techniques. It involves initializing variables with specific strings, performing character-by-character iteration, swapping characters, alphabetically shifting letters, and reversing the string, thus providing hands-on experience in critical text processing skills. The second problem shifts the focus to symmetric encryption, tasking students with the creation of an "Encryption System" script. This script enables encryption and decryption of user-provided text using a predefined key, demonstrating the encryption process while emphasizing the importance of key confidentiality in cybersecurity. Together, these problems equip students with essential skills in string operations and understanding the fundamentals of encryption and decryption, key aspects of data protection and cybersecurity.

#### Problem 1 - Performing Complex String Operations
Problem 1 focuses on creating a Python script called the "String Tester." In this lab, students work on various string manipulation tasks. They start by initializing two variables, `string1` and `string2`, with specific values ("ABCDEFG" and "TUVWXYZ" respectively), and then print each of these strings to the screen. Next, they iterate through each character in `string1` and `string2` separately, printing each character on a new line. The lab continues by swapping the odd characters in `string1` with the odd characters in "string2" and displaying both strings after the swap. Following this, students combine `string1` and `string2` into a new variable called `string3`. They manipulate `string3` by shifting letters in the alphabet: letters from 'A' to 'M' are shifted one character to the right, while letters from 'N' to 'Z' are shifted one character to the left. Lastly, they reverse the value of `string3` and print it to the screen. This lab exercise helps students gain hands-on experience in string manipulation, iteration, and basic text processing in Python, essential skills for cybersecurity and scripting tasks.

#### Problem 2 - Working with Symmetric Encryption
Problem 2 introduces students to encryption and decryption using a symmetric key. In this lab, students work on a Python script called the "Encryption System." The lab begins with the creation of an `encrypt_message` function that encrypts a user-provided text using a predefined key. The students are then prompted to enter a text message they would like to encrypt, and the script uses the `encrypt_message` function to encrypt it. Subsequently, a `decrypt_message` function is introduced to decrypt the encrypted text using the same key. The lab demonstrates the encryption and decryption processes, emphasizing the importance of maintaining the secrecy of the encryption key to protect sensitive information. This exercise helps students understand the basics of encryption and decryption, a fundamental concept in cybersecurity and data protection.

### 📝  Requirements
This lab requires you to write code that adheres to the following requirements:

#### Problem 1
In Problem 1, you will edit the script template to perform the following tasks:

- Part A: Creates two variables, `string1` and `string2`, and prints their values to the screen.
- Part B: Iterates through each character in `string1` and prints each character to a new line.
- Part C: Iterates through each character in `string2` and prints each character to a new line.
- Part D: Swaps the odd characters in `string1` with the odd characters in `string2` and prints both strings to the screen.
- Part E: Combines `string1` and `string2` into a new variable `string3`. For each character in `string3`, if it's a letter between A and M (inclusive), it changes the letter to the next letter to the right. If it's a letter between N and Z (inclusive), it changes the letter to the letter to the left. It then prints the value of `string3` to the screen.
- Part F: Reverses the value of `string3` and prints it to the screen.

#### Problem 2
In Problem 2, you will edit the script template to perform the following tasks:

- Part A: The script requires you to create a `decrypt_message` function that decrypts ciphertext created using the `encrypt_message` function.
- Part B: It asks the user for text to encrypt using an input call and saves it in a variable called `input_text`.
- Part C: The script encrypts the input text using the `encrypt_message` function and stores the result in a variable called `encrypted_text`.
- Part D: It decrypts the encrypted text using the `decrypt_message` function and stores the result in a variable called `decrypted_text`.
- Part E: The script displays the original input text, the encrypted message, and the decrypted message in a specific format.

#### Additional Requirements
In order to receive credit for this lab, you must replace `YOUR_NAME_HERE` with your name and `YOUR_EMAIL_HERE` with your Tri-C email address in the code file headers for all script files in the template. Students who do not perform this action will receive a zero score.

### 🚀  Usage
To run the script, execute the script file with Python. Each part of the lab problem is commented, and you should replace the placeholder text with your own information. From the code directory of this lab, you can run the various problems using the following commands:

- Problem 1: `python lab5_problem1.py`
- Problem 2: `python lab5_problem2.py`

### 🎯  Testing
The problems in this lab are tested using code that can be found in the corresponding `tests_*.py` file for each problem. You can use these tests to check if your code runs properly and to specifications. You can run these tests on your local machine by setting your working directory to the problem folder and running `pytest` with the `tests_*.py` file for the problem. From the code directory of this lab, you can run tests using the following commands:

- Problem 1: `pytest tests_lab5_problem1.py`
- Problem 2: `pytest tests_lab5_problem2.py`

### 🏆  Grading
This lab is worth 40 points in total using the following breakdown by problem:

- Problem 1 is worth 15 points
- Problem 2 is worth 25 points

You are awarded these points if all assertions in the test file pass successfully for a problem. There is no partial credit for lab problems.

### 💻  Academic Integrity and Copyright
This lab was created by the course professor (Matthew Crowley) and he asserts copyright over all material. You are not permitted to share the labs, tests, or solutions with anyone without express written consent. Breaches of this assertion may result in both academic and legal sanctions.