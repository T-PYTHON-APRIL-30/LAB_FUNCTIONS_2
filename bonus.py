def string_correcter(string:str) -> str:
    result = ""
    for i in range (0, len(string), 1):
        if string[i].isupper() == True:
            new_char= " "+ string[i].lower()
            result += new_char
        else:
            result += string[i]
    return result

print(string_correcter("helloWorldThere"))

