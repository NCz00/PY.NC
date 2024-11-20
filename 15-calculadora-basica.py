def calculadora():
    opcao = 0

    while opcao != 6:
        print("CALCULADORA DAS OPERAÇÕES BÁSICAS:")
        print("Menu de escolha:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Resto da Divisão")
        print("6. Sair")
        opcao = int(input("Digite a sua opção: "))

        if opcao in [1, 2, 3, 4, 5]:
            n1 = float(input("\nInsira o primeiro valor: "))
            n2 = float(input("Insira o segundo valor: "))

        if opcao == 1:
            print(f"A soma dos valores é: {n1 + n2}\n")
        elif opcao == 2:
            print(f"A subtração dos valores é: {n1 - n2}\n")
        elif opcao == 3:
            print(f"A multiplicação dos valores é: {n1 * n2}\n")
        elif opcao == 4:
            if n2 == 0:
                print("Erro: Divisão por zero não é permitida.\n")
            else:
                print(f"A divisão dos valores é: {n1 / n2}\n")
        elif opcao == 5:
            if n2 == 0:
                print("Erro: Divisão por zero não é permitida.\n")
            else:
                print(f"O resto da divisão dos valores é: {n1 % n2}\n")
        elif opcao == 6:
            print("Finalizando o código!\n")
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    calculadora()