def find_primes (prime1:int,prime2:int)->int:
    factors = 0              #prime numbers known for only 2 factors dividing the number on 1 and dividing the number on it self
    for i in range(prime1,prime2):
        nmbrType = i/3 #this is done so the decimal is removed from resault Ex:  1/1 python gives = 1.0  
        if i == 0:
            continue

        if i == i/1:
            factors += 1     

        if i/i == 1:
            factors+=1
            
        if  nmbrType%1 == 0:
            nmbrType = int(nmbrType)


        if isinstance(nmbrType,int) == True:
            factors+=1
           
        if factors > 2:
            factors = 0  
   
        if  factors == 2:
            print (i)
            factors = 0
      
        else:
            continue

find_primes(0,12)