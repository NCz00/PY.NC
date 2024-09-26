#Atividade 08-tabuada
#Faça um programa que mostre a tabuada de um número que o usuário escolher.

# variáveis
contador = 0
multiplicador = int(input("Digite o valor do multiplicador: "))

while contador <= 10:
    resultado = multiplicador * contador
    print(f"{multiplicador} X {contador} = {resultado}")
    contador += 1
