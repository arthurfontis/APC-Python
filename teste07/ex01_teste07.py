def catalog():
    products = {}
    entrada = input().split()
    qntd = input().split()
    for i in range(0,len(entrada), 2):
        product = entrada[i]
        value = entrada[i + 1]
        value = float(value)

        products[product] = value

    print(products)

catalog()