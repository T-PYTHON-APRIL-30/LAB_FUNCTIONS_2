'''
# Bonus
## write a function that takes a string as a parameter
- first check that the type of the parameter is of type str
- then, it should separates the word at any capital letter and replace it with a small letter 
- and  should return the new modified string !

Example: `helloWorldThere` should return :
```hello world there```
'''

def string_checked (sentence:str):
    result=""
    for i in range(0,len(sentence),1):
        if type(sentence)==str:
            if sentence[i].isupper()== True:
                new_char= " "+ sentence[i].lower()
                result += new_char      
            else:
                result += sentence[i]
    return result

print(string_checked("helloWorldThere"))

