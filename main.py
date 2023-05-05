# ---------- Lab ----------
print("---- Lab ----")
print('Hello dear user ! (= ')
print("There's where you can find the prime numbers!")
def find_primes ( number1 : int , number2 : int ) -> int:
    '''The user will give you two numbers and the funcation ( find_primes ) will find all the prime numbers between the first and the second'''
    for prime in range(number1,number2+1):
        if prime > 1 :
            for i in range(2,prime):
                if (prime % i) == 0:
                    break
            else: # end of the for
                print(prime , end=" ")
num1 = int(input("Please enter your first number: "))
num2 = int(input("Please enter your second number: "))
print(f"The primes numbers between {num1} and {num2} is :")

find_primes(num1,number2=num2)
# ---------- Bonus ----------
print()
print("---- Bonuse ----")
def sentenceMixed (mixedW :str) -> str :
    '''This funcation is sperates the word in sentence and make it in lower case.'''
    newWord = ""
    if mixedW.isalpha():
        for leter in mixedW : 
            if leter.isupper():
                newWord += (f" {leter.lower()}")
            else:
                newWord += (leter)
    else:
        print("It's not a word !")
    print(newWord.strip())
mixedWord = str(input("Write a mixed sentence you need to seprate it : "))
sentenceMixed(mixedWord)