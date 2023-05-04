

def find_primes(first_number, second_number):
    i = first_number
    for i in range (first_number,second_number, 1):
        flag = False #if the flag stays as false, it means its a prime number
        for j in range (2,i,1):
            if i % j == 0:
                flag = True
        if flag == False:
            print(i)


find_primes (25, 50)