def separate_words_at_capital(input_str):
    modified_str = ''
    for char in input_str:
        if char.isupper():
            modified_str += ' ' + char.lower()
        else:
            modified_str += char

    return modified_str.strip()

input_string = "WelcomeToMyWorld"
result = separate_words_at_capital(input_string)
print(result)
