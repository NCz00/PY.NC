# Inicio
quantidade = 0
soma = 0

while True:
    # Lendo o número digitado
    numero = int(input("Digite um número inteiro (ou 0 para encerrar): "))
    
    # Verificando se o número é 0 para encerrar
    if numero == 0:
        break
    
    # Atualizando a soma e a quantidade de números digitados
    soma += numero
    quantidade += 1

# Calculando a média se ao menos um número foi digitado
if quantidade > 0:
    media = soma / quantidade
else:
    media = 0

# Resultados
print(f"Quantidade de números digitados: {quantidade}")
print(f"Soma dos números: {soma}")
print(f"Média aritmética: {media:.2f}")