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
        inp = raw_input('$user ')
        if inp == 'help':
            help()
        elif inp == 'ls':
            ls()
    #    elif inp.startsWith('open'):
    #        open()
        else:
            print('No such command. Enter \'help\' to list the available commands')

def help():
    listdict = {
        "help": "List of available commands (this)",
        "ls": "List apps and files in OS"
    }
    for x, y in listdict.items():
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
    if inp.startsWith('guessthenumber', 5, 19):
        guessthenumber()
    elif inp.startsWith('void', 5, 9):
        print('This file is actually a temporary placeholder, it might be removed later')
    else:
        print('An error occurred. There might be additional spaces in your command, or that file just do not exist.')
    

    def guessthenumber():
        print('there are 50 numbers.Try to guess them!')
        MIN_NUMBER = 1
        MAX_NUMBER = 50
        random_number = randint(MIN_NUMBER,MAX_NUMBER)
        flag = 0
        NO_OF_GUESSES = 3
        while NO_OF_GUESSES > 0:
            guess = int(input('Guess a number from %d-%d :' %(MIN_NUMBER, MAX_NUMBER)))
            if guess == random_number:
                flag = 1
                break
            elif guess < random_number:
                print('Your guess is too low!')
            else:
                print('Your guess is too high')
            NO_OF_GUESSES -= 1
        if flag == 1:
            print('Congratulation!')
        else:
            print('Game Over! The number is', random_number)


startup()

'''
def loadingscreen():
    print('   .....   ')
    print(' ..     ..')
    print(' ..     ..')
    print('   .....   ')
'''