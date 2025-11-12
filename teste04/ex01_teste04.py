def qntdFuncionarios():
    contador = 0
    nome = input()
    while nome != 'Fim':
        contador += 1
        nome = input()

    print(contador)


qntdFuncionarios()