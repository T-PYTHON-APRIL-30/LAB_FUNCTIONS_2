def find_primes(f_number:int, s_number:int) :

    dvided_result = []

    number_round = range(f_number,s_number + 1,+1)
    

    for round in number_round:
        check_result = 0
        

        if round < 2:
             continue
                
        if round == 2:
                dvided_result.append(2)
                continue
               

        for round2 in range(2,round):
           
           if round % round2 == 0:
                check_result = 1
                break
           
           
        if check_result == 0:
            dvided_result.append(round)

        
    print(dvided_result)
        

find_primes(int(input("Enter a first number!")), int(input("Enter a secound number!")))
