for numero in range(1, 100):
    if numero == 6:
        print("Não mostrar o 6")
        continue
    elif 10 <= numero <= 27:
        print(f"Não mostrar o {numero}")
        continue
    elif numero == 40:
        break
    
    print(numero)

print("Acabou")