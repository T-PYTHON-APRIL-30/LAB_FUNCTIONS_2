x = int(input("first number x: "))
y = int(input("first number y: "))

def find_primes(x,y):
    '''This is a function for finding prime number by the given intervals'''
    
    for number in range(x,y+1):
        if number > 1:
            for j in range (2,number):
                if number % j == 0:
                    break
            else:
                print(number)
        
find_primes(x,y)
print(find_primes.__doc__)