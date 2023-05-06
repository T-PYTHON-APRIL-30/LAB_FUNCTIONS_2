num1 = int(input ("Please enter the fisrt number: "))  
num2 = int(input ("Please enter the second number: "))
def find_prime(num1,num2):
    for num in range (num1, num2):  
        if num > 1:  
            for n in range (2, num):  
                if (num % n) == 0:  
                    break  
            else:  
                print (num)
find_prime(num1,num2)