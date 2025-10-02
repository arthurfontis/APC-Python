def calcMencao(n1,n2,n3):
    resultado = ((n1 * 3) + (n2 * 4) + (n3 * 3)) / 10
    
    if resultado >= 9:
        print(f"Menção SS")
        
    elif resultado >= 7:
        print(f"Menção MS")
    elif resultado >= 5:
        print(f"Menção MM")
    elif resultado >= 3:
        print(f"Menção MI")
    elif resultado > 0:
        print(f"Menção II")
    else:
        print(f"Menção SR")
        
calcMencao(9,9,9)