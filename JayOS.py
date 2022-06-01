import time
from random import randint
def minimathgame():
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
def loadingscreen():
    print('   .....   ')
    print(' ..     ..')
    print(' ..     ..')
    print('   .....   ')
def JayOSstartup():
    loadingscreen()
    time.sleep(3)
    print('initializing startup...performing virus scan...performing checks...')
    time.sleep(5)
    print('Jay.exe loaded   OSystem.exe loaded   Pythoninterperter.exe loaded...')
    time.sleep(5)
    print('                      JAYOS LOADED                                   ')
    print('           Jaycorps pte ltd  all rights reserved@2019                ')
    print('                          WELCOME                                    ')
    time.sleep(2)
def startscreen():
    print('Hello there!What would you like to do?')
    print('Remember, you have to write everything the same as what we say, for example, I say "hi",you can only write "hi" or "Hi".')
    print('please select any of these activities!')
    print('File_explorer    Google_chrome    Recycling_bin    Jaycorps_bestantivirus')
    time.sleep(4)
    act = input('Please select.')
    print(act)
    if act == File_explorer:
        print('There is nothing here...Wait, nevermind.There is a folder called "games". Go inside?')
        gameact = input('Yes or No?')
        if gameact == Yes or yes:
            littlenumbergame()
startscreen()
