'''
write a function that takes a string as a parameter
first check that the type of the parameter is of type str
then, it should separates the word at any capital letter and replace it with a small letter
and should return the new modified string !
Example: helloWorldThere should return : hello world there

'''

def string_checker(input :str) -> str:
    '''Function that takes a string as a parameter to check that the type of the parameter is str
        then, separates the word at any capital letter and replace it with a small letter'''

    #check the if string is digit
    if input.isdigit() == True:
        print("You typed a number, please type a valid string\n")

    else:
        #add spaces in a string & lowercase the string
        new_string :str = ""
        for char in range(len(input)):
            if input[char].isupper():
                new_string += " "
                new_string += input[char]
            else:
                new_string += input[char]
        return new_string.lower()


user_input = input("Enter a string: ")
print(string_checker(user_input))