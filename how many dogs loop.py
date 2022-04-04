
def main():
    print('How many dogs do you have?')
    numDogs = input()
    try:
        if int(numDogs)  < -1:
            print ('That is not possible')
        elif int(numDogs) >= 4:
            print ('That is a lot of dogs.')
        else:
            print ('That is not that many dogs.')
    ## could print anything e.g. 'six' rather than 6 creates an error
    ##    int('six') is not a thing

        
    except ValueError:
        print('You did not enter a number.')

    restart = input('Would you like to try again?')
    if restart == 'yes':
        main()

    else:
        exit()
