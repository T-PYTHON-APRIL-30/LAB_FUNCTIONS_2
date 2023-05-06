'''
# Bonus
## write a function that takes a string as a parameter
- first check that the type of the parameter is of type str
- then, it should separates the word at any capital letter and replace it with a small letter 
- and  should return the new modified string !

Example: `helloWorldThere` should return :
```hello world there```
'''
import re
sentence= input("Enter your sentence:")

def string_checked (sentence:str):
    for i in range(len(sentence)):
        if type(sentence)==str:
            if (sentence[i].isupper()):
                sentence= re.sub(r'\B(?=[A-Z])', r' ', sentence)
                break      
    else:
        print("This is not a string sentence, pleas try agein")
    
    return sentence

print(string_checked(sentence))

