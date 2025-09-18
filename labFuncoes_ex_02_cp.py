def calcularArea(largura, altura):
    area = largura * altura
    return area

area_calculada = calcularArea(5, 12)

print(f"A área do retêngulo é {area_calculada}")


print('-' * 30)

mensagem_global =  "Acesso global permitido"

def exibir_escopo():
    mensagem_local = "Acesso local somente"
    print(f"Dentro da função (local): {mensagem_local}")
    print(f"Dentro da função (global): {mensagem_global}")
    
def alterarGlobal():
    mensagem_global = "O valor global foi alterado!"
    print(f"Dentro da função, após a alteração: {mensagem_global}")
    
exibir_escopo()
print(f"Fora da função: {mensagem_global}")

alterarGlobal()
print(f"Fora da função após a alteração: {mensagem_global}")