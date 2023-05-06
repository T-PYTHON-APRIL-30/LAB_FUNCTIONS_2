'''
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
'''
def find_primes(num1 :int, num2 :int):
    '''Function takes in two parameters of type int, and print the prime numbers between the first parameter and the second parameter.'''
    print("-"*60)
    print("\nFinding Prime Numbers Between two Values\n")
    print("-"*60)

    for number in range(num1,num2+1):
        for i in range (2, number):
            if number % i  == 0:
                break
        else:
            print(number)

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
print(find_primes(first_number, second_number))