class Cachorro: 
    def __init__(self, nome, idade, raca, comida):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.comida = comida
        self.acordado = False
        self.feliz = False

    def acordar(self):
        self.acordado = True
        print(f"{self.nome} está acordado")

    def dormir(self):
        self.acordado = False
        print(f"{self.nome} está dormindo")
    
    def brincar(self):
       if self.acordado:
           self.feliz = True
           print(f"{self.nome} está brincando")
       else:
           print(f"{self.nome} está triste")
    def ignorar(self):
        self.feliz = True
        print(f"{self.nome} está triste")
    def comer(self):
        if self.acordado:
            self.comida -=1
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
cachorro1 = Cachorro("Bertinho", 1, "Vira-Lata", 8)
cachorro1.exibirstatus()
        
    