#register
# - first_name,last_name,password, Email
# - generate user id
# - 

#Login
# - Account Number and password

#bank operations

#initializing system

import random

Database = {}

def init():

    isvalidOptionSelected = False
    print('Welcome to Survival Bank\n')

    while isvalidOptionSelected == False:
        haveAccount = int(input('Do you have an account with us: \n1 (Yes) \n2 (No)\n'))
            
        if(haveAccount == 1):
            isvalidOptionSelected = True
            login()
        elif(haveAccount == 2):
            isvalidOptionSelected = True
            print(register())
        else:
            print('You have selected an invalid option')

def login():

    print ('\n******** Login *********\n')

    isLoginSuccessful = False

    while isLoginSuccessful == False:

        accountNumberFromUser = int(input('What is your Account Number ?\n'))
        password = input('What is your Password?\n')

        for accountNumber,userDetails in Database.items():
            if(accountNumber == accountNumberFromUser):
                if(userDetails[3] == password):
                    isLoginSuccessful = True
                else:
                    print ('Ivalid Account or Password\n')
    bankOperation(userDetails)

def register():

    print ('\n******* Register *******\n')
    
    email = input('What is your Email Address\n')

    first_name = input('What is your First Name\n')

    last_name = input('What is your Last Name\n')

    password = input('Create a password\n')

    accountNumber = generateAccountNumber()

    Database[accountNumber] = [first_name, last_name, email, password]
    
    print('\nYour Account has been Created Successfully\n')
    print(' === ======= ====== ==== ===== ======= =====\n')
    print('Your Account Number is: %d' % accountNumber)
    print('Make sure you keep it safe\n')
    print(' === ======= ====== ==== ===== ======= =====\n')

    login()


def bankOperation(user):

    print(' === ====== ====== ==== ===== ==== ===')

    print('\nWelcome %s %s \n' %( user[0], user[1] ) )
    
    import datetime
    
    now = datetime.datetime.now()
    print(now)
    
    print('\n')
    
    option = int(input('What do you like to do?\n (1) Deposit\n (2) Withdraw\n (3) Complain\n (4) Logout\n (5) Exit\n'))

    if  (option == 1):
        DepositOperation(user)
        
    elif (option == 2):
        withdrawalOperation(user)
        
    elif (option == 3):
        ComplaintOperation(user)
        
    elif (option == 4):
        login()
        
    elif (option == 5):
        exit()
        
    else:
        print('Invalid Option Selected\n')
        bankOperation(user)

def withdrawalOperation(user):
    print('\n********* Welcome %s %s TO THE WITHDRAWL PAGE *********\n' % (user[0], user[1] ) )

    wd = int(input('How much do you want to Withdraw ?\n#'))

    print('\nTake your cash #%s\n' % wd)

    print('Thanks for banking with us\n')

    print('POWERED BY OMOH JOSEPH\n')

def DepositOperation(user):
    print('\n********* Welcome %s %s TO THE DEPOSIT PAGE *********\n' % (user[0], user[1] ) )

    dp = int(input('How much do you want to Deposit ?\n#'))

    print('\nYour Current Balance is #%s\n' % dp)

    print('Thanks for Banking with us\n')

    print('POWERED BY OMOH JOSEPH\n')

def ComplaintOperation(user):
    print('\n********* Welcome %s %s TO THE COMPLAINT PAGE *********\n' % (user[0], user[1] ) )

    print('Your can write your Complain here\n')

    cm = input('What issue would you like to Report ?\n')

    print('Thanks For Contacting Us\n')

    print('POWERED BY OMOH JOSEPH\n')


def generateAccountNumber():

    return random.randrange(1111111111,9999999999)


#### ACTUAL BANKING SYSTEM ####

#### BY OMOH JOSEPH ####

#### SURVIVALJAY ####

init()