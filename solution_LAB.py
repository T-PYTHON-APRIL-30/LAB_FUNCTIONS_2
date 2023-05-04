def PrimeNumbers(number1:int,number2:int) -> int:
    # the auction for the prime number 
    for number in range(number1, number2 + 1) :
        for i in range(2, number) :
         if (number % i) == 0 :
            break
         else :
             print(number)
             
 #First number input 
number1 = int(input ("Please Enter the Fisrt Number: ")) 
 #seond number input
number2 = int(input ("Please Enter the Second Number: "))
# the print_line 
print (f"The Prime Numbers between {number1} and {number2} are: ")
#calling funcation
PrimeNumbers(number1, number2)

