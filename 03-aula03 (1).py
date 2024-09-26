# Tipos de dados primitivos:
# - inteiro (int): números inteiros
# - (float): numeros reais, decimais
# - String (str): cadeia de caracteres, utilizando aspas
# - bollean (bool): tipo lógico true ou false
# - complex (complex): numeros complexos, com parte real e imaginaria
# - List (list): Lista de elementos, ordenados e indexados
# - Tuple (tuple): Tupla de elementos, ordenados e imutáveis
# - Dictionary (dict): dicionário de elementos, não ordenados e indexados

#Atribuição de variável por captura
nome = input("Digite seu nome: ")
print("ola", nome)
idade = input("digite a sua idade: ")
print(idade)
altura = input("Digite a sua altura: ")
print(type(altura))

#Exibir na tela
print(f"nome: {nome} idade: {idade} altura: {altura}")

# Exemplo de conversão de string para inteiro
valorA = int(inpu("Digite o valor de A: "))
valorB = int(inpu("Digite o valor de B: "))
resultado = valorA + valorB
print(f"A soma = {resultado}")
# Exemplo de conversão de string para float
valorA = float(input("Digite o valor de A: "))
valorB = float(input("Digite o valor de B: "))
print(f"A soma = {resultado}")