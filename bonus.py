def stringformating(words:str):
    
    if words.isalpha()==False:
        print("only for alphaBit")
    else:
        for char in words:
                    
            if char.islower()==False:
                print(" "+char.lower(),end="")
            else:
                print(char,end ="")

stringformating("helloWorldThere")
