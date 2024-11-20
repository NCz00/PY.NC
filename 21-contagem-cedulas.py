# Início
cedulas = [50, 20, 10, 5, 1]

# Inserir valor inteiro
valor = int(input("digite o valor total a ser pago (ou 0 para sair): "))

# Definir valor
valor_original = valor
print(f"\npara pagar o valor de R$ {valor_original}, serão necessárias:")

# Calcule a quantidade de cédulas para cada valor
for cedula in cedulas:
        if valor >= cedula:
            quantidade = valor // cedula
            print(f"R$ {cedula}: {quantidade} cédula(s)")
            valor %= cedula
        else:
            print(f"R$ {cedula}: 0 cédula(s)")

print("\npagamento concluído.\n")