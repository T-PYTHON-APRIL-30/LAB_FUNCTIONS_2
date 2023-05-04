def find_primes(frist_number:int,last_number:int):

    for i in range(frist_number,last_number+1):
        not_prime=False
        for j in range(2,i//2):
            if i%j==0:
                not_prime=True
                break  
        if not_prime==False:
            print(i)
find_primes(25,50)

