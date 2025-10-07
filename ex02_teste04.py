def sem_funcionarios():
    print('Não tem média')
    print('Não tem')
    print('Não tem')

def funcionarios_validos(n):
    soma = 0
    validos = 0
    maiorS = 0.00
    menorS = 1000000000.00
    nomeMaiorS = ''
    nomeMenorS = ''

    for i in range(n):
        nome,salario = input().split(',')
        salarioInt = float(salario)

        if salarioInt < 0 or salarioInt > 1000000000.00:
            print('Não tem média')
            continue

        else:
            soma += salarioInt
            validos += 1

            if salarioInt > maiorS:
                maiorS = salarioInt
                nomeMaiorS = nome

            if salarioInt < menorS:
                menorS = salarioInt
                nomeMenorS = nome
                
    if validos == 0:
        sem_funcionarios()
    else:
        media = soma / validos
        print(f'{media:.2f}')
        print(f'{nomeMaiorS} {maiorS:.2f}')
        print(f'{nomeMenorS} {menorS:.2f}')
        
def funcionarios():
    n = int(input())
    if n == 0:
        sem_funcionarios()
    else:
        funcionarios_validos(n)


funcionarios()