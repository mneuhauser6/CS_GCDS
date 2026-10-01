""""
┌───────────────────────────────────────────────────────────────────────────┐
│                            What's In a Name                               │
├───────────────────────────────────────────────────────────────────────────┤
│ Name: Max Neuhauser                                                       │
| Course: CS2                                                               |
│ Log: 1.0 MN                                                               |
| Bugs: Program does not work if input contains a title, program also does  │
│       not work if there is numbers or special characters                  │
│ Description: Numerous functions that manipulate and interrogate an array  |
|              of characters. Accessible through a menu.                    |
└───────────────────────────────────────────────────────────────────────────┘
""" 

import random

def reverse(word):
    '''
    Reverses any word the user inputs

    Arg:
        word (str): any word that the user inputs
    Return:
        reversed_string (str): the users original input in reverse order
    '''
    reversed_string = (word[::-1])                            # Takes in a full index and reverses the list
    return reversed_string                            
 
def count_vowels(any):
    '''
    Determines the number of vowels in the users input

    Arg:
        any (str): anything the user input
    Return:
        total (int): the amount of times a vowel appeared in the users input
    '''
    vowels = ["a", "e", "i", "o", "u"]
    total = 0

    lower_any = convert_lowercase(any)

    for letter in lower_any:
        if letter in vowels:
            total += 1
    return total

