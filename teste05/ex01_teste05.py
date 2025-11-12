def apelidos():
    nome = input()
    if (nome.find(' ') > 0):
        indice_espaco = nome.find(' ')
        primeiro_nome = nome[:indice_espaco]
        segundo = nome[indice_espaco + 1:]
        
        
        apelidinho = primeiro_nome[0:2] + segundo[0:2]
        print(apelidinho.lower())
        
    else:
        if(len(nome) <=3):
            apelidinho = nome[0:2]
            print(apelidinho.lower())
        else:
            apelidinho = nome[0:3]
            print(apelidinho.lower())
apelidos()