def validacao():
    pF = input("O programa funciona?\n")
    if(pF == 'SIM'):
        eleSabe = input("Você entende o que fez?\n")
        if(eleSabe == 'SIM'):
            print("Ótimo. Então não mexe!")
        else:
            tutoria = input("Já foi na tutoria?\n")
            if(tutoria == 'SIM'):
                print("Choremos!")
            else:
                print("Temos um time a disposição!")
    else:
            sabeErro = input("Você sabe onde está o erro?\n")
            if(sabeErro == 'SIM'):
                consegue = input("Acha que pode solucionar sozinho?\n")
                if(consegue == 'SIM'):
                    print("Então mão na massa!")
                else:
                    google = input("Já pesquisou no Google?\n")
                    if(google == 'SIM'):
                        tutoria = input("Já foi na tutoria?")
                        if(tutoria == 'SIM'):
                            print("Choremos!")
                        else:
                            print("Temos um time a disposição!")
                    else:
                        print("Corre lá então!")
            else:
                tutoria = input("Já foi na tutoria?\n")         
                if(tutoria == 'SIM'):
                    print("Choremos!")
                else:
                    print("Temos um time a disposição!")
                    
validacao()