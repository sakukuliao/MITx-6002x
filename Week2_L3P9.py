#playing number guessing game with users

def GuessingNumbers(low,high):
    '''
    Last updated on 2013/10/27 by SakukuLiao
    Input : the number of range is [low,high],not inclusive. All are intergers.
    Output: none
    What this function do : Playing a number guessing game with users
    '''
    print('Please think of a number between 0 and 100!')
    #low = 0
    #high = 100
    
    while True:
        guess = (low + high)/2
        ans = raw_input("Is your secret number "+str(guess)+"?"+"\n"+"Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
        
        if ans != 'h' and ans != 'l' and ans != 'c':#invalid input
            while True:
                print('Sorry, I did not understand your input.')
                ans = raw_input("Is your secret number "+str(guess)+"?"+"\n"+"Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
                if ans == 'c' or ans == 'h' or ans == 'l':# valid input
                    break 
        if ans == 'c':
            print('Game over. Your secret number was: '+str(guess))
            break
        elif ans == 'h':
            high = guess
        else:# ans == 'l'
            low = guess