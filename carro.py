class Carro:
    def __init__(self, marca, modelo, ano, cor, combustivel, ligado=False, velocidade=0):
        self.marca = marca          
        self.modelo = modelo        
        self.ano = ano              
        self.cor = cor              
        self.combustivel = combustivel 
        self.ligado = ligado       
        self.velocidade = velocidade  
    
    def ligar(self):
        if self.combustivel > 0:
            self.ligado = True
            print(f"O carro {self.modelo} está ligado.")
        else:
            print("Não há combustível suficiente para ligar o carro.")
    
    def desligar(self):
        if self.velocidade == 0:
            self.ligado = False
            print(f"O carro {self.modelo} está desligado.")
        else:
            print("O carro não pode ser desligado enquanto estiver em movimento.")
    
    def acelerar(self):
        if self.ligado:
            if self.combustivel > 0:
                self.velocidade += 350
                self.combustivel -= 5
                print(f"Acelerando... A velocidade atual é {self.velocidade} km/h.")
            else:
                print("Não há combustível suficiente para acelerar.")
        else:
            print("O carro precisa estar ligado para acelerar.")
    
    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 300
            print(f"Freando... A velocidade atual é {self.velocidade} km/h.")
        else:
            print("O carro já está parado.")
    
    def abastecer(self, quantidade):
        if self.combustivel < 100:
            self.combustivel += quantidade
            if self.combustivel > 100:
                self.combustivel = 100
            print(f"Abastecido. O tanque agora tem {self.combustivel} unidades de combustível.")
        else:
            print("O tanque já está cheio.")
    
    def buzinar(self):
        print("BIBIBIBI")
    
    def status(self):
        ligado_str = "ligado" if self.ligado else "desligado"
        print(f"Carro {self.modelo} ({self.ano}):\n"
              f"Cor: {self.cor}\n"
              f"Combustível: {self.combustivel} unidades\n"
              f"Velocidade: {self.velocidade} km/h\n"
              f"Status: {ligado_str}")

meu_carro = Carro(marca="Ferrari", modelo="LaFerrari", ano=2013, cor="Vermelho", combustivel=100)

meu_carro.ligar()
meu_carro.acelerar()
meu_carro.frear()
meu_carro.buzinar()
meu_carro.abastecer(30)
meu_carro.status()
meu_carro.desligar()