"""
# LAB_FUNCTIONS_2


## Create a function : find_primes that takes in 2 parameters of type int , and print the prime numbers between the first parameter and the second parameter . 

### hint
a prime number i a number that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11)    
Also , you can think of it as A Prime Number is a number that cannot be made by multiplying other whole numbers


#### for example, primes between `25` and `50` are:
```
29   
31   
37   
41   
43   
47   
```
"""

def findPrime(first_number:int ,seconed_number:int)->int:
    """Find the Primes number between two numbers"""
    for number in range(first_number,seconed_number+1):
        if number > 1:
            for i in range(2,number):
                if number % i ==0:
                    break
            else:
                print(number)

findPrime(25,50)

