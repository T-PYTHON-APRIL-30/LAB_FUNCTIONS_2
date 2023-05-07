def is_prime(number : int) -> bool:

    for n in range(2, number):
        if number%n == 0:
            return False
    
    return True

def find_primes(number1 : int, number2 : int):

    for number in range(number1, number2):
        if is_prime(number):
            print(number)


print("the prime numbers between 25 to 50 are:")
find_primes(0, 100)