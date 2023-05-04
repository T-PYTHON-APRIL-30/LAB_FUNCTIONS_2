'''LAB_FUNCTIONS_2
Create a function : find_primes that takes in 2 parameters of type int , and print the prime numbers between the first parameter and the second parameter .
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
Bonus
write a function that takes a string as a parameter
first check that the type of the parameter is of type str
then, it should separates the word at any capital letter and replace it with a small letter
and should return the new modified string !
Example: helloWorldThere should return : hello world there'''
def PrimeNum(prNum1:int,prNum2:int)->int:
             print(f"primes between {prNum1} and {prNum2} are:")
             for Number in range(prNum1,prNum2):
                 if prNum1%prNum1==0 and prNum2%prNum2==0:
                       print("this is prime number ^^")
                       print(Number,len)
                 else:
                       print("this is not prime number, sorry try again")
while True:
    print("please give me your first prime number:")
    prNum1 =int(input())
    print("please give me your secound prime number:")
    prNum2 =int(input())    
    PrimeNum(25,50)
         
