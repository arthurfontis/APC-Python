def medias():
    n1,n2,n3 = input().split()
    n1,n2,n3 = float(n1), float(n2), float(n3)
    operacao = input()
    if operacao.lower() not in ['a', 'p', 'h']:
        print("Operacao inexistente")
    elif operacao.lower() == 'p':
        p1,p2,p3 = input().split()
        p1,p2,p3 = int(p1), int(p2), int(p3)
        
        soma = (p1*n1)+(p2*n2)+(p3*n3)
        resultadoP = soma / (p1+p2+p3)
        print(f"Ponderada")        
        print(f"{resultadoP:.2f}")
    elif operacao.lower() == 'a':
        resultadoA = (n1 + n2 + n3) / 3
        print("Aritmetica")
        print(f"{resultadoA:.2f}")
        
    elif operacao.lower() == 'h':
        resultadoH = 3 / ((1/n1) + (1/n2) + (1/n3))
        print("Harmonica")
        print(f"{resultadoH:.2f}")
        
medias()