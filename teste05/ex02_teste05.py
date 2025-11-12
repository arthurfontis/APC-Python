def validationPassword():
    password = input()
    
    upper = False
    lower = False
    digit = False
    
    if(len(password) < 6 or len(password) > 32 or not password.isalnum()):
        print("Senha invalida.")
    else:
        for i in password:
            if(i.isupper()):
                upper = True
                continue
            elif(i.islower()):
                lower = True
                continue
            elif(i.isdigit()):
                digit = True
                continue
        if upper and lower and digit:
            print("Senha valida.")
        else:
            print("Senha invalida.")
            
validationPassword()
            