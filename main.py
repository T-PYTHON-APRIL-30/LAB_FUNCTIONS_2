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

print("-"*60)
print("\nFinding Prime Numbers Between two Values\n")
print("-"*60)
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
for number in range(first_number,second_number+1):
        for i in range (2, number):
            if number % i  == 0:
                break
        else:
            print(number)
