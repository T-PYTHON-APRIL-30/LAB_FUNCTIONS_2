'''
# LAB_FUNCTIONS_2


## Create a function : find_primes that takes in 2 parameters of type int , 
and print the prime numbers between the first parameter and the second parameter . 

### hint
a prime number i a number that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11)    
Also , you can think of it as A Prime Number is a number that 
cannot be made by multiplying other whole numbers


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
 

def prime_numbers(num1:int,num2:int) -> int:
    for num in range (num1, num2):  
        if num > 1:  
            for i in range (2, num):  
                if (num % i) == 0:  
                    break  
            else:  
                print (num)


num1 = int(input ("Please Enter the Fisrt Number: "))  
num2 = int(input ("Please Enter the Second Number: "))
print(" ")
print (f"The Prime Numbers between {num1} and {num2} are: ")
prime_numbers(num1, num2)


