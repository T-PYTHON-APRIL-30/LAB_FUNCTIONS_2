'''
write a function that takes a string as a parameter
first check that the type of the parameter is of type str
then, it should separates the word at any capital letter and replace it with a small letter
and should return the new modified string !
Example: helloWorldThere should return : hello world there
'''
def seprate_word(text:str)->str:
    '''This fuction takes a parameter of type string, and seprates the word at any capital letter and replace it with a small letter.'''
    modified_string:str= ""
    if text.isalpha():
        
        for character in text:
            if character.isupper():
                #swapcase = character.swapcase()
               # print(" "+ swapcase,end="")
                modified_string+= " "+character.swapcase()
            else:
                #print(character,end="")
                modified_string+= character
    
        return modified_string

user_input:str= input("Please enter text: ")
print(seprate_word(user_input))
