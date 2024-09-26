print("Programa para cálculo de IMC")
peso = float(input("Digite o seu peso (em kg): "))
altura = float(input("Digite a sua altura (em metros): "))
imc = peso / (altura**2)

print(f"Seu IMC é (imc:.2f)")   # .2f é uasdo
# para mostrar apenas duas casas decimais

if (imc < 18.5):
    print("Abaixo do peso")
elif (18.5 <= imc < 25):
    print("Peso normal.")
elif (25 <= imc < 35):
    print("Sobrepeso.")
else:
    print("Obesidade.")
    