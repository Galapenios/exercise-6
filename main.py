import random
import re
from getpass import getpass
import time

def passgen():
    print('''
    Password Generator
    ==================
    ''')
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'
    number = input('how many passwords would you like to have?')
    number = int(number)
    length = input('what should be the password length?')
    length = int(length)
    possiblepass = ['']
    print('\nhere are your passwords:')
    password = ''

    for x in range(number):
        for c in range(length):
            password += random.choice(chars)

        possiblepass.append(password)
        password = ''

    for x in possiblepass:
        print(x)

    chosenpass = int(input("\n what password would you like to use?"))

    print("Choose one!")


def checkpw():
    print('''
        Password Checker
        ==================
        ''')
    password = getpass("please state your password, and press enter:")

    while True:
        if (len(password) < 8):
            punten = -1
            break
        elif not re.search("[a-z]", password):
            punten = -1
            break
        elif not re.search("[A-Z]", password):
            punten = -1
            break
        elif not re.search("[0-9]", password):
            punten = -1
            break
        elif not re.search("[_@$]", password):
            punten = -1
            break
        elif re.search("\s", password):
            punten = -1
            break
        else:
            punten = 0
            print("Safe Password!")
            break

    if punten == -1:
        print("Not a safe password")

def yes_or_no(question):
    reply = str(input(question+' (c/g): ')).lower().strip()
    if reply[0] == 'c':
        checkpw()
    if reply[0] == 'g':
        passgen()
    else:
        return yes_or_no("Uhhhh... please enter ")



if __name__ == "__main__":
    yes_or_no("would you like to check (c) your pass for strength?\n or generate (g) a password? ")
