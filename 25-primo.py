def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

try:
    number = int(input("Digite um número: "))
    if is_prime(number):
        print(f"{number} é um número primo.")
    else:
        print(f"{number} não é um número primo.")
except ValueError:
    print("Por favor, digite um número inteiro válido.")