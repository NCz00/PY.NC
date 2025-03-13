class Cachorro:
    def __init__(self, nome, raca, comida):
        self.nome=nome
        self.comida=comida
        self.raca=raca
        self.acordado=True
        self.feliz=False

    def __str__(self):
        return f"nome: {self.nome}, raça: {self.raca}, comida: {self.comida}, acordado: {self.acordado}, feliz: {self.feliz}"

    def comer(self):
        if self.comida>0:
            self.comida -=1
            self.feliz=True
            print(f"{self.nome} comeu e agora está feliz!")
        else: print(f"{self.nome} está sem comida!")

    def dormir (self):
            self.acordado = False
            print(f"{self.nome} dormindo.")

    def acordar (self):
            self.acordado = True
            print(f"{self.nome} está acordado!")    

    def brincar (self):
            self.feliz = False
            print(f"{self.nome} está brincando feliz!")

    def ignorar (self):
            self.feliz = False
            print(f"{self.nome} está triste porque foi ignorado.")

    def latir (self):
        if self.acordado is True:
            print(f"{self.nome} está latindo: au au au!")
        else: print(f"{self.nome} está dormindo e não pode latir.")

#Criando os cachorros:
chucky = Cachorro ("Smokey", "huski", 1)
pipoca = Cachorro ("Bela", "shitzu", 3)
#Interagindo com os cachorros
chucky.comer ()
pipoca.dormir()
chucky.brincar()
pipoca.acordar()
chucky.ignorar()
pipoca.latir()
print (chucky)
print (pipoca)