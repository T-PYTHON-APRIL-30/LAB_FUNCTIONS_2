
#Functions LAB 2

'''Create a function : find_primes that takes in 2 parameters of type int , and print the prime numbers between the first parameter
 and the second parameter .
hint
a prime number i a number that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11)
Also , you can think of it as A Prime Number is a number that cannot be made by multiplying other whole numbers

for example, primes between 25 and 50 are:
29   
31   
37   
41   
43   
47   
'''


def findPrimes (num1:int, num2:int):

    for n in range (num1+1, num2):
        if n > 1:
            for i in range (2,n):
                if n%i == 0:
                    break
            else:
                print(n) 
                


num1 = int(input('Please enter a positive integer: '))
num2 = int(input('Please enter a positive integer: '))
findPrimes(num1,num2)



#Bonus LAB


'''Bonus
write a function that takes a string as a parameter
first check that the type of the parameter is of type str
then, it should separates the word at any capital letter and replace it with a small letter
and should return the new modified string !
Example: helloWorldThere should return : hello world there'''

def capitalToSmall (str1:str) -> str:
    editedSring = ''

    if type(str1) == str:
        for char in str1:
            if char.isupper() == True:
                editedSring += " " + char.lower() 
            else:
                editedSring += char
    
    return editedSring



sentence = input('Please Enter a sentence: ')
print(capitalToSmall(sentence))