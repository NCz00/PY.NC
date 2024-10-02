# Declaração da função exibirmensagem(nome)
def exibirMensagem(nome):
    print(f"ola, {nome}!")


def somar (a,b):
    return a + b

def calcularAreaCirculo(raio):
    area = 3.1415 * raio**2
    return area

# inicio do meu algoritimo
nome = input("Digite o seu nome: ")
idade = input("Digite sua idade: ")
exibirMensagem(nome, idade) # Exibe a mensagem com nome do usuário.

#chamando função com retorno
print ("Soma de 2 valores")
valorA = int(input("Digite o primeiro número: "))
valorB = int(input("digite o segundo numero: "))
resultado = somar(valorA, valorB)
print(f"O resultado da soma = {resultado}")

#calcular area do cirulo
print("Área do circulo!!")
raio = float(input("Digite o valor do raio: "))
area = calcularAreaCirculo(raio)
print("A área do circulo : {area: .2f}")