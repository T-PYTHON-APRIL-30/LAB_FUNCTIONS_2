'''
LAB_FUNCTIONS_2
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
47   '''

def find_primes(frist_number:int,second_number:int):
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
find_primes(user_input1,user_input2)

