"""
# Bonus
## write a function that takes a string as a parameter
- first check that the type of the parameter is of type str
- then, it should separates the word at any capital letter and replace it with a small letter 
- and  should return the new modified string !

Example: `helloWorldThere` should return :
```hello world there```
"""


def returnTheStringWithSpaces(sentence):
    if type(sentence) != str:
        return "is not a string"
    else:
        new_sentence = ""
        for i in range(len(sentence)):
            if sentence[i].isupper() and i != 0:
                new_sentence += " "
            new_sentence += sentence[i].lower()
        return new_sentence


print(returnTheStringWithSpaces("HelloWorldMyNameIsBakr"))
