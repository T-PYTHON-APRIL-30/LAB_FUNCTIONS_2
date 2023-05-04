'''
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
'''
import math


def find_primes(start: int, end: int) -> str:
    if start > end:
        temp = start
        start = end
        end = temp

    numbers: str = ""

    for number in range(start, end+1):
        root_number: int = math.floor(math.sqrt(number))
        flag = False
        for divided in range(2, root_number+1):
            if number % divided == 0:
                flag = True

        if not flag:
            print(number)
            numbers += f"{number} "
    return numbers


print(find_primes(25, 50))


'''
# Bonus
## write a function that takes a string as a parameter
- first check that the type of the parameter is of type str
- then, it should separates the word at any capital letter and replace it with a small letter 
- and  should return the new modified string !

Example: `helloWorldThere` should return :
```hello world there```

'''
