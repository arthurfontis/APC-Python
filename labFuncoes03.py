def dobra(x):
    print(f"O dobro de {x} é {x * 2}")
    
def dobra_incremento(x):
    print(f"Incrementando {x} em 1 antes de dobrar")
    dobra(x + 1)
    
def processa_metade(x):
    print(f"Calculando a metade inteira de {x} antes de processar")
    dobra_incremento(x // 2)
    
    
    
valor_inicial = 10
print("\n--- Chamada 1: dobra(valor_inicial) ---")
dobra(valor_inicial)

print("\n--- Chamada 2: dobra_incremento(valor_inicial * 2) ---")
dobra_incremento(valor_inicial * 2)

print("\n--- Chamada 3: processa_metade(valor_inicial * 8) ---")
processa_metade(valor_inicial * 8)