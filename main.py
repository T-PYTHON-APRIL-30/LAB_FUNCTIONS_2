def find_primes(num1: int, num2: int) -> int:
    ''' a Function that print the prime number between two numbers... '''

    if num1 > num2:
        print("Make the first input upper than the second input!!")
    else:
        print(f"the prime number between {num1} and {num2} is: ")

    for i in range(num1, num2 + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                print(i)

while True:
    print("Enter a two number : ")
    user_input1 = input("> ")
    user_input2 = input("> ")

    if user_input1.isdigit() and user_input2.isdigit():
        number1 = int(user_input1)
        number2 = int(user_input2)

        find_primes(number1, number2)
        break
    else:
        print("type a integer number pleas!!")