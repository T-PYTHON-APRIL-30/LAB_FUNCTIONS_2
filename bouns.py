def separates_text(text: str) -> str:
    new_text = ""
    for i in text:
        if i.isupper():
            replace_text = i.replace(i,  " " + i.lower())
            new_text += replace_text
        else:
            new_text += i
    return print(new_text)


while True:
    user_input = input("Enter some text: ")
    if user_input.isalpha():
        separates_text(user_input)
        break
    else:
        print("type a text has only a alphabet pleas!!")