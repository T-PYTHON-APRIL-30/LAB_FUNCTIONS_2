# LAB_FUNCTIONS_2

def check_prime(number: int):
    '''This function will check if the the number inserted is 
    prime or not and return true or false based on the result'''
    for i in range(2, number):
        if (number % i) == 0:
            return False
    return True

def find_primes(number1: int, number2: int):
    '''This function will take two numbers from the user 
    and print the prime number between these numbers '''
    for i in range(number1, number2):
        if check_prime(i) == True:
            print(i)



print("-"*40)
print("|This program will show all the prime   |")
print("|numbers in a range that the user puts  |")
print("-"*40)

#inputs
number1 = int(input("Please enter a number: "))
number2 = int(input("Please enter a number bigger than the first number: "))

#function call
find_primes(number1, number2)

print("-"*38)

#---------------------------------------------------------------------------------------
# Bonus

print("|This program will take any sentance |")
print("|with CammelCaseFormat and turn it   |")
print("|inro a regular format               |")
print("-"*38)

def separate_words(sentence:str ="helloWorldThere"):
    '''This function will take any sentance with CammelCaseFormat and turn it inro a regular format'''
    for character in sentence:
        #print(character,end="")
        if character.isupper()==True:
            print(character.replace(character,f" "),end="")
            #print(character,end="")
        print(character.lower(),end="")

#input
sentence=str(input("Please Enter a sentence in CammelCaseFormat: "))

#function call
separate_words(sentence)
