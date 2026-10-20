# ==================================================
# IT 2750 - Scripting Fundamentals for Cybersecurity
# Cuyahoga Community College
# Lab 5 – Problem 1
# ==================================================
# Student Name: Kyle Quiros
# Student Email: S01026892@acad.tri-c.edu
# ==================================================

def main():  # DO NOT EDIT THIS LINE

    print("Welcome to the String Tester!")

    # PART A
    # ======
    string1 = "ABCDEFG"
    string2 = "TUVWXYZ"

    print(string1)
    print(string2)

    # PART B
    # ======
    for character in string1:
        print(character)

    # PART C
    # ======
    for character in string2:
        print(character)

    # PART D
    # ======
    characters1 = list(string1)
    characters2 = list(string2)

    for index in range(1, len(string1), 2):
        characters1[index], characters2[index] = (
            characters2[index], characters1[index]
        )

    string1 = "".join(characters1)
    string2 = "".join(characters2)

    print(string1)
    print(string2)

    # PART E
    # ======
    string3 = string1 + string2
    shifted_string = ""

    for character in string3:
        if "A" <= character <= "M":
            shifted_string += chr(ord(character) + 1)
        elif "N" <= character <= "Z":
            shifted_string += chr(ord(character) - 1)
        else:
            shifted_string += character

    string3 = shifted_string
    print(string3)

    # PART F
    # ======
    string3 = string3[::-1]
    print(string3)

    return  # DO NOT EDIT THIS LINE

if __name__ == "__main__":  # DO NOT EDIT THIS LINE
    main()                  # DO NOT EDIT THIS LINE
