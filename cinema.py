def verificar_ingresso(idade, estudante=False, idoso=False):
    # Verificando se a pessoa é elegível para meia entrada
    if idade < 18 or idoso or estudante:
        return "Meia entrada"
    else:
        return "Ingresso normal"

def main():
    print("Bem-vindo ao sistema de venda de ingressos!")
    
    idade = int(input("Digite sua idade: "))
    estudante = input("Você é estudante? (sim/não): ").strip().lower() == "sim"
    idoso = input("Você é idoso (60 anos ou mais)? (sim/não): ").strip().lower() == "sim"

    ingresso = verificar_ingresso(idade, estudante, idoso)
    
    print(f"Você pagará: {ingresso}")

if __name__ == "__main__":
    main()