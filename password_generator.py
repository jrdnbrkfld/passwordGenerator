import random

print('Welcome to the Password Generator!')

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!"£$%^&*()_+'

number = input('\nHow many passwords would you like to generate? ')
number = int(number)

length = input('\nHow many characters would you like your password to have? ')
length = int(length)

print('\nHere you go!')

for pwd in range(number):
    passwords = ''
    for char in range(length):
        passwords += random.choice(characters)
    print(passwords)

input('\nHit Enter to exit the program')