def consonant_frequency(any):
    '''
    counts the amount of time consonants appear in a users input

    Arg:   
        word (str): any word that the user inputs
    Return:
        total (int): the amount of times a consonant appeared in the users input
    '''
    consonants = ["b","c", "d" ,"f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    total = 0
    lower_word = convert_lowercase(any)
    for i in lower_word:                        
        if i in consonants:
            total += 1
    return total

def get_first_name(name):
    '''
    Returns the users first name

    Arg:
        name (str): Asks for the users first and last name
    Return:
        given_name (str): The users first name / name given at birth
    '''
    given_name = name.split()[0]                           # splits a input at the character: "space," and chooses the first index
    return given_name

def get_last_name(name):
    '''
    Returns the users last name 

    Arg:
        name (str): Asks for the users first and last name
    Return:
        last_name (str): Returns the users last name
    '''
    last_name = name.split()                                # splits a input at the space
    return last_name[-1]                                    # returns last "item" in the user input (their last name)

def get_middle_name(fullname):
    '''
    Returns the users middle name(s)

    Arg:
        fullname (str): asks for the users full name, including all middle names if available
    Return:
        middle_name (str): the users middle name(s), excludes first and last name
        "You have no middle name" (str): only appicable if the users input is 2 or less (demonstrating that there is no middle name, only first and last)
    '''
    names = fullname.split()
    length = len(names)
    if length > 2:
        middle_name = ""
        names.pop(0)                                        # gets rid of the index 0 in the list of names
        names.pop()                                         # gets rid of the last index in the list of names
        for name in names:                                  # moves the leftover names (middlenames) from the list into the string
            if middle_name != "":                           # if the middle name is not an empty string. "!="" means not equal to.
                middle_name += " "                          # add a space before the next name
            middle_name += name
        return middle_name
    else:
        return "You have no middle name." 

def look_for_hyphen(last_name):
    '''
    return boolean if last name contains a hyphen

    Arg:
        last_name (str): Asks for the users last name 
    Returns:
    True (boolean): if the last name contains a hyphen, then return True
    False (boolean): if the last name does not contain a hyphen, then return False 
    '''
    for letter in last_name:
        if letter == "-":
            return True
    return False                                            # Only does so after checking every letter

def convert_lowercase(any):
    '''
    converts any input into lowercase letters

    Arg:
        any (str): anything the user input
    Return:
        end (str): the users original input in lowercase letters
    '''
    end = ""
    for letters in any: 
        asc = ord(letters)                                    # Assigns ASCII value to every letter
        if 65 <= asc <= 90:                                   # if uppercase (assgined ASCII values for uppercase letters)
          end += chr(asc + 32)                                # chr converts the ASCII value back to a letter. +32 is the difference in the paramaters of the uppercase, meaning that when you add 32 you transform that specific uppercase value to its lowercase value
        else:
            end += letters
    return end

def convert_uppercase(any):
    '''
    converts any input into uppercase letters

    Arg:
        any (str): anything the user inputs 
    Return:
        end (str): the users original input in uppercase letters
    '''
    end = ""
    for letters in any: 
        asc = ord(letters)         
        if 97 <= asc <= 122:                                   # if lowercase (assigned ASCII values for lowercase letters)
          end += chr(asc - 32)                                 # -32 is the difference in the parameters of the lowercase, meaning that when you subtract 32, it transforms that specific lowercase value to its uppercase value
        else:
            end += letters
    return end


def random_name(first_name):
    '''
    Asks for the users name and then mixes up the letters 

    Arg:
        first_name (str): the users first name 
    Return:
        output (str): array of the new randomly sorted characters
    '''
    output = ""
    characters = list(first_name)
    while len(characters) > 0:                                  # While the length of the list is greater than 0 (is there are still characters from the users input left in the list)
        r = random.randint(0, len(characters)-1)                # Choose a random character in the length of the the list between 0 and -1 (the start and end of the list)
        output = output + characters[r]                         # Update the output by adding the random character (r) chosen in the step before
        del characters[r]                                       # Delete the random character chosen from the original list of the users input
    return output   

def if_palindrome(first_name):
    '''
    Check if the users first name is a palindrome 
    
    Arg:
        first_name (str): the users first name
    Returns:
        True (boolean): if the value is a palindrome, then return True
        False (boolean): if the value is not a palindrome, then return False
    '''
    lower_name = convert_lowercase(first_name)                 # Call the lowercase function to transform the users input into lowercase
    palindrome = lower_name[::-1]                              # Take the entire index of the lowercase users input (the first name or first names entered) and reverse it by a count of -1
    if lower_name == palindrome:
        return True 
    else:
        return False

def get_initials(name):
    '''
    Asks for the users fullname and returns their initials

    Arg:
        fullname (str): the users fullname (first and last)
    Return:
        initials (str): the first letter of the first name and last name added together in one line
    '''
    names = name.split()
    initials = ""

    for part in names:
        initials += part[0]
    return initials

def main():
    ''''''
    while True:
        choice = input("What would you like to do with your name? \n Would you like to: \n 1. Reverse word \n 2. Determine the number of vowels \n 3. Determine the amount of consonants \n 4. Return first name \n 5. Return last name \n 6. Return middle name(s) \n 7. Check if last name contains a hyphen \n 8. Convert input to lowercase \n 9. Convert input to uppercase \n 10. Modify array to create a random name \n 11. Check if first name is a palindrome \n 12. Make initials from name \n type 'q' to break code at any time \n" )
        if choice == "1":
            word = input("Please enter any word (and prepare for it to be reversed):")
            print(reverse(word))
        elif choice == "2":
            any = input("Type whatever you want in the following space: ")
            print(count_vowels(any))
        elif choice == "3": 
            any = input("Type whatever you want in the following space: ")
            print(consonant_frequency(any))
        elif choice == "4":
            name = input("Please enter your first and last name: ")
            print(get_first_name(name))
        elif choice == "5":
            name = input("Please enter your first and last name: ")
            print(get_last_name(name))
        elif choice == "6":
            fullname = input("Please enter your full name, including your middle name if you have one: ")
            print(get_middle_name(fullname))
        elif choice == "7":
            last_name = input("Please enter your last name: ")
            print(look_for_hyphen(last_name))
        elif choice == "8":
            any = input("Type whatever you want in the following space: ")
            print(convert_lowercase(any))
        elif choice == "9":
            any = input("Type whatever you want in the following space: ")
            print(convert_uppercase(any))
        elif choice == "10":
            first_name = input("Please enter your first name: ")
            print(random_name(first_name))
        elif choice == "11":
            first_name = input("Please enter your first name: ")
            print(if_palindrome(first_name))
        elif choice == "12":
            name = input("Please enter your first and last name: ")
            print(get_initials(name))
        elif choice == "q":
            break
        else:
            print("Invalid response. try again")
print(main())