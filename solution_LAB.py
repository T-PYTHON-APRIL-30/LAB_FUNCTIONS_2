def Prime_input(frist_number:int,second_number:int):
    '''This function takes 2 parameters, and print the prime numbers between the first number and the second number'''
    if frist_number > second_number:
        switch = frist_number
        frist_number=second_number
        second_number=switch
    print(f"primes between {frist_number} and {second_number} are:")
    flag=False
    for number in range(frist_number,second_number):
        for i in range(2,number):
            if (number%i) == 0 :
                flag= True
        if flag:   
            flag = False
        else:
            print(number)

user_input1 = int(input("Please enter the first number: "))
user_input2 =int(input("Please inter the second number: "))
Prime_input(user_input1,user_input2)