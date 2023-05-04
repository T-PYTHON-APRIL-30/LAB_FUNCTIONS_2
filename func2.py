def find_primes(first, second):
    for num in range(first, second + 1):
        if num > 1:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(num)
# Example usage
find_primes(25, 50)
