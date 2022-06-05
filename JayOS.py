import os
import time
import datetime
from random import randint

def startup():
    os.system('cls||clear')
    print('Initializing startup... Performing virus scan... Performing checks...')
    print('')
    time.sleep(2)
    print('            [][][]  [][]   []    []     _______           ')
    print('              []   []  []   []  []     |       |          ')
    print('          []  []  [][][][]    []       |   S   |          ')
    print('           [][]  []      []   []       |_______|          ')
    print('')
    print('Copyright @ 2022 Jay Operating System.  All Rights Reserved')
    print('')
    time.sleep(2)
    print('Logged in as \'user\' on {}'.format(datetime.datetime.now()))
    startscreen()

def startscreen():
    print('Welcome back, user. What would you like to do today?')
    while True:
        print('')
        global inp
        inp = raw_input('$user ')
        if inp == 'help':
            help()
        elif inp == 'ls':
            ls()
        elif inp.startswith('open'):
            open()
        else:
            print('No such command. Enter \'help\' to list the available commands')

def help():
    cmddict = {
        "help": "List of available commands (this)",
        "ls": "List apps and files in OS",
        "open": "Open files"
    }
    for x, y in cmddict.items():
        print(x + ": " + y)

def ls():
    filelist = ['guessthenumber', 'void']
    for x in filelist:
        print(x)
    '''
    print('File_explorer    Google_chrome    Recycling_bin    Jaycorps_bestantivirus')
    time.sleep(4)
    act = input('Please select.')
    print(act)
    if act == File_explorer:
        print('There is nothing here...Wait, nevermind.There is a folder called "games". Go inside?')
        gameact = input('Yes or No?')
        if gameact == Yes or yes:
            guessthenumber()
    '''

def open():

    def guessthenumber():   
        min = 1
        max = 100
        num = randint(min, max)
        flag = False
        tries = 5
        print('A number was picked between {} to {}, try guessing it within your limited number of tries'.format(min, max))
        while tries > 0:
            guess = input('{} tries left: '.format(tries))
            if isinstance(guess, int):
                if guess == num:
                    flag = True
                    break
                elif guess < num:
                    print('The number is higher than that.')
                elif guess > num:
                    print('The number is lower than that.')
                print('')
                tries -= 1
            else:
                print('That is not a number')

        if flag == True:
            print('Congratulations! You\'ve guessed correctly!')
        else:
            print('You have exceeded the maximum number of tries, the number is ' + str(num))

    if inp.startswith('guessthenumber', 5, 19):
        print('---------------------------------------------------------------------------------------------')
        guessthenumber()
        print('---------------------------------------------------------------------------------------------')
    elif inp.startswith('void', 5, 9):
        print('---------------------------------------------------------------------------------------------')
        print('This file is actually a temporary placeholder, it might be removed later')
        print('---------------------------------------------------------------------------------------------')
    else:
        print('Syntax: \"open (file)\"')

startup()

'''
def loadingscreen():
    print('   .....   ')
    print(' ..     ..')
    print(' ..     ..')
    print('   .....   ')
'''