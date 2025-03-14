class Cachorro:
    def __init__(self, nome, idade, raca, comida):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.comida = comida
        self.acordado = False
        self.feliz = False
        self.energia = 100  

    def acordar(self):
        self.acordado = True
        print(f"{self.nome} está acordado")

    def dormir(self):
        self.acordado = False
        self.energia = 100  
        print(f"{self.nome} está dormindo. Energia restaurada para 100.")

    def brincar(self):
        if self.acordado:
            if self.energia >= 20: 
                self.feliz = True
                self.energia -= 20  
                print(f"{self.nome} está brincando. Energia restante: {self.energia}.")
            else:
                print(f"{self.nome} não tem energia suficiente para brincar.")
        else:
            print(f"{self.nome} está triste")

    def ignorar(self):
        self.feliz = True
        print(f"{self.nome} está triste")

    def comer(self):
        if self.acordado:
            self.comida -= 1
            print(f"{self.nome} está comendo")
        else:
            print(f"{self.nome} está dormindo")

    def latir(self):
        if self.acordado:
            print(f"{self.nome} está latindo")
        else:
            print(f"{self.nome} não pode latir")

    def exibirstatus(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Raça: {self.raca}")
        print(f"Comida: {self.comida}")
        print(f"Acordado: {self.acordado}")
        print(f"Feliz: {self.feliz}")
        print(f"Energia: {self.energia}")

cachorro1 = Cachorro("Bertinho", 1, "Vira-Lata", 8)
cachorro1.exibirstatus()

cachorro1.acordar()
cachorro1.brincar()
cachorro1.exibirstatus()
cachorro1.dormir()
cachorro1.exibirstatus()