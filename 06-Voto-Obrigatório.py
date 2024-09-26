idade = float(input("escreva a sua idade:"))
print("você quer votar?\n ")
if(idade <= 15):{print("você não pode votar")}
elif(idade >= 16 and idade < 18 or idade >= 65 and idade < 120):{print("Você pode votar se quiser")}
elif(idade >= 120):{print("você esta morto ou é não é humano")}
elif(idade >= 18 and idade < 65):{print("você é obrigado a votar\n")}

elif(idade >= 18 and idade < 65):{print("você vai votar mesmo sabendo disso?\n")}
verificação = str(input("Sim ou Não? "))

if verificação == "sim":
    print("ok então vote")
elif verificação == "não":
    print("vai ter que pagar 3,51 reais por turno")
else:
    print("Resposta inválida.")