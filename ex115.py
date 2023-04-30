class retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.altura * self.largura

    def perimetro(self):
        return self.largura * 2 + self.altura * 2

    def diagonal(self):
        return (self.largura ** 2 + self.altura ** 2) ** 0.5

    def escala(self, fator):
        print()
        return self.area()*fator, self.perimetro()*fator, self.diagonal()*fator


r = retangulo(3, 5)

print(f"A área é:{r.area()}\nO Perímetro é : {r.perimetro()}\nA diagonal é :{r.diagonal()}\nA escala é : {r.escala(5.4)}")