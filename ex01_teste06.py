def chamadaInverse():
    liNomes = []
    
    qntd = int(input())
    for _ in range(qntd):
        nome = input()
        liNomes.append(nome)
            
    liNomes.sort(reverse=True)
    print(*liNomes, sep='\n')
        

chamadaInverse